# Generated by Django 2.2.2 on 2024-10-16 22:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('non_profit', '0010_topicmedia_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='topicmedia',
            name='file_extension',
            field=models.CharField(default='', max_length=50),
        ),
    ]
