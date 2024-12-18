# Generated by Django 2.2.2 on 2022-04-08 11:18

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ChatMessage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_ID', models.CharField(default='none', max_length=50)),
                ('business_ID', models.CharField(default='none', max_length=50)),
                ('message_ID', models.CharField(default='none', max_length=50)),
                ('supportAgent', models.CharField(default='none', max_length=50)),
                ('userName', models.CharField(default='none', max_length=50)),
                ('country', models.CharField(default='none', max_length=20)),
                ('message', models.TextField()),
                ('phone', models.CharField(default='s-00', max_length=50)),
                ('dateadded', models.DateTimeField(default=django.utils.timezone.now)),
                ('supportMessage', models.BooleanField(default=False)),
            ],
        ),
    ]
