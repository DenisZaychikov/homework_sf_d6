from django.contrib import admin
from django.urls import path
from animals_shelter import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('animal/<int:id>/', views.animal_detail, name='animal_detail'),
    path('about_shelter/', views.about_shelter, name='about_shelter'),
    path('animal_type/<int:id>/', views.animal_type_list, name='animal_type'),
    path('add_animal/', views.add_animal, name='add_animal'),
    path('add_animal_type/', views.add_animal_type, name='add_animal_type'),
    path('search_animal_breed/', views.search_animal_breed, name='search_animal_breed')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
