from django import forms
from .models import Room

class RoomForm(forms.ModelForm):
    class Meta:
        model = Room
        fields = ['rows', 'columns', 'projection_type', 'accessibility']