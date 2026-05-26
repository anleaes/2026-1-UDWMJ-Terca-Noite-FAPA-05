from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import redirect, render, get_object_or_404
from django.urls import reverse

from accounts.decorators import employee_required
from .forms import EmployeeForm
from .models import Employee


@staff_member_required
def add_employee(request):
    return redirect(reverse('admin:employee_employee_add'))


@employee_required
def employee_list(request):
    template_name = 'employee/employee_list.html'
    employees = Employee.objects.all()
    context = {
        'employees': employees
    }

    return render(request, template_name, context)


@employee_required
def edit_employee(request, pk):
    return redirect(reverse('admin:employee_employee_change', args=[pk]))


@employee_required
def delete_employee(request, pk):
    return redirect(reverse('admin:employee_employee_delete', args=[pk]))
