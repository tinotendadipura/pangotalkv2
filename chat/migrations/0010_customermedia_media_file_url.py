# Generated by Django 2.2.2 on 2022-08-04 21:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0009_customermedia'),
    ]

    operations = [
        migrations.AddField(
            model_name='customermedia',
            name='media_file_url',
            field=models.URLField(default=''),
        ),
    ]
