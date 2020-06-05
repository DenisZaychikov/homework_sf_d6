from django.db import models


class AnimalType(models.Model):
    type_name = models.CharField(max_length=50, verbose_name='Вид животного')

    def __str__(self):
        return self.type_name


class Animal(models.Model):
    animal_name = models.CharField(max_length=100, verbose_name='Кличка')
    breed = models.CharField(max_length=50, verbose_name='Порода')
    description = models.TextField(verbose_name='Описание', help_text='Описание данного животного')
    receipt_date = models.DateField(verbose_name='Дата поступления')
    photo = models.ImageField(verbose_name='Фото')
    animal_type = models.ForeignKey(AnimalType,  null=True, on_delete=models.CASCADE, verbose_name='Тип животного')

    def __str__(self):
        return self.animal_name