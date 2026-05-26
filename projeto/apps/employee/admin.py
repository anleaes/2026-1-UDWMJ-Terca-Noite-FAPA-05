from django import forms
from django.contrib import admin
from django.contrib.auth.models import User

from .models import Employee


class EmployeeAdminForm(forms.ModelForm):
    username = forms.CharField(max_length=150, label='Username (login)')
    password = forms.CharField(
        widget=forms.PasswordInput,
        label='Password',
        required=False,
        help_text='Required when creating a new employee.',
    )

    class Meta:
        model = Employee
        exclude = ['user']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance and self.instance.pk and self.instance.user_id:
            self.fields['username'].initial = self.instance.user.username
            self.fields['password'].required = False
            self.fields['password'].help_text = 'Leave blank to keep the current password.'

    def clean_username(self):
        username = self.cleaned_data['username']
        qs = User.objects.filter(username=username)
        if self.instance and self.instance.pk and self.instance.user_id:
            qs = qs.exclude(pk=self.instance.user_id)
        if qs.exists():
            raise forms.ValidationError('This username is already in use.')
        return username

    def clean(self):
        cleaned = super().clean()
        is_new = not self.instance or not self.instance.pk
        if is_new and not cleaned.get('password'):
            raise forms.ValidationError('Enter a password for the new employee.')
        return cleaned


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    form = EmployeeAdminForm
    list_display = ('first_name', 'last_name', 'position', 'email', 'user')
    search_fields = ('first_name', 'last_name', 'email', 'user__username')

    def save_model(self, request, obj, form, change):
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']

        if change and obj.user_id:
            user = obj.user
            user.username = username
            user.email = obj.email
            user.first_name = obj.first_name
            user.last_name = obj.last_name
            if password:
                user.set_password(password)
            user.is_staff = True
            user.save()
        else:
            user = User.objects.create_user(
                username=username,
                password=password,
                email=obj.email,
                first_name=obj.first_name,
                last_name=obj.last_name,
            )
            user.is_staff = True
            user.save()
            obj.user = user

        super().save_model(request, obj, form, change)
