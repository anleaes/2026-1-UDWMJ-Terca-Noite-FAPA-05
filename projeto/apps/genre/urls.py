from django.urls import path
from . import views

app_name = 'genre'

urlpatterns = [
    path('', views.genre_list, name='genre_list'),
    path('add/', views.add_genre, name='add_genre'),
    path('edit/<int:pk>/', views.edit_genre, name='edit_genre'),
    path('delete/<int:pk>/', views.delete_genre, name='delete_genre'),
]