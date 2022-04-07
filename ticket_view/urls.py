from django.urls import path
from . import views

urlpatterns = [

    path('', views.ticketview, name='ticket_view')
]