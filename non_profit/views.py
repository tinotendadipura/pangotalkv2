from locale import currency
from time import strptime
from django.shortcuts import render , redirect , get_object_or_404,redirect
from django.db.models import Q
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.decorators import login_required 
from django.urls import reverse_lazy
from django.contrib.auth import  login ,logout, authenticate
from django.contrib.auth.models import User
from django.contrib.auth import update_session_auth_hash
from django.views.decorators.csrf import csrf_exempt
from datetime import datetime
import random
from django.contrib.auth.models import Group
from django.contrib.auth.forms import  PasswordChangeForm
from django.core.paginator import Paginator
from django.contrib import messages
from django.utils.timezone import datetime
from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template
from django.core.mail import send_mail
#from kangaroo.settings import EMAIL_HOST_USER
from pangotalk.settings import EMAIL_HOST
from django.http import JsonResponse
import json
import requests
from . models import Partner
from app. userInvite import SendInvite 
from app. emailmanager import InviteEmail
from app. models import (UserProfile,
    BusinessProfile,
    Invite,
    ProductListing,
    Order,
    Customer,
    Event,
    EventBooking,
    BusinessBranch,
    KnoledgeBase,
    MediaType,
    Plan,
    BillingInvoice,
     ProofOfPayment,
     PlanPackage,
     Testimonial,
     ProductFeature,
     UseCase,
     Integration,
     OrderNotification,
     DiskManager,
     AccountUpgrade,
     BusinessConfiguration,
     CustomerEmails,
      Feedback,
     FeedbackCount,

    )
import os
import uuid
import datetime
import random
import random
import json

from app. decorators import (
    user_controller
    ,allowed_users,
    form_complete,
    account_verification
    ,category_access,
    allowed_account,
    
    )

import uuid
from . models import Forum,Comment,Our_Projects,ProjectMedia,Topic,Category,TopicMedia,Partner_Request,Question,Question_Category,Q_Answer
import mimetypes
plan_Id = uuid.uuid1()
customer_Id = str(plan_Id)

# main homepage
@login_required(login_url='accounts/login' )
@form_complete

@category_access
@allowed_users(allowed_roles = ['Business'])

def home(request):
    
    return render(request,'app/index.html')




@login_required(login_url='accounts/login' )
@form_complete

@allowed_users(allowed_roles = ['Business'])

def main_dashboard(request):
    currentUser         = request.user
    profile             = UserProfile.objects.get(user = currentUser )
    businessInfo        = BusinessProfile.objects.get(business_ID = profile.business_ID)
    our_projects        = Our_Projects.objects.filter(business_ID = profile.business_ID)
    total_projects      = our_projects.count()
    info                = UserProfile.objects.get(user = currentUser)
    businessInfo        = BusinessProfile.objects.get(business_ID = info.business_ID)
    count_orders        = Order.objects.filter(Q(business_ID = info.business_ID) & Q(viewed = False)).count()
    customers           = Customer.objects.filter(business_ID = info.business_ID)
    inbox_messages      = customers.filter(inbox_messages__gt = 0).count()
    invoice_info        = BillingInvoice.objects.filter(business_ID = profile.business_ID)
    all_invoice         = BillingInvoice.objects.filter(business_ID = profile.business_ID).first()
    invoice_ID          = info.business_ID
    Our_Projects.objects.filter(business_ID = info.business_ID)
    ordernotification_status = OrderNotification.objects.filter(business_ID = info.business_ID).first()
    context = {"all_invoice":all_invoice,'total_projects':total_projects,"invoice_ID":invoice_ID,"count_orders":count_orders,"businessInfo":businessInfo, "inbox_messages":inbox_messages,"ordernotification_status":ordernotification_status}
    #send_mail_func.delay()
    business_ID = info.business_ID
    return render(request,'non_profit/non_profit.html',context)




def ecomm_dashboard_landing(request):
    
    return render(request,'landing-pages/index.html')


@login_required(login_url='accounts/login' )
@form_complete
@account_verification
@allowed_users(allowed_roles = ['Business'])

def non_profit_layer(request):
    currentUser    = request.user
    info           = UserProfile.objects.get(user = currentUser)
    businessInfo   = BusinessProfile.objects.get(business_ID = info.business_ID)
    totalcustomers = Customer.objects.filter(business_ID = info.business_ID).count()
    customers      = Customer.objects.filter(business_ID = info.business_ID)
    totalorders    = Order.objects.filter(business_ID = info.business_ID).count()
    inbox_messages = customers.filter(inbox_messages__gt = 0).count()
    configInfo     = BusinessConfiguration.objects.get(business_ID = info.business_ID)
    our_projects        = Our_Projects.objects.filter(business_ID = info.business_ID)
    total_projects      = our_projects.count()
    all_events          = Event.objects.filter(business_ID = info.business_ID)
    all_customers       = Customer.objects.filter(business_ID = info.business_ID)
    total_members       = all_customers.count()
    total_events        = all_events.count() 
    context  ={'total_projects':total_projects,'total_events':total_events,'total_members':total_members}
    # url = "https://api.gupshup.io/sm/api/v2/wallet/balance"

    # headers = {"apikey": configInfo.bot_apiKey}
    # response = requests.get(url, headers=headers)
    # data = json.loads(response.text)
    # balance = data['balance']
    # balance = "{:.2f}".format(round(balance, 2))

    
    # all_orders  =  Order.objects.filter(Q(business_ID = info.business_ID) & Q(viewed = False))
    
    # customers   = Customer.objects.filter(business_ID = info.business_ID)
    # inbox_messages = customers.filter(inbox_messages__gt = 0).count()
    # business_id = info.business_ID
    # diskspace = DiskManager.objects.get(business_ID =  business_id)
    
    
  
    # context = {"balance":balance,"businessInfo":businessInfo,'diskspace':diskspace,'all_orders':all_orders, "inbox_messages":inbox_messages,'totalcustomers':totalcustomers,'totalorders':totalorders,'customers':customers}
    return render(request,'layer/non-profit-layer.html', context)


# ======== Account ========== #
@form_complete
@account_verification
@login_required(login_url='accounts/login' )
@allowed_users(allowed_roles = ['Business'])
def addUser(request):
    currentUser    = request.user
    info           = UserProfile.objects.get(user = currentUser)
    all_invoice    = BillingInvoice.objects.filter(business_ID = info.business_ID).first()
    

    
    businessInfo   = BusinessProfile.objects.get(business_ID = info.business_ID)
    customers      = Customer.objects.filter(business_ID = info.business_ID)
    inbox_messages = customers.filter(inbox_messages__gt = 0).count()
    if request.method == "POST":
        # imagePreview       = request.FILES['imagePreview']
        firstname            = request.POST.get('firstname','')
        lastname             = request.POST.get('lastname','')
        email                = request.POST.get('email','')
        phone                = request.POST.get('phone','')
        role                 = request.POST.get('role','')
        
        currentUser = request.user
        info = UserProfile.objects.get(user = currentUser)
        qs = User.objects.filter(
                    Q(username__iexact = email)|
                    Q(email__iexact = email)
                )
        email_qs = Invite.objects.filter(
                    Q(phone__iexact = phone)|
                    Q(email__iexact = email)
                )
        if qs.exists():
                    messages.error(request, 'User With this email already exist!')
                    return redirect('main/non-profit/add-user')
        elif email_qs.exists():
            messages.error(request, 'User invite with this email or phone number already exist!')
            return redirect('main/non-profit/add-user')

                    
        else:
            inviteID    = uuid.uuid1()
            inviteID    = str(inviteID)
            Invite.objects.create(
            invite_ID   = inviteID,
            business_ID = info.business_ID,
            firstName   = firstname ,
            last_Name   = lastname,
            email       = email,
            role        = role ,
            phone       = phone,
           
            )
            user_invite = SendInvite()
            user_invite.invite_email(invite_ID   = inviteID,request = request)
            return redirect('main/non-profit/all-users')
            
    context ={"businessInfo":businessInfo,"inbox_messages":inbox_messages,}    
    return render(request,'non_profit/add-user.html',context)




def inviteForm(request,invite_ID):
    invite_info = Invite.objects.get(invite_ID = invite_ID)
        
    if invite_info.invite_status == True:
        messages.error(request, 'Account Already Exist!')
        return redirect('/')

    else:
        
            if request.method == "POST":
                email     = invite_info.email
                firstName = request.POST.get('firstName','')
                lastName  = request.POST.get('lastName','')
                password1 = request.POST.get('password1','')
                password2 = request.POST.get('password2','')
                qs = User.objects.filter(
                    Q(username__iexact = email)|
                    Q(email__iexact = email)
                )
                
                if password1 != password2 :
                    
                    messages.error(request, 'The two passwords fields did not match!')
                    return redirect('accounts/user-invite/create-account', invite_ID=invite_ID)
                    
                elif qs.exists():
                    messages.error(request, 'User With this email already exist!')
                    return redirect('accounts/user-invite/create-account', invite_ID=invite_ID) 
                    
                else:
                    user = User.objects.create_user(email ,email,password1)
                    login(request,user)
                    group = Group.objects.get(name='Business')
                    user.groups.add(group)
                    
                    useprofileID    = uuid.uuid1()
                    useprofileID    = str(useprofileID)
                    UserProfile.objects.create(user = user,
                    userprofileID  = invite_ID,
                    business_ID    = invite_info.business_ID,
                    firstName      = firstName,
                    last_Name      = lastName,
                    phone          =  invite_info.phone,
                    form_completed = True,
                            
                    
                    )
                    Invite.objects.filter(invite_ID = invite_ID).update(
                    firstName   = firstName,
                    last_Name   = lastName,
                    email       = email,
                    invite_status = True 
                    )
                    return redirect('/')
    context = {'invite_info':invite_info}  
    return render(request,'app/invite-form.html',context)




@form_complete
@account_verification
@login_required(login_url='accounts/login' )
@allowed_users(allowed_roles = ['Business'])
def allUser(request):
    currentUser    = request.user
    info           = UserProfile.objects.get(user = currentUser)
   


    
    businessInfo = BusinessProfile.objects.get(business_ID = info.business_ID)
    customers   = Customer.objects.filter(business_ID = info.business_ID)
    inbox_messages = customers.filter(inbox_messages__gt = 0).count()
    
    all_invite  = Invite.objects.filter(business_ID = info.business_ID)
    total_invite = all_invite.count()
    context     = { "businessInfo":businessInfo,
                   "inbox_messages":inbox_messages,
                   "all_invite":all_invite,
                    "total_invite":total_invite,
                    }
    return render(request,'non_profit/all-agents.html',context)



# ========   Members     ========== #
@login_required(login_url='accounts/login' )
@form_complete
@account_verification
@allowed_users(allowed_roles = ['Business'])
def all_members(request):
    currentUser = request.user
    info = UserProfile.objects.get(user = currentUser)
    
    businessInfo = BusinessProfile.objects.get(business_ID = info.business_ID)
    all_products = ProductListing.objects.filter(business_ID = info.business_ID)
    all_customers = Customer.objects.filter(business_ID = info.business_ID)
    total_customers = Customer.objects.filter(business_ID = info.business_ID).count()
    customers   = Customer.objects.filter(business_ID = info.business_ID)
    inbox_messages = customers.filter(inbox_messages__gt = 0).count()
    context = {"businessInfo":businessInfo,
               'all_customers':all_customers,
               "inbox_messages":inbox_messages,
               'total_customers':total_customers}
    return render(request,'non_profit/all-members.html',context)



@login_required(login_url='accounts/login' )
@form_complete
@account_verification
@allowed_users(allowed_roles = ['Business'])
def add_member(request):
    currentUser = request.user
    info        = UserProfile.objects.get(user = currentUser)
    invoice_ID  = info.business_ID
    businessInfo = BusinessProfile.objects.get(business_ID = info.business_ID)
    customers   = Customer.objects.filter(business_ID = info.business_ID)
    inbox_messages = customers.filter(inbox_messages__gt = 0).count()
    customer_ID    = uuid.uuid1()
    customer_ID    = str(customer_ID)
    if request.method == "POST":
        FullName      = request.POST.get('FullName','')
        PhoneNumber   = request.POST.get('PhoneNumber','')
        Code          = request.POST.get('Code','')
        Country       = request.POST.get('Country','')
        Orders        = request.POST.get('Orders','')
        TotalSpent    = request.POST.get('TotalSpent','')
        Location      = request.POST.get('Location','')
        customers     = Customer.objects.filter(business_ID = info.business_ID)
        if customers.filter(phone = PhoneNumber).exists:
            messages.error(request, 'This member you are trying to add already exist!')

        else:
                Customer.objects.create(
                        business_ID        = info.business_ID,
                        customer_ID        = customer_ID,
                        customerName       = FullName,
                        phone              = PhoneNumber,
                        code               = Code,
                        country            = Country,
                        total_Amount       = TotalSpent,
                        location           = Location,
                        orderQuantity      = Orders 
                    )
                messages.success(request, 'Member has been successifully created.')
                return redirect('main/account/members')
    context = {"invoice_ID":invoice_ID,"businessInfo":businessInfo,"inbox_messages":inbox_messages,}
    return render(request,'non_profit/add-customer.html',context)





@login_required(login_url='accounts/login' )
@form_complete
@account_verification
@allowed_users(allowed_roles = ['Business'])
def forum_detail(request,postID):
   info          =  Forum.objects.get(postID     = postID)
   info_comment  = Comment.objects.filter(postID     = postID)
   total_comment = info_comment.count()
   context = {'info':info,'info_comment':info_comment,'total_comment':total_comment}

   return render(request,'non_profit/forum-post.html',context)


# ==========     Partners   =========== #

@login_required(login_url='accounts/login' )
@form_complete
@account_verification
@allowed_users(allowed_roles = ['Business'])
def all_partners(request):
   
   user          = request.user
   user_profile  = UserProfile.objects.get(user = user)
   all_partner   = Partner.objects.filter(business_ID  = user_profile.business_ID)
   
   context       = {'all_partner':all_partner}

   return render(request,'non_profit/partiners.html',context)




@login_required(login_url='accounts/login' )
@form_complete
@account_verification
@allowed_users(allowed_roles = ['Business'])
def add_partner(request):
   
   user                          = request.user
   user_profile                  = UserProfile.objects.get(user = user)
   all_partner                   = Partner.objects.filter(business_ID  = user_profile.business_ID)

   if request.method == "POST":
        organisation_logo             = request.FILES['organisation_logo']
        organisation_name             = request.POST.get('organisation_name','')
        description                   = request.POST.get('description','') 

        Partner.objects.create(business_ID  = user_profile.business_ID,
                               partner_organisation         =  organisation_name,
                                partner_type                = 'NGO',
                               
                                partner_thubnail            =  organisation_logo,
                                description                 =  description ,
                               )
        return redirect('main/non-profit/All-Partners')
   
   context       = {'all_partner':all_partner}

   return render(request,'non_profit/add_partner.html',context)





@login_required(login_url='accounts/login' )
@form_complete
@account_verification
@allowed_users(allowed_roles = ['Business'])
def partner_requests(request):
   
   user                          = request.user
   user_profile                  = UserProfile.objects.get(user = user)
   all_partners                  = Partner_Request.objects.filter(business_ID  = user_profile.business_ID)
   total_request                 = all_partners.count()
   context                       = {'all_partners':all_partners, 'total_request':total_request }
   return render(request,'non_profit/partner_request.html',context)

# ========   Community    ========== #

@login_required(login_url='accounts/login' )
@form_complete
@account_verification
@allowed_users(allowed_roles = ['Business'])
def create_forum_topic(request):
   
   user          = request.user
   user_profile  = UserProfile.objects.get(user = user)
   
   if request.method == "POST":
        thumb_image             = request.FILES['thumb_image']
        topic_tittle            = request.POST.get('topic_tittle','')
        topic_type              = request.POST.get('topic_type','')
        description             = request.POST.get('description','')

        topic_ID     = uuid.uuid1()
        topic_ID     = str(topic_ID )
        Forum.objects.create(

             business_ID       = user_profile.business_ID,
            topic_ID           = topic_ID,
            topic_status      = topic_type,
            topic_title       = topic_tittle,
            topic_thubnail    = thumb_image,
            topic_description = description,

        )
        return redirect('main/non-profit/account/forum')


   return render(request,'non_profit/create-forum-topic.html')




@login_required(login_url='accounts/login' )
@form_complete
@account_verification
@allowed_users(allowed_roles = ['Business'])
def forum_topic_list(request):
   
   user             = request.user
   business_profile = BusinessProfile.objects.get(user = user)
   business_ID      = business_profile.business_ID
   forum_info       = Forum.objects.filter(business_ID = business_ID)
   context = {'forum_info':forum_info}

   return render(request,'non_profit/forum.html',context)



@login_required(login_url='accounts/login' )
@form_complete
@account_verification
@allowed_users(allowed_roles = ['Business'])
def forum_topic_detail(request,topic_ID):
   user             = request.user
   forum_info       = Forum.objects.get(topic_ID = topic_ID)
   business_profile = BusinessProfile.objects.get(user = user)
   business_ID      = business_profile.business_ID
   forum_data       = Forum.objects.filter(business_ID = business_ID)
   if request.method == "POST":
        
        comment            = request.POST.get('comment','')

        Comment.objects.create(
          
         business_ID       = business_ID ,
        topic_ID          =  topic_ID,
        topic_status      = 'Closed',
        member_first_name = 'Tinoteda',
        member_last_name  ='Tinoteda',
        member_comment    =  comment,
        comment_type     = 'Self',

        )
   
   all_comments     = Comment.objects.filter(topic_ID = topic_ID)
   context          = {'forum_info':forum_info,'forum_data':forum_data,'all_comments':all_comments,'topic_ID': topic_ID}

   return render(request,'non_profit/messages.html',context)


@login_required(login_url='accounts/login' )
@form_complete
@account_verification
@allowed_users(allowed_roles = ['Business'])
def delete_forum(request,topic_ID):
     Forum.objects.filter(topic_ID = topic_ID).delete()
     Comment.objects.filter(topic_ID = topic_ID).delete()
     messages.success(request, "You have successifully deleted forum topic.")
     return redirect('/')


# ========   Customer Feedback    ========== #
@login_required(login_url='accounts/login' )
@form_complete
@account_verification
@allowed_users(allowed_roles = ['Business'])
def customer_feedback(request):
    currentUser    = request.user
    info           = UserProfile.objects.get(user = currentUser)
   
    
    businessInfo      = BusinessProfile.objects.get(business_ID = info.business_ID)
    customers         = Customer.objects.filter(business_ID     = info.business_ID)
    current_customer  = Customer.objects.filter(business_ID  = info.business_ID).first()
    all_feedback      = Feedback.objects.filter(customer_ID     = info.userprofileID)
    total_feedback    = FeedbackCount.objects.filter(business_ID = info.business_ID).first()
    inbox_messages    = customers.filter(inbox_messages__gt = 0).count()
    context           = {"total_feedback":total_feedback,"current_customer":current_customer,"customers":customers,"businessInfo":businessInfo,'all_feedback':all_feedback,"inbox_messages":inbox_messages,}
    return render(request,'non_profit/customerfeedback.html',context)



@login_required(login_url='accounts/login' )
@form_complete
@account_verification
@allowed_users(allowed_roles = ['Business'])
def customer_feedback_details(request,customer_ID):
    currentUser    = request.user
    info           = UserProfile.objects.get(user = currentUser)
    
   
    
    businessInfo      = BusinessProfile.objects.get(business_ID = info.business_ID)
    all_feedback      = Feedback.objects.filter(customer_ID = customer_ID)
    customers         = Customer.objects.filter(business_ID = info.business_ID)
    current_customer  = Customer.objects.get(customer_ID = customer_ID)
    inbox_messages    = customers.filter(inbox_messages__gt = 0).count()
    context           = {"current_customer":current_customer,"customers":customers,"businessInfo":businessInfo,'all_feedback':all_feedback,"inbox_messages":inbox_messages,}
    return render(request,'non_profit/customerfeedback-detail.html',context)





# ========   Our Projects    ========== #
@login_required(login_url='accounts/login' )
@form_complete
@account_verification
@allowed_users(allowed_roles = ['Business'])
def work_and_impact(request):
   
   user             = request.user
   business_profile = BusinessProfile.objects.get(user = user)
   business_ID      = business_profile.business_ID
   all_projects     = Our_Projects.objects.filter(business_ID      = business_ID )
   total_projects   = all_projects.count()



   if request.method == "POST":
        form_type               = request.POST.get('form_type','')
        if form_type == 'add-project':
        
            thumb_image             = request.FILES['thumb_image']
            project_date            = request.POST.get('project_date','')
            project_tittle          = request.POST.get('project_tittle','')
            description             = request.POST.get('description','')
            project_date            = datetime.datetime.strptime(project_date,'%m-%d-%Y  %I:%M')
            project_ID              = uuid.uuid1()
            project_ID              = str(project_ID)

            Our_Projects.objects.create(
            business_ID            =   business_ID,
                project_ID             =  project_ID,
                project_date           =  project_date, 
                project_tittle         =  project_tittle, 
                project_thubnail       =   thumb_image,
                project_description    =  description
            )
            return redirect('main/account/non-profit/Work-and-impact')
        else:
            project_id              = request.POST.get('project_id','')
            project_date            = request.POST.get('project_date','')
            project_tittle          = request.POST.get('project_tittle','')
            description             = request.POST.get('description','')
            project_date            = datetime.datetime.strptime(project_date,'%m-%d-%Y  %I:%M')
            

            Our_Projects.objects.filter(project_ID  =  project_id,).update(
            
                project_date           =  project_date, 
                project_tittle         =  project_tittle, 
                project_description    =  description
            )
        return redirect('main/account/non-profit/Work-and-impact')

   context = {'all_projects':all_projects, 'total_projects':total_projects }

   return render(request,'non_profit/Work-and-impact.html',context)





@login_required(login_url='accounts/login' )
@form_complete
@account_verification
@allowed_users(allowed_roles = ['Business'])
def work_and_impact_detail(request,project_ID):
   user             = request.user
   business_profile = BusinessProfile.objects.get(user = user)
   business_ID      = business_profile.business_ID
   projects_detail  = Our_Projects.objects.get(project_ID = project_ID)
   all_media        =  ProjectMedia.objects.filter(project_ID = project_ID)
   total_media      =  ProjectMedia.objects.filter(project_ID = project_ID).count()

   if request.method == "POST":
        
        thumb_image    = request.FILES['thumb_image']


        ProjectMedia.objects.create(
       business_ID                      = business_ID,
       project_ID                       =project_ID,
       project_media                    = thumb_image,

        )
        return redirect('main/account/non-profit/Work-and-impact/project',project_ID = project_ID)

   context          = {'projects_detail':projects_detail,'all_media':all_media,'total_media':total_media,'project_ID':project_ID}

   return render(request,'non_profit/impact_project_detail.html',context)




@login_required(login_url='accounts/login' )
@form_complete
@account_verification
@allowed_users(allowed_roles = ['Business'])
def delete_project_media(request,id,project_ID):
    ProjectMedia.objects.filter(id = id).delete()
    return redirect('main/account/non-profit/Work-and-impact/project',project_ID = project_ID)


@login_required(login_url='accounts/login' )
@form_complete
@account_verification
@allowed_users(allowed_roles = ['Business'])
def delete_project(request,project_ID):
    ProjectMedia.objects.filter(project_ID   = project_ID,).delete()
    Our_Projects.objects.filter(project_ID = project_ID).delete()
    return redirect('main/account/non-profit/Work-and-impact')


# ========   Knowledge_hub    ========== #

@login_required(login_url='accounts/login' )
@form_complete
@account_verification
@allowed_users(allowed_roles = ['Business'])
def knowledge_hub(request):
   
   user             = request.user
   business_profile = BusinessProfile.objects.get(user = user)
   business_ID      = business_profile.business_ID
   all_categories   =  Category.objects.filter(business_ID  = business_ID)
   all_topics       = Topic.objects.filter(business_ID  = business_ID)
   total_topics     = all_topics.count()

   if request.method == "POST":
        form_type               = request.POST.get('form_type','')
        if form_type == 'add-topic':
        
           
            topic_tittle            = request.POST.get('topic_tittle','')
            category                = request.POST.get('category','')
            description             = request.POST.get('description','')
            
            topic_ID              = uuid.uuid1()
            topic_ID              = str(topic_ID)
           

            Topic.objects.create(
            business_ID            = business_ID,
            topic_ID               = topic_ID,
            topic_tittle           = topic_tittle,
            category               = category,
            description            = description
            )

            return redirect('main/account/non-profit/knowledge_hub')
        else:
            category                = request.POST.get('category','')
            
            Category.objects.create(
                business_ID     = business_ID,
                category        = category,
             )
            return redirect('main/account/non-profit/knowledge_hub')
   context = {'all_categories':all_categories,'all_topics':all_topics,'total_topics':total_topics}

   return render(request,'non_profit/learning_material.html',context)



@login_required(login_url='accounts/login' )
@form_complete
@account_verification
@allowed_users(allowed_roles = ['Business'])
def knowledge_hub_detail(request,topic_ID):
   user             = request.user
   business_profile = BusinessProfile.objects.get(user = user)
   business_ID      = business_profile.business_ID
   topic_details    = Topic.objects.get(topic_ID = topic_ID  )
   all_media        = TopicMedia.objects.filter(topic_ID = topic_ID)
   my_media_files    = TopicMedia.objects.filter(topic_ID = topic_ID)
   all_files         = TopicMedia.objects.filter(topic_ID = topic_ID)
   images            = all_files.filter(Q(file_type ='image/jpeg') or Q(file_type ='image/png') or Q(file_type ='image/jpg')) 
   total_images      = images.count()

   videos            = all_files.filter(file_type ='video/mp4') 
   total_videos      = videos.count()  
   documents         =  all_files.filter(file_type = 'application/pdf')
   audio_file        =  all_files.filter(Q(file_type = 'audio/mpeg') or Q(file_type = 'audio/ogg'))
   total_audio_files = audio_file.count()
   total_documents   = documents.count()
   total_media_files =  my_media_files.count()

   if request.method == 'POST':
        
        upload_file = request.FILES.get('upload_file')
        
        

        if not  upload_file:
            messages.error(request, " file is required.")

            return redirect('main/account/non-profit/knowledge_hub/details/info',topic_ID=topic_ID)

        max_size_mb = 4

        if upload_file.size > 4 * 1024 * 1024:
            messages.error(request, f"File size cannot exceed {max_size_mb}MB.")
            return redirect('main/account/non-profit/knowledge_hub/details/info',topic_ID=topic_ID)

        mime_type, _ = mimetypes.guess_type(upload_file.name)
        mime_type = mime_type or 'application/octet-stream'

        ALLOWED_MIME_TYPES = [
            'image/jpeg', 'image/png', 'image/jpg',           # Image formats
            'video/mp4',                         # Video format
            'audio/mpeg', 'audio/ogg',           # Audio formats
            'application/pdf'                    # Document format
        ]

        if mime_type not in ALLOWED_MIME_TYPES:
            messages.error(request, "Unsupported file type.")
            return redirect('main/account/non-profit/knowledge_hub/details/info',topic_ID=topic_ID)

        # Extract file extension
        _, file_extension = os.path.splitext(upload_file.name)
        file_extension = file_extension.lower()  # Normalize to lowercase
        file_size_mb = round(upload_file.size / (1024 * 1024), 2)
        TopicMedia.objects.create(

            business_ID          = business_ID,
            topic_ID             = topic_ID, 
            media                = upload_file,
            title                = upload_file.name,
            file_type            = mime_type,
            file_extension       = file_extension,
            file_size            = file_size_mb,
        )

        messages.success(request, "File uploaded successfully!")
        return redirect('main/account/non-profit/knowledge_hub/details/info',topic_ID=topic_ID)
   context = {'total_videos':total_videos,'videos':videos,'total_images':total_images,'images':images,'audio_file':audio_file,'total_audio_files':total_audio_files,'total_documents':total_documents,'documents':documents,'topic_details':topic_details,'all_media':all_media,'my_media_files':my_media_files,'total_media_files':total_media_files,'topic_ID':topic_ID}
   
   return render(request,'non_profit/knowledgehub_details.html',context)

@login_required(login_url='accounts/login' )
@form_complete
@account_verification
@allowed_users(allowed_roles = ['Business'])
def delete_topic(request,topic_ID):
    
    Topic.objects.filter(topic_ID = topic_ID  ).delete()
    TopicMedia.objects.filter(topic_ID = topic_ID).delete()
    messages.success(request, "You have successifully deleted topic.")
    return redirect('main/account/non-profit/knowledge_hub')


@login_required(login_url='accounts/login' )
@form_complete
@account_verification
@allowed_users(allowed_roles = ['Business'])
def delete_media(request,id,topic_ID):
     TopicMedia.objects.filter(id = id).delete()
     messages.success(request, "You have successifully deleted media.")
     return redirect('main/account/non-profit/knowledge_hub/details/info',topic_ID=topic_ID)


@login_required(login_url='accounts/login' )
@form_complete
@account_verification
@allowed_users(allowed_roles = ['Business'])
def edit_topic(request,topic_ID):
   topic_details    = Topic.objects.get(topic_ID = topic_ID  )
   user             = request.user
   business_profile = BusinessProfile.objects.get(user = user)
   business_ID      = business_profile.business_ID
   all_categories   =  Category.objects.filter(business_ID  = business_ID)
   topic_details    = Topic.objects.get(topic_ID = topic_ID  )
   if request.method == "POST":
        
           
            topic_tittle            = request.POST.get('topic_tittle','')
            category                = request.POST.get('category','')
            description             = request.POST.get('description','')
            
            
            Topic.objects.filter(topic_ID   = topic_ID).update(
            topic_tittle           = topic_tittle,
            category               = category,
            description            = description
            )
            return redirect('main/account/non-profit/knowledge_hub/details/info',topic_ID=topic_ID) 

   context          = {'topic_details':topic_details,'all_categories':all_categories,'topic_details':topic_details}
   return render(request,'non_profit/edit-topic.html',context)



# =========  FAQs   ============ #

@login_required(login_url='accounts/login' )
@form_complete
@account_verification
@allowed_users(allowed_roles = ['Business'])
def faqs(request):
     
   currentUser  = request.user
   info         = UserProfile.objects.get(user = currentUser)
   business_ID  = info.business_ID
   all_question = Question.objects.filter(business_ID  = business_ID )
   all_answer   = Q_Answer.objects.filter(business_ID  = business_ID )
   all_category     = Question_Category.objects.filter(business_ID  = business_ID)

   if request.method == "POST":
        form_type               = request.POST.get('form_type','')
        if form_type == 'add-question':
        
           
            question                = request.POST.get('question','')
            category                = request.POST.get('category','')
            
            
            question_ID              = uuid.uuid1()
            question_ID              = str(question_ID)
           

            Question.objects.create(
            business_ID                = business_ID,
            question_ID                = question_ID,
            question                   =  question,
            category                  = category,
            )

            return redirect('account/non-profit/faqs')
        else:
            category                = request.POST.get('category','')
            
            Question_Category.objects.create(
                business_ID     = business_ID,
                category        = category,
             )
            return redirect('account/non-profit/faqs')
   
   context       = {'all_question':all_question,'all_category':all_category,'all_answer':all_answer}

   return render(request,'non_profit/faqs.html',context)

@login_required(login_url='accounts/login' )
@form_complete
@account_verification
@allowed_users(allowed_roles = ['Business'])
def faqs_answers(request,question_ID ):
   question    = Question.objects.get(question_ID = question_ID)
   all_answers = Q_Answer.objects.filter(question_ID = question_ID)

   if request.method == "POST":
        answer               = request.POST.get('answer','')
        Q_Answer.objects.create(
          business_ID                   = question.business_ID, 
          question_ID                   = question_ID ,
          answer                        =  answer,   
        )
        

   context       = {'question':question,'all_answers':all_answers}

   return render(request,'non_profit/faq-answers.html',context)


@login_required(login_url='accounts/login' )
@form_complete
@account_verification
@allowed_users(allowed_roles = ['Business'])
def delete_answer(request,question_ID,id ):
   Q_Answer.objects.filter(id = id).delete()
   
   return redirect('account/non-profit/faqs/answers',question_ID = question_ID)



@login_required(login_url='accounts/login' )
@form_complete
@account_verification
@allowed_users(allowed_roles = ['Business'])
def delete_question(request,question_ID ):
   Q_Answer.objects.filter(question_ID = question_ID).delete()
   Question.objects.filter(question_ID = question_ID).delete()
   
   return redirect('account/non-profit/faqs/answers',question_ID = question_ID)


# ========  Event    ========== #
@login_required(login_url='accounts/login' )
@allowed_users(allowed_roles = ['Business'])
def publishEvent(request):
    currentUser = request.user
    info        = UserProfile.objects.get(user = currentUser)
    invoice_ID  = info.business_ID
    customers   = Customer.objects.filter(business_ID = info.business_ID)
    inbox_messages = customers.filter(inbox_messages__gt = 0).count()
    businessInfo = BusinessProfile.objects.get(business_ID = info.business_ID)
    if request.method == "POST":
        try:
            event_tittle         = request.POST.get('event_tittle','')
            event_week_day       = request.POST.get('week_day','')
            event_day            = request.POST.get('event_day','')
            event_month          = request.POST.get('event_month','')
            event_year           = request.POST.get('event_year','')
            event_time           = request.POST.get('event_time','')
            
            event_type           = request.POST.get('event_type','')
            if event_type == 'online':
                online_status = True
            else:
                online_status = False
            # end_event_day            = request.POST.get('end_event_day','')
            # end_event_month          = request.POST.get('end_event_month','')
            # end_event_year           = request.POST.get('end_event_year','')
            # end_event_time           = request.POST.get('end_event_time','')
            start_time               = request.POST.get('start_time','')
            end_time                 = request.POST.get('end_time','')
            description              = request.POST.get('description','')
            event_image              = request.FILES['event_image']
            months = {"1":"January",
                    "2":"February", 
                    "3":"March", 
                    "4":"April", 
                    "5":"May", 
                    "6":"June",
                    "7":"July", 
                    "8":"August", 
                    "9":"September", 
                    "10":"October", 
                    "11":"November",
                    "12":"December"}
            month = months[event_month]
            
            start_fullDate           = event_week_day + ' ' + event_day  + ' ' + month + ' ' + event_year
            start_Date               = event_day+'/'+event_month +'/'+event_year
            actualdate               = event_month +'/'+event_day+'/'+event_year+' '+event_time
            dateobj                  = datetime.datetime.strptime(actualdate,'%m/%d/%Y  %H:%M')
            # endfullDate              = end_week_day + '' + end_event_day + '' + end_event_month + '' + end_event_year
            print(start_fullDate)
            print(actualdate)
            print(dateobj)
            currentUser = request.user
            info = UserProfile.objects.get(user = currentUser)
            
            eventID    = uuid.uuid1()
            eventID    = str(eventID)
            Event.objects.create(
                business_ID        = info.business_ID,
                event_ID           = eventID,
                event_Name         = event_tittle,
                event_Description  = description,
                eventimage         = event_image,
                startTime          = event_time,
                image_status       = True,
                startfulldate      = start_fullDate,
                startactualdate    = dateobj,
                
                # endfullDate        = endfullDate,
                online_event       =  online_status,
                endTime            = end_time,)
            messages.success(request, 'You have successifully published an event.!')    
        except Exception as exp:
            print(exp)
    context = {"invoice_ID":invoice_ID,"businessInfo":businessInfo,"inbox_messages":inbox_messages,}
    return render(request,'non_profit/add-event.html',context)




# ========  Event  Edit  ========== #
@login_required(login_url='accounts/login' )
@allowed_users(allowed_roles = ['Business'])
def editEvent(request,EventID):
    currentUser = request.user
    info        = UserProfile.objects.get(user = currentUser)
    invoice_ID  = info.business_ID
    customers   = Customer.objects.filter(business_ID = info.business_ID)
    inbox_messages = customers.filter(inbox_messages__gt = 0).count()
    eventInfo = Event.objects.get(event_ID =EventID)
    businessInfo = BusinessProfile.objects.get(business_ID = info.business_ID)
    context = {
        "invoice_ID":invoice_ID,
        "businessInfo":businessInfo,
        "inbox_messages":inbox_messages,
        'eventInfo':eventInfo
    }
    if request.method == "POST":

        try:
            event_tittle         = request.POST.get('event_tittle','')
            event_week_day       = request.POST.get('week_day','')
            event_day            = request.POST.get('event_day','')
            event_month          = request.POST.get('event_month','')
            event_year           = request.POST.get('event_year','')
            event_time           = request.POST.get('event_time','')

            event_type           = request.POST.get('event_type','')
            if event_type == 'online':
                online_status = True
            else:
                online_status = False
            # end_event_day            = request.POST.get('end_event_day','')
            # end_event_month          = request.POST.get('end_event_month','')
            # end_event_year           = request.POST.get('end_event_year','')
            # end_event_time           = request.POST.get('end_event_time','')
            start_time               = request.POST.get('start_time','')
            end_time                 = request.POST.get('end_time','')
            description              = request.POST.get('description','')
            
            months = {"1":"January",
                    "2":"February", 
                    "3":"March", 
                    "4":"April", 
                    "5":"May", 
                    "6":"June",
                    "7":"July", 
                    "8":"August", 
                    "9":"September", 
                    "10":"October", 
                    "11":"November",
                    "12":"December"}
            month = months[event_month]
            start_fullDate           = event_week_day + ' ' + event_day  + ' ' + month + ' ' + event_year
            start_Date               = event_day+'/'+event_month +'/'+event_year
            actualdate               = event_month +'/'+event_day+'/'+event_year+' '+event_time
            dateobj                  = datetime.datetime.strptime(actualdate,'%m/%d/%Y  %H:%M')
            # endfullDate              = end_week_day + '' + end_event_day + '' + end_event_month + '' + end_event_year
            
            print(dateobj)
            currentUser = request.user
            info = UserProfile.objects.get(user = currentUser)
            
            
            Event.objects.filter(event_ID =EventID).update(
                
                event_Name         = event_tittle,
                event_Description  = description,
                image_status       = True,
                 startTime         = event_time,
                startfulldate      = start_fullDate,
                startactualdate    = dateobj,
                
                # endfullDate        = endfullDate,
                online_event       =  online_status,
                endTime            = end_time,

            )
            event_image              = request.FILES['event_image']
            if len(event_image) != 0:
                if len(eventInfo.eventimage) > 0:
                    os.remove(eventInfo.eventimage.path)
                    eventInfo.eventimage = event_image
                    eventInfo.save()
            return redirect('events/all-events')
        except Exception as exp:
            print(exp)
           
    
    return render(request,'non_profit/edit-event.html',context)


@login_required(login_url='accounts/login' )
@allowed_users(allowed_roles = ['Business'])
def deleteEvent(request,EventID):
    Event.objects.filter(event_ID =EventID).delete()
    return redirect('events/all-events')



@login_required(login_url='accounts/login' )
@allowed_users(allowed_roles = ['Business'])
def allEvents(request):
    currentUser = request.user
    info      =  UserProfile.objects.get(user = currentUser)
    invoice_ID  = info.business_ID
    all_events =  Event.objects.filter(business_ID = info.business_ID)
    total_events = all_events.count()
    customers   = Customer.objects.filter(business_ID = info.business_ID)
    inbox_messages = customers.filter(inbox_messages__gt = 0).count()
    current_time  = datetime.datetime.now()
    businessInfo = BusinessProfile.objects.get(business_ID = info.business_ID)
    context    = {
        "invoice_ID":invoice_ID,
        "businessInfo":businessInfo,
        "current_time":current_time,
        "inbox_messages":inbox_messages,
        'total_events':total_events,
       'all_events': all_events
    }
    return render(request,'non_profit/all-events.html',context)



@login_required(login_url='accounts/login' )
@allowed_users(allowed_roles = ['Business'])
def eventsBookings(request):
    currentUser = request.user
    info        =  UserProfile.objects.get(user = currentUser)
    invoice_ID  = info.business_ID
    customers   = Customer.objects.filter(business_ID = info.business_ID)
    inbox_messages = customers.filter(inbox_messages__gt = 0).count()
    all_bookings =  EventBooking.objects.filter(business_ID = info.business_ID)
    totalBookings = all_bookings.count()
    current_time  = datetime.datetime.now()
    businessInfo = BusinessProfile.objects.get(business_ID = info.business_ID)
    
   
        
    context    = {
        "invoice_ID":invoice_ID,
        "businessInfo":businessInfo,
        "current_time":current_time,
        "totalBookings":totalBookings,
        "inbox_messages":inbox_messages,
       'all_bookings': all_bookings
    }
    return render(request,'non_profit/event-bookings.html',context)


def deletebooking(request,booking_ID):
    EventBooking.objects.filter(booking_ID = booking_ID).delete()
    messages.success(request, 'You have  successifully deleted  event booking!')
    return redirect('main/account/non-profit/all-events/bookings')



@login_required(login_url='accounts/login' )
@allowed_users(allowed_roles = ['Business'])
def my_settings(request):
    current_user = request.user
    profile      = UserProfile.objects.get(user = current_user)
    invoice_ID     = profile.business_ID
    businessInfo = BusinessProfile.objects.get(business_ID = profile.business_ID)
    if request.method == "POST":
        try:
            if request.FILES:
            
                business_name        = request.POST.get('business_name','')
                business_adress      = request.POST.get('business_adress','')
                street_name          = request.POST.get('street_name','')
                email                = request.POST.get('email','')
                
                BusinessProfile.objects.filter(business_ID = profile.business_ID).update(
                    BusinessName    = business_name,
                    Business_adress = business_adress,
                    street_name     = street_name,
                    email           = email,
                   

                )
                company_logo         = request.FILES['company_logo']
                if len(company_logo) != 0:
                    if businessInfo.logo_image:
                        if len(businessInfo.logo_image) > 0:
                            os.remove(businessInfo.logo_image.path)
                            businessInfo.logo_image = company_logo
                            businessInfo.save()
                    else:
                        businessInfo.logo_image = company_logo
                        businessInfo.save()
                        messages.success(request, 'Your have successifully updated your business profile.')
                        
            else:    
                business_name        = request.POST.get('business_name','')
                business_adress      = request.POST.get('business_adress','')
                street_name          = request.POST.get('street_name','')
                email                = request.POST.get('email','')
                BusinessProfile.objects.filter(business_ID = profile.business_ID).update(
                        BusinessName    = business_name,
                        Business_adress = business_adress,
                        street_name     = street_name,
                        email           = email,
                )
                messages.success(request, 'Your have successifully updated your business profile.')
                return redirect('account/non-profit/settings')
        except Exception as exp:
            print(exp)
    context      = {'businessInfo':businessInfo}
    return render(request,'non_profit/settings.html',context )







@login_required(login_url='accounts/login' )
@allowed_users(allowed_roles = ['Business'])
def billing_plan(request):
    all_plan     = Plan.objects.all()
    current_user = request.user
    profile      = UserProfile.objects.get(user = current_user)
    invoice_ID     = profile.business_ID
    businessInfo = BusinessProfile.objects.get(business_ID = profile.business_ID)
    current_plan = Plan.objects.get(Plan_ID = businessInfo.Plan_ID)
    
    packages     = PlanPackage.objects.all()
    context      = {'packages':packages,'all_plan':all_plan,'businessInfo':businessInfo,'current_plan':current_plan}
    return render(request,'non_profit/plans.html',context)




@login_required(login_url='accounts/login' )
@allowed_users(allowed_roles = ['Business'])
def billing_invoices(request):
    current_time  = datetime.datetime.now()
    current_user = request.user
    profile      = UserProfile.objects.get(user = current_user)
    
    businessInfo = BusinessProfile.objects.get(business_ID = profile.business_ID)
    current_plan = Plan.objects.get(Plan_ID = businessInfo.Plan_ID)
    invoice_info  = BillingInvoice.objects.filter(business_ID = profile.business_ID)
    all_invoice  = BillingInvoice.objects.filter(business_ID = profile.business_ID).first()
    
    context      = {"invoice_info":invoice_info,'current_time': current_time,'all_invoice':all_invoice,'businessInfo':businessInfo,'current_plan':current_plan}
    return render(request,'non_profit/billing.html',context)

@login_required(login_url='accounts/login' )
@allowed_users(allowed_roles = ['Business'])
def invoices_detail(request,invoice_ID):
    current_user = request.user
    profile      = UserProfile.objects.get(user = current_user)
    invoice_ID     = profile.business_ID
    businessInfo = BusinessProfile.objects.get(business_ID = profile.business_ID)
    current_plan = Plan.objects.get(Plan_ID = businessInfo.Plan_ID)
    all_invoice  = BillingInvoice.objects.get(business_ID = invoice_ID)
    context      = {"invoice_ID":invoice_ID,'all_invoice':all_invoice,'businessInfo':businessInfo,'current_plan':current_plan}
    return render(request,'app/invoice/invoice.html',context)


@login_required(login_url='accounts/login' )
@allowed_users(allowed_roles = ['Business'])
def payment_page(request,Invoice_ID):
    current_user = request.user
    profile      = UserProfile.objects.get(user = current_user)
    invoice_ID     = profile.business_ID
    businessInfo = BusinessProfile.objects.get(business_ID = profile.business_ID)
    all_invoice  = BillingInvoice.objects.get(Invoice_ID = Invoice_ID)
    context      = {"invoice_ID":invoice_ID,'all_invoice':all_invoice}
    return render(request,'app/pay.html',context)



@login_required(login_url='accounts/login' )
@allowed_users(allowed_roles = ['Business'])
def account_upgrade(request,plan_ID):
    
    all_plan     = Plan.objects.all()
    current_user = request.user
    profile      = UserProfile.objects.get(user = current_user)
    invoice_ID     = profile.business_ID
    businessInfo = BusinessProfile.objects.get(business_ID = profile.business_ID)
    current_plan = Plan.objects.get(Plan_ID = businessInfo.Plan_ID)
    planupdate   = Plan.objects.get(Plan_ID = plan_ID)
    account_upgrade_info = AccountUpgrade.objects.filter(business_ID = profile.business_ID)
    if account_upgrade_info.exists():
        AccountUpgrade.objects.filter(business_ID = profile.business_ID).update(
            Plan_upgrade_to        = planupdate.Plan_Name,
            Plan_upgrade_Id        = planupdate.Plan_ID,
            price                  = planupdate.Price 
        )
        messages.success(request, "Your account upgrade have been sceduled successifully.")
    else:
        planinfo   = Plan.objects.get(Plan_ID = businessInfo.Plan_ID)
        AccountUpgrade.objects.create(
            business_ID            = profile.business_ID,
            Business_Name          = businessInfo.BusinessName,
            current_Plan           = planinfo.Plan_Name,
            current_Plan_Id        = current_plan.Plan_ID,
            current_monthly_amount = current_plan.Price ,
            Plan_upgrade_to        = planupdate.Plan_Name,
            price                  = planupdate.Price,
            Plan_upgrade_Id        = planupdate.Plan_ID,

        )
        messages.success(request, "Your account upgrade have been sceduled successifully.")

    return redirect('account/billing-plan')


@login_required(login_url='accounts/login' )
@allowed_users(allowed_roles = ['Business'])
def diskspace(request):
    current_user = request.user
    profile      = UserProfile.objects.get(user = current_user)
    invoice_ID     = profile.business_ID
    businessInfo = BusinessProfile.objects.get(business_ID = profile.business_ID)
    context = {"invoice_ID":invoice_ID,"businessInfo":businessInfo}
    return render(request,'non_profit/storage-disk.html',context)



@login_required(login_url='accounts/login' )
@allowed_users(allowed_roles = ['Business'])
def message_balance(request):
    current_user = request.user
    profile      = UserProfile.objects.get(user = current_user)
    invoice_ID     = profile.business_ID
    businessInfo = BusinessProfile.objects.get(business_ID = profile.business_ID)
    configInfo     = BusinessConfiguration.objects.get(business_ID = profile.business_ID)
    url = "https://api.gupshup.io/sm/api/v2/wallet/balance"

    headers = {"apikey": configInfo.bot_apiKey}
    response = requests.get(url, headers=headers)
    data = json.loads(response.text)
    balance = data['balance']
    balance = "{:.2f}".format(round(balance, 2))
    balance = float(balance)
    context = {"invoice_ID":invoice_ID,"businessInfo":businessInfo,'balance':balance}
    return render(request,'non_profit/message_balance.html',context)






@form_complete
def signup_complete(request):
    return render(request,'registration/onboarding-complete.html')






def logout_view(request):
    logout(request)
    return redirect('/')





def change_password(request):
    if request.method == "POST":
        form = PasswordChangeForm(data = request.POST,user = request.user)

        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            messages.success(request, 'You have Successfully changed your password')
            return redirect('account/settings')
        else:
            
            password_error =  form.error_messages['password_mismatch']
            messages.error(request, "{}".format(password_error))
            return redirect('user/account/profile/change/password')

    else:
            form = PasswordChangeForm(user = request.user)
            context = {'form':form}
            return render(request,'registration/non_profit/user-changepassword.html',context)




