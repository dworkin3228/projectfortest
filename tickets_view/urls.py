from django.urls import path, re_path
from . import views

urlpatterns = [

    path('', views.ticketsview, name='tickets_view'),
    path('ticket_view/<int:id>/', views.ticketview, name='ticket_view')
]