from django.shortcuts import render
from contact_form.forms import *


def ticketview(request):
    if request.method == 'POST':
        tv = Contact.objects.all()
        print(tv)
    else:
        tv = Contact.objects.all()
        print(tv)
        return render(request, "ticket_view/ticket_view.html")
