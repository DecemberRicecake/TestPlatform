# Generated by Django 2.0.1 on 2018-05-11 17:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0013_auto_20180511_1739'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='taskType',
            field=models.IntegerField(default=0),
        ),
    ]
