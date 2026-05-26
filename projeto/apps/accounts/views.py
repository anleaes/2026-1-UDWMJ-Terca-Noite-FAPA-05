from django.contrib import messages
from django.core.exceptions import PermissionDenied
from django.shortcuts import render, redirect

from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm

from client.models import Client
from .forms import ClientRegistrationForm, UserChangeInformationForm

LOGIN_URL = '/accounts/user_login/'

# Create your views here.

def add_user(request):
    template_name = 'accounts/add_user.html'
    context = {}

    if request.method == 'POST':
        form = ClientRegistrationForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = User.objects.create_user(
                username=data['username'],
                password=data['password'],
                email=data['email'],
                first_name=data['first_name'],
                last_name=data['last_name'],
            )
            Client.objects.create(
                user=user,
                first_name=data['first_name'],
                last_name=data['last_name'],
                email=data['email'],
                address=data['address'],
                phone=data['phone'],
                gender=data['gender'],
                cpf=data['cpf'],
                date_of_birth=data['date_of_birth'],
            )
            return redirect('accounts:user_login')
        context['form'] = form
    else:
        context['form'] = ClientRegistrationForm()

    return render(request, template_name, context)


def user_login(request):
    template_name = 'accounts/user_login.html'
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            next_url = request.GET.get('next')
            if next_url:
                return redirect(next_url)
            if hasattr(user, 'client_profile'):
                return redirect('core:home')
            if user.is_staff or user.is_superuser:
                return redirect('cinema:cinema_list')
            return redirect('core:home')
        else:
            return redirect('accounts:user_login')
    return render(request, template_name, {})


@login_required(login_url=LOGIN_URL)
def user_logout(request):
    logout(request)
    return redirect('accounts:user_login')


@login_required(login_url=LOGIN_URL)
def user_change_password(request):
    template_name = 'accounts/user_change_password.html'
    if request.method == 'POST':
        form = PasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            messages.success(request, 'Password changed successfully.')
            return redirect('accounts:user_change_password')
    else:
        form = PasswordChangeForm(user=request.user)
    return render(request, template_name, {'form': form})


@login_required(login_url=LOGIN_URL)
def user_change_information(request, username):
    if request.user.username != username:
        raise PermissionDenied
    template_name = 'accounts/user_change_information.html'
    context = {}
    user = request.user
    if request.method == 'POST':
        form = UserChangeInformationForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            if hasattr(request.user, 'client_profile'):
                client = request.user.client_profile
                client.first_name = user.first_name
                client.last_name = user.last_name
                client.email = user.email
                client.save()
    form = UserChangeInformationForm(instance=user)
    context['form'] = form
    return render(request, template_name, context)