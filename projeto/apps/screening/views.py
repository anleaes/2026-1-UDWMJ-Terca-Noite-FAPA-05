from django.shortcuts import render, get_object_or_404, redirect

from accounts.decorators import employee_required
from .models import Screening
from .forms import ScreeningForm


def screening_list(request):
    template_name = 'screening/screening_list.html'
    screenings = Screening.objects.filter()
    context = {
        'screenings': screenings
    }

    return render(request, template_name, context)


@employee_required
def add_screening(request):
    template_name = 'screening/add_screening.html'

    if request.method == 'POST':
        form = ScreeningForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('screening:screening_list')
    else:
        form = ScreeningForm()

    context = {
        'form': form
    }

    return render(request, template_name, context)


@employee_required
def edit_screening(request, pk):
    template_name = 'screening/add_screening.html'

    screening = get_object_or_404(Screening, pk=pk)

    if request.method == 'POST':
        form = ScreeningForm(request.POST, instance=screening)

        if form.is_valid():
            form.save()
            return redirect('screening:screening_list')
    else:
        form = ScreeningForm(instance=screening)

    context = {
        'form': form,
    }

    return render(request, template_name, context)


@employee_required
def delete_screening(request, pk):
    screening = get_object_or_404(Screening, pk=pk)
    screening.delete()
    return redirect('screening:screening_list')
