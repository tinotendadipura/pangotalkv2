# Generated by Django 2.2.2 on 2022-08-04 22:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0010_customermedia_media_file_url'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customermedia',
            name='media_available',
        ),
    ]
