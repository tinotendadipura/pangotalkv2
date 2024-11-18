from locale import currency
from turtle import title
from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.db.models.signals import post_save
from django.utils import timezone

from datetime import datetime
import pytz



class Forum(models.Model):
    TOPIC_STATUS = (
    ('ACTIVE', 'ACTIVE'),
    ('CLOSED', 'CLOSED'),
   
    
    )
    business_ID       = models.CharField(max_length = 500,default='')
    topic_ID          = models.CharField(max_length = 500,default='')
    topic_status      = models.CharField(max_length = 500,default='ACTIVE',choices=TOPIC_STATUS)
    topic_title       = models.CharField(max_length = 5000,default='')
    topic_thubnail    = models.FileField(upload_to='forum/%Y/%m/%d/',null=True,blank=True)
    topic_description = models.TextField(max_length = 5000,default='')
    total_comments    = models.IntegerField(default=0)
    total_members     = models.IntegerField(default=0)
    dateadded         = models.DateTimeField(default = timezone.now)
   
    
    def __str__(self):
      return self.topic_title




class Joined_Forum(models.Model):
    business_ID       = models.CharField(max_length = 500,default='')
    topic_ID          = models.CharField(max_length = 500,default='')
    topic_status      = models.CharField(max_length = 500,default='')
    member_first_name = models.CharField(max_length = 20,default='')
    member_last_name  = models.CharField(max_length = 20,default='')
    mobile_number     = models.CharField(max_length = 20,default='')
    dateadded         = models.DateTimeField(default = timezone.now)
   
    
    def __str__(self):
      return self.member_first_name





class Comment(models.Model):
    
    business_ID       = models.CharField(max_length = 500,default='')
    topic_ID          = models.CharField(max_length = 500,default='')
    topic_status      = models.CharField(max_length = 500,default='')
    member_first_name = models.CharField(max_length = 20,default='')
    member_last_name  = models.CharField(max_length = 20,default='')
    member_comment    = models.TextField(max_length = 5000,default='')
    comment_type      = models.CharField(max_length = 5000,default='Self')
    dateadded         = models.DateTimeField(default = timezone.now)
    
    def __str__(self):
      return self.member_first_name




class Our_Projects(models.Model):
    
    business_ID            = models.CharField(max_length = 500,default='')
    project_ID             = models.CharField(max_length = 500,default='')
    project_date           = models.DateTimeField(default = timezone.now)
    project_tittle         = models.CharField(max_length = 200,default='')
    project_description    = models.TextField(max_length = 5000,default='')
    project_thubnail       = models.FileField(upload_to='forum/%Y/%m/%d/',null=True,blank=True)
    dateadded              = models.DateTimeField(default = timezone.now)
    
    def __str__(self):
      return self.project_tittle


class ProjectMedia(models.Model):
   
    business_ID                      = models.CharField(max_length = 500,default='')
    project_ID                       = models.CharField(max_length = 500,default='')
    project_media                    = models.FileField(upload_to='projects/%Y/%m/%d/',null=True,blank=True)
    dateadded                        = models.DateTimeField(default = timezone.now)
   
    
    def __str__(self):
      return self.project_ID



class Topic(models.Model):
    
    business_ID            = models.CharField(max_length = 500,default='')
    topic_ID               = models.CharField(max_length = 500,default='')
    topic_tittle           = models.CharField(max_length = 200,default='')
    category               = models.CharField(max_length = 200,default='')
    description            = models.TextField(max_length = 5000,default='')
    dateadded              = models.DateTimeField(default = timezone.now)
    
    def __str__(self):
      return self.topic_tittle



class Category(models.Model):
    
    business_ID            = models.CharField(max_length = 500,default='')
    topic_ID               = models.CharField(max_length = 500,default='')
    category_ID            = models.CharField(max_length = 500,default='')
    category               = models.CharField(max_length = 200,default='')
    
    def __str__(self):
      return self.category




class TopicMedia(models.Model):
    FILE_TYPE = (
    ('Document', 'Document'),
    
    ('Image', 'Image'),
    ('Video', 'Video'),
    ('Audio', 'Audio'),
    
    )
    business_ID                      = models.CharField(max_length = 500,default='')
    topic_ID                         = models.CharField(max_length = 500,default='')
    title                            = models.CharField(max_length = 500,default='')
    media                            = models.FileField(upload_to='forum/%Y/%m/%d/',null=True,blank=True)
    file_type                        = models.CharField(max_length=50,default='')
    file_extension                   = models.CharField(max_length=50,default='')
    file_size                        = models.DecimalField(max_digits=5, decimal_places=2,default= 0)
    dateadded                        = models.DateTimeField(default = timezone.now)
   
    
    def __str__(self):
      return self.topic_ID







class Partner(models.Model):
    
    business_ID                   = models.CharField(max_length = 500,default='')
    partner_organisation          = models.CharField(max_length = 500,default='')
    partner_type                  = models.CharField(max_length = 5000,default='')
    partner_thubnail              = models.FileField(upload_to='partner/%Y/%m/%d/',null=True,blank=True)
    description                   = models.TextField(max_length = 5000,default='')
    dateadded                     = models.DateTimeField(default = timezone.now)
   
    
    def __str__(self):
      return self.partner_organisation




class Partner_Request(models.Model):
    
    business_ID                   = models.CharField(max_length = 500,default='')
    partner_organisation          = models.CharField(max_length = 500,default='')
    partner_type                  = models.CharField(max_length = 5000,default='')
    partner_request_status        = models.CharField(max_length = 5000,default='')
    description                   = models.TextField(max_length = 5000,default='')
    dateadded                     = models.DateTimeField(default = timezone.now)
   
    
    def __str__(self):
      return self.partner_organisation





class Question(models.Model):
    
    business_ID                   = models.CharField(max_length = 500,default='')
    question_ID                   = models.CharField(max_length = 500,default='')
    question                      = models.TextField(max_length = 5000,default='')
    category                      = models.CharField(max_length = 500,default='')
    dateadded                     = models.DateTimeField(default = timezone.now)
   
    
    def __str__(self):
      return self.business_ID


class Q_Answer(models.Model):
    
    business_ID                   = models.CharField(max_length = 500,default='')
    question_ID                   = models.CharField(max_length = 500,default='')
    answer                        = models.TextField(max_length = 5000,default='')
    dateadded                     = models.DateTimeField(default = timezone.now)
   
    
    def __str__(self):
      return self.business_ID




class Question_Category(models.Model):
    
    business_ID                   = models.CharField(max_length = 500,default='')
    question_ID                   = models.CharField(max_length = 500,default='')
    category                      = models.CharField(max_length = 500,default='')
    dateadded                     = models.DateTimeField(default = timezone.now)
   
    
    def __str__(self):
      return self.category
