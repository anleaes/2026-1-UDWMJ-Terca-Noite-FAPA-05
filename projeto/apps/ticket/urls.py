from django.urls import path
from . import views

app_name = 'ticket'

urlpatterns = [
    path('meus/', views.ticket_list, name='ticket_list'),
    path('order/<int:order_id>/seats/', views.select_seats, name='select_seats'),
]
