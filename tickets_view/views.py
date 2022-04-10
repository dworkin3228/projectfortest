from django.http import HttpResponse
from django.shortcuts import render, redirect
from tickets_view.forms import *
from users.views import is_member, is_manager


def ticketsview(request):
    if request.method == 'GET':
        if is_manager(request.user):
            tickets = Contact.objects.all()
            return render(request, "tickets_view/tickets_view.html", {'tickets': tickets})
        elif is_member(request.user):
            tickets = Contact.objects.filter(user=request.user)
            return render(request, "tickets_view/tickets_view.html", {'tickets': tickets})


def ticketview(request, id):
    if is_manager(request.user):
        manager = True
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
        return render(request, 'tickets_view/ticket_view.html', {'ticket': ticket, 'form': form, 'manager': manager})

    if is_member(request.user):
        manager = False
        if request.method == 'GET':
            ticket = Contact.objects.filter(id=id).last()
            return render(request, 'tickets_view/ticket_view.html', {'ticket': ticket, 'manager': manager})



