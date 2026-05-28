from django.shortcuts import redirect, render, get_object_or_404
from django.urls import reverse

from .forms import EmployeeForm
from .models import Employee
from django.contrib.auth.decorators import login_required


@login_required(login_url='/accounts/user_login/')
def add_employee(request):
    template_name = 'employee/add_employee.html'
    context = {}

    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('employee:employee_list')
    else:
        form = EmployeeForm()

    context['form'] = form
    return render(request, template_name, context)


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
    template_name = 'employee/add_employee.html'
    context = {}
    employee = get_object_or_404(Employee, pk=pk)

    if request.method == 'POST':
        form = EmployeeForm(request.POST, instance=employee)

        if form.is_valid():
            form.save()
            return redirect('employee:employee_list')
    else:
        form = EmployeeForm(instance=employee)

    context['form'] = form
    context['editing'] = True
    return render(request, template_name, context)


@login_required(login_url='/accounts/user_login/')
def delete_employee(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    employee.delete()
    return redirect('employee:employee_list')