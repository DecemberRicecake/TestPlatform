# Generated by Django 2.0.1 on 2018-05-09 16:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0010_task_hasreport'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='status',
            field=models.IntegerField(default=1),
        ),
    ]
