from django.shortcuts import render, redirect, get_object_or_404

from .forms import RoomForm
from .models import Room
from cinema.models import Cinema
# Create your views here.
def add_room(request, cinema_id):
    template_name = 'room/add_room.html'
    cinema = get_object_or_404(Cinema, id=cinema_id)

    if request.method == 'POST':
        form = RoomForm(request.POST)

        if form.is_valid():
            room = form.save(commit=False)
            room.cinema = cinema
            room.save()

            return redirect('cinema:edit_cinema', cinema_id=cinema.id)
    else:
        form = RoomForm()

    context = {
        'form': form,
        'cinema': cinema
    }

    return render(request, template_name, context)


def edit_room(request, cinema_id, pk):
    template_name = 'room/add_room.html'

    room = get_object_or_404(Room, id=pk, cinema_id=cinema_id)

    if request.method == 'POST':
        form = RoomForm(request.POST, instance=room)

        if form.is_valid():
            room = form.save()
            return redirect('cinema:edit_cinema', cinema_id=room.cinema_id)
    else:
        form = RoomForm(instance=room)

    context = {
        'form': form,
        'cinema': room.cinema,
        'room': room
    }

    return render(request, template_name, context)


def delete_room(request, cinema_id, pk):
    room = get_object_or_404(Room, id=pk, cinema_id=cinema_id)
    room.delete()
    return redirect('cinema:edit_cinema', cinema_id=cinema_id)


def room_list(request, cinema_id):
    template_name = 'room/room_list.html'

    cinema = get_object_or_404(Cinema, id=cinema_id)
    rooms = Room.objects.filter(cinema_id=cinema.id)

    context = {
        'cinema': cinema,
        'rooms': rooms
    }

    return render(request, template_name, context)