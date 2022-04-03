from django.db import models


class Contact(models.Model):
   # first_name = models.CharField(max_length=200)
   # last_name = models.CharField(max_length=200)
    subject = models.TextField(max_length=200)
    message = models.TextField(max_length=1000)

    def __str__(self):
        # Будет отображаться следующее поле в панели администрирования
        return self.subject