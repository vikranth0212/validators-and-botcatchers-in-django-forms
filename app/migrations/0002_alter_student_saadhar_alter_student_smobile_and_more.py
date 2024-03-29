# Generated by Django 4.2.6 on 2024-01-11 13:09

import app.models
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='saadhar',
            field=models.CharField(max_length=12, unique=True, validators=[django.core.validators.RegexValidator('[1-9]\\d{11}')]),
        ),
        migrations.AlterField(
            model_name='student',
            name='smobile',
            field=models.CharField(max_length=10, unique=True, validators=[django.core.validators.RegexValidator('[6-9]\\d{9}')]),
        ),
        migrations.AlterField(
            model_name='student',
            name='sname',
            field=models.CharField(max_length=100, primary_key=True, serialize=False, validators=[app.models.validator_for_a]),
        ),
        migrations.AlterField(
            model_name='student',
            name='span',
            field=models.CharField(max_length=10, validators=[django.core.validators.RegexValidator('[\x07\\d]{10}')]),
        ),
    ]
