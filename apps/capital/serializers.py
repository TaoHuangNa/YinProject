from datetime import datetime
from decimal import Decimal

from django.db.models import Q
from requests import Response
from rest_framework import serializers, status

from apps.capital.models import Capital, MoneyRecord
from apps.users.models import UserProfile


class CapitalModelsSerializer(serializers.ModelSerializer):
    add_time = serializers.DateTimeField(read_only=True, format='%Y-%m-%d %H:%M:%S')

    class Meta:
        model = Capital
        fields = '__all__'


class MoneyRecordTasksModelsSerializer(serializers.ModelSerializer):
    add_time = serializers.DateTimeField(read_only=True, format='%Y-%m-%d %H:%M:%S')
    password = serializers.CharField(required=False, write_only=True,
                                         error_messages={"blank": "请输入密码", "required": "请输入密码"},
                                         help_text="密码", label="密码")
    # money = serializers.CharField(required=False, write_only=True,
    #                                  error_messages={"blank": "提现金额", "required": "提现金额"},
    #                                  help_text="提现金额", label="提现金额")
    state = serializers.SerializerMethodField()

    def get_state(self, obj):
        for i in obj.STATE_CHOICES:
            if i[0] == obj.state:
                return i[1]

    def validate_password(self, password):
        # old_password = base64.b64decode(old_password).decode('utf8')
        if password:
            # 判断原密码是否正确
            verify = UserProfile.check_password(self.context['request'].user, password)

            if not verify:
                # 密码不正确
                raise serializers.ValidationError('密码不正确')
                # raise Response({"订单审核状态不存在"}, status=status.HTTP_400_BAD_REQUEST)
        return password

    def validate(self, attrs):
        # password是自己添加得，数据库中并没有这个字段，验证完就删除掉
        if attrs.get("password", ""):
            del attrs["password"]
        return attrs

    # def validate_money(self, money):
    #     # old_password = base64.b64decode(old_password).decode('utf8')
    #
    #     return money

    def create(self, validated_data):
        today = datetime.now()
        year = today.strftime("%Y")
        month = today.strftime("%m")
        day = today.strftime("%d")
        if not self.context['request'].user.ZFB_name or not self.context['request'].user.ZFB_account:
            raise serializers.ValidationError({"message": '请设置支付宝账号和姓名'})
        if Decimal(self.context['request'].user.balance) < validated_data["money"]:
            raise serializers.ValidationError({"message": '余额不足'})
        # 查询该用户今天是否首次提现
        num = MoneyRecord.objects.filter(Q(add_time__year=year) & Q(add_time__month=month) & Q(add_time__day=day)
                                         & Q(user=self.context["request"].user) & Q(state__in=['0', '1'])).count()
        if num > 0:
            raise serializers.ValidationError({"message": '提现失败：今日已提现'})
        c_models = super(MoneyRecordTasksModelsSerializer, self).create(validated_data=validated_data)
        # 默认为当前用户为创建人
        c_models.user = self.context['request'].user
        c_models.ZFB_name = self.context['request'].user.ZFB_name
        c_models.ZFB_account = self.context['request'].user.ZFB_account
        c_models.save()
        return c_models

    class Meta:
        depth = 1
        model = MoneyRecord
        fields = ('record_id', 'user', 'money', 'ZFB_name', 'ZFB_account', 'state', 'remarks', 'add_time', 'password')


class MoneyRecordTasksUpdateModelsSerializer(serializers.ModelSerializer):
    add_time = serializers.DateTimeField(read_only=True, format='%Y-%m-%d %H:%M:%S')

    class Meta:
        model = MoneyRecord
        fields = '__all__'
