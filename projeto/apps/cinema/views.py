from django.shortcuts import render, get object_or_404, redirect

from .forms import CinemaForm
from .models import Cinema

# Create your views here.
def add_cinema(request):
    template_name = 'cinema/add_cinema.html'
    context = {}

    if request.method == 'POST':
        form = CinemaForm(request.POST)

        if form.is_valid():
            f = form.save(commit=False)
            f.save()

            return redirect('cinema:cinema_list')
    
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

def edit_cinema(request, id_cinema):
    template_name = 'cinema/add_cinema.html'
    context = {}
    cinema = get_object_or_404(Cinema, pk=id_cinema)

    if request.method == 'POST':
        form = CinemaForm(request.POST, instance=cinema)

        if form.is_valid():
            form.save()
            return redirect('cinema:cinema_list')
    
    form = CinemaForm(instance=cinema)
    context['form'] = form
    return render(request, template_name, context)

def delete_cinema(request, id_cinema):
    cinema = Cinema.objects.get(pk=id_cinema)
    cinema.delete()
    return redirect('cinema:cinema_list')