from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404

from .models import Ticket


@login_required(login_url='/accounts/user_login/')
def ticket_list(request):
    template_name = 'ticket/ticket_list.html'
    tickets = Ticket.objects.all()
    context = {'tickets': tickets}
    return render(request, template_name, context)


@login_required(login_url='/accounts/user_login/')
def add_ticket(request, pk):
    return redirect('order:order_list')


@login_required(login_url='/accounts/user_login/')
def delete_ticket(request, pk):
    ticket = get_object_or_404(Ticket, pk=pk)
    ticket.delete()
    return redirect('ticket:ticket_list')
