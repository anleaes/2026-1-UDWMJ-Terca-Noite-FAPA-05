from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404

from order.models import Order
from screening.models import Screening

from .models import Ticket


@login_required(login_url='/accounts/user_login/')
def ticket_list(request):
    template_name = 'ticket/ticket_list.html'
    tickets = Ticket.objects.all()
    context = {'tickets': tickets}
    return render(request, template_name, context)


@login_required(login_url='/accounts/user_login/')
def add_ticket(request, order_id):
    template_name = 'ticket/add_ticket.html'
    order = get_object_or_404(Order, pk=order_id)
    screenings = Screening.objects.all()
    context = {
        'order': order,
        'screenings': screenings,
        'screening': None,
        'available_seats': [],
    }
    return render(request, template_name, context)


@login_required(login_url='/accounts/user_login/')
def add_ticket_seat(request, order_id):
    template_name = 'ticket/add_ticket.html'
    order = get_object_or_404(Order, pk=order_id)

    screening = get_object_or_404(Screening, pk=request.POST.get('screening'))

    tickets = Ticket.objects.filter(screening=screening)
    used_seats = tickets.values_list('seat_id', flat=True)
    available_seats = screening.room.seats.exclude(id__in=used_seats)

    if request.POST.get('seat'):
        seat = get_object_or_404(available_seats, pk=request.POST.get('seat'))
        Ticket.objects.create(order=order, screening=screening, seat=seat)
        order.total_price = sum(t.screening.price for t in order.tickets.all())
        order.save()
        if hasattr(order, 'payment'):
            order.payment.charged_amount = order.total_price
            order.payment.save()
        return redirect('order:edit_order', order_id=order.id)

    context = {
        'order': order,
        'screening': screening,
        'screenings': [],
        'available_seats': available_seats,
    }
    return render(request, template_name, context)


@login_required(login_url='/accounts/user_login/')
def delete_ticket(request, order_id, pk):
    order = get_object_or_404(Order, pk=order_id)
    ticket = get_object_or_404(Ticket, pk=pk, order_id=order_id)
    ticket.delete()
    order.total_price = sum(t.screening.price for t in order.tickets.all())
    order.save()
    if hasattr(order, 'payment'):
        order.payment.charged_amount = order.total_price
        order.payment.save()
    return redirect('order:edit_order', order_id=order_id)
