# Generated by Django 3.2.4 on 2021-06-15 22:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20210615_2146'),
    ]

    operations = [
        migrations.AlterField(
            model_name='key',
            name='value',
            field=models.CharField(max_length=8, unique=True),
        ),
    ]
