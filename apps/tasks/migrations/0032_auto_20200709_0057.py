# Generated by Django 2.1.1 on 2020-07-09 00:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0031_auto_20200707_2052'),
    ]

    operations = [
        migrations.AddField(
            model_name='tasks',
            name='remarks',
            field=models.CharField(blank=True, help_text='备注', max_length=360, null=True, verbose_name='备注'),
        ),
        migrations.AlterField(
            model_name='tasks',
            name='state',
            field=models.CharField(choices=[('0', '未支付'), ('1', '已支付'), ('2', '进行中'), ('3', '审核不通过'), ('4', '已完成'), ('5', '已删除')], default='0', help_text='状态  0:未支付,1:已支付,2:进行中, 3:审核不通过, 4:已完成', max_length=10, verbose_name='状态'),
        ),
    ]