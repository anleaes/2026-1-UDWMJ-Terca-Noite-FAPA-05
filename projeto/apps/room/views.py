from django.shortcuts import render, redirect, get_object_or_404

from .forms import RoomForm
from .models import Room
# Create your views here.
def add_room(request, cinema_id):
    template_name = 'room/add_room.html'
    context = {}

    if request.method == 'POST':
        form = RoomForm(request.POST)

        if form.is_valid():
            room = form.save(commit=False)
            room.cinema_id = cinema_id
            room.save()
            return redirect('cinema:cinema_list')
    else:
        form = RoomForm()

    context['form'] = form
    return render(request, template_name, context)

def edit_room(request, pk):
    template_name = 'room/add_room.html'
    context = {}
    room = get_object_or_404(Room, pk=pk)

    if request.method == 'POST':
        form = RoomForm(request.POST, instance=room)

        if form.is_valid():
            form.save()
            return redirect('cinema:cinema_list')
    else:
        form = RoomForm(instance=room)

    context['form'] = form
    return render(request, template_name, context)

def delete_room(request, pk):
    room = get_object_or_404(Room, pk=pk)
    if request.method == 'POST':
        room.delete()
        return redirect('cinema:cinema_list')
    return render(request, 'room/confirm_delete.html', {'room': room})

def room_list(request, cinema_id):
    template_name = 'room/room_list.html'
    rooms = Room.objects.filter(cinema_id=cinema_id)
    context = {
        'rooms': rooms
    }

    return render(request, template_name, context)


