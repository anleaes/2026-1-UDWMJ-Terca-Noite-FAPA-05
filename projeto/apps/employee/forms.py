from django import forms

from .models import Employee


class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        widgets = {
            'hire_date': forms.DateInput(attrs={'type': 'date'}),
        }
        fields = '__all__'