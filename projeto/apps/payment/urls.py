from django.urls import path
from . import views

app_name = 'payment'

urlpatterns = [
    path('', views.payment_list, name='payment_list'),
    path('order/<int:order_id>/add/', views.add_payment, name='add_payment'),
    path('order/<int:order_id>/delete/', views.delete_payment, name='delete_payment'),
    path('edit/<int:pk>/', views.edit_payment, name='edit_payment'),
]
