# Generated by Django 2.2.2 on 2022-06-27 15:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0007_auto_20220627_1551'),
    ]

    operations = [
        migrations.AddField(
            model_name='chatmessage',
            name='media_type',
            field=models.CharField(default='none', max_length=20),
        ),
    ]
