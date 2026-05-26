from django.urls import path
from . import views

app_name = 'screening'

urlpatterns = [
    path('/', views.screening_list, name='screening_list'),
    path('add/', views.add_screening, name='add_screening'),
    path('<int:pk>/edit/', views.edit_screening, name='edit_screening'),
    path('<int:pk>/delete/', views.delete_screening, name='delete_screening'),
]