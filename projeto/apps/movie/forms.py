from django import forms
from .models import Movie


class EnglishClearableFileInput(forms.ClearableFileInput):
    initial_text = 'Current'
    input_text = 'Change'
    clear_checkbox_label = 'Clear'


class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = '__all__'
        widgets = {
            'genres': forms.CheckboxSelectMultiple(),
            'poster': EnglishClearableFileInput(),
        }