from django.shortcuts import render, get_object_or_404, redirect

from accounts.decorators import employee_required
from .forms import CinemaForm
from .models import Cinema


@employee_required
def add_cinema(request):
    template_name = 'cinema/add_cinema.html'
    context = {}

    if request.method == 'POST':
        form = CinemaForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('cinema:cinema_list')
    else:
        form = CinemaForm()

    context['form'] = form
    return render(request, template_name, context)


def cinema_list(request):
    template_name = 'cinema/cinema_list.html'
    cinemas = Cinema.objects.filter()
    context = {
        'cinemas': cinemas
    }

    return render(request, template_name, context)


@employee_required
def edit_cinema(request, pk):
    template_name = 'cinema/edit_cinema.html'

    cinema = get_object_or_404(Cinema, pk=pk)

    if request.method == 'POST':
        form = CinemaForm(
            request.POST,
            instance=cinema
        )

        if form.is_valid():
            form.save()

            return redirect('cinema:cinema_list')

    else:
        form = CinemaForm(instance=cinema)

    rooms = cinema.rooms.all()

    context = {
        'cinema_form': form,
        'cinema': cinema,
        'rooms': rooms
    }

    return render(request, template_name, context)


@employee_required
def delete_cinema(request, pk):
    cinema = Cinema.objects.get(pk=pk)
    cinema.delete()
    return redirect('cinema:cinema_list')
