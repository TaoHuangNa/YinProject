import base64
from datetime import datetime, timedelta
from decimal import Decimal

from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password
from django.db.models import Q
from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from apps.users.models import UserProfile, VerifyCode, Member, HomeData
from apps.capital.models import Capital
from apps.tasks.models import CompleteTasks

User = get_user_model()


class UserProfileModelsSerializer(serializers.ModelSerializer):
    date_joined = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S')
    password = serializers.CharField(
        style={'input_type': 'password'}, label="密码", write_only=True
    )

    class Meta:
        # depth = 1
        model = UserProfile
        fields = "__all__"


class VerifyCodeModelsSerializer(serializers.ModelSerializer):
    # 函数名必须：validate + 验证字段名
    def validate_mobile(self, mobile):
        """
        手机号码验证
        """
        # 是否已经注册
        # if User.objects.filter(username=mobile).count():
        #     raise serializers.ValidationError("用户已经存在")

        # 是否合法
        if len(mobile) != 11:
            raise serializers.ValidationError("手机号码不为11位")

        # 验证码发送频率
        # 60s内只能发送一次
        one_mintes_ago = datetime.now() - timedelta(hours=0, minutes=1, seconds=0)
        if VerifyCode.objects.filter(add_time__gt=one_mintes_ago, mobile=mobile).count():
            raise serializers.ValidationError("距离上一次发送未超过60s")

        return mobile

    class Meta:
        model = VerifyCode
        fields = ('mobile',)


class MemberModelsSerializer(serializers.ModelSerializer):
    add_time = serializers.DateTimeField(read_only=True, format='%Y-%m-%d %H:%M:%S')
    member_name = serializers.SerializerMethodField()
    time_type = serializers.SerializerMethodField()

    def get_member_name(self, obj):
        # 昵称
        for i in obj.CHOICES:
            if i[0] == obj.member_name:
                return i[1]

    def get_time_type(self, obj):
        # 昵称
        for i in obj.TYPE:
            if i[0] == obj.time_type:
                return i[1]

    class Meta:
        depth = 1
        model = Member
        fields = '__all__'


class UserRegSerializer(serializers.ModelSerializer):
    """用户注册"""
    # UserProfile中没有code字段，这里需要自定义一个code序列化字段
    code = serializers.CharField(required=True, write_only=True, max_length=6, min_length=6,
                                 error_messages={
                                     "blank": "请输入验证码",
                                     "required": "请输入验证码",
                                     "max_length": "验证码格式错误",
                                     "min_length": "验证码格式错误"
                                 }, help_text="验证码")
    # 验证用户名是否存在
    username = serializers.CharField(label="用户名", help_text="用户名", required=True, allow_blank=False,
                                     validators=[UniqueValidator(queryset=User.objects.all(), message="用户已经存在")])
    password = serializers.CharField(
        style={'input_type': 'password'}, label="密码", write_only=True
    )

    # 密码加密保存
    def create(self, validated_data):
        user = super(UserRegSerializer, self).create(validated_data=validated_data)
        user.password = make_password(validated_data["password"])
        # user.set_password(validated_data["password"])
        user.save()
        return user

    # def validate_password(self, password):
    #     return base64.b64decode(password).decode('utf8')

    # 验证code
    def validate_code(self, code):
        # 用户注册，已post方式提交注册信息，post的数据都保存在initial_data里面
        # username就是用户注册的手机号，验证码按添加时间倒序排序，为了后面验证过期，错误等
        verify_records = VerifyCode.objects.filter(mobile=self.initial_data["username"]).order_by("-add_time")

        if verify_records:
            # 最近的一个验证码
            last_record = verify_records[0]
            # 有效期为五分钟。
            five_mintes_ago = datetime.now() - timedelta(hours=0, minutes=5, seconds=0)
            if five_mintes_ago > last_record.add_time:
                raise serializers.ValidationError("验证码过期")

            if last_record.code != code:
                raise serializers.ValidationError("验证码错误")

        else:
            raise serializers.ValidationError("验证码错误")

    # 所有字段。attrs是字段验证合法之后返回的总的dict
    def validate(self, attrs):
        # 前端没有传mobile值到后端，这里添加进来
        # attrs["mobile"] = attrs["username"]
        # code是自己添加得，数据库中并没有这个字段，验证完就删除掉
        del attrs["code"]
        return attrs

    class Meta:
        model = User
        fields = ('username', 'code', 'password', 'invitation_name', 'name')


class PasswordResetSerializer(serializers.ModelSerializer):
    """用户登陆密码重置"""
    # 验证手机号是否存在
    username = serializers.CharField(required=False, write_only=True,
                                     error_messages={"blank": "请输入手机号", "required": "请输入手机号"},
                                     help_text="手机号", label="手机号")
    # UserProfile中没有code字段，这里需要自定义一个code序列化字段
    code = serializers.CharField(required=False, write_only=True, max_length=6, min_length=6,
                                 error_messages={
                                     "blank": "请输入验证码",
                                     "required": "请输入验证码",
                                     "max_length": "验证码格式错误",
                                     "min_length": "验证码格式错误"
                                 }, help_text="验证码", label="验证码")
    password = serializers.CharField(
        required=False, style={'input_type': 'password'}, label="密码", write_only=True
    )

    # def validate_password(self, password):
    #     if password:
    #         return base64.b64decode(password).decode('utf8')

    # 所有字段。attrs是字段验证合法之后返回的总的dict
    def validate(self, attrs):
        mobile = attrs.pop('username', '')
        code = attrs.pop('code', '')
        if mobile and code:
            verify_records = VerifyCode.objects.filter(mobile=mobile).order_by("-add_time")
            if verify_records:
                # 最近的一个验证码
                last_record = verify_records[0]
                # 有效期为五分钟。
                five_mintes_ago = datetime.now() - timedelta(hours=0, minutes=30, seconds=0)
                if five_mintes_ago > last_record.add_time:
                    raise serializers.ValidationError("验证码过期")

                if last_record.code != code:
                    raise serializers.ValidationError("验证码错误")
            else:
                raise serializers.ValidationError("验证码错误")
        return attrs

    # 重写update方法使更新的密码加密
    def update(self, instance, validated_data):
        user = super(PasswordResetSerializer, self).update(instance, validated_data)
        print(validated_data["password"])
        user.password = make_password(validated_data["password"])
        user.save()
        return user

    class Meta:
        model = User
        fields = ('username', 'code', 'password')


class UserBalanceModelsSerializer(serializers.ModelSerializer):
    username = serializers.SerializerMethodField()
    name = serializers.SerializerMethodField()
    balance = serializers.SerializerMethodField()
    task_reward = serializers.SerializerMethodField()
    commission = serializers.SerializerMethodField()
    team_income = serializers.SerializerMethodField()
    # serializers.CharField(read_only=True)

    # 今日收益
    balance_today = serializers.SerializerMethodField()
    # 今日已做普通任务
    common_task_complete = serializers.SerializerMethodField()
    # 今日可做普通任务
    common_task_num = serializers.SerializerMethodField()
    # 今日已做会员任务
    member_task_complete = serializers.SerializerMethodField()
    # 今日可做会员任务
    member_task_num = serializers.SerializerMethodField()

    def get_username(self, obj):
        # 用户名
         return self.context["request"].user.username

    def get_name(self, obj):
        # 昵称
         return self.context["request"].user.name

    def get_balance(self, obj):
        # 余额
         return self.context["request"].user.balance

    def get_task_reward(self, obj):
        # 任务奖励
         return self.context["request"].user.task_reward

    def get_commission(self, obj):
        # 套餐提成
         return self.context["request"].user.commission

    def get_team_income(self, obj):
        # 团队收益
         return self.context["request"].user.team_income

    def get_balance_today(self, obj):
        # 今天的收益
        today = datetime.now()
        # 今年
        year = today.strftime("%Y")
        month = today.strftime("%m")
        day = today.strftime("%d")
        capital_today_list = Capital.objects.filter(Q(add_time__year=year) & Q(add_time__month=month)
                                                    & Q(add_time__day=day) & Q(type="0") & Q(user=self.context["request"].user)).values("money")
        balance_today = Decimal(0.00)
        # 将今天的资金明细收入相加
        for capital_today in capital_today_list:
            balance_today = balance_today + capital_today["money"]
        return balance_today

    def get_common_task_complete(self, obj):
        # 今日已做普通任务
        today = datetime.now()
        # 今年
        year = today.strftime("%Y")
        month = today.strftime("%m")
        day = today.strftime("%d")
        num = CompleteTasks.objects.filter(
            Q(add_time__year=year) & Q(add_time__month=month) & Q(add_time__day=day) & Q(tasks_id__type="0") & Q(complete_user=self.context["request"].user)).count()
        return num

    def get_common_task_num(self, obj):
        # 今日可做普通任务
         return self.context["request"].user.member_level.common_num

    def get_member_task_complete(self, obj):
        # 今日已做会员任务
        today = datetime.now()
        # 今年
        year = today.strftime("%Y")
        month = today.strftime("%m")
        day = today.strftime("%d")
        num = CompleteTasks.objects.filter(
            Q(add_time__year=year) & Q(add_time__month=month) & Q(add_time__day=day) & Q(tasks_id__type="1") & Q(complete_user=self.context["request"].user)).count()
        return num

    def get_member_task_num(self, obj):
        # 今日可做会员任务
         return self.context["request"].user.member_level.member_num

    class Meta:
        model = UserProfile
        fields = ["username", "name", "balance", "task_reward", "commission", "team_income", "balance_today",
                  "common_task_complete", "common_task_num", "member_task_complete", "member_task_num"]


class PasswordUpdateSerializer(serializers.ModelSerializer):
    """用户登陆密码修改"""
    # 验证手机号是否存在
    old_password = serializers.CharField(required=False, write_only=True,
                                         error_messages={"blank": "请输入旧密码", "required": "请输入旧密码"},
                                         help_text="旧密码", label="旧密码")
    password = serializers.CharField(
        required=False, style={'input_type': 'password'}, label="密码", write_only=True
    )

    # def validate_password(self, password):
    #     if password:
    #         return base64.b64decode(password).decode('utf8')

    # 所有字段。attrs是字段验证合法之后返回的总的dict
    def validate_old_password(self, old_password):
        # old_password = base64.b64decode(old_password).decode('utf8')
        if old_password:
            # 判断原密码是否正确
            verify = UserProfile.check_password(self.instance, old_password)

            if not verify:
                # 原密码不正确
                raise serializers.ValidationError("原密码不正确")
        return old_password

    # 重写update方法使更新的密码加密
    def update(self, instance, validated_data):
        user = super(PasswordUpdateSerializer, self).update(instance, validated_data)
        print(validated_data["password"])
        user.password = make_password(validated_data["password"])
        user.save()
        return user

    class Meta:
        model = User
        fields = ('old_password', 'password')


class TeamModelsSerializer(serializers.ModelSerializer):
    member_level = serializers.SerializerMethodField()
    name = serializers.SerializerMethodField()

    def get_member_level(self, obj):
        # 昵称
        for i in obj.member_level.CHOICES:
            if i[0] == obj.member_level.member_name:
                return i[1]

    def get_name(self, obj):
        # 会员等级
         return obj.name

    class Meta:
        model = UserProfile
        fields = ["name", "member_level"]


class HomeDataModelsSerializer(serializers.ModelSerializer):
    add_time = serializers.DateTimeField(read_only=True, format='%Y-%m-%d %H:%M:%S')

    class Meta:
        model = HomeData
        fields = '__all__'
