from django import forms
from contact_form.models import *


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ["subject", 'message', 'fileupload']