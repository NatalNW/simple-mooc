# Generated by Django 4.0.4 on 2022-05-04 15:45

import django.core.validators
from django.db import migrations, models
import re


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20211021_2225'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(max_length=30, unique=True, validators=[django.core.validators.RegexValidator(re.compile('^[\\w.@+--]+$'), 'The username can only contain letters, digits or the following characters: @/./+/-/_', 'invalid')], verbose_name='Username'),
        ),
    ]
