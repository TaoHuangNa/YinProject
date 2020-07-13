# Generated by Django 2.1.1 on 2020-06-26 23:39

import datetime
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0006_auto_20200626_1005'),
    ]

    operations = [
        migrations.CreateModel(
            name='TasksType',
            fields=[
                ('type_id', models.AutoField(help_text='任务类型编号', primary_key=True, serialize=False, verbose_name='任务类型编号')),
                ('type', models.CharField(help_text='任务类型 例：点赞加关注', max_length=200, verbose_name='任务类型')),
                ('price', models.CharField(help_text='发布任务价格', max_length=10, verbose_name='发布任务价格')),
                ('complete_price', models.CharField(help_text='完成任务价格', max_length=10, verbose_name='完成任务价格')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, help_text='创建时间', verbose_name='创建时间')),
            ],
            options={
                'verbose_name': '任务类型',
                'verbose_name_plural': '任务类型',
            },
        ),
        migrations.AddField(
            model_name='completetasks',
            name='price',
            field=models.CharField(default=django.utils.timezone.now, help_text='价格', max_length=10, verbose_name='价格'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tasks',
            name='type',
            field=models.CharField(blank=True, choices=[('0', '普通任务'), ('1', '会员任务')], help_text='任务类型  0:普通任务,1:会员任务', max_length=10, null=True, verbose_name='任务类型'),
        ),
        migrations.AlterField(
            model_name='tasks',
            name='requirement',
            field=models.ForeignKey(help_text='任务要求', max_length=64, on_delete=django.db.models.deletion.DO_NOTHING, to='tasks.TasksType', verbose_name='任务要求'),
        ),
        migrations.AlterField(
            model_name='tasks',
            name='url',
            field=models.CharField(help_text='视频链接', max_length=200, verbose_name='视频链接'),
        ),
    ]