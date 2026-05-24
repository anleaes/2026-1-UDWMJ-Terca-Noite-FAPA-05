from django.urls import path
from . import views

app_name = 'cinema'

urlpatterns = [
    path('', views.cinema_list, name='cinema_list'),
    path('create/', views.add_cinema, name='add_cinema'),
    path('<int:pk>/edit/', views.edit_cinema, name='edit_cinema'),
    path('<int:pk>/delete/', views.delete_cinema, name='delete_cinema'),
]