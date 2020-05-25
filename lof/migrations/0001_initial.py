# Generated by Django 3.0.3 on 2020-05-25 16:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('openid', models.CharField(blank=True, max_length=50, null=True)),
                ('truename', models.CharField(blank=True, max_length=30, null=True)),
                ('text', models.CharField(blank=True, max_length=500, null=True)),
                ('photo', models.CharField(blank=True, max_length=500, null=True)),
                ('date', models.CharField(blank=True, max_length=100, null=True)),
                ('time', models.CharField(blank=True, max_length=100, null=True)),
                ('phoneNumber', models.CharField(blank=True, max_length=30, null=True)),
                ('qqNumber', models.CharField(blank=True, max_length=30, null=True)),
                ('status', models.CharField(blank=True, max_length=10, null=True)),
                ('type', models.CharField(blank=True, max_length=10, null=True)),
                ('iscard', models.CharField(blank=True, max_length=10, null=True)),
            ],
            options={
                'db_table': 'event',
            },
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('openid', models.CharField(max_length=50, unique=True)),
                ('truename', models.CharField(blank=True, max_length=30, null=True)),
                ('college', models.CharField(blank=True, max_length=30, null=True)),
                ('cardNumber', models.CharField(blank=True, max_length=30, null=True)),
                ('phoneNumber', models.CharField(blank=True, max_length=30, null=True)),
                ('qqNumber', models.CharField(blank=True, max_length=30, null=True)),
                ('email', models.CharField(blank=True, max_length=30, null=True)),
            ],
            options={
                'db_table': 'student',
            },
        ),
    ]
