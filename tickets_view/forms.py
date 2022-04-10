from django import forms
from contact_form.models import *


class TicketForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['moderatorreply']
