# Generated by Django 5.0 on 2024-11-26 10:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='businessprofile',
            name='business_subdomain',
            field=models.BooleanField(default=False),
        ),
    ]
