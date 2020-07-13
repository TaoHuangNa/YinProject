# Generated by Django 2.1.1 on 2020-07-10 22:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0032_auto_20200709_0057'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transfer',
            name='state',
            field=models.CharField(choices=[('0', '已支付'), ('1', '审核通过'), ('2', '驳回，已退款')], default='0', help_text='状态 0：已支付, 1：审核通过, 2：驳回，已退款', max_length=10, verbose_name='状态'),
        ),
    ]
