from django.shortcuts import render, redirect, get_object_or_404

from .forms import GenreForm
from .models import Genre
from django.contrib.auth.decorators import login_required

@login_required(login_url='/accounts/user_login/')
def add_genre(request):
    template_name = 'genre/add_genre.html'
    context = {}

    if request.method == 'POST':
        form = GenreForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('genre:genre_list')
    else:
        form = GenreForm()

    context['form'] = form
    return render(request, template_name, context)


@login_required(login_url='/accounts/user_login/')
def genre_list(request):
    template_name = 'genre/genre_list.html'
    genres = Genre.objects.all()
    context = {
        'genres': genres
    }

    return render(request, template_name, context)


@login_required(login_url='/accounts/user_login/')
def edit_genre(request, pk):
    template_name = 'genre/add_genre.html'
    context = {}
    genre = get_object_or_404(Genre, pk=pk)

    if request.method == 'POST':
        form = GenreForm(request.POST, instance=genre)

        if form.is_valid():
            form.save()
            return redirect('genre:genre_list')
    else:
        form = GenreForm(instance=genre)

    context['form'] = form
    return render(request, template_name, context)


@login_required(login_url='/accounts/user_login/')
def delete_genre(request, pk):
    genre = get_object_or_404(Genre, pk=pk)
    genre.delete()
    return redirect('genre:genre_list')
