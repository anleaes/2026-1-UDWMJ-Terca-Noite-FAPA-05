from django import forms

from .models import Ticket
from seat.models import Seat


class TicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ['screening', 'seat']
