from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('add_user/',views.add_user, name='add_user'),
    path('user_login/',views.user_login, name='user_login'),
    path('user_logout/',views.user_logout, name='user_logout'),
    path('user_change_password/',views.user_change_password, name='user_change_password'),
    path('user_change_information/<username>/',views.user_change_information, name='user_change_information'),
]