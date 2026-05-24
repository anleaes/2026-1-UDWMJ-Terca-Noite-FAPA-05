from django.shortcuts import render, redirect, get_object_or_404

from .forms import ClientForm
from .models import Client

# Create your views here.
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

def client_list(request):
    template_name = 'client/client_list.html'
    clients = Client.objects.all()
    context = {
        'clients': clients
    }

    return render(request, template_name, context)

def edit_client(request, pk):
    template_name = 'client/add_client.html'
    context = {}
    client = get_object_or_404(Client, pk=pk)

    if request.method == 'POST':
        form = ClientForm(request.POST, instance=client)

        if form.is_valid():
            form.save()
            return redirect('client:client_list')
    else:
        form = ClientForm(instance=client)

    context['form'] = form
    return render(request, template_name, context)

def delete_client(request, pk):
    client = Client.objects.get(pk=pk)
    client.delete()
    return redirect('client:client_list')