from decimal import Decimal

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect, render
from order.models import Order
from order.utils import orders_for_user, tickets_for_user
from seat.models import Seat

from .models import Ticket


def _occupied_seat_ids(screening):
    return set(
        Ticket.objects.filter(screening=screening).values_list('seat_id', flat=True)
    )


def _get_user_order(order_id, user):
    return get_object_or_404(
        Order,
        Q(pk=order_id) & orders_for_user(user),
    )


@login_required(login_url='/accounts/user_login/')
def ticket_list(request):
    tickets = (
        Ticket.objects.filter(tickets_for_user(request.user))
        .select_related('screening', 'seat', 'order')
        .order_by('-id')
    )
    return render(request, 'ticket/ticket_list.html', {'tickets': tickets})


@login_required(login_url='/accounts/user_login/')
def select_seats(request, order_id):
    order = _get_user_order(order_id, request.user)
    screening = order.screening
    if screening is None:
        messages.error(request, 'This order has no screening.')
        return redirect('order:order_list')

    room = screening.room
    occupied_ids = _occupied_seat_ids(screening)
    all_seats = Seat.objects.filter(room=room).order_by('row', 'number')

    if request.method == 'POST':
        if order.status != Order.STATUS_PENDING_SEATS:
            messages.error(request, 'Seats can only be selected while the order is pending seats.')
            return redirect('order:order_detail', pk=order.pk)

        seat_ids = request.POST.getlist('seats')
        if not seat_ids:
            messages.error(request, 'Select at least one seat.')
            return redirect('ticket:select_seats', order_id=order.pk)

        try:
            with transaction.atomic():
                order.tickets.all().delete()
                total = Decimal('0')
                for seat_id in seat_ids:
                    seat = get_object_or_404(Seat, pk=seat_id, room=room)
                    if Ticket.objects.filter(screening=screening, seat=seat).exists():
                        raise ValueError(f'Seat {seat} is no longer available.')

                    Ticket.objects.create(
                        order=order,
                        screening=screening,
                        seat=seat,
                        unit_price=screening.price,
                    )
                    total += screening.price

                order.total_price = total
                order.status = Order.STATUS_PENDING_PAYMENT
                order.save()
        except ValueError as exc:
            messages.error(request, str(exc))
            return redirect('ticket:select_seats', order_id=order.pk)

        messages.success(request, 'Seats reserved. Proceed to payment.')
        return redirect('payment:checkout', order_id=order.pk)

    seat_rows = []
    current_row = None
    row_items = []
    for seat in all_seats:
        if current_row != seat.row:
            if current_row is not None:
                seat_rows.append({'row': current_row, 'items': row_items})
            current_row = seat.row
            row_items = []
        row_items.append(
            {
                'seat': seat,
                'occupied': seat.id in occupied_ids,
            }
        )
    if current_row is not None:
        seat_rows.append({'row': current_row, 'items': row_items})

    return render(
        request,
        'ticket/select_seats.html',
        {
            'order': order,
            'screening': screening,
            'seat_rows': seat_rows,
        },
    )
