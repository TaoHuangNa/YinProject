# Generated by Django 2.1.1 on 2020-06-28 21:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0017_auto_20200628_1111'),
    ]

    operations = [
        migrations.AlterField(
            model_name='completetasks',
            name='complete_user',
            field=models.ForeignKey(help_text='完成人', max_length=11, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='complete_task', to=settings.AUTH_USER_MODEL, to_field='username', verbose_name='完成人'),
        ),
        migrations.AlterField(
            model_name='tasks',
            name='created',
            field=models.ForeignKey(help_text='创建人', max_length=11, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='created_task', to=settings.AUTH_USER_MODEL, to_field='username', verbose_name='创建人'),
        ),
    ]