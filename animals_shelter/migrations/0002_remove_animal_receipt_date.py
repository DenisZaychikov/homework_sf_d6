# Generated by Django 2.2.6 on 2020-06-07 16:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('animals_shelter', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='animal',
            name='receipt_date',
        ),
    ]
