# Generated by Django 2.1.1 on 2020-07-05 21:55

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0028_auto_20200705_1726'),
    ]

    operations = [
        migrations.CreateModel(
            name='Transfer',
            fields=[
                ('transfer_id', models.AutoField(help_text='转账编号', primary_key=True, serialize=False, verbose_name='转账编号')),
                ('money', models.DecimalField(decimal_places=2, help_text='金额', max_digits=9, verbose_name='金额')),
                ('cheques_account', models.CharField(help_text='收款人账号', max_length=200, verbose_name='收款人账号')),
                ('cheques_name', models.CharField(help_text='收款人名称', max_length=200, verbose_name='收款人名称')),
                ('payment_account', models.CharField(help_text='付款人账号', max_length=200, verbose_name='付款人账号')),
                ('payment_name', models.CharField(help_text='付款人名称', max_length=200, verbose_name='付款人名称')),
                ('state', models.CharField(choices=[('0', '已支付'), ('1', '已退回')], default='1', help_text='状态 0：已支付,1：已退回 暂时没用到这个字段', max_length=10, verbose_name='状态')),
                ('remarks', models.CharField(blank=True, help_text='备注', max_length=360, null=True, verbose_name='备注')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, help_text='创建时间', verbose_name='创建时间')),
                ('image', models.ManyToManyField(blank=True, help_text='照片', to='tasks.ImageInfo', verbose_name='照片')),
            ],
            options={
                'verbose_name': '转账信息',
                'verbose_name_plural': '转账信息',
            },
        ),
        migrations.AlterField(
            model_name='tasks',
            name='state',
            field=models.CharField(choices=[('0', '未支付'), ('1', '已支付'), ('2', '进行中'), ('3', '审核不通过'), ('4', '已完成'), ('5', '已删除')], default='0', help_text='状态  0:未支付,1:已支付,2:审核通过, 3:审核不通过, 4:已完成', max_length=10, verbose_name='状态'),
        ),
        migrations.AddField(
            model_name='transfer',
            name='tasks_id',
            field=models.ForeignKey(blank=True, help_text='任务编号', max_length=11, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='tasks.Tasks', verbose_name='任务编号'),
        ),
    ]
