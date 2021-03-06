# Generated by Django 3.2.4 on 2021-06-15 23:11

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_auto_20210615_2333'),
    ]

    operations = [
        migrations.AlterField(
            model_name='key',
            name='name',
            field=models.CharField(max_length=8),
        ),
        migrations.AlterField(
            model_name='key',
            name='value',
            field=models.CharField(max_length=16, unique=True, validators=[django.core.validators.MinLengthValidator(4)]),
        ),
    ]
