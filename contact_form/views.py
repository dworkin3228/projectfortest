from django.core.mail import send_mail, BadHeaderError
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from datetime import datetime
from .forms import ContactForm, Contact
from django.http import HttpResponse
from projectfortest import settings
import asyncio

@login_required()
def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST, request.FILES)
        # Если форма заполнена корректно, сохраняем все введённые пользователем значения
        if form.is_valid():
            new_ticket = form.save(commit=False)
            new_ticket.user = request.user
            new_ticket.name = request.user.first_name + ' ' + request.user.last_name
            new_ticket.email = request.user.email
            new_ticket.fileupload = request.FILES['fileupload']
            new_ticket.subject = form.cleaned_data['subject']
            new_ticket.message = form.cleaned_data['message']
            new_ticket.created = datetime.now()
            contact = Contact.objects.filter(user=request.user).last()
            if contact is None or (datetime.now() - contact.created).days > 0:
                new_ticket.save()
                ticket = Contact.objects.filter(user=request.user).last()
                asyncio.run(sendmail(ticket))
                return redirect('success')
            return HttpResponse('Вы уже оставляли заявку за последние сутки, попробуйте позже')
    else:
        # Заполняем форму
        form = ContactForm()
    # Отправляем форму на страницу
    return render(request, 'contact_form/contact_form.html', {'form': form})


@login_required()
def success_view(request):
    return HttpResponse('Заявка успешно отправлена.')


async def sendmail(ticket):
    try:
        send_mail(
            'New ticket: ' + ticket.subject,
            ticket.message,
            settings.EMAIL_HOST_USER,
            ['manager.djangoproject@gmail.com'])
    except BadHeaderError:
        return HttpResponse('Invalid header found.')