from django.contrib import admin
from .models import Animal, AnimalType


@admin.register(Animal)
class AnimalAdmin(admin.ModelAdmin):
    list_display = ('animal_name', 'breed', 'receipt_date')


@admin.register(AnimalType)
class AnimalTypeAdmin(admin.ModelAdmin):
    pass


