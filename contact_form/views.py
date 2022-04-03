from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import send_mail, BadHeaderError
from contact_form.forms import ContactForm


def contactview(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        # Если форма заполнена корректно, сохраняем все введённые пользователем значения
        if form.is_valid():
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            return render(request, 'users/fortest.html')
    else:
        # Заполняем форму
        form = ContactForm()
    # Отправляем форму на страницу'''
    return render(request, 'contact_form/contact_form.html', {'form': form})
