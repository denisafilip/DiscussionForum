# Generated by Django 4.0 on 2021-12-28 14:53

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('discussion', '0002_reply_rate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reply',
            name='rate',
            field=models.FloatField(default=1, validators=[django.core.validators.MaxValueValidator(10), django.core.validators.MinValueValidator(1)]),
        ),
    ]