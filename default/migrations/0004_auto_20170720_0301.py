# Generated by Django 2.0 on 2017-07-20 03:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('default', '0003_auto_20170720_0258'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='sex',
            field=models.BooleanField(choices=[('男', 'True'), ('女', 'False')]),
        ),
    ]
