from django.shortcuts import render, redirect, get_object_or_404

from .forms import ClientForm
from .models import Client
from django.contrib.auth.decorators import login_required


def _sync_user_from_client(client):
    if client.user_id:
        user = client.user
        user.first_name = client.first_name
        user.last_name = client.last_name
        user.email = client.email
        user.save()


@login_required(login_url='/accounts/user_login/')
def client_list(request):
    template_name = 'client/client_list.html'
    clients = Client.objects.all()
    context = {
        'clients': clients
    }

    return render(request, template_name, context)


@login_required(login_url='/accounts/user_login/')
def add_client(request):
    template_name = 'client/add_client.html'
    context = {}

    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('client:client_list')
    else:
        form = ClientForm()

    context['form'] = form
    return render(request, template_name, context)


@login_required(login_url='/accounts/user_login/')
def edit_client(request, pk):
    template_name = 'client/add_client.html'
    context = {}
    client = get_object_or_404(Client, pk=pk)

    if request.method == 'POST':
        form = ClientForm(request.POST, instance=client)

        if form.is_valid():
            client = form.save()
            _sync_user_from_client(client)
            return redirect('client:client_list')
    else:
        form = ClientForm(instance=client)

    context['form'] = form
    context['editing'] = True
    return render(request, template_name, context)


@login_required(login_url='/accounts/user_login/')
def delete_client(request, pk):
    client = get_object_or_404(Client, pk=pk)
    user = client.user
    client.delete()
    if user:
        user.delete()
    return redirect('client:client_list')
