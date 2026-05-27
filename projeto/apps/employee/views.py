from django.shortcuts import redirect, render, get_object_or_404
from django.urls import reverse

from .forms import EmployeeForm
from .models import Employee
from django.contrib.auth.decorators import login_required


@login_required(login_url='/accounts/user_login/')
def add_employee(request):
    return redirect(reverse('admin:employee_employee_add'))


@login_required(login_url='/accounts/user_login/')
def employee_list(request):
    template_name = 'employee/employee_list.html'
    employees = Employee.objects.all()
    context = {
        'employees': employees
    }

    return render(request, template_name, context)


@login_required(login_url='/accounts/user_login/')
def edit_employee(request, pk):
    return redirect(reverse('admin:employee_employee_change', args=[pk]))


@login_required(login_url='/accounts/user_login/')
def delete_employee(request, pk):
    return redirect(reverse('admin:employee_employee_delete', args=[pk]))
