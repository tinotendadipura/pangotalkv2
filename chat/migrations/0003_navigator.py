# Generated by Django 2.2.2 on 2022-04-11 13:01

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0002_chatmessage_message_is_opened'),
    ]

    operations = [
        migrations.CreateModel(
            name='Navigator',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_ID', models.CharField(default='none', max_length=50)),
                ('business_ID', models.CharField(default='none', max_length=50)),
                ('current_page', models.CharField(default='none', max_length=50)),
                ('phone', models.CharField(default='s-00', max_length=50)),
                ('dateadded', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]
