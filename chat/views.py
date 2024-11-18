from django.shortcuts import render , redirect , get_object_or_404,redirect
from django.db.models import Q
from rest_framework import generics

from django.contrib.auth.decorators import login_required 
from django.urls import reverse_lazy
from django.contrib.auth import  login ,logout, authenticate
from django.contrib.auth.models import User

from rest_framework.response import Response
from django.http import HttpResponse
from django.contrib import messages

from django.template.loader import get_template
from django.core.mail import send_mail
import json
from pangotalk.settings import EMAIL_HOST
from django.http import JsonResponse
import json
from app. models import (UserProfile,
    BusinessProfile,
    Invite,
    ProductListing,
    Order,
    Customer,
    Event,
    EventBooking ,
    BusinessBranch,
    MediaType,
    BusinessConfiguration
    )

from . models import ChatMessage,AddNote
from django.utils import timezone
import uuid
import datetime
import pytz
from datetime import timedelta 
import random
from django.utils import timezone
import random
import json
import requests
from app. decorators import (
    user_controller
    ,allowed_users,
    form_complete,
    account_verification
    ,category_access,
    allowed_account,
    
    
    )

import uuid

from tablib import Dataset
plan_Id = uuid.uuid1()
customer_Id = str(plan_Id)




@form_complete
@account_verification
@login_required(login_url='accounts/login' )
@allowed_users(allowed_roles = ['Business'])
def chat_intro(request):
    currentUser = request.user
    info        = UserProfile.objects.get(user = currentUser)
    customers   = Customer.objects.filter(business_ID = info.business_ID)
    inbox_messages = customers.filter(inbox_messages__gt = 0).count()
    messageinfo = ChatMessage.objects.filter(business_ID = info.business_ID)
    context     = {"customers":customers,'inbox_messages':inbox_messages,'info':info}
    return render(request,'chat/messaging/index.html',context)



@form_complete
@account_verification
@login_required(login_url='accounts/login' )
@allowed_users(allowed_roles = ['Business'])
def chat(request,customerID):
    currentUser = request.user
    
    info        = UserProfile.objects.get(user = currentUser)
    all_customer   = Customer.objects.filter(business_ID = info.business_ID).order_by('-dateadded')
    inbox_messages = all_customer.filter(inbox_messages__gt = 0).count()
    info        = UserProfile.objects.get(user = currentUser)
    all_invite  = Invite.objects.filter(business_ID = info.business_ID)
    customers   = Customer.objects.filter(business_ID = info.business_ID )
    customer_personalInfo   = Customer.objects.get(customer_ID = customerID)
    branch_detail           = BusinessBranch.objects.filter(branch_ID = customer_personalInfo.branch_ID).first()
    configInfo              = BusinessConfiguration.objects.get(business_ID = info.business_ID)
    customers.filter(customer_ID = customerID).update(inbox_messages = 0)
    customerInfo = customers.get(customer_ID = customerID)
    messageinfo = ChatMessage.objects.filter(business_ID = info.business_ID)
    all_messages =messageinfo.filter(customer_ID = customerID).order_by('dateadded')
    total_invite = all_invite.count()
    notes        = AddNote.objects.filter(business_ID = info.business_ID)
    notes        = notes.filter(customer_ID = customerID)
    
    context     = {
        "notes":notes,
                "branch_detail":branch_detail,
                  "customer_personalInfo":customer_personalInfo,
                  "inbox_messages":inbox_messages,
                 "all_messages":all_messages,
                   "all_invite":all_invite,
                    "total_invite":total_invite,
                    "all_customer":all_customer,
                    "customer_ID":customerID,
                    'customerInfo':customerInfo}
    customer_number = customerInfo.code+customerInfo.phone
    if request.method == "POST":
        message  = request.POST.get('message','')
        message_ID    = uuid.uuid1()
        message_ID    = str(message_ID)
        url           = configInfo.bot_endpoint+'/chat-message'
        payload       = {'business_ID':info.business_ID,
                         'message': message,
                         'phone'  : customer_number,
                         }
        headers       = {'Content-Type': 'application/json'}
        r             = requests.post(url,headers= headers,data=json.dumps(payload))
        
        ChatMessage.objects.create(

            customer_ID      = customerID,
            business_ID      = info.business_ID,
            message_ID       = message_ID,
            supportAgent     = info.firstName,
            # userName         = ,
            # country          = ,
            message          = message,
            # phone_number            = ,
           supportMessage      = True,
            # message_is_opened= True,
        )


    return render(request,'chat/messaging/chat.html',context)

@form_complete
@account_verification
@login_required(login_url='accounts/login' )
@allowed_users(allowed_roles = ['Farmer'])
def send_image(request,customerID):
    currentUser = request.user
    info        = UserProfile.objects.get(user = currentUser)
    all_customer   = Customer.objects.filter(business_ID = info.business_ID).order_by('-dateadded')
    inbox_messages = all_customer.filter(inbox_messages__gt = 0).count()
    info        = UserProfile.objects.get(user = currentUser)
    all_invite  = Invite.objects.filter(business_ID = info.business_ID)
    customers   = Customer.objects.filter(business_ID = info.business_ID )
    customer_personalInfo   = Customer.objects.get(customer_ID = customerID)
    branch_detail           = BusinessBranch.objects.get(branch_ID = customer_personalInfo.branch_ID)
    customers.filter(customer_ID = customerID).update(inbox_messages = 0)
    customerInfo = customers.get(customer_ID = customerID)
    messageinfo = ChatMessage.objects.filter(business_ID = info.business_ID)
    all_messages =messageinfo.filter(customer_ID = customerID).order_by('dateadded')
    total_invite = all_invite.count()
    notes        = AddNote.objects.filter(business_ID = info.business_ID)
    notes        = notes.filter(customer_ID = customerID)
    
    context     = {
        "notes":notes,
                "branch_detail":branch_detail,
                  "customer_personalInfo":customer_personalInfo,
                  "inbox_messages":inbox_messages,
                 "all_messages":all_messages,
                   "all_invite":all_invite,
                    "total_invite":total_invite,
                    "all_customer":all_customer,
                    "customer_ID":customerID,
                    'customerInfo':customerInfo}
    if request.method == "POST" and 'fileupload' in request.FILES:
        caption              = request.POST.get('message','')
        media_file           = request.FILES
        media_file           = media_file['fileupload']
        file_type            = media_file.content_type
        data_info = MediaType.objects.filter(media_type  = file_type).first()

        message_ID    = uuid.uuid1()
        message_ID    = str(message_ID)
        ChatMessage.objects.create(
            media_type       = data_info.category,
            customer_ID      = customerID,
            business_ID      = info.business_ID,
            message_ID       = message_ID,
            supportAgent     = info.firstName,
            media_available  = True,
            message          = caption,
            media_file       = media_file,
           supportMessage    = True,
           
        )
        return redirect('account/user/chat',customerID = customerID)
    return render(request,'chat/messaging/send-image.html',context)




@form_complete
@account_verification
@login_required(login_url='accounts/login' )
@allowed_users(allowed_roles = ['Farmer'])
def send_audio(request,customerID):
    currentUser = request.user
    info        = UserProfile.objects.get(user = currentUser)
    all_customer   = Customer.objects.filter(business_ID = info.business_ID).order_by('-dateadded')
    inbox_messages = all_customer.filter(inbox_messages__gt = 0).count()
    info        = UserProfile.objects.get(user = currentUser)
    all_invite  = Invite.objects.filter(business_ID = info.business_ID)
    customers   = Customer.objects.filter(business_ID = info.business_ID )
    customer_personalInfo   = Customer.objects.get(customer_ID = customerID)
    branch_detail           = BusinessBranch.objects.get(branch_ID = customer_personalInfo.branch_ID)
    customers.filter(customer_ID = customerID).update(inbox_messages = 0)
    customerInfo = customers.get(customer_ID = customerID)
    messageinfo = ChatMessage.objects.filter(business_ID = info.business_ID)
    all_messages =messageinfo.filter(customer_ID = customerID).order_by('dateadded')
    total_invite = all_invite.count()
    notes        = AddNote.objects.filter(business_ID = info.business_ID)
    notes        = notes.filter(customer_ID = customerID)
    
    context     = {
        "notes":notes,
                "branch_detail":branch_detail,
                  "customer_personalInfo":customer_personalInfo,
                  "inbox_messages":inbox_messages,
                 "all_messages":all_messages,
                   "all_invite":all_invite,
                    "total_invite":total_invite,
                    "all_customer":all_customer,
                    "customer_ID":customerID,
                    'customerInfo':customerInfo}
    if request.method == "POST" and 'fileupload' in request.FILES:
        caption              = request.POST.get('message','')
        media_file           = request.FILES
        media_file           = media_file['fileupload']
        file_type            = media_file.content_type
        data_info = MediaType.objects.filter(media_type  = file_type).first()

        message_ID    = uuid.uuid1()
        message_ID    = str(message_ID)
        if MediaType.objects.filter(media_type  = file_type).exists():
            ChatMessage.objects.create(
                media_type       = data_info.category,
                customer_ID      = customerID,
                business_ID      = info.business_ID,
                message_ID       = message_ID,
                supportAgent     = info.firstName,
                media_available  = True,
                message          = caption,
                media_file       = media_file,
            supportMessage    = True,
            
            )
            return redirect('account/user/chat',customerID = customerID)
    return render(request,'chat/messaging/send-audio.html',context)



@form_complete
@account_verification
@login_required(login_url='accounts/login' )
@allowed_users(allowed_roles = ['Farmer'])
def send_video(request,customerID):
    currentUser = request.user
    info        = UserProfile.objects.get(user = currentUser)
    all_customer   = Customer.objects.filter(business_ID = info.business_ID).order_by('-dateadded')
    inbox_messages = all_customer.filter(inbox_messages__gt = 0).count()
    info        = UserProfile.objects.get(user = currentUser)
    all_invite  = Invite.objects.filter(business_ID = info.business_ID)
    customers   = Customer.objects.filter(business_ID = info.business_ID )
    customer_personalInfo   = Customer.objects.get(customer_ID = customerID)
    branch_detail           = BusinessBranch.objects.get(branch_ID = customer_personalInfo.branch_ID)
    customers.filter(customer_ID = customerID).update(inbox_messages = 0)
    customerInfo = customers.get(customer_ID = customerID)
    messageinfo = ChatMessage.objects.filter(business_ID = info.business_ID)
    all_messages =messageinfo.filter(customer_ID = customerID).order_by('dateadded')
    total_invite = all_invite.count()
    notes        = AddNote.objects.filter(business_ID = info.business_ID)
    notes        = notes.filter(customer_ID = customerID)
    
    context     = {
        "notes":notes,
                "branch_detail":branch_detail,
                  "customer_personalInfo":customer_personalInfo,
                  "inbox_messages":inbox_messages,
                 "all_messages":all_messages,
                   "all_invite":all_invite,
                    "total_invite":total_invite,
                    "all_customer":all_customer,
                    "customer_ID":customerID,
                    'customerInfo':customerInfo}
    if request.method == "POST" and 'fileupload' in request.FILES:
        caption              = request.POST.get('message','')
        media_file           = request.FILES
        media_file           = media_file['fileupload']
        file_type            = media_file.content_type
        data_info = MediaType.objects.filter(media_type  = file_type).first()

        message_ID    = uuid.uuid1()
        message_ID    = str(message_ID)
        if MediaType.objects.filter(media_type  = file_type).exists():
            ChatMessage.objects.create(
                media_type       = data_info.category,
                customer_ID      = customerID,
                business_ID      = info.business_ID,
                message_ID       = message_ID,
                supportAgent     = info.firstName,
                media_available  = True,
                message          = caption,
                media_file       = media_file,
            supportMessage    = True,
            
            )
            return redirect('account/user/chat',customerID = customerID)
    return render(request,'chat/messaging/send-video.html',context)



@form_complete
@account_verification
@login_required(login_url='accounts/login' )
@allowed_users(allowed_roles = ['Farmer'])
def send_document(request,customerID):
    currentUser = request.user
    info        = UserProfile.objects.get(user = currentUser)
    all_customer   = Customer.objects.filter(business_ID = info.business_ID).order_by('-dateadded')
    inbox_messages = all_customer.filter(inbox_messages__gt = 0).count()
    info        = UserProfile.objects.get(user = currentUser)
    all_invite  = Invite.objects.filter(business_ID = info.business_ID)
    customers   = Customer.objects.filter(business_ID = info.business_ID )
    customer_personalInfo   = Customer.objects.get(customer_ID = customerID)
    branch_detail           = BusinessBranch.objects.get(branch_ID = customer_personalInfo.branch_ID)
    customers.filter(customer_ID = customerID).update(inbox_messages = 0)
    customerInfo = customers.get(customer_ID = customerID)
    messageinfo = ChatMessage.objects.filter(business_ID = info.business_ID)
    all_messages =messageinfo.filter(customer_ID = customerID).order_by('dateadded')
    total_invite = all_invite.count()
    notes        = AddNote.objects.filter(business_ID = info.business_ID)
    notes        = notes.filter(customer_ID = customerID)
    
    context     = {
        "notes":notes,
                "branch_detail":branch_detail,
                  "customer_personalInfo":customer_personalInfo,
                  "inbox_messages":inbox_messages,
                 "all_messages":all_messages,
                   "all_invite":all_invite,
                    "total_invite":total_invite,
                    "all_customer":all_customer,
                    "customer_ID":customerID,
                    'customerInfo':customerInfo}
    if request.method == "POST" and 'fileupload' in request.FILES:
        caption              = request.POST.get('message','')
        media_file           = request.FILES
        media_file           = media_file['fileupload']
        file_type            = media_file.content_type
        data_info = MediaType.objects.filter(media_type  = file_type).first()

        message_ID    = uuid.uuid1()
        message_ID    = str(message_ID)
        if MediaType.objects.filter(media_type  = file_type).exists():
            ChatMessage.objects.create(
                media_type       = data_info.category,
                customer_ID      = customerID,
                business_ID      = info.business_ID,
                message_ID       = message_ID,
                supportAgent     = info.firstName,
                media_available  = True,
                message          = caption,
                media_file       = media_file,
            supportMessage    = True,
            
            )
            return redirect('account/user/chat',customerID = customerID)
    return render(request,'chat/messaging/send-document.html',context)


@form_complete
@account_verification
@login_required(login_url='accounts/login' )
@allowed_users(allowed_roles = ['Farmer'])
def broadcast_table(request):
    currentUser = request.user
    info        = UserProfile.objects.get(user = currentUser)
    customers   = Customer.objects.filter(business_ID = info.business_ID)
    inbox_messages = customers.filter(inbox_messages__gt = 0).count()
    messageinfo = ChatMessage.objects.filter(business_ID = info.business_ID)
    context     = {"customers":customers,'inbox_messages':inbox_messages,'info':info}
    return render(request,'chat/broadcast-table.html',context)


@form_complete
@account_verification
@login_required(login_url='accounts/login' )
@allowed_users(allowed_roles = ['Farmer'])
def create_notes(request):
    if request.method == "POST":
        body       = json.loads(request.body)
        addNoteName     = body['addNoteName']
        addNoteDetails  = body['addNoteDetails']
        Notetag         = body['Notetag']
        customerID         = body['customerID']
        currentUser = request.user
        info        = UserProfile.objects.get(user = currentUser)
        AddNote.objects.create(
            customer_ID        = customerID,
            business_ID        = info.business_ID,
            supportAgent_ID    = info.userprofileID,
            supportAgent       = info.firstName,
            addNoteName        = addNoteName,
            addNoteDetails     = addNoteDetails,
            Notetag            = Notetag,
        )
        print(addNoteName)
        print(addNoteDetails)
        print(request.user)
    return  JsonResponse({'dummy_key': 'dummy_value'})


