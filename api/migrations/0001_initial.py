# Generated by Django 2.0.1 on 2018-03-20 09:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Api',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('apiName', models.CharField(max_length=200)),
                ('url', models.CharField(max_length=200)),
                ('method', models.CharField(max_length=20)),
                ('questData', models.CharField(max_length=3000, null=True)),
                ('validators', models.CharField(max_length=3000, null=True)),
                ('extractFlag', models.BooleanField(default=False)),
                ('extracts', models.CharField(max_length=3000, null=True)),
                ('createTime', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='ApiHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('taskId', models.IntegerField()),
                ('caseId', models.IntegerField()),
                ('apiId', models.IntegerField()),
                ('taskName', models.CharField(max_length=200)),
                ('caseName', models.CharField(max_length=200)),
                ('apiName', models.CharField(max_length=200)),
                ('url', models.CharField(max_length=200)),
                ('questData', models.CharField(max_length=3000)),
                ('responseData', models.CharField(max_length=10000)),
                ('result', models.CharField(max_length=20, null=True)),
                ('startTime', models.DateTimeField(null=True)),
                ('endTime', models.DateTimeField(null=True)),
                ('createTime', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='CustomParameters',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('value', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=200, null=True)),
                ('createTime', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Environment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=200)),
                ('ip', models.CharField(max_length=200)),
                ('port', models.CharField(max_length=200)),
                ('createTime', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('projectName', models.CharField(max_length=200)),
                ('people', models.CharField(max_length=200, null=True)),
                ('description', models.CharField(max_length=200, null=True)),
                ('createTime', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('taskName', models.CharField(max_length=200)),
                ('caseIds', models.CharField(max_length=300, null=True)),
                ('taskType', models.CharField(max_length=200)),
                ('standardTime', models.DateTimeField(null=True)),
                ('createTime', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='TestCase',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('caseName', models.CharField(max_length=200)),
                ('apiIds', models.CharField(max_length=300, null=True)),
                ('caseDesc', models.CharField(max_length=500, null=True)),
                ('createTime', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userName', models.CharField(max_length=200)),
                ('account', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=50)),
                ('createTime', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.AddField(
            model_name='api',
            name='env',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Environment'),
        ),
        migrations.AddField(
            model_name='api',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Project'),
        ),
    ]
