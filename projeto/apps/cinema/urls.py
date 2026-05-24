from django.urls import path
from . import views

app_name = 'cinema'

urlpatterns = [
    path('', views.cinema_list, name='cinema_list'),
    path('create/', views.cinema_create, name='add_cinema'),
    path('<int:pk>/edit/', views.cinema_edit, name='edit_cinema'),
    path('<int:pk>/delete/', views.cinema_delete, name='delete_cinema'),
]