from django.urls import path
from . import views

app_name = 'ticket'

urlpatterns = [
    path('', views.ticket_list, name='ticket_list'),
    path('order/<int:order_id>/add/', views.add_ticket, name='add_ticket'),
    path('order/<int:order_id>/add/seat/', views.add_ticket_seat, name='add_ticket_seat'),
    path('order/<int:order_id>/<int:pk>/delete/', views.delete_ticket, name='delete_ticket'),
]
