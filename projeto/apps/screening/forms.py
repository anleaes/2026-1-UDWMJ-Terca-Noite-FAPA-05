from django import forms
from .models import Screening

class ScreeningForm(forms.ModelForm):
    
    class Meta:
        model = Screening
        exclude = ()