from django.urls import path
from .views import *
urlpatterns = [
    path('mydata', ToDoView.as_view())
]

