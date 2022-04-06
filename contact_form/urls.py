from django.urls import path
from . import views

urlpatterns = [

    path('', views.contactview, name='contact_form'),
]
