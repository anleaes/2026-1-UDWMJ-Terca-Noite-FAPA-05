from django.urls import path
from . import views

app_name = 'payment'

urlpatterns = [
    path('', views.payment_list, name='payment_list'),
    path('pending/', views.pending_payments, name='pending_payments'),
    path('checkout/<int:order_id>/', views.checkout, name='checkout'),
    path('<int:pk>/approve/', views.approve_payment, name='approve_payment'),
    path('<int:pk>/reject/', views.reject_payment, name='reject_payment'),
]
