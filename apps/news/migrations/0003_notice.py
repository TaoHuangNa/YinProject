# Generated by Django 2.1.1 on 2020-07-08 21:17

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_auto_20200627_0003'),
    ]

    operations = [
        migrations.CreateModel(
            name='Notice',
            fields=[
                ('notice_id', models.AutoField(help_text='通知id', primary_key=True, serialize=False, verbose_name='通知id')),
                ('notice_content', models.CharField(help_text='通知内容', max_length=6400, verbose_name='通知内容')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, help_text='创建时间', verbose_name='创建时间')),
            ],
            options={
                'verbose_name': '通知',
                'verbose_name_plural': '通知',
            },
        ),
    ]
