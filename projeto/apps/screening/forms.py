from django import forms
from .models import Screening


class ScreeningForm(forms.ModelForm):
    class Meta:
        model = Screening
        fields = '__all__'
        widgets = {
            'start_time': forms.DateTimeInput(
                attrs={'type': 'datetime-local'},
                format='%Y-%m-%dT%H:%M',
            ),
        }
