# Generated by Django 2.1.1 on 2020-07-01 23:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0020_auto_20200701_2346'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tasks',
            name='state',
            field=models.CharField(choices=[('0', '未支付'), ('1', '已支付'), ('2', '审核通过'), ('3', '审核不通过'), ('4', '已完成')], default='0', help_text='状态  0:未支付,1:已支付,2:审核通过, 3:审核不通过, 4:已完成', max_length=10, verbose_name='状态'),
        ),
    ]
