from django.shortcuts import render


def ticketview(request):
    return render(request, "ticket_view/ticket_view.html")

