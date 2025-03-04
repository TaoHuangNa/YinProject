# Generated by Django 2.1.1 on 2020-07-04 23:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0010_auto_20200704_2306'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='member_level',
            field=models.ForeignKey(blank=True, default=0, help_text='会员等级', null=True, on_delete=django.db.models.deletion.SET_NULL, to='users.Member', verbose_name='会员等级'),
        ),
    ]
