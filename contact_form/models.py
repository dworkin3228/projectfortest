from django.db import models


class Contact(models.Model):
    id = models.AutoField(primary_key=True)
    subject = models.CharField(max_length=200)
    message = models.TextField(max_length=1000)
    name = models.CharField(max_length=200)
    email = models.EmailField()
    fileupload = models.FileField(upload_to='uploads/')
    created = models.DateTimeField()
    replied = models.BooleanField(default=False)
    user = models.CharField(max_length=200, blank=False)
    manager_reply = models.TextField(max_length=1000, null=True)

    def __str__(self):
        # Будет отображаться следующее поле в панели администрирования
        return self.subject
