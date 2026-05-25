from django.shortcuts import render, redirect, get_object_or_404

from .forms import EmployeeForm
from .models import Employee

# Create your views here.
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

def employee_list(request):
    template_name = 'employee/employee_list.html'
    employees = Employee.objects.all()
    context = {
        'employees': employees
    }

    return render(request, template_name, context)

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
    return render(request, template_name, context)

def delete_employee(request, pk):
    employee = Employee.objects.get(pk=pk)
    employee.delete()
    return redirect('employee:employee_list')