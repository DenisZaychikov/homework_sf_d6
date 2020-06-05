from django.shortcuts import render
from .models import Animal, AnimalType


def home(request):
    animals = Animal.objects.all()
    animal_types = AnimalType.objects.all()
    context = {'animals': animals,
               'animal_types': animal_types}
    return render(request, 'home.html', context)


def animal_detail(request, id):
    animal = Animal.objects.get(id=id)
    animal_types = AnimalType.objects.all()
    context = {'animal': animal,
               'animal_types': animal_types}
    return render(request, 'animal_detail.html', context)


def about_shelter(request):
    animal_types = AnimalType.objects.all()
    context = {'animal_types': animal_types}
    return render(request, 'about_shelter.html', context)


def animal_type_list(request, id):
    animal_type = AnimalType.objects.get(id=id)
    animal_types = AnimalType.objects.all()
    animals = Animal.objects.filter(animal_type=animal_type)
    context = {'animals': animals,
               'animal_type': animal_type,
               'animal_types': animal_types}
    return render(request, 'animal_type_list.html', context)

