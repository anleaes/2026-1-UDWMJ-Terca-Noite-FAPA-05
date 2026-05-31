from django.urls import path
from . import views

app_name = 'payment'

urlpatterns = [
    path('', views.payment_list, name='payment_list'),
    path('edit/<int:pk>/', views.edit_payment, name='edit_payment'),
    path('delete/<int:pk>/', views.delete_payment, name='delete_payment'),
]
