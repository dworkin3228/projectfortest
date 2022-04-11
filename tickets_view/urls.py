from django.urls import path, re_path
from . import views

urlpatterns = [

    path('', views.tickets_view, name='tickets_view'),
    path('ticket_view/<int:id>/', views.ticket_view, name='ticket_view')
]