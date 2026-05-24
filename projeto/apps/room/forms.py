from django import forms
from .models import ScreeningRoom

class RoomForm(forms.ModelForm):
    class Meta:
        model = Room
        fields = ['capacity', 'projection_type', 'accessibility']