# Generated by Django 4.0.3 on 2022-04-07 06:42

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('contact_form', '0005_alter_contact_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='filelink',
        ),
        migrations.AddField(
            model_name='contact',
            name='fileupload',
            field=models.FileField(default=django.utils.timezone.now, upload_to='uploads/'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='contact',
            name='subject',
            field=models.CharField(max_length=200),
        ),
    ]
