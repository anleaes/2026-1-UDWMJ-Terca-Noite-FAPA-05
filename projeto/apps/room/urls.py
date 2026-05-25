from django.urls import path
from . import views

app_name = 'room'

urlpatterns = [
    path('cinema/<int:cinema_id>/rooms/', views.room_list, name='room_list'),
    path('cinema/<int:cinema_id>/rooms/add/', views.add_room, name='add_room'),
    path('cinema/<int:cinema_id>/rooms/<int:pk>/edit/', views.edit_room, name='edit_room'),
    path('cinema/<int:cinema_id>/rooms/<int:pk>/delete/', views.delete_room, name='delete_room'),
]