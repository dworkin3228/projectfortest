from django.urls import path
from . import views

urlpatterns = [

    path('', views.contact_view, name='contact_form'),
    path('success/', views.success_view, name='success')
]
