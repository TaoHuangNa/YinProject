# Generated by Django 2.1.1 on 2020-07-09 23:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0014_auto_20200709_2347'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='time',
            field=models.IntegerField(help_text='有效期限：单位：年', verbose_name='有效期限'),
        ),
    ]