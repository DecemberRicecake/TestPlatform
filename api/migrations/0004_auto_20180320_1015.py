# Generated by Django 2.0.1 on 2018-03-20 10:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20180320_0947'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='standardTime',
            field=models.TimeField(blank=True, null=True),
        ),
    ]
