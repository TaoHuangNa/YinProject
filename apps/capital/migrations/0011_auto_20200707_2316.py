# Generated by Django 2.1.1 on 2020-07-07 23:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('capital', '0010_auto_20200707_2304'),
    ]

    operations = [
        migrations.AddField(
            model_name='moneyrecord',
            name='ZFB_account',
            field=models.CharField(blank=True, help_text='支付宝账号', max_length=30, null=True, verbose_name='支付宝账号'),
        ),
        migrations.AddField(
            model_name='moneyrecord',
            name='ZFB_name',
            field=models.CharField(blank=True, help_text='支付宝名称', max_length=30, null=True, verbose_name='支付宝名称'),
        ),
    ]