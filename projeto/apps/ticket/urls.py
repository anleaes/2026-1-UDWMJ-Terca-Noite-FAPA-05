from django.urls import path
from . import views

app_name = 'ticket'

urlpatterns = [
    path('', views.ticket_list, name='ticket_list'),
    path('add/<int:pk>/', views.add_ticket, name='add_ticket'),
    path('delete/<int:pk>/', views.delete_ticket, name='delete_ticket'),
]
