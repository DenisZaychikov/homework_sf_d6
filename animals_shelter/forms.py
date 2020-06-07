from django import forms
from django.forms import ModelForm
from .models import Animal


class AddAnimal(ModelForm):
    class Meta:
        model = Animal
        fields = '__all__'