from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from tickets_view.forms import *


@login_required()
def ticketsview(request):
    if request.method == 'GET':
        if is_manager(request.user):
            tickets = Contact.objects.all()
            return render(request, "tickets_view/tickets_view.html", {'tickets': tickets, 'manager': True})
        else:
            tickets = Contact.objects.filter(user=request.user)
            return render(request, "tickets_view/tickets_view.html", {'tickets': tickets, 'manager': False})


@login_required()
def ticketview(request, id):
    if is_manager(request.user):
        if request.method == 'GET':
            ticket = Contact.objects.filter(id=id).last()
            form = TicketForm(initial={'moderatorreply': ticket.moderatorreply})
            print(ticket.moderatorreply)
        else:
            form = TicketForm(request.POST)
            ticket = Contact.objects.filter(id=id).last()
            if form.is_valid():
                ticketupdate = form.save(commit=False)
                ticketupdate.moderatorreply = form.cleaned_data['moderatorreply']
                ticket.moderatorreply = ticketupdate.moderatorreply
                ticket.replied = True
                ticket.save()
        return render(request, 'tickets_view/ticket_view.html', {'ticket': ticket, 'form': form, 'manager': True})
    else:
        if request.method == 'GET':
            ticket = Contact.objects.filter(id=id).last()
            return render(request, 'tickets_view/ticket_view.html', {'ticket': ticket, 'manager': False})


def is_manager(user):
    return user.groups.filter(name='Managers').exists()
