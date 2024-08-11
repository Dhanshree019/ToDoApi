from django.urls import path
from .views import *
urlpatterns = [
    # path('mydata', ToDoView.as_view()),
    # path('home', home),

    path('home', home, name='home'),
    path('edit', edit_todo , name='edit'),
    path('delete', todo_delete , name='delete'),

]

