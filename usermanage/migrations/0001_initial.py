# Generated by Django 2.1.2 on 2018-11-16 11:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Token',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('token', models.CharField(max_length=50, verbose_name='token')),
                ('createTime', models.DateTimeField(auto_now=True, verbose_name='创建时间')),
            ],
            options={
                'verbose_name': '用户token',
                'db_table': 'UserToken',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=20, unique=True, verbose_name='用户名')),
                ('password', models.CharField(max_length=100, verbose_name='密码')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='邮箱')),
                ('createTime', models.DateTimeField(auto_now=True, verbose_name='创建时间')),
            ],
            options={
                'verbose_name': '用户信息',
                'db_table': 'UserInfo',
            },
        ),
        migrations.AddField(
            model_name='token',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='usermanage.User'),
        ),
    ]
