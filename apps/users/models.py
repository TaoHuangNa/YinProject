from django.db import models

# Create your models here.
from datetime import datetime
from django.contrib.auth.models import AbstractUser


class Member(models.Model):
    """
    会员信息
    """
    CHOICES = (
        ("0", "无会员"),
        ("1", "青铜"),
        ("2", "白银"),
        ("3", "黄金"),
        ("4", "白金"),
        ("5", "钻石"),
    )
    TYPE = (
        ("0", "日"),
        ("1", "月"),
        ("2", "年")
    )
    member_id = models.AutoField(verbose_name="会员编号", primary_key=True, help_text="会员编号")
    member_name = models.CharField(verbose_name="会员等级名称", choices=CHOICES, max_length=10, help_text="会员等级名称")
    common_num = models.CharField(verbose_name="普通任务条数", max_length=10, help_text="普通任务条数")
    member_num = models.CharField(verbose_name="会员任务条数", max_length=10, help_text="会员任务条数")
    time = models.IntegerField(verbose_name="有效期限", help_text="有效期限")
    time_type = models.CharField(verbose_name="期限类型", choices=TYPE, max_length=10, help_text="期限类型 0.日 1.月 2.年")
    # place = models.CharField(verbose_name="价格", max_length=11, help_text="价格")
    place = models.DecimalField(verbose_name="价格", max_digits=16, decimal_places=2, default=0.00, help_text="价格")
    add_time = models.DateTimeField(verbose_name="添加时间", default=datetime.now, help_text="添加时间")

    class Meta:
        verbose_name = "会员信息"
        verbose_name_plural = verbose_name

    def __str__(self):
        return str(self.member_id)


class UserProfile(AbstractUser):
    """
    用户信息
    """
    # GENDER_CHOICES = (
    #     ("male", u"男"),
    #     ("female", u"女")
    # )
    # 用户用手机注册，所以姓名，生日和邮箱可以为空
    name = models.CharField(verbose_name="昵称", max_length=30, null=True, blank=True, help_text="昵称")
    pay_password = models.CharField(verbose_name="支付密码", max_length=30, null=True, blank=True, help_text="支付密码")
    ZFB_name = models.CharField(verbose_name="支付宝名称", max_length=30, null=True, blank=True, help_text="支付宝名称")
    ZFB_account = models.CharField(verbose_name="支付宝账号",  max_length=30, null=True, blank=True, help_text="支付宝账号")
    # task_num = models.CharField(verbose_name="普通任务条数", max_length=10, null=True, blank=True, help_text="普通任务条数")
    member_limit = models.CharField(verbose_name="会员到期日", max_length=10, null=True, blank=True,
                                    help_text="会员到期日 格式：20200630")
    invitation_code = models.CharField(verbose_name="邀请码",  max_length=30, null=True, blank=True, help_text="邀请码")
    invitation_name = models.ForeignKey('self', verbose_name="邀请人",  max_length=30, null=True, blank=True,
                                        help_text="邀请人", to_field="username", on_delete=models.DO_NOTHING)
    member_level = models.ForeignKey(Member, null=True, blank=True, verbose_name="会员等级", help_text="会员等级", default=1,
                                     on_delete=models.SET_NULL)
    balance = models.DecimalField(verbose_name="余额", max_digits=16, decimal_places=2, default=0.00, help_text="余额")
    task_reward = models.DecimalField(verbose_name="任务奖励", max_digits=9, decimal_places=2, default=0.00, help_text="任务奖励")
    commission = models.DecimalField(verbose_name="套餐提成", max_digits=9, decimal_places=2, default=0.00, help_text="套餐提成")
    team_income = models.DecimalField(verbose_name="团队收益", max_digits=9, decimal_places=2, default=0.00, help_text="团队收益")

    class Meta:
        verbose_name = "用户信息"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.username


class VerifyCode(models.Model):
    """
    验证码
    """
    code = models.CharField(verbose_name="验证码", max_length=10)
    mobile = models.CharField(verbose_name="电话", max_length=11)
    add_time = models.DateTimeField(verbose_name="添加时间", default=datetime.now)

    class Meta:
        verbose_name = "短信验证"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.code


class HomeData(models.Model):
    """
    APP首页数据
    """
    id = models.AutoField(verbose_name="会员编号", primary_key=True, help_text="会员编号")
    tasks_today = models.CharField(verbose_name="今日任务数", max_length=10)
    user_today = models.CharField(verbose_name="今日用户数", max_length=11)
    complete = models.CharField(verbose_name="今日已完成", max_length=11)
    goal = models.CharField(verbose_name="今日排行榜", max_length=11)
    add_time = models.DateTimeField(verbose_name="添加时间", default=datetime.now)

    class Meta:
        verbose_name = "APP首页数据"
        verbose_name_plural = verbose_name

    def __str__(self):
        return str(self.id)
