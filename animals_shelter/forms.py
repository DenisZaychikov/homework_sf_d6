from django import forms
from django.forms import ModelForm
from .models import Animal, AnimalType


class AddAnimal(ModelForm):
    class Meta:
        model = Animal
        fields = '__all__'


class AddAnimalType(ModelForm):
    class Meta:
        model = AnimalType
        fields = '__all__'
