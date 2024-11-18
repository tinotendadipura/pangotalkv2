from turtle import title
from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.db.models.signals import post_save
from django.utils import timezone
from django.core.files import File
import os
import urllib
from datetime import datetime
import pytz





BUSINESS_CATEGORY = (
    ('RETAIL AND ECOMM', 'RETAIL AND ECOMM'),
    
    ('CAR RENTAL', 'CAR RENTAL'),
    ('CAR REPAIR', 'CAR REPAIR'),
    ('DRIVING SCHOOL','DRIVING SCHOOL')
)



class ChatMessage(models.Model):
    customer_ID   = models.CharField(max_length = 50,default='none')
    branch_ID     = models.CharField(max_length = 50,default='none')
    business_ID   = models.CharField(max_length = 50,default='none')
    message_ID    = models.CharField(max_length = 50,default='none')
    supportAgent  = models.CharField(max_length = 50,default='none')
    userName      = models.CharField(max_length = 50,default='none')
    country       = models.CharField(max_length = 20,default='none')
    message       = models.TextField()
    phone         = models.CharField(max_length = 50,default="s-00")
    dateadded         = models.DateTimeField(default = timezone.now)
    supportMessage    = models.BooleanField(default=False)
    media_file        = models.FileField(upload_to='files/%Y/%m/%d/',null=True,blank=True)
    media_type        = models.CharField(max_length = 20,default='none')
    media_available   = models.BooleanField(default=False)
    message_is_opened = models.BooleanField(default=False)

    
    def __str__(self):
      return self.userName

class CustomerMedia(models.Model):
  customer_ID   = models.CharField(max_length = 50,default='none')
  branch_ID     = models.CharField(max_length = 50,default='none')
  business_ID   = models.CharField(max_length = 50,default='none')
  message_ID    = models.CharField(max_length = 50,default='none')
  media_file    = models.FileField(upload_to='files/%Y/%m/%d/',null=True,blank=True)
  media_file_url = models.URLField(default='')
  media_type     = models.CharField(max_length = 20,default='none')
  

  def get_remote_image(self):
    if self.media_file_url and not self.media_file:
        result = urllib.urlretrieve(self.media_file_url)
        self.media_file.save(
                os.path.basename(self.media_file_url),
                File(open(result[0]))
                )
        self.save()

class AddNote(models.Model):
    customer_ID        = models.CharField(max_length = 50,default='none')
    business_ID        = models.CharField(max_length = 50,default='none')
    supportAgent_ID    = models.CharField(max_length = 50,default='none')
    supportAgent       = models.CharField(max_length = 50,default='none')
    addNoteName        = models.CharField(max_length = 500,default='none')
    addNoteDetails     = models.TextField(default='none')
    Notetag            = models.CharField(max_length = 500,default='none')
    dateadded          = models.DateTimeField(default = timezone.now)
    
    
    def __str__(self):
      return self.supportAgent



