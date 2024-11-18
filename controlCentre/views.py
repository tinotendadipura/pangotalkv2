from django.shortcuts import render , redirect , get_object_or_404,redirect
from django.db.models import Q
from django.views.generic.edit import CreateView,UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required 
from django.urls import reverse_lazy
from django.contrib.auth.forms import   UserCreationForm 
from django.views.generic.edit import CreateView,UpdateView
from django.contrib.auth import  login ,logout, authenticate
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import datetime
import random
from datetime import timedelta 
from django.contrib import messages
from django.utils import timezone
from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template
from app.views import business_category
#from kangaroo.settings import EMAIL_HOST_USER
from pangotalk.settings import EMAIL_HOST
#from send_mail_app.tasks1 import send_mail_func ,payment_success_mail_func,billing_reminder_func
from  app. decorators import (
    user_controller
    ,allowed_users,
    form_complete,
    account_verification
    ,category_access,
    allowed_account,
    
    )

from app. models import (
    BusinessProfile,AccountUpgrade,UserProfile,
    BusinessConfiguration,Plan,BillingInvoice,
    AccountUpgrade,ProofOfPayment,Transaction,
    BusinessConfiguration
    )
from django.http import JsonResponse
from controlCentre. models import BillingManager



import uuid
import json
import requests


@login_required(login_url='accounts/login' )
@allowed_users(allowed_roles = ['Adminstrator'])
def control_center_dashboard(request):
    unverified_business_total = BusinessProfile.objects.filter(account_authorisation_status = False).count()
    verified_business   = BusinessProfile.objects.filter(account_authorisation_status = True).count()
    suspended_qaccounts = BusinessProfile.objects.filter(account_suspended_status     = True).count()
    all_upgrades = AccountUpgrade.objects.all().count()

    datetime_zone  = timezone.now()

    #================================================#

    total_overdue = BillingInvoice.objects.filter(due_date__lte = datetime_zone).count()
    all_overdue = BillingInvoice.objects.filter(due_date__lte = datetime_zone)
    totalproofOfpayment  = ProofOfPayment.objects.filter(verified_status = False).count()
    
    #================================================#
    
    context = {
        'suspended_qaccounts':suspended_qaccounts,
        'all_upgrades':all_upgrades,
        "unverified_business_total":unverified_business_total,
        "verified_business":verified_business,
        "total_overdue":total_overdue,
        "all_overdue":all_overdue,
        " totalproofOfpayment": totalproofOfpayment,
    }
    
    return render(request,'default/helpdesk-index.html',context)





@login_required(login_url='accounts/login' )
@allowed_users(allowed_roles = ['Adminstrator'])
def new_accounts(request):
    current_user = request.user
    profile      = UserProfile.objects.get(user = current_user)
    unverified_business_total = BusinessProfile.objects.filter(account_authorisation_status = False).count()
    unverified_business = BusinessProfile.objects.filter(account_authorisation_status = False)
    verified_business   = BusinessProfile.objects.filter(account_authorisation_status = True).count()
    suspended_qaccounts = BusinessProfile.objects.filter(account_suspended_status     = True).count()
    all_upgrades = AccountUpgrade.objects.all().count()
    context = {
        'unverified_business':unverified_business, 
        'unverified_business_total':unverified_business_total,
        'suspended_qaccounts':suspended_qaccounts,
        'all_upgrades':all_upgrades,
        "verified_business":verified_business,
    }
    return render(request,'default/new-accounts.html',context)



@login_required(login_url='accounts/login' )
@allowed_users(allowed_roles = ['Adminstrator'])
def new_accounts_profile(request,business_ID):
    unverified_business_total = BusinessProfile.objects.filter(account_authorisation_status = False).count()
    unverified_business = BusinessProfile.objects.filter(account_authorisation_status = False)
    verified_business   = BusinessProfile.objects.filter(account_authorisation_status = True).count()
    suspended_qaccounts = BusinessProfile.objects.filter(account_suspended_status     = True).count()
    all_upgrades = AccountUpgrade.objects.all().count()
    businessinfo = BusinessProfile.objects.get(business_ID = business_ID)
    if request.method == "POST":
        bot_url           = request.POST.get('bot_url','')
        bot_name          = request.POST.get('bot_name','')
        bot_apiKey        = request.POST.get('bot_apiKey','')
        page_id           = request.POST.get('page_id','')
        web_url           = request.POST.get('web_url','')
        username          = request.POST.get('username','')
        password          = request.POST.get('password','')
        category          = request.POST.get('category','')
        billing_plan      = request.POST.get('billing_plan','')
        payment_method    = request.POST.get('payment_method','')

       

        

        if request.POST['bot_url'] and request.POST['bot_name'] and request.POST['page_id'] and request.POST['web_url'] and request.POST['payment_method'] and request.POST['username'] and request.POST['password']:
            planInfo = Plan.objects.get(Plan_Name = billing_plan)
            business_data=BusinessConfiguration.objects.filter(business_ID      = business_ID,)
            datetime_zone  = timezone.now()
            total_days     = timedelta(days=30)
            bar_var_1      = random.randint(1000,19000)
            bar_var_2      = random.randint(1000,19000)
            bar_var        = random.randint(1000,19000)
            invoice_id     = bar_var_1 + bar_var_2 + bar_var
            invoice_id     = str(invoice_id)
            exp_date       =  datetime_zone + total_days
            business_manager  = BillingManager.objects.filter(business_ID  = business_ID)
            next_billing_date = exp_date
            datetime_zone           = timezone.now()
            second_billing_date     = timedelta(days=1)
            third_billing_date      = timedelta(days=3)
            forth_billing_date      = timedelta(days=5)
            account_suspension_date = timedelta(days=8)

            second_billing_date = second_billing_date + next_billing_date 
            third_billing_date  = third_billing_date  + next_billing_date
            forth_billing_date  = forth_billing_date  + next_billing_date
            account_suspension_date =  account_suspension_date + next_billing_date
            if  business_manager.exists():
                billingDetail   = BillingManager.objects.get(business_ID = business_ID)
                email_counter   = int(billingDetail.emailCounter)
                email_counter   = email_counter + 1
                
                business_manager.update(
                    emailCounter             = email_counter,  
                    first_billing_date       = next_billing_date,
                    second_billing_date      = second_billing_date,
                    third_billing_date       = third_billing_date,
                    account_suspension_date  = account_suspension_date
                    )
                
            else:
                BillingManager.objects.create(
                    business_ID = business_ID,
                    business_Name         =  businessinfo.BusinessName,
                    billing_Name          =  billing_plan,
                    Price                 =  planInfo.Price,
                    first_billing_date    = next_billing_date,
                    second_billing_date   = second_billing_date,
                    third_billing_date    = third_billing_date,
                    forth_billing_date    = forth_billing_date,
                    account_suspension_date = account_suspension_date,
                    

                )


            if business_data.exists():
                
                BusinessConfiguration.objects.filter(business_ID      = business_ID,).update(
                    BusinessName     = businessinfo.BusinessName,      
                    business_ID      = business_ID,       
                    BillingPlan      = billing_plan,       
                    Plan_ID          = planInfo.Plan_ID,             
                    businessCategory = category,    
                    bot_endpoint     = bot_url,     
                    bot_name         = bot_name,         
                    fb_page_id       = page_id,    
                    partiner_web     = web_url, 
                    bot_apiKey       = bot_apiKey,   
                    username         = username,      
                    password         = password, 
                            )
                BusinessProfile.objects.filter(business_ID = business_ID).update(
                    account_authorisation_status  = True,
                    businessprofile_status        = True,
                    businessCategory_status       = True,
                    form_completed                = True,
                    category                      = category,
                    Plan_ID                       =planInfo.Plan_ID,
                    next_billing_date             = exp_date,)
            else:
                BusinessConfiguration.objects.create(
                    BusinessName     = businessinfo.BusinessName,      
                    business_ID      = business_ID,       
                    BillingPlan      = billing_plan,       
                    Plan_ID          = planInfo.Plan_ID,             
                    businessCategory = category,    
                    bot_endpoint     = bot_url,     
                    bot_name         = bot_name,         
                    fb_page_id       = page_id,    
                    partiner_web     = web_url,    
                    username         = username,      
                    password         = password, 
                     bot_apiKey      = bot_apiKey, 
                            )
                BusinessProfile.objects.filter(business_ID = business_ID).update(
                    account_authorisation_status  = True,
                    businessprofile_status        = True,
                    businessCategory_status       = True,
                    form_completed                = True,
                    category                      = category,
                    Plan_ID                       = planInfo.Plan_ID,
                    next_billing_date             = exp_date,


                )
                
                BillingInvoice.objects.create(
                    business_ID      = business_ID,
                    Business_Name    = businessinfo.BusinessName,
                    Plan_Name        = billing_plan,
                    Invoice_ID       = invoice_id,
                    payment_method   = payment_method,
                    amount           = planInfo.Price,
                    due_date         =  exp_date,
                    invoice_status   = 'PAID',
                )

                payment_success_mail_func.delay(invoice_id)
                Transaction.objects.create(
                    business_ID      =  business_ID,
                    Business_Name    = businessinfo.BusinessName,
                    Plan_Name        = billing_plan,
                    Invoice_ID       = invoice_id,
                    payment_method   = payment_method,
                    amount           = planInfo.Price
                        )
        
    
    context = {
       'businessinfo':businessinfo,
       'unverified_business':unverified_business,
        'unverified_business_total':unverified_business_total,
        'suspended_qaccounts':suspended_qaccounts,
        'all_upgrades':all_upgrades,
        "verified_business":verified_business,
    }
    return render(request,'default/busiiness-profie.html',context)




@login_required(login_url='accounts/login' )
@allowed_users(allowed_roles = ['Adminstrator'])
def active_accounts(request):
    current_user = request.user
    profile      = UserProfile.objects.get(user = current_user)
    unverified_business = BusinessProfile.objects.filter(account_authorisation_status = False).count()
    active_business = BusinessProfile.objects.filter(account_authorisation_status = True, )
    all_verified_business = BusinessProfile.objects.filter(account_authorisation_status = True, ).count()
    datetime_zone  = timezone.now()
    unverified_business_total = BusinessProfile.objects.filter(account_authorisation_status = False).count()
    verified_business   = BusinessProfile.objects.filter(account_authorisation_status = True).count()
    suspended_qaccounts = BusinessProfile.objects.filter(account_suspended_status     = True).count()
    all_upgrades = AccountUpgrade.objects.all().count()
    context = {
        'datetime_zone':datetime_zone,
        'all_verified_business':all_verified_business,
        'active_business':active_business,
        'unverified_business':unverified_business,
        
        'unverified_business_total':unverified_business_total,
        'suspended_qaccounts':suspended_qaccounts,
        'all_upgrades':all_upgrades,
        "verified_business":verified_business,
    }
    return render(request,'default/verified-business.html',context)


@login_required(login_url='accounts/login' )
@allowed_users(allowed_roles = ['Adminstrator'])
def account_upgrade(request):
    accounts_upgrade = AccountUpgrade.objects.all()
    
    context = {
        'accounts_upgrade':accounts_upgrade
        
    }
    return render(request,'default/account-upgrade.html',context)



@login_required(login_url='accounts/login' )
@allowed_users(allowed_roles = ['Adminstrator'])
def account_suspended(request):
    total_suspend = BusinessProfile.objects.filter(account_suspended_status = True, ).count()
    suspended     = BusinessProfile.objects.filter(account_suspended_status = True, )
    
    context = {
        'total_suspend':total_suspend,
        'suspended': suspended 
        
    }
    return render(request,'default/account-suspend.html',context)



@login_required(login_url='accounts/login' )
@allowed_users(allowed_roles = ['Adminstrator'])
def account_configuration(request):
    current_user = request.user
    profile      = UserProfile.objects.get(user = current_user)
    config       = BusinessConfiguration.objects.all()
    unverified_business_total = BusinessProfile.objects.filter(account_authorisation_status = False).count()
    unverified_business = BusinessProfile.objects.filter(account_authorisation_status = False)
    verified_business   = BusinessProfile.objects.filter(account_authorisation_status = True).count()
    suspended_qaccounts = BusinessProfile.objects.filter(account_suspended_status     = True).count()
    all_upgrades = AccountUpgrade.objects.all().count()
    context = {
        'unverified_business':unverified_business, 
        'unverified_business_total':unverified_business_total,
        'suspended_qaccounts':suspended_qaccounts,
        'all_upgrades':all_upgrades,
        "verified_business":verified_business,
        'config':config 
    }
    if request.method == "POST":
        bot_url           = request.POST.get('bot_url','')
        bot_name          = request.POST.get('bot_name','')
        bot_apiKey        = request.POST.get('bot_apiKey','')
        page_id           = request.POST.get('page_id','')
        web_url           = request.POST.get('web_url','')
        username          = request.POST.get('username','')
        password          = request.POST.get('password','')
        category          = request.POST.get('category','')
        billing_plan      = request.POST.get('billing_plan','')
        business_ID      = request.POST.get('business_ID','')
       

        if request.POST['bot_url'] and request.POST['bot_name'] and request.POST['page_id'] and request.POST['web_url'] and  request.POST['username'] and request.POST['password']:
           BusinessConfiguration.objects.filter(business_ID =  business_ID).update(
            BillingPlan         = billing_plan,
            businessCategory    = category,
            bot_endpoint        = bot_url,
            bot_apiKey          = bot_apiKey,
            bot_name            = bot_name,
            fb_page_id          = page_id,
            partiner_web        = web_url,
            username            =  username,
            password            = password,
            account_config_status  = True,
           )

    return render(request,'default/account-configuration.html',context)



# ============ Payments Manager  ================ #
@login_required(login_url='accounts/login' )
@allowed_users(allowed_roles = ['Adminstrator'])
def payments_dashboard(request):
    datetime_zone  = timezone.now()
    current_month = datetime_zone.month
    current_year = datetime_zone.year
    transaction_history = Transaction.objects.filter(date__year__iexact = current_year,date__month__iexact = current_month)
    proofOfpayment  = ProofOfPayment.objects.filter(verified_status = False)
    totalproofOfpayment  = ProofOfPayment.objects.filter(verified_status = False).count()
    #================================================#

    total_overdue = BillingInvoice.objects.filter(due_date__lte = datetime_zone).count()
    unverified_business = BusinessProfile.objects.filter(account_authorisation_status = False).count()
    verified_business   = BusinessProfile.objects.filter(account_authorisation_status = True).count()
    suspended_qaccounts = BusinessProfile.objects.filter(account_suspended_status     = True).count()
    all_upgrades = AccountUpgrade.objects.all().count()
    all_overdue = BillingInvoice.objects.filter(due_date__lte = datetime_zone)
    
    #================================================#
    overdue_balance = BillingInvoice.objects.filter(due_date__lte = datetime_zone)
    current_month = datetime_zone.month
    current_year = datetime_zone.year
    revenue_balance = BillingInvoice.objects.filter(date__year__iexact = current_year,date__month__iexact = current_month)
    amount_topay = 0
    total_revenue = 0
    for revenue in revenue_balance:
        finalrevenue = revenue.amount
        finalrevenue = float(finalrevenue)
        total_revenue = total_revenue + finalrevenue

    for total_amount in overdue_balance:
        finalBalance = total_amount.amount
        finalBalance = float(finalBalance)
        amount_topay = finalBalance +  amount_topay
    
    context = {
        'transaction_history':transaction_history,
        'amount_topay':amount_topay,
        'total_revenue':total_revenue,

        'proofOfpayment':proofOfpayment,
        'totalproofOfpayment':totalproofOfpayment,
        'all_overdue':all_overdue,
        'total_overdue':total_overdue,
        'suspended_qaccounts':suspended_qaccounts,
        'all_upgrades':all_upgrades,
        "unverified_business":unverified_business,
        "verified_business":verified_business,
        'totalproofOfpayment':totalproofOfpayment,
     }
    return render(request,'default/manage-finance.html',context)


@login_required(login_url='accounts/login' )
@allowed_users(allowed_roles = ['Adminstrator'])
def bank_payments(request):
    proofOfpayment  = ProofOfPayment.objects.filter(verified_status = False)
    totalproofOfpayment  = ProofOfPayment.objects.filter(verified_status = False).count()
    datetime_zone  = timezone.now()

    #================================================#

    total_overdue = BillingInvoice.objects.filter(due_date__lte = datetime_zone).count()
    unverified_business = BusinessProfile.objects.filter(account_authorisation_status = False).count()
    verified_business   = BusinessProfile.objects.filter(account_authorisation_status = True).count()
    suspended_qaccounts = BusinessProfile.objects.filter(account_suspended_status     = True).count()
    all_upgrades = AccountUpgrade.objects.all().count()
    all_overdue = BillingInvoice.objects.filter(due_date__lte = datetime_zone)
    
    #================================================#
    
    context = {
        'proofOfpayment':proofOfpayment,
        'totalproofOfpayment':totalproofOfpayment,
        'all_overdue':all_overdue,
        'total_overdue':total_overdue,
        'suspended_qaccounts':suspended_qaccounts,
        'all_upgrades':all_upgrades,
        "unverified_business":unverified_business,
        "verified_business":verified_business,
        'totalproofOfpayment':totalproofOfpayment,
     }
    return render(request,'default/proofOfpayment.html',context)



@login_required(login_url='accounts/login' )
@allowed_users(allowed_roles = ['Adminstrator'])
def verify_payment(request,refference):

   

    info_proof = ProofOfPayment.objects.get(refference = refference)
    ProofOfPayment.objects.filter(refference = refference).update(
    verified_by      = request.user.username,
    verified_status  = True,
    approved_status  = True
    )
    

    billing_cycle  = info_proof.billingCycle
    billing_cycle  = int(billing_cycle)
    days           = billing_cycle * 30
    datetime_zone  = timezone.now()
    total_days     = timedelta(days=days)
    bar_var_1 = random.randint(1000,19000)
    bar_var_2 = random.randint(1000,19000)
    bar_var = random.randint(1000,19000)
    invoice_id = bar_var_1 +  bar_var + bar_var_2
    invoice_id = str(invoice_id)
    exp_date       =  datetime_zone + total_days

    
    BillingInvoice.objects.filter(Invoice_ID = info_proof.Invoice_ID).update(
     Invoice_ID     = invoice_id,
     date           = datetime_zone,
     invoice_status = 'PAID',
     due_date       = exp_date,
     payment_method = 'Bank Transfer' 

    )
    
    
    billingInfo = BillingInvoice.objects.get(Invoice_ID = invoice_id)
    
    
    Transaction.objects.create(
        business_ID      = billingInfo.business_ID,
        Business_Name    = billingInfo.Business_Name,
        Plan_Name        = billingInfo.Plan_Name,
        Invoice_ID       = invoice_id,
        payment_method   = 'Bank Transfer',
        amount           = billingInfo.amount
    )
    BusinessProfile.objects.filter(business_ID  = info_proof.business_ID , ).update(
        next_billing_date = exp_date,
    )
    billingInfo = BillingManager.objects.filter(business_ID  = info_proof.business_ID)

    if billingInfo.exists():
        billingmanagerInfo = BillingManager.objects.get(business_ID  = info_proof.business_ID)
        get_emailCounter   = int(billingmanagerInfo.emailCounter)
        get_emailCounter   = get_emailCounter + 1
        second_billing_date     = timedelta(days=1)
        third_billing_date      = timedelta(days=3)
        forth_billing_date      = timedelta(days=5)
        account_suspension_date = timedelta(days=8)

        second_billing_date = second_billing_date + exp_date 
        third_billing_date  = third_billing_date  + exp_date
        forth_billing_date  = forth_billing_date  + exp_date
        account_suspension_date =  account_suspension_date + exp_date
        billingInfo.update(
        
        billing_Name               = billingInfo.Plan_Name,
        emailCounter               = get_emailCounter,
        Price                      = billingInfo.amount,
        first_billing_date         = exp_date,
        second_billing_date        = second_billing_date,
        third_billing_date         = third_billing_date,
        forth_billing_date         = forth_billing_date,
        account_suspension_date    = account_suspension_date
        
        )
    payment_success_mail_func.delay(invoice_id)
    return redirect('manager/Bank-payments')



@login_required(login_url='accounts/login' )
@allowed_users(allowed_roles = ['Adminstrator'])
def overdue_payments(request):
    datetime_zone  = timezone.now()
    all_overdue = BillingInvoice.objects.filter(due_date__lte = datetime_zone)
     
    unverified_business_total = BusinessProfile.objects.filter(account_authorisation_status = False).count()
    total_overdue = BillingInvoice.objects.filter(due_date__lte = datetime_zone).count()
    unverified_business = BusinessProfile.objects.filter(account_authorisation_status = False).count()
    verified_business   = BusinessProfile.objects.filter(account_authorisation_status = True).count()
    suspended_qaccounts = BusinessProfile.objects.filter(account_suspended_status     = True).count()
    all_upgrades = AccountUpgrade.objects.all().count()
    totalproofOfpayment  = ProofOfPayment.objects.filter(verified_status = False).count()
    context = {
        'all_overdue':all_overdue,
        'total_overdue':total_overdue,
        'suspended_qaccounts':suspended_qaccounts,
        'all_upgrades':all_upgrades,
        "unverified_business":unverified_business,
        "verified_business":verified_business,
        'totalproofOfpayment':totalproofOfpayment,
        'unverified_business_total':unverified_business_total
    }
    
    return render(request,'default/overdue-payments.html',context)

@login_required(login_url='accounts/login' )
@allowed_users(allowed_roles = ['Adminstrator'])
def send_billing_invoice(request,invoice_id):
    billingInfo      = BillingInvoice.objects.get(Invoice_ID = invoice_id)
    billing_counter  = int(billingInfo.reminder)
    billing_counter  = billing_counter + 1
    BillingInvoice.objects.filter(Invoice_ID = invoice_id).update(reminder = billing_counter )
    business_ID = billingInfo.business_ID
    billing_reminder_func.delay(business_ID,invoice_id)
    return redirect('manager/overdue/payments')


@login_required(login_url='accounts/login' )
@allowed_users(allowed_roles = ['Adminstrator'])
def transaction_history(request):
    all_transactions = Transaction.objects.all()
    
    context = {
        'all_transactions':all_transactions
        
    }
    return render(request,'default/transaction-history.html',context)
