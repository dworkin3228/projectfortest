from django import forms
from contact_form.models import *


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        exclude = ('id', 'name', 'email', 'filelink', 'created')
        #fields = ["subject", 'message']
        widgets = {
            'subject': forms.TextInput(attrs={'class': 'form-input'}),
            'message': forms.Textarea(attrs={'cols': 60, 'rows': 10})
        }

# subject = forms.CharField(max_length = 100)
# message = forms.CharField(widget = forms.Textarea(attrs = {'class': 'form-control'}))
