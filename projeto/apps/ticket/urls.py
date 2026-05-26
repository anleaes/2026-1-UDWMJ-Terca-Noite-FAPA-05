from django.urls import path
from . import views

app_name = 'ticket'

urlpatterns = [
    path('meus/', views.my_tickets, name='my_tickets'),
    path('add/<int:pk>/', views.add_ticket, name='add_ticket'),
]
