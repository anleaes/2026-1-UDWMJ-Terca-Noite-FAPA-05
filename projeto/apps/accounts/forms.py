from django import forms
from django.contrib.auth.models import User

from client.models import Client


class UserChangeInformationForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']


class ClientRegistrationForm(forms.Form):
    first_name = forms.CharField(max_length=100, label='Name')
    last_name = forms.CharField(max_length=100, label='Last Name')
    username = forms.CharField(max_length=150, label='Username')
    password = forms.CharField(widget=forms.PasswordInput, label='Password')
    email = forms.EmailField(label='Email')
    address = forms.CharField(max_length=200, label='Address')
    phone = forms.CharField(max_length=20, label='Phone')
    gender = forms.ChoiceField(
        choices=Client._meta.get_field('gender').choices,
        label='Gender',
    )
    cpf = forms.CharField(max_length=11, label='CPF')
    date_of_birth = forms.DateField(
        label='Date of Birth',
        widget=forms.DateInput(attrs={'type': 'date'}),
    )

    def clean_username(self):
        username = self.cleaned_data['username']
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError('This username is already in use.')
        return username

    def clean_cpf(self):
        cpf = self.cleaned_data['cpf']
        if Client.objects.filter(cpf=cpf).exists():
            raise forms.ValidationError('This CPF is already registered.')
        return cpf
