# Generated by Django 2.2.6 on 2020-06-07 16:34

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('animals_shelter', '0002_remove_animal_receipt_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='animal',
            name='receipt_date',
            field=models.DateField(default=datetime.date(2020, 6, 7), verbose_name='Дата поступления'),
        ),
    ]