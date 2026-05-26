from django.shortcuts import render, redirect, get_object_or_404

from accounts.decorators import employee_required
from .forms import RoomForm
from .models import Room
from cinema.models import Cinema


@employee_required
def add_room(request, cinema_id):
    template_name = 'room/add_room.html'
    cinema = get_object_or_404(Cinema, pk=cinema_id)

    if request.method == 'POST':
        form = RoomForm(request.POST)

        if form.is_valid():
            room = form.save(commit=False)
            room.cinema = cinema
            room.save()

            return redirect('cinema:edit_cinema', pk=cinema.id)
    else:
        form = RoomForm()

    context = {
        'form': form,
        'cinema': cinema
    }

    return render(request, template_name, context)


@employee_required
def edit_room(request, cinema_id, pk):
    template_name = 'room/add_room.html'

    room = get_object_or_404(Room, pk=pk, cinema_id=cinema_id)

    if request.method == 'POST':
        form = RoomForm(request.POST, instance=room)

        if form.is_valid():
            form.save()
            return redirect('cinema:edit_cinema', pk=room.cinema_id)
    else:
        form = RoomForm(instance=room)

    context = {
        'form': form,
        'cinema': room.cinema,
        'room': room
    }

    return render(request, template_name, context)


@employee_required
def delete_room(request, cinema_id, pk):
    room = get_object_or_404(Room, pk=pk, cinema_id=cinema_id)
    room.delete()
    return redirect('cinema:edit_cinema', pk=cinema_id)


def room_list(request, cinema_id):
    template_name = 'room/room_list.html'

    cinema = get_object_or_404(Cinema, pk=cinema_id)
    rooms = Room.objects.filter(cinema=cinema)

    context = {
        'cinema': cinema,
        'rooms': rooms
    }

    return render(request, template_name, context)
