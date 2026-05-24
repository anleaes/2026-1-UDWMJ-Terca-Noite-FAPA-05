from django.urls import path
from . import views

app_name = 'client'

urlpatterns = [
    path('', views.client_list, name='client_list'),
    path('add/', views.add_client, name='add_client'),
    path('edit/<int:client_id>/', views.edit_client, name='edit_client'),
    path('delete/<int:client_id>/', views.delete_client, name='delete_client'),
]