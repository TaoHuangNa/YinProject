from datetime import datetime

from django.db import models


# Create your models here.
from apps.users.models import UserProfile
from apps.tasks.storage import ImageStorage


# class TasksType(models.Model):
#     """
#     任务类型
#     """
#     type_id = models.AutoField(verbose_name="任务类型编号", primary_key=True, help_text="任务类型编号")
#     type = models.CharField(verbose_name="任务类型", max_length=200, help_text="任务类型 例：点赞加关注")
#     # price = models.CharField(verbose_name="发布任务价格", max_length=10, help_text="发布任务价格")
#     price = models.DecimalField(verbose_name="发布任务价格", max_digits=9, decimal_places=2, default=0.00,
#                                 help_text="发布任务价格")
#     # complete_price = models.CharField(verbose_name="完成任务价格", max_length=10, help_text="完成任务价格")
#     complete_price = models.DecimalField(verbose_name="完成任务价格", max_digits=9, decimal_places=2, default=0.00,
#                                          help_text="完成任务价格")
#     add_time = models.DateTimeField(verbose_name="创建时间", default=datetime.now, help_text="创建时间")
#
#     class Meta:
#         verbose_name = "任务类型"
#         verbose_name_plural = verbose_name
#
#     def __str__(self):
#         return str(self.type_id)


class Tasks(models.Model):
    """
    任务信息
    """
    TYPE_CHOICES = (
        ("0", "普通任务"),
        ("1", "会员任务")
    )
    STATE_CHOICES = (
        ("0", "未支付"),
        ("1", "已支付"),
        ("2", "进行中"),
        ("3", "审核不通过"),
        ("4", "已完成"),
        ("5", "已删除")
    )
    tasks_id = models.AutoField(verbose_name="任务编号", primary_key=True, help_text="任务编号")
    url = models.CharField(verbose_name="视频链接", max_length=200, help_text="视频链接")
    target_times = models.IntegerField(verbose_name="目标次数",  help_text="目标次数")
    completed_times = models.IntegerField(verbose_name="已完成次数", null=True, blank=True, default="0", help_text="已完成次数")
    tasks_name = models.CharField(verbose_name="任务名称", max_length=360, help_text="任务名称")
    # cost = models.CharField(verbose_name="单条价格", max_length=11, help_text="单条价格")
    cost = models.DecimalField(verbose_name="发布任务价格", max_digits=9, decimal_places=2, default=0.00,
                               help_text="发布任务价格")
    # complete_cost = models.CharField(verbose_name="单条完成价格", max_length=11, help_text="单条完成价格")
    complete_cost = models.DecimalField(verbose_name="单条完成价格", max_digits=9, decimal_places=2, default=0.00,
                                        help_text="单条完成价格")
    # requirement = models.ForeignKey(TasksType, verbose_name="任务要求", max_length=64,
    #                                 help_text="任务要求", on_delete=models.DO_NOTHING)
    # total_cost = models.CharField(verbose_name="费用总计", max_length=11, help_text="费用总计")
    total_cost = models.DecimalField(verbose_name="费用总计", max_digits=9, decimal_places=2, default=0.00,
                                     help_text="费用总计")
    state = models.CharField(verbose_name="状态", max_length=10, choices=STATE_CHOICES, default="0",
                             help_text="状态  0:未支付,1:已支付,2:进行中, 3:审核不通过, 4:已完成")
    type = models.CharField(verbose_name="任务类型", max_length=10, choices=TYPE_CHOICES, null=True, blank=True,
                            help_text="任务类型  0:普通任务,1:会员任务")
    created = models.ForeignKey(UserProfile, max_length=11, help_text="创建人", verbose_name="创建人", null=True,
                                related_name='created_task', to_field="username", on_delete=models.DO_NOTHING)
    remarks = models.CharField(verbose_name="备注", null=True, blank=True, max_length=360, help_text="备注")
    add_time = models.DateTimeField(verbose_name="创建时间", default=datetime.now, help_text="创建时间")

    class Meta:
        verbose_name = "任务信息"
        verbose_name_plural = verbose_name

    def __str__(self):
        return str(self.tasks_id)


class ImageInfo(models.Model):
    """
    图片信息
    """
    id = models.AutoField(verbose_name="图片id", primary_key=True, help_text="图片id")
    url = models.ImageField(upload_to='img/%Y/%m/%d', storage=ImageStorage(), verbose_name="图片")
    add_time = models.DateTimeField("创建时间", auto_now_add=True, help_text='创建时间')

    class Meta:
        verbose_name = "图片信息表"
        verbose_name_plural = verbose_name

    def __str__(self):
        return str(self.url)


class CompleteTasks(models.Model):
    """
    任务完成信息
    """
    STATE_CHOICES = (
        ("0", "待审核"),
        ("1", "已驳回"),
        ("2", "已完成")
    )
    execute_id = models.AutoField(verbose_name="执行编号", primary_key=True, help_text="执行编号")
    tasks_id = models.ForeignKey(Tasks, max_length=11, help_text="任务编号", verbose_name="任务编号",
                                 on_delete=models.DO_NOTHING)
    complete_user = models.ForeignKey(UserProfile, max_length=11, help_text="完成人", verbose_name="完成人", null=True,
                                      related_name='complete_task', to_field="username", on_delete=models.DO_NOTHING)
    # price = models.CharField(verbose_name="价格", max_length=10, help_text="价格")
    price = models.DecimalField(verbose_name="价格", max_digits=9, decimal_places=2, default=0.00,
                                help_text="价格")
    # image = models.ImageField(upload_to='img/%Y%m%d', storage=ImageStorage(), verbose_name="任务图片")
    image = models.ManyToManyField(ImageInfo, verbose_name="照片", blank=True, help_text="照片")
    state = models.CharField(verbose_name="状态", max_length=10, choices=STATE_CHOICES, default="1",
                             help_text="状态 0：待审核,1：已驳回,2:已完成")
    remarks = models.CharField(verbose_name="备注", null=True, blank=True, max_length=360, help_text="备注")
    add_time = models.DateTimeField(verbose_name="创建时间", default=datetime.now, help_text="创建时间")

    class Meta:
        verbose_name = "任务完成信息"
        verbose_name_plural = verbose_name

    def __str__(self):
        return str(self.execute_id)


class Banner(models.Model):
    """
    首页轮播的图片
    """
    image = models.ImageField(upload_to='img/%Y%m%d', storage=ImageStorage(), verbose_name="轮播图片")
    index = models.IntegerField("轮播顺序", default=0)
    add_time = models.DateTimeField("添加时间", default=datetime.now)

    class Meta:
        verbose_name = '首页轮播'
        verbose_name_plural = verbose_name

    def __str__(self):
        return str(self.image)


class Transfer(models.Model):
    """
    转账信息
    """
    STATE_CHOICES = (
        ("0", "已支付"),
        ("1", "审核通过"),
        ("2", "驳回，已退款"),
    )
    transfer_id = models.AutoField(verbose_name="转账编号", primary_key=True, help_text="转账编号")
    # tasks_id = models.ForeignKey(Tasks, max_length=11, help_text="任务编号或者会员编号", verbose_name="任务编号或者会员编号", null=True, blank=True,
    #                              on_delete=models.DO_NOTHING)
    tasks_id = models.CharField(verbose_name="任务编号或者会员编号", max_length=200, help_text="任务编号或者会员编号")
    created = models.ForeignKey(UserProfile, max_length=11, help_text="创建人", verbose_name="创建人", null=True,
                                related_name='transfer', to_field="username", on_delete=models.DO_NOTHING)
    money = models.DecimalField(verbose_name="金额", max_digits=9, decimal_places=2, help_text="金额")
    member = models.BooleanField(verbose_name="是否开通会员转账", default=False, help_text="是否开通会员转账")
    cheques_account = models.CharField(verbose_name="收款人账号", max_length=200, help_text="收款人账号")
    cheques_name = models.CharField(verbose_name="收款人名称", max_length=200, help_text="收款人名称")
    payment_account = models.CharField(verbose_name="付款人账号", max_length=200, help_text="付款人账号")
    payment_name = models.CharField(verbose_name="付款人名称", max_length=200, help_text="付款人名称")
    image = models.ManyToManyField(ImageInfo, verbose_name="照片", blank=True, help_text="照片")
    state = models.CharField(verbose_name="状态", max_length=10, choices=STATE_CHOICES, default="0",
                             help_text="状态 0：已支付, 1：审核通过, 2：驳回，已退款")
    remarks = models.CharField(verbose_name="备注", null=True, blank=True, max_length=360, help_text="备注")
    add_time = models.DateTimeField(verbose_name="创建时间", default=datetime.now, help_text="创建时间")

    class Meta:
        verbose_name = "转账信息"
        verbose_name_plural = verbose_name

    def __str__(self):
        return str(self.transfer_id)
