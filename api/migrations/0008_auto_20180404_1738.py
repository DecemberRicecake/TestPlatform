# Generated by Django 2.0.1 on 2018-04-04 17:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_task_report'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='report',
            field=models.CharField(max_length=10000, null=True),
        ),
    ]