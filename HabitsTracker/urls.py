from django.contrib import admin
from django.urls import path
from .views import addPerson, index, sayHello

urlpatterns = [
    path('', index),
    path('addperson', addPerson),
    path('<str:name>', sayHello)
]