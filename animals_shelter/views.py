from django.shortcuts import render, redirect
from .models import Animal, AnimalType
from .forms import AddAnimal, AddAnimalType


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


def add_animal(request):
    if request.method == 'POST':
        form = AddAnimal(request.POST, request.FILES)
        form.save()
        return redirect('home')
    else:
        form = AddAnimal()
        animal_types = AnimalType.objects.all()
        context = {
            'form': form,
            'animal_types': animal_types
        }
        return render(request, 'add_animal.html', context)


def add_animal_type(request):
    if request.method == 'POST':
        form = AddAnimalType(request.POST)
        form.save()
        return redirect('home')
    else:
        form = AddAnimalType()
        animal_types = AnimalType.objects.all()
        context = {
            'form': form,
            'animal_types': animal_types
        }
        return render(request, 'add_animal_type.html', context)


def search_animal_breed(request):
    breed = request.GET.get('breed')
    animals = Animal.objects.filter(breed=breed).all()
    animal_types = AnimalType.objects.all()
    context = {
        'animals': animals,
        'animal_types': animal_types
    }
    return render(request, 'search_animal_breed.html', context)