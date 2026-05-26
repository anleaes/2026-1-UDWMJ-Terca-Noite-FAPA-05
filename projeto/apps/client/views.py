from django.shortcuts import render, redirect, get_object_or_404

from accounts.decorators import employee_required
from .forms import ClientForm
from .models import Client


def _sync_user_from_client(client):
    if client.user_id:
        user = client.user
        user.first_name = client.first_name
        user.last_name = client.last_name
        user.email = client.email
        user.save()


@employee_required
def client_list(request):
    template_name = 'client/client_list.html'
    clients = Client.objects.all()
    context = {
        'clients': clients
    }

    return render(request, template_name, context)


@employee_required
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


@employee_required
def delete_client(request, pk):
    client = get_object_or_404(Client, pk=pk)
    user = client.user
    client.delete()
    if user:
        user.delete()
    return redirect('client:client_list')
