from django.core.mail import send_mail, BadHeaderError
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.context_processors import auth
from django_registration.forms import User

from contact_form.forms import ContactForm
from django.http import HttpResponse, HttpResponseRedirect
from projectfortest import settings


@login_required()
def contactview(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        # Если форма заполнена корректно, сохраняем все введённые пользователем значения
        if form.is_valid():
            new_ticket = form.save(commit=False)
            new_ticket.name = request.user
            #new_ticket.email = request.user.email
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            new_ticket.save()
            try:
                send_mail('New ticket: '+subject, message, settings.EMAIL_HOST_USER, ['xah3000@gmail.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('success')
    else:
        # Заполняем форму
        form = ContactForm()
    # Отправляем форму на страницу'''
    return render(request, 'contact_form/contact_form.html', {'form': form})


def succesview(request):
    return HttpResponse('Success! Thank you for your message.')
