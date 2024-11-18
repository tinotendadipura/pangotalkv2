from django.conf import settings
from django.db import models
from django.db.models.signals import post_save
from django.utils import timezone

from datetime import datetime
import uuid
import random
slugify = uuid.uuid1()
slugify = str(slugify)


slugify_mebership = uuid.uuid1()
slugify_mebership = str(slugify_mebership)
plan_Id = uuid.uuid1()
plan_Id = str(plan_Id)



class ApiCofig(models.Model):
    user                  = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    school_Name           = models.CharField(max_length=500,default='none')
    school_ID             = models.CharField(max_length=500,default='none')
    apiUrl1               = models.CharField(max_length=400,default='http//')
    apiUrl2               = models.CharField(max_length=400,default='http//')
    date                  = models.DateTimeField(default = timezone.now)
    update                = models.DateTimeField(default = timezone.now)
    account_active_status = models.BooleanField(default=False)
    setup_ready           = models.BooleanField(default=False)



class SchoolPortalImage(models.Model):
    

    Instance_ID                   = models.CharField(max_length = 50,default='None')
    Instance_IP                   = models.CharField(max_length = 50,default='None')
    School_name                   = models.CharField(max_length=250,default='None')
    school_ID                     = models.CharField(max_length = 50)
    Port                          = models.CharField(max_length=250,default='---')
    Instance_assinged_status      = models.BooleanField(default=False)
    BillingAccount_active_status  = models.BooleanField(default=False)
    config_date                   = models.DateTimeField(default = timezone.now)

    
    def __str__(self):
      return self.School_name




class InstanceImage(models.Model):
    Instance_ID           = models.CharField(max_length = 50,default='None')
    Instance_IP           = models.CharField(max_length = 50)
    Port                  = models.CharField(max_length=250,default='---')
    instanceUser          = models.CharField(max_length=250,default='None')
    instancePassword      = models.CharField(max_length=250,default='None')
    SSH_Key               = models.CharField(max_length=250,default='None')
    assinged_status       = models.BooleanField(default=False)
    portal_installed      = models.BooleanField(default=False)
    created_date          = models.DateTimeField(default = timezone.now)

    
    def __str__(self):
      return self.Instance_IP
  



class BillingManager(models.Model):
    business_ID           = models.CharField(max_length = 50,default='None')
    business_Name         = models.CharField(max_length = 50,default='None')
    billing_Name          = models.CharField(max_length = 50,default='None')
    emailCounter          = models.IntegerField(default=1)
    Price                 = models.DecimalField(max_digits=10, decimal_places=2,default=0)
   
    first_billing_date    = models.DateTimeField(default = timezone.now)
    second_billing_date   = models.DateTimeField(default = timezone.now)
    third_billing_date    = models.DateTimeField(default = timezone.now)
    forth_billing_date    = models.DateTimeField(default = timezone.now)
    account_suspension_date = models.DateTimeField(default = timezone.now)
    first_billing_status    = models.BooleanField(default=False)
    second_billing_status   = models.BooleanField(default=False)
    third_billing_status    = models.BooleanField(default=False)
    forth_billing_status    = models.BooleanField(default=False)
    suspend_status          = models.BooleanField(default=False)

    
    def __str__(self):
      return self.business_Name
  
