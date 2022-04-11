from django.core.mail import send_mail, BadHeaderError
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.context_processors import auth
# from django_registration.forms import User
from django.utils import timezone
from django.contrib.auth.models import User
from datetime import datetime
from .forms import ContactForm, Contact
from django.http import HttpResponse, HttpResponseRedirect
from projectfortest import settings
import asyncio
from asgiref.sync import sync_to_async, async_to_sync
from time import sleep

#queue = asyncio.Queue()


@login_required()
def contactview(request):
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
                contact = Contact.objects.filter(user=request.user).last()
                queue = asyncio.Queue()
                asyncio.run(queue.put(contact))
                asyncio.run(main(queue))
                return redirect('success')
            return HttpResponse('Вы уже оставляли заявку за последние сутки, попробуйте позже')


    else:
        # Заполняем форму
        form = ContactForm()
    # Отправляем форму на страницу
    return render(request, 'contact_form/contact_form.html', {'form': form})


@login_required()
def succesview(request):
    return HttpResponse('Success! Thank you for your message.')


async def main(queue):
    await index(queue)
    await asyncio.sleep(10)


async def sendmail(ticket_queue):
    ticket = await ticket_queue.get()
    try:
        send_mail('New ticket: ' + ticket.subject, ticket.message, settings.EMAIL_HOST_USER, ['xah3000@gmail.com'])
    except BadHeaderError:
        return HttpResponse('Invalid header found.')
    ticket_queue.task_done()


async def index(queue):
    tasks = []
    task = asyncio.create_task(sendmail(queue))
    tasks.append(task)
    await queue.join()
    for task in tasks:
        task.cancel()
    await asyncio.gather(*tasks, return_exceptions=True)



