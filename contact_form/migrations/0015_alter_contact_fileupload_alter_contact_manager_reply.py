# Generated by Django 4.0.3 on 2022-04-12 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact_form', '0014_alter_contact_manager_reply'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='fileupload',
            field=models.FileField(blank=True, null=True, upload_to='uploads/'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='manager_reply',
            field=models.TextField(max_length=1000, null=True),
        ),
    ]