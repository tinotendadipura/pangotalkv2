# Generated by Django 2.2.2 on 2021-01-18 07:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='SchoolPortalImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('SchoolPortalImage_ID', models.CharField(max_length=50)),
                ('School_name', models.CharField(default='None', max_length=250)),
                ('instanceUser', models.CharField(default='None', max_length=250)),
                ('instancePassword', models.CharField(default='None', max_length=250)),
                ('school_ID', models.CharField(max_length=50)),
                ('default_url', models.CharField(default='None', max_length=250)),
                ('IpAdress', models.GenericIPAddressField(default='127.0.0.1', unique=True)),
                ('port', models.PositiveIntegerField(default=80)),
                ('package', models.CharField(default='None', max_length=50)),
                ('amount', models.CharField(default='0', max_length=40)),
                ('billingStartedOn', models.DateTimeField(default=django.utils.timezone.now)),
                ('NextbillingStartsOn', models.DateTimeField(default=django.utils.timezone.now)),
                ('assinged_status', models.BooleanField(default=False)),
                ('portal_active_status', models.BooleanField(default=False)),
                ('active_status_since', models.DateTimeField(default=django.utils.timezone.now)),
                ('config_date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='ApiCofig',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('school_Name', models.CharField(default='none', max_length=500)),
                ('school_ID', models.CharField(default='none', max_length=500)),
                ('apiUrl1', models.CharField(default='http//', max_length=400)),
                ('apiUrl2', models.CharField(default='http//', max_length=400)),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('update', models.DateTimeField(default=django.utils.timezone.now)),
                ('account_active_status', models.BooleanField(default=False)),
                ('setup_ready', models.BooleanField(default=False)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
