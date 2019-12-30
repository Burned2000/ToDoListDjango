from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('viewToDo',views.ViewToDo,name='ViewToDo'),
    path('DeleteToDo/<int:todos_id>/',views.deleteToDo,name="delete"),
]
