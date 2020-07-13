from datetime import datetime
from django.db import models

# Create your models here.
from apps.users.models import UserProfile


class Capital(models.Model):
    """
    资金明细
    """
    CHOICES = (
        ("0", "收入"),
        ("1", "支出")
    )

    capital_id = models.AutoField(verbose_name="明细编号", primary_key=True, help_text="明细编号")
    # user = models.ForeignKey(UserProfile, max_length=11, help_text="所属人", verbose_name="所属人",
    #                          related_name='capital_user', to_field="username", on_delete=models.DO_NOTHING)
    user = models.CharField(verbose_name="所属人", max_length=128, help_text="所属人")
    # money = models.CharField(verbose_name="价格", max_length=128, help_text="价格")
    money = models.DecimalField(verbose_name="金额", max_digits=9, decimal_places=2, default=0.00,
                                help_text="金额")
    type = models.CharField(verbose_name="类型", max_length=10, choices=CHOICES, help_text="类型")
    operation = models.CharField(verbose_name="执行操作", max_length=128, help_text="类型")
    add_time = models.DateTimeField(verbose_name="创建时间", default=datetime.now, help_text="创建时间")

    class Meta:
        verbose_name = "资金明细"
        verbose_name_plural = verbose_name

    def __str__(self):
        return str(self.capital_id)


class MoneyRecord(models.Model):
    """
    提现记录
    """
    STATE_CHOICES = (
        ("0", "待放款"),
        ("1", "已放款"),
        ("2", "已驳回")
    )
    record_id = models.AutoField(verbose_name="记录编号", primary_key=True, help_text="记录编号")
    user = models.ForeignKey(UserProfile, max_length=11, help_text="提现人", verbose_name="提现人", null=True, blank=True,
                             related_name='money_record_user', to_field="username", on_delete=models.DO_NOTHING)
    # money = models.CharField(verbose_name="提现金额", max_length=11, help_text="提现金额")
    money = models.DecimalField(verbose_name="提现金额", max_digits=9, decimal_places=2, default=0.00,
                                help_text="提现金额")
    ZFB_name = models.CharField(verbose_name="支付宝名称", max_length=30, null=True, blank=True, help_text="支付宝名称")
    ZFB_account = models.CharField(verbose_name="支付宝账号", max_length=30, null=True, blank=True, help_text="支付宝账号")
    state = models.CharField(verbose_name="状态", max_length=10, choices=STATE_CHOICES, default="0", null=True, blank=True,
                             help_text="状态  0：待放款,1:已放款,2:已驳回")
    remarks = models.CharField(verbose_name="备注", null=True, blank=True, max_length=360, help_text="备注")
    add_time = models.DateTimeField("创建时间", default=datetime.now, help_text="创建时间")

    class Meta:
        verbose_name = "提现记录"
        verbose_name_plural = verbose_name

    def __str__(self):
        return str(self.record_id)
