from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("breeds/list/all", views.dogs_breeds_list, name = "dogs_breeds_list"),
    path("breed/<str:breed_name>/image/random", views.dog_random_pic_by_breed, name = "dog_random_pic_by_breed"),
]