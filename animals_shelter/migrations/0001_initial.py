# Generated by Django 2.2.6 on 2020-06-05 11:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Animal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('animal_name', models.CharField(max_length=100, verbose_name='Кличка')),
                ('breed', models.CharField(max_length=50, verbose_name='Порода')),
                ('description', models.TextField(help_text='Описание данного животного', verbose_name='Описание')),
                ('receipt_date', models.DateField(verbose_name='Дата поступления')),
                ('photo', models.ImageField(upload_to='', verbose_name='Фото')),
            ],
        ),
    ]
