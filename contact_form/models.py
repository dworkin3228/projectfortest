from django.db import models
from django.utils import timezone


class Contact(models.Model):
    # first_name = models.CharField(max_length=200)
    # last_name = models.CharField(max_length=200)
    id = models.AutoField(primary_key=True)
    subject = models.TextField(max_length=200)
    message = models.TextField(max_length=1000)
    name = models.CharField(max_length=200)
    email = models.EmailField()
    filelink = models.URLField()  # Разобраться и сделать верно!
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        # Будет отображаться следующее поле в панели администрирования
        return self.subject