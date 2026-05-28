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

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['start_time'].input_formats = ['%Y-%m-%dT%H:%M', '%d/%m/%Y %H:%M']