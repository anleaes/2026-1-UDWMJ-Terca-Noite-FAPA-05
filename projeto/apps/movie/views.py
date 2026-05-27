from django.shortcuts import render, get_object_or_404, redirect

from .models import Movie
from .forms import MovieForm
from django.contrib.auth.decorators import login_required


@login_required(login_url='/accounts/user_login/')
def add_movie(request):
    template_name = 'movie/add_movie.html'
    context = {}

    if request.method == 'POST':
        form = MovieForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect('movie:movie_list')
    else:
        form = MovieForm()

    context['form'] = form

    return render(request, template_name, context)


def movie_list(request):
    template_name = 'movie/movie_list.html'
    context = {}

    movies = Movie.objects.all()
    context['movies'] = movies

    return render(request, template_name, context)


@login_required(login_url='/accounts/user_login/')
def edit_movie(request, pk):
    template_name = 'movie/add_movie.html'
    context = {}

    movie = get_object_or_404(Movie, pk=pk)

    if request.method == 'POST':
        form = MovieForm(
            request.POST,
            request.FILES,
            instance=movie
        )

        if form.is_valid():
            form.save()
            return redirect('movie:movie_list')
    else:
        form = MovieForm(instance=movie)

    context['form'] = form

    return render(request, template_name, context)


@login_required(login_url='/accounts/user_login/')
def delete_movie(request, movie_id):
    movie = get_object_or_404(Movie, pk=movie_id)

    movie.delete()

    return redirect('movie:movie_list')
