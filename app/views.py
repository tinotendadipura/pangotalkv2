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
from django.views.decorators.csrf import csrf_exempt
from pangotalk.settings import EMAIL_HOST
from django.http import JsonResponse
import json
import re


from django.http import JsonResponse
from celery.result import AsyncResult


from . userInvite import SendInvite 
from . emailmanager import InviteEmail
from . models import (UserProfile,
    BusinessProfile,
    Invite,
    ProductListing,
    Order,
    Customer,
    Event,
    EventBooking,
    ProductCategory,
    Coupon,
    InvoiceGenerator,
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
     CouponClaim,
     OrderGroup,
     Feedback,
     FeedbackCount,
     CustomerEmails

    )
import os
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
from . decorators import (
    user_controller
    ,allowed_users,
    form_complete,
    account_verification
    ,category_access,
    allowed_account,
    prevent_logged_in_access_to_public_tenant,
    prevent_authenticated
    
    )

import uuid
from app.models import Client, Domain
from send_mail_app.tasks import create_comapany_subdomain_task

plan_Id = uuid.uuid1()
customer_Id = str(plan_Id)

# main homepage

@form_complete

@category_access
@allowed_users(allowed_roles = ['Business'])

def home(request):
    currentUser  = request.user
    profile      = UserProfile.objects.get(user = currentUser )
    businessInfo = BusinessProfile.objects.get(business_ID = profile.business_ID) 
    if businessInfo.category == 'RETAIL AND ECOMM':
            
            return redirect('main/home/dashboard')
        
    else: 
        
        return redirect('main/home/dashboard/non-profit')
    
    





@form_complete

@allowed_users(allowed_roles = ['Business'])

def main_dashboard(request):
    currentUser         = request.user
    profile             = UserProfile.objects.get(user = currentUser )
    businessInfo        = BusinessProfile.objects.get(business_ID = profile.business_ID)

    info                = UserProfile.objects.get(user = currentUser)
    businessInfo        = BusinessProfile.objects.get(business_ID = info.business_ID)
    count_orders        = Order.objects.filter(Q(business_ID = info.business_ID) & Q(viewed = False)).count()
    customers           = Customer.objects.filter(business_ID = info.business_ID)
    inbox_messages      = customers.filter(inbox_messages__gt = 0).count()
    invoice_info        = BillingInvoice.objects.filter(business_ID = profile.business_ID)
    all_invoice         = BillingInvoice.objects.filter(business_ID = profile.business_ID).first()
    invoice_ID          = info.business_ID
    
    ordernotification_status = OrderNotification.objects.filter(business_ID = info.business_ID).first()
    context = {"all_invoice":all_invoice,"invoice_ID":invoice_ID,"count_orders":count_orders,"businessInfo":businessInfo, "inbox_messages":inbox_messages,"ordernotification_status":ordernotification_status}
    #send_mail_func.delay()
    business_ID = info.business_ID
    return render(request,'app/index.html',context)




def ecomm_dashboard_landing(request):
    
    return render(request,'landing-pages/index.html')


@login_required(login_url='accounts/login' )
@form_complete
@account_verification
@allowed_users(allowed_roles = ['Business'])

def ecomm_layer(request):
    currentUser = request.user
    info           = UserProfile.objects.get(user = currentUser)
    businessInfo   = BusinessProfile.objects.get(business_ID = info.business_ID)
    totalcustomers = Customer.objects.filter(business_ID = info.business_ID).count()
    customers      = Customer.objects.filter(business_ID = info.business_ID)
    totalorders    = Order.objects.filter(business_ID = info.business_ID).count()
    inbox_messages = customers.filter(inbox_messages__gt = 0).count()
    configInfo     = BusinessConfiguration.objects.get(business_ID = info.business_ID)
    url = "https://api.gupshup.io/sm/api/v2/wallet/balance"

    headers = {"apikey": configInfo.bot_apiKey}
    response = requests.get(url, headers=headers)
    data = json.loads(response.text)
    balance = data['balance']
    balance = "{:.2f}".format(round(balance, 2))

    
    all_orders  =  Order.objects.filter(Q(business_ID = info.business_ID) & Q(viewed = False))
    
    customers   = Customer.objects.filter(business_ID = info.business_ID)
    inbox_messages = customers.filter(inbox_messages__gt = 0).count()
    business_id = info.business_ID
    diskspace = DiskManager.objects.get(business_ID =  business_id)
    
    
  
    context = {"balance":balance,"businessInfo":businessInfo,'diskspace':diskspace,'all_orders':all_orders, "inbox_messages":inbox_messages,'totalcustomers':totalcustomers,'totalorders':totalorders,'customers':customers}
    return render(request,'layer/ecomm-layer.html',context)


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
                    return redirect('accounts/add-user')
        elif email_qs.exists():
            messages.error(request, 'User invite with this email or phone number already exist!')
            return redirect('accounts/add-user')

                    
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
            return redirect('accounts/all-users')
            
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
    invoice_ID     = info.business_ID
    all_invoice    = BillingInvoice.objects.filter(business_ID = info.business_ID).first()
    


    
    businessInfo = BusinessProfile.objects.get(business_ID = info.business_ID)
    customers   = Customer.objects.filter(business_ID = info.business_ID)
    inbox_messages = customers.filter(inbox_messages__gt = 0).count()
    
    all_invite  = Invite.objects.filter(business_ID = info.business_ID)
    total_invite = all_invite.count()
    context     = { "businessInfo":businessInfo,
                   "inbox_messages":inbox_messages,
                   "all_invite":all_invite,
                    "total_invite":total_invite,
                    "invoice_ID":invoice_ID}
    return render(request,'app/all-agents.html',context)




# ========   Catalog    ========== #

@login_required(login_url='accounts/login' )
@form_complete
@account_verification
@allowed_users(allowed_roles = ['Business'])
def addProduct(request):
    currentUser = request.user
    info        = UserProfile.objects.get(user = currentUser)
    invoice_ID  = info.business_ID
    businessInfo = BusinessProfile.objects.get(business_ID = info.business_ID)
    customers   = Customer.objects.filter(business_ID = info.business_ID)
    inbox_messages = customers.filter(inbox_messages__gt = 0).count()
    business_ID = info.business_ID
    
    if request.method == "POST":
       
        tittle               = request.POST.get('tittle','')
        price                = request.POST.get('price','')
        compare_price        = request.POST.get('compare_price','')
        product_image        = request.FILES['product_image']
        currency              = request.POST.get('currency','')
        category              = request.POST.get('category','')
        description           = request.POST.get('description','')
        
        
        
        productID    = uuid.uuid1()
        productID    = str(productID)
        size_kb=product_image.size/1024
        ProductListing.objects.create(
             branch_ID  =  info.branch_ID,
            product_ID  = productID,
            category    = category,
            business_ID = info.business_ID, 
            title       = tittle,
            description = description,
            price       = price ,
            currency    = currency,
            media_size  = size_kb,
            product_image =product_image,
            compare_price = compare_price,
          )
        business_ID      = info.business_ID
        diskspace        = DiskManager.objects.get(business_ID =  business_ID)
    
        currentusage = float(diskspace.disk_space)
        finalusage   = currentusage + size_kb
        DiskManager.objects.filter(business_ID =  business_ID).update(disk_space = finalusage)
        messages.success(request, 'You Have Succesifully Added Product!')
        return redirect('catalog/all-products')
    all_category = ProductCategory.objects.filter(business_ID = info.business_ID,)
    context = {"invoice_ID":invoice_ID,"businessInfo":businessInfo,'all_category':all_category,"inbox_messages":inbox_messages,}
    return render(request,'app/add-product.html',context)


@login_required(login_url='accounts/login' )
@form_complete
@account_verification
@allowed_users(allowed_roles = ['Business'])
def allProduct(request):
    currentUser    = request.user
    info           = UserProfile.objects.get(user = currentUser)
    invoice_ID  = info.business_ID
    businessInfo = BusinessProfile.objects.get(business_ID = info.business_ID)
    all_products   = ProductListing.objects.filter(business_ID = info.business_ID)
    customers      = Customer.objects.filter(business_ID = info.business_ID)
    inbox_messages = customers.filter(inbox_messages__gt = 0).count()
    
    total_products = all_products.count()
    context        = {"invoice_ID":invoice_ID,"businessInfo":businessInfo,"all_products":all_products,"total_products":total_products,"inbox_messages":inbox_messages,}
    return render(request,'app/all-products.html',context)

@login_required(login_url='accounts/login' )
@allowed_users(allowed_roles = ['Business'])
def deleteproduct(request,product_ID):
    ProductListing.objects.filter(product_ID = product_ID).delete()
    messages.success(request, 'You have successifully deleted a product!')
    return redirect('catalog/all-products')


@login_required(login_url='accounts/login' )
@form_complete
@account_verification
@allowed_users(allowed_roles = ['Business'])
def addCategory(request):
    currentUser  = request.user
    info         = UserProfile.objects.get(user = currentUser)
    invoice_ID  = info.business_ID
    businessInfo = BusinessProfile.objects.get(business_ID = info.business_ID)
    all_category = ProductCategory.objects.filter(business_ID = info.business_ID,)
    customers   = Customer.objects.filter(business_ID = info.business_ID)
    inbox_messages = customers.filter(inbox_messages__gt = 0).count()
    if request.method == "POST":
        
        
        category    = request.POST.get('category','')
        description = request.POST.get('description','')
        ProductCategory.objects.create(
        business_ID = info.business_ID,
         category   = category.title(),
         description = description,
        )
    context = {"invoice_ID":invoice_ID,"businessInfo":businessInfo,'all_category':all_category,"inbox_messages":inbox_messages,}
    return render(request,'app/add-category.html',context)




# ========   Customers     ========== #
@login_required(login_url='accounts/login' )
@form_complete
@account_verification
@allowed_users(allowed_roles = ['Business'])
def all_customers(request):
    currentUser = request.user
    info = UserProfile.objects.get(user = currentUser)
    invoice_ID  = info.business_ID
    businessInfo = BusinessProfile.objects.get(business_ID = info.business_ID)
    all_products = ProductListing.objects.filter(business_ID = info.business_ID)
    all_customers = Customer.objects.filter(business_ID = info.business_ID)
    total_customers = Customer.objects.filter(business_ID = info.business_ID).count()
    customers   = Customer.objects.filter(business_ID = info.business_ID)
    inbox_messages = customers.filter(inbox_messages__gt = 0).count()
    context = {"invoice_ID":invoice_ID,"businessInfo":businessInfo,'all_customers':all_customers,"inbox_messages":inbox_messages,'total_customers':total_customers}
    return render(request,'app/all-customers.html',context)



@login_required(login_url='accounts/login' )
@form_complete
@account_verification
@allowed_users(allowed_roles = ['Business'])
def add_customers(request):
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
            messages.error(request, 'This customer you are trying to add already exist!')

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
                messages.success(request, 'Customer has been successifully created.')
                return redirect('manage/all-customer')
    context = {"invoice_ID":invoice_ID,"businessInfo":businessInfo,"inbox_messages":inbox_messages,}
    return render(request,'app/add-customer.html',context)



# ========   Orders     ========== #
@login_required(login_url='accounts/login' )
@form_complete
@account_verification
@allowed_users(allowed_roles = ['Business'])
def orders(request):
    currentUser    = request.user
    info           = UserProfile.objects.get(user = currentUser)
    invoice_ID  = info.business_ID
    Order.objects.filter(business_ID = info.business_ID).update(viewed = True)
    totalOrders    = OrderGroup.objects.filter(business_ID = info.business_ID).count()
    
    businessInfo   = BusinessProfile.objects.get(business_ID = info.business_ID)
    all_orders     = OrderGroup.objects.filter(business_ID = info.business_ID)
    customers      = Customer.objects.filter(business_ID = info.business_ID)
    inbox_messages = customers.filter(inbox_messages__gt = 0).count()
    context        = {"invoice_ID":invoice_ID,"totalOrders":totalOrders,"businessInfo":businessInfo,'all_orders':all_orders,"inbox_messages":inbox_messages,}
    return render(request,'app/orders.html',context)




# ========   Customer Feedback    ========== #
@login_required(login_url='accounts/login' )
@form_complete
@account_verification
@allowed_users(allowed_roles = ['Business'])
def customer_feedback(request):
    currentUser    = request.user
    info              = UserProfile.objects.get(user = currentUser)
    invoice_ID  = info.business_ID
    totalOrders       = OrderGroup.objects.filter(business_ID = info.business_ID).count()
    businessInfo      = BusinessProfile.objects.get(business_ID = info.business_ID)
    customers         = Customer.objects.filter(business_ID     = info.business_ID)
    current_customer  = Customer.objects.filter(business_ID  = info.business_ID).first()
    all_feedback      = Feedback.objects.filter(customer_ID     = info.userprofileID)
    total_feedback    = FeedbackCount.objects.filter(business_ID = info.business_ID).first()
    inbox_messages    = customers.filter(inbox_messages__gt = 0).count()
    context           = {"invoice_ID":invoice_ID,"total_feedback":total_feedback,"current_customer":current_customer,"customers":customers,"totalOrders":totalOrders,"businessInfo":businessInfo,'all_feedback':all_feedback,"inbox_messages":inbox_messages,}
    return render(request,'app/customerfeedback.html',context)



@login_required(login_url='accounts/login' )
@form_complete
@account_verification
@allowed_users(allowed_roles = ['Business'])
def customer_feedback_details(request,customer_ID):
    currentUser    = request.user
    info           = UserProfile.objects.get(user = currentUser)
    invoice_ID  = info.business_ID
    totalOrders    = OrderGroup.objects.filter(business_ID = info.business_ID).count()
    
    businessInfo   = BusinessProfile.objects.get(business_ID = info.business_ID)
    all_feedback   = Feedback.objects.filter(customer_ID = customer_ID)
    customers      = Customer.objects.filter(business_ID = info.business_ID)
    current_customer  = Customer.objects.get(customer_ID = customer_ID)
    inbox_messages = customers.filter(inbox_messages__gt = 0).count()
    context        = {"invoice_ID":invoice_ID,"current_customer":current_customer,"customers":customers,"totalOrders":totalOrders,"businessInfo":businessInfo,'all_feedback':all_feedback,"inbox_messages":inbox_messages,}
    return render(request,'app/customerfeedback-detail.html',context)



@login_required(login_url='accounts/login' )
@form_complete
@account_verification
@allowed_users(allowed_roles = ['Business'])
def order_details(request,customer_number):
    currentUser    = request.user
    info           = UserProfile.objects.get(user = currentUser)
    invoice_ID  = info.business_ID
    Order.objects.filter(business_ID = info.business_ID).update(viewed = True)
    customer_orders = Order.objects.filter(Q(business_ID = info.business_ID) and Q(customer_ID = customer_number))
    businessInfo   = BusinessProfile.objects.get(business_ID = info.business_ID)
    all_orders     = OrderGroup.objects.filter(business_ID = info.business_ID)
    customers      = Customer.objects.filter(business_ID = info.business_ID)
    current_customer= Customer.objects.get(customer_ID = customer_number)
    inbox_messages = customers.filter(inbox_messages__gt = 0).count()
    all_order_balance = 0
    for total in customer_orders:
        currenttotal           = float(total.total_Amount)
        all_order_balance      = currenttotal + all_order_balance
        all_order_balance      = "{:.2f}".format(round(all_order_balance, 2))
        all_order_balance      = float(all_order_balance)

    if request.method == "POST":
        items              = request.POST.get('items','')
        order_ID           = request.POST.get('order_ID','')
        
        finalItems         = int(items)
        if finalItems < 1:
            messages.error(request, 'Order Items  should not be less than 1! ')
            return redirect('customer/product/orders',customer_number)
        else:
            oderUpdateInfo     = Order.objects.get(order_ID = order_ID)
            oldOrderItems    = int(oderUpdateInfo.orderQuantity)
            oderInfo           = Order.objects.filter(order_ID = order_ID)
            current_product_ID =  oderUpdateInfo.product_ID
            productInfo        = ProductListing.objects.get( product_ID = current_product_ID)
            productPrice       = float(productInfo.price) 
            items              = float(items)
            finalOrderPrice    =  productPrice * items
            oderInfo.update(
                total_Amount    = finalOrderPrice,
                orderQuantity   = finalItems,
            )

            ordergroupInfo   = OrderGroup.objects.get(customer_ID = customer_number)
            OrderGroupItems  = int(ordergroupInfo.orderQuantity)
            
            BalanceQuantity  = OrderGroupItems - oldOrderItems
            BalanceQuantity  = BalanceQuantity + finalItems
            total_Amount     = float(ordergroupInfo.total_Amount)
            olderOrderTotal  = float(oderUpdateInfo.total_Amount) 
            finalOrderGroupTotal = total_Amount - olderOrderTotal
            finalOrderGroupTotal = finalOrderGroupTotal + finalOrderPrice
            OrderGroup.objects.filter(customer_ID = customer_number).update(
            total_Amount         =   finalOrderGroupTotal,
            orderQuantity        =   BalanceQuantity
            )
            messages.success(request, 'You have successifully updated customer order!')
            return redirect('customer/product/orders',customer_number)

    context        = {"invoice_ID":invoice_ID,"current_customer":current_customer,"all_order_balance":all_order_balance,"customer_orders":customer_orders,"businessInfo":businessInfo,'all_orders':all_orders,"inbox_messages":inbox_messages,}
    return render(request,'app/cart.html',context)




@login_required(login_url='accounts/login' )
@allowed_users(allowed_roles = ['Business'])
def deleteOrder(request,OrderID):
    order_info = Order.objects.get(order_ID  = OrderID)
    customer_number  = order_info.customer_ID
    ordergroupInfo   = OrderGroup.objects.get(customer_ID = customer_number)
    amount_deducted  = float(order_info.total_Amount)
    orderGroupAmount = float(ordergroupInfo.total_Amount)
    finalAmount      = orderGroupAmount - amount_deducted
    finalAmount      = "{:.2f}".format(round(finalAmount, 2))

    ordertoremove   = int(order_info.orderQuantity)
    currentOrderQ   = int(ordergroupInfo.orderQuantity)
    final_quantity  = currentOrderQ - ordertoremove

    OrderGroup.objects.filter(customer_ID = customer_number).update(
     orderQuantity =  final_quantity,
     total_Amount  = finalAmount, 
    )
    Order.objects.filter(order_ID  = OrderID).delete()
    
    messages.success(request, 'Customer order was successifully deleted!')
    return redirect('customer/product/orders',customer_number)


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
    return render(request,'app/add-event.html',context)




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
           
    
    return render(request,'app/edit-event.html',context)


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
    return render(request,'app/all-events.html',context)

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
    return render(request,'app/event-bookings.html',context)


def deletebooking(request,booking_ID):
    EventBooking.objects.filter(booking_ID = booking_ID).delete()
    messages.success(request, 'You have  successifully deleted  event booking!')
    return redirect('events/all-bookings')

# ========  Coupons    ========== #

@login_required(login_url='accounts/login' )
@form_complete
@account_verification
@allowed_users(allowed_roles = ['Business'])
def createCoupon(request):
    currentUser    = request.user
    info           = UserProfile.objects.get(user = currentUser)
    invoice_ID  = info.business_ID
    all_category   = ProductCategory.objects.filter(business_ID = info.business_ID,)
    customers      = Customer.objects.filter(business_ID = info.business_ID)
    inbox_messages = customers.filter(inbox_messages__gt = 0).count()
    all_coupons    = Coupon.objects.filter(business_ID = info.business_ID)
    total_coupons  = all_coupons.count()
    current_time   = datetime.datetime.now()
    p              = Paginator(all_coupons,10)
    page           = request.GET.get('page')
    current_page   = p.get_page(page)

    
    
    businessInfo = BusinessProfile.objects.get(business_ID = info.business_ID)
        
    if request.method == "POST":
            try:
                if request.FILES['coupon_image'] and request.POST['campaignName'] and request.POST['StartDate'] and request.POST['validDate'] and request.POST['percent'] and request.POST['minimum_amount'] and request.POST['Usage_limit'] and request.POST['category']:
                    coupon_banner_image  = request.FILES['coupon_image']
                    campaignName         = request.POST.get('campaignName','')
                    StartDate            = request.POST.get('StartDate','')
                    validDate            = request.POST.get('validDate','')
                    percent              = request.POST.get('percent','')
                    minimum_amount       = request.POST.get('minimum_amount','')
                    Usage_limit          = request.POST.get('Usage_limit','')
                    category             = request.POST.get('category','')
                    startdate            = datetime.datetime.strptime(StartDate,'%m-%d-%Y  %I:%M')
                    enddate              = datetime.datetime.strptime(validDate,'%m-%d-%Y  %I:%M')
                    startTime            = startdate.time()
                    endTime              = enddate.time()
                    parentTime           = str(startdate)
                    oldTime              = str(enddate)
                    Usage_limit          = int(Usage_limit)
                    currentUser = request.user
                    info = UserProfile.objects.get(user = currentUser)
                    
                    
                    subscipt=['A','B','C','D','E','F','G','H','I','J','K','L','M'
                                ,'N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
                    realvalue0 =    random.choice(subscipt)
                    realvalue1 =    random.choice(subscipt)
                    realvalue2 =    random.choice(subscipt)
                    realvalue3 =    random.choice(subscipt)
                    realvalue4 =    random.choice(subscipt)
                    realvalue5 =    random.choice(subscipt)
                    code       =    realvalue0 + realvalue1 + realvalue2 + realvalue3  + realvalue4 + realvalue5 
                        
                                    
                    Coupon.objects.create(
                            business_ID        = info.business_ID,
                            campaignBanner     = coupon_banner_image,
                            campaignName       = campaignName,
                            couponCode         = code,
                            percentage         = percent,
                            category           = category,
                            minimum_amount     = minimum_amount,
                            Usage_limit      =   Usage_limit,
                            startactualdate    = startdate,
                            
                            # endfullDate        = ,
                            endactuallDate     = enddate,
                            startTime          = parentTime,
                            endTime            = oldTime,


                        )
    
                        
                        
                    messages.success(request, 'Your Coupons were successifully created')
                    return redirect('promo/customer-coupons')
                    
                else:
                    messages.error(request, 'Form was not completely filled, re-submit the form!')
                    return render(request,'app/createCoupon.html',context)       
            except Exception as exp:
                print(exp)
    context        = {"invoice_ID":invoice_ID,"businessInfo":businessInfo,'current_page':current_page,'current_time':current_time,'total_coupons':total_coupons,'all_coupons':all_coupons,'all_category':all_category,"inbox_messages":inbox_messages,}
   
    return render(request,'app/createCoupon.html',context)


@login_required(login_url='accounts/login' )
@allowed_users(allowed_roles = ['Business'])
def claimed_coupon(request):
    currentUser    = request.user
    info           = UserProfile.objects.get(user = currentUser)
    invoice_ID     = info.business_ID
    businessInfo = BusinessProfile.objects.get(business_ID = info.business_ID)
    claimed_coupon = CouponClaim.objects.filter(business_ID = info.business_ID)
    context = {
        "invoice_ID":invoice_ID,
        'info':info,
        'businessInfo':businessInfo,
        'claimed_coupon':claimed_coupon,
    }
    return render(request,'app/claimed_coupons.html',context)




@login_required(login_url='accounts/login' )
@allowed_users(allowed_roles = ['Business'])
def used_coupon(request,couponCode):
    CouponClaim.objects.filter(couponCode = couponCode).update(claimed_status = True)
    messages.success(request, 'Coupon has been used.!')
    return redirect('promo/claimed-coupons')


@login_required(login_url='accounts/login' )
@allowed_users(allowed_roles = ['Business'])
def delete_claimed_coupon(request,id):
    CouponClaim.objects.filter(id = id).delete()
    messages.success(request, 'You have successifully deleted a claimed coupon!')
    return redirect('promo/claimed-coupons')




@login_required(login_url='accounts/login' )
@allowed_users(allowed_roles = ['Business'])
def deletecoupon(request,couponCode):
    Coupon.objects.filter(couponCode = couponCode).delete()
    messages.success(request, 'You have successifully deleted a coupon!')
    return redirect('/')


@login_required(login_url='accounts/login' )
@allowed_users(allowed_roles = ['Business'])
def deletecoupon(request,couponCode):
    Coupon.objects.filter(couponCode = couponCode).delete()
    messages.success(request, 'You have successifully deleted a coupon!')
    return redirect('/')




# ========  Knoledge Base    ========== #
@login_required(login_url='accounts/login' )
@allowed_users(allowed_roles = ['Business'])
def publishArticle(request):
    current_user = request.user
    profile      = UserProfile.objects.get(user = current_user)
    invoice_ID     = profile.business_ID
    businessInfo = BusinessProfile.objects.get(business_ID = profile.business_ID)
    context      = {"invoice_ID":invoice_ID,'businessInfo':businessInfo}
    return render(request,'app/index.html',context)



@login_required(login_url='accounts/login' )
@allowed_users(allowed_roles = ['Business'])
def allArticles(request):
    current_user = request.user
    profile      = UserProfile.objects.get(user = current_user)
    invoice_ID     = profile.business_ID
    businessInfo = BusinessProfile.objects.get(business_ID = profile.business_ID)
    context      = {'businessInfo':businessInfo}
    return render(request,'app/index.html',context)


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
                return redirect('account/settings')
        except Exception as exp:
            print(exp)
    context      = {'businessInfo':businessInfo}
    return render(request,'app/settings.html',context )



# ========= Store Manager =========== #

@login_required(login_url='accounts/login' )
@allowed_users(allowed_roles = ['Business'])
def store_manager(request):
    current_user = request.user
    profile      = UserProfile.objects.get(user = current_user)
    invoice_ID     = profile.business_ID
    businessInfo = BusinessProfile.objects.get(business_ID = profile.business_ID)
    if request.method == "POST":
        try:
           
            
                branch_name          = request.POST.get('branch_name','')
                branch_adress        = request.POST.get('branch_adress','')
                branch_city          = request.POST.get('branch_city','')
                mobile_phone         = request.POST.get('mobile_phone','')
                other_phone          = request.POST.get('other_phone','')
                email                = request.POST.get('email','')
                latitude             = request.POST.get('latitude','')
                longitude            = request.POST.get('longitude','')
                ExtraMobile          = request.POST.get('ExtraMobile','')
                
                branch_ID            = uuid.uuid1()
                branch_ID            = str(branch_ID)
                BusinessBranch.objects.create(
                    business_ID         = profile.business_ID,
                    branch_ID           = branch_ID ,
                    branch_name         = branch_name,
                    branch_phone        = mobile_phone,
                    other_phone         = other_phone,
                    extra_phone         = ExtraMobile,
                    email               = email,
                    branch_city         = branch_city,
                    branch_adress       = branch_adress,
                    longitude           = longitude,
                    latitude            = latitude,


                )
                messages.success(request, 'Your new store was successifully created.')
                
            
        except Exception as exp:
            print(exp)
    context      = {"invoice_ID":invoice_ID,'businessInfo':businessInfo}
    return render(request,'app/branch-manager.html',context )



@login_required(login_url='accounts/login' )
@allowed_users(allowed_roles = ['Business'])
def all_stores(request):
    all_plan     = Plan.objects.all()
    current_user = request.user
    profile      = UserProfile.objects.get(user = current_user)
    invoice_ID     = profile.business_ID
    businessInfo = BusinessProfile.objects.get(business_ID = profile.business_ID)
    stores       = BusinessBranch.objects.filter(business_ID = profile.business_ID)
    context      = {"invoice_ID":invoice_ID,'businessInfo':businessInfo,'stores':stores}
    return render(request,'app/all-stores.html',context)




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
    return render(request,'app/plans.html',context)

@login_required(login_url='accounts/login' )
@allowed_users(allowed_roles = ['Business'])
def billing_invoices(request):
    current_time  = datetime.datetime.now()
    current_user = request.user
    profile      = UserProfile.objects.get(user = current_user)
    invoice_ID     = profile.business_ID
    businessInfo = BusinessProfile.objects.get(business_ID = profile.business_ID)
    current_plan = Plan.objects.get(Plan_ID = businessInfo.Plan_ID)
    invoice_info  = BillingInvoice.objects.filter(business_ID = profile.business_ID)
    all_invoice  = BillingInvoice.objects.filter(business_ID = profile.business_ID).first()
   
    context      = {"invoice_info":invoice_info,"invoice_ID":invoice_ID,'current_time': current_time,'all_invoice':all_invoice,'businessInfo':businessInfo,'current_plan':current_plan}
    return render(request,'app/billing.html',context)

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
    return render(request,'app/storage-disk.html',context)




def PaymentView(request,Invoice_ID):
    current_user = request.user
    profile      = UserProfile.objects.get(user = current_user)
    invoice_ID     = profile.business_ID
    businessInfo = BusinessProfile.objects.get(business_ID = profile.business_ID)
    current_plan = Plan.objects.get(Plan_ID = businessInfo.Plan_ID)
    all_invoice  = BillingInvoice.objects.get(Invoice_ID = Invoice_ID)
    context = {"invoice_ID":invoice_ID,'Invoice_ID':Invoice_ID}

    if request.method == "POST":
        AccountNumber   = request.POST.get('AccountNumber','')
        BankName        = request.POST.get('BankName','')
        amount          = request.POST.get('amount','')
        currency        = request.POST.get('currency','')
        date            = request.POST.get('date','')
        reference       = request.POST.get('reference','')
        CardName        = request.POST.get('CardName','')
        billingCycle    = request.POST.get('billingCycle','')
        if request.POST['AccountNumber'] and ['BankName'] and ['amount'] and ['currency'] and ['date'] and ['reference'] and ['billingCycle'] and ['CardName']:

            proof_refference = ProofOfPayment.objects.filter(refference = reference)
            if proof_refference.exists():
                messages.error(request, "The proof of payment you are trying to submit already exist")

               
            else:
                ProofOfPayment.objects.create(
                    Business_Name      = businessInfo.BusinessName,
                    business_ID        = profile.business_ID,
                    accountnumber    = AccountNumber,
                    bankname         = BankName,
                    amount           = amount,
                    currency         = currency,
                    date             = date,
                    refference       = reference,
                    cardName         = CardName,
                    Invoice_ID        = Invoice_ID,
                    billingCycle     = billingCycle
                )
                BillingInvoice.objects.filter(Invoice_ID   = Invoice_ID).update(invoice_status = 'PENDING')
                
                messages.success(request, "You have succesfully submitted your proof of payment, your account will be activated soon after your payment is verified...")
                return redirect('account/billing-invoices')
            
        else:
            messages.info(request, "Please complete the form missing input field.")

  
    return render(request,'app/pay.html',context)





@login_required(login_url='accounts/login' )
@allowed_users(allowed_roles = ['Business'])
def user_profile(request):
    currentUser = request.user
    
    if request.method == "POST":
        firstname       = request.POST.get('firstname','')
        lastname        = request.POST.get('lastname','')
        gender          = request.POST.get('gender','')
        mobile_number   = request.POST.get('mobile_number','')
        accepts_whatsapp= request.POST.get('accepts_whatsapp','')
        landline        = request.POST.get('landline','')
        suburb_ac       = request.POST.get('suburb_ac','')
        street_name     = request.POST.get('street_name','')
        city            = request.POST.get('city','')
        latitude        = request.POST.get('latitude','')
        longitude       = request.POST.get('longitude','')
        UserProfile.objects.filter(user = currentUser).update(
        firstName   = firstname,
        last_Name   = lastname,
        gender      = gender,
        home_adress = suburb_ac,
        street_name = street_name,
        city        = city,
        phone       = mobile_number,
        accepts_whatsapp=accepts_whatsapp,
        other_phone = landline,
        longitude   = longitude,
        latitude    = latitude,
 
        )
    
        messages.success(request, "You have succesfully updated your profile.")
    userprofile = UserProfile.objects.get(user = currentUser)
    context = {"invoice_ID":invoice_ID,"userprofile": userprofile}
    return render(request,'app/default/User-profile.html',context)



# ------------- knoledge_base -------------- #
# @login_required(login_url='accounts/login' )
# @allowed_account(allowed_account = ['RETAIL AND ECOMM'])
# @allowed_users(allowed_roles = ['Business'])

def knoledge_center(request):
    currentUser = request.user
    info        = UserProfile.objects.get(user = currentUser)
    invoice_ID     = info.business_ID
    businessInfo = BusinessProfile.objects.get(business_ID =  info.business_ID)
    customers   = Customer.objects.filter(business_ID = info.business_ID)
   
    inbox_messages = customers.filter(inbox_messages__gt = 0).count()
    
    if request.method == "POST":
       
        tittle               = request.POST.get('tittle','')
        caption              = request.POST.get('caption','')
        media_file           = request.FILES['media_file']
        file_type            = media_file.content_type
        
        print('this is the file type ' + file_type)
        size_kb              = media_file.size/1000
        size_mb = size_kb/1000
        data_access = MediaType.objects.all()
        print(data_access.filter(media_type  = media_file.content_type))
        if MediaType.objects.filter(media_type  = file_type).exists():
            data_info = MediaType.objects.filter(media_type  = file_type).first()
            articleID    = uuid.uuid1()
            articleID    = str(articleID)
            KnoledgeBase.objects.create(
                business_ID        = info.business_ID,
                branch_ID          = info.branch_ID,
                article_ID         = articleID,
                tittle             =  tittle,
                description        = caption,
                mediafile          = media_file,
                author             = info.firstName + ' ' + info.last_Name,
                category           = data_info.category,

            )
            messages.success(request, 'You Have Succesifully Uploaded Media!')
        else:
            messages.error(request, 'File format not supported!')
   
    context = {"invoice_ID":invoice_ID,"businessInfo":businessInfo,"inbox_messages":inbox_messages,}
    return render(request,'app/knowledge-base.html',context)



@login_required(login_url='accounts/login' )
@allowed_account(allowed_account = ['RETAIL AND ECOMM'])
@allowed_users(allowed_roles = ['Business'])
def all_articles(request):
    currentUser = request.user
    info        = UserProfile.objects.get(user = currentUser)
    invoice_ID     = info.business_ID
    businessInfo = BusinessProfile.objects.get(business_ID =  info.business_ID)
    all_knoledge = KnoledgeBase.objects.filter(business_ID = info.business_ID)
    context = {"invoice_ID":invoice_ID,"businessInfo":businessInfo,"all_knoledge":all_knoledge}
    return render(request,'app/all-articles.html',context)




@login_required(login_url='accounts/login' )
@allowed_users(allowed_roles = ['Business'])
def business_profile(request):
    currentUser = request.user
    
    if request.method == "POST":
        businessname     = request.POST.get('businessname','')
        email            = request.POST.get('email','')
        facebook         = request.POST.get('facebook','')
        website          = request.POST.get('website','')
        mobile_number    = request.POST.get('mobile_number','')
        accepts_whatsapp = request.POST.get('accepts_whatsapp','')
        other_mobile     = request.POST.get('other_mobile','')
        streetName       = request.POST.get('streetName','')
        businessadress   = request.POST.get('businessadress','')
        city            = request.POST.get('city','')
        latitude        = request.POST.get('latitude','')
        longitude       = request.POST.get('longitude','')
        BusinessProfile.objects.filter(user = currentUser).update(
            BusinessName    = businessname,
            Business_adress = businessadress, 
            street_name     = streetName ,
            email           = email,
            city            = city,
            facebook        = facebook,
            website         = website,
            phone           = mobile_number,
            accepts_whatsapp= accepts_whatsapp,
            other_phone     = other_mobile,
            longitude       = longitude,
            latitude        = latitude,
            form_completed  = True

 
        )
    
        messages.success(request, "You have succesfully updated your profile.")
    currentUser = request.user
    businessprofile = BusinessProfile.objects.get(user = currentUser)
    context         = {"businessprofile": businessprofile}
    return render(request,'app/default/business-profile.html',context)

















@login_required(login_url='accounts/login' )
@allowed_users(allowed_roles = ['Business'])
def manage_business_details(request):
    
    return render(request,'app/masai/index.html')


@login_required(login_url='accounts/login' )
@allowed_users(allowed_roles = ['Business'])
def manage_payment_options(request):
    
    return render(request,'app/masai/index.html')

#=====================#
#Platform home pages
#=====================#

@prevent_authenticated
@prevent_logged_in_access_to_public_tenant
def index(request):
    all_testimonies = Testimonial.objects.all()
    current_domain = request.get_host()
    print('Website: ' + current_domain )
    context         = {"all_testimonies":all_testimonies}
    if request.method == "POST":
        email     = request.POST.get('email','')
        CustomerEmails.objects.create(
            email = email
        )
        return redirect('account/user/signup')
    return render(request,'home/index.html',context)


@user_controller
def pricing_table(request):
    return render(request,'home/pricing.html')

# ================ # 
# Products 
# ================ #
@user_controller
def wa_chatbot(request):
    all_features = ProductFeature.objects.get(feature = 'Whatsapp Chatbot')
    context = {'all_features':all_features}
    return render(request,'home/products/product-type.html',context)

@user_controller
def team_inbox(request):
    all_features = ProductFeature.objects.get(feature = 'Team Inbox')
    context = {'all_features':all_features}
    return render(request,'home/products/product-type.html',context)

@user_controller
def help_center(request):
    return render(request,'home/products/product-type.html')

@user_controller
def manage_orders(request):
    all_features = ProductFeature.objects.get(feature = 'Manage Orders')
    context = {'all_features':all_features}
    return render(request,'home/products/product-type.html',context)

@user_controller
def contacts_manager(request):
    return render(request,'home/products/product-type.html')


@user_controller
def knoledge_base(request):
    return render(request,'home/products/product-type.html')

@user_controller
def event_booking(request):
    return render(request,'home/products/product-type.html')

@user_controller
def catalogoue(request):
    return render(request,'home/products/product-type.html')

@user_controller
def prom_coupons(request):
    return render(request,'home/products/promo-coupons.html')

@user_controller
def live_trans(request):
    return render(request,'home/products/product-type.html')

# ================ # 
# Use Cases
# ================ # 
@user_controller
def e_comm(request):
    current_usecase = UseCase.objects.get(usecase = 'E-Commerce')
    context = {'current_usecase':current_usecase}
    return render(request,'home/use-cases/use-case.html',context)

@user_controller
def automotive(request):
    return render(request,'home/use-cases/use-case.html')

@user_controller
def wholesale(request):
    return render(request,'home/use-cases/use-case.html')

@user_controller
def finance_insurance(request):
    return render(request,'home/use-cases/use-case.html')

@user_controller
def beauty_wellness(request):
    return render(request,'home/use-cases/use-case.html')

@user_controller
def driving_school(request):
    return render(request,'home/use-cases/use-case.html')

@user_controller
def dentist(request):
    return render(request,'home/use-cases/use-case.html')

@user_controller
def agriculture(request):
    return render(request,'home/use-cases/use-case.html')

@user_controller
def car_rental(request):
    return render(request,'home/use-cases/use-case.html')

@user_controller
def food_ordering(request):
    return render(request,'home/use-cases/use-case.html')


@user_controller
def banking(request):
    return render(request,'home/use-cases/use-case.html')


@user_controller
def education(request):
    return render(request,'home/use-cases/contact-us.html')

# ============ Use Case End Here ============= #

@user_controller
def about_us(request):
    return render(request,'home/about.html')


@user_controller
def integrations(request):
    all_integrations = Integration.objects.all()
    context = {'all_integrations':all_integrations}
    return render(request,'home/integrations-partiners.html',context)


@user_controller
def ecommerce_price(request):
    all_plan     = Plan.objects.all()
    packages     = PlanPackage.objects.all()
    context      = {'packages':packages,'all_plan':all_plan}

    return render(request,'home/pricing_ecommerce.html',context)


@user_controller
def non_profit_price(request):
    all_plan     = Plan.objects.all()
    packages     = PlanPackage.objects.all()
    context      = {'packages':packages,'all_plan':all_plan}

    return render(request,'home/pricing_non_profit.html',context)




@user_controller
def signup(request):
    if request.method == "POST":
        email    = request.POST.get('email','')
        fullName = request.POST.get('fullName','')
        phone    = request.POST.get('phone','')
        password1 = request.POST.get('password1','')
        password2 = request.POST.get('password2','')
        qs = User.objects.filter(
            Q(username__iexact = email)|
            Q(email__iexact = email)
        )
        
        if password1 != password2 :
            messages.error(request, 'The two password fields did not match.')
            return render(request, 'registration/signup.html') 
        elif qs.exists():
            messages.error(request, 'The username you have supplied already exists.')
            return render(request, 'registration/signup.html') 
            
        else:
            user = User.objects.create_user(email ,email,password1)
            login(request,user)
            group = Group.objects.get(name='Business')
            user.groups.add(group)
           

            useprofileID    = uuid.uuid1()
            useprofileID    = str(useprofileID)
            BusinessProfile.objects.create(user = user,
            email           = email,
            phone           = phone,
            contactPerson   = fullName
            
            )
            UserProfile.objects.create(user = request.user,
            userprofileID  = useprofileID,
            firstName      = fullName,
            phone          =  phone,
            form_completed = True,
                    
            
            )
            
            return redirect('account/user/business/profile')
            
    return render(request, 'registration/signup.html') 


def business_profile(request):
    if request.method == "POST":
        company      = request.POST.get('company','')
        streetAdress = request.POST.get('streetAdress','')
        country      = request.POST.get('country','')
        city         = request.POST.get('city','')
        curentUser   = request.user
        branch_ID    = uuid.uuid1()
        branch_ID    = str(branch_ID)
        
        
        
        
        businessID = uuid.uuid1()
        businessID = str(businessID)
        UserProfile.objects.filter(user = curentUser).update(branch_ID  = branch_ID,business_ID    = businessID)
        if request.POST['company'] and ['streetAdress'] and ['country'] and ['city']:
            BusinessProfile.objects.filter(user =  curentUser).update(
                business_ID    = businessID,
                BusinessName    = company,
                country         = country,
                city            = city,
                
                street_name     = streetAdress,
                businessprofile_status   = True,
            )
            
            BusinessBranch.objects.create(
                business_ID         = businessID,
                branch_ID           = branch_ID,
                branch_name         = streetAdress,
                branch_city         = city,
                branch_adress       = streetAdress,
                longitude           = 000000,
                latitude            = 000000,

        )
            DiskManager.objects.create(business_ID = businessID,BusinessName = company)
        return redirect('account/user/business/category/business-type')   
        
        
        
            
    return render(request, 'registration/businessProfile-01.html') 




def business_category(request):
    if request.method == "POST":
        website                  = request.POST.get('website','')
        
        business_category        = request.POST.get('business_category','')
        
        curentUser = request.user
        if request.POST['business_category']:
            BusinessProfile.objects.filter(user =  curentUser).update(
                
                website                  =  website,
                businessCategory_status  = True,
                businessCategory         = business_category,
            )
            
            curentUser = request.user
            business_info  = BusinessProfile.objects.get(user =  curentUser)
            company_domain = generate_subdomain(business_info.BusinessName)
            BusinessProfile.objects.filter(user =  curentUser).update(business_domain = company_domain)
            temp_company_domain =  company_domain
            base_domain         = ".pangotalk.com"
            company_domain      = company_domain + base_domain
            
            final_domain        = temp_company_domain + ".pangotalk.com"
            subdomain_url               = f"https://pangotalk.com"
            user_id = request.user.id
            #create_comapany_subdomain_task(temp_company_domain,  final_domain)
            task = create_comapany_subdomain_task.delay(temp_company_domain,  final_domain)
            request.session['task_id'] = task.id

            return redirect('account/user/business/setting-up-account')
        
        
        
            
    return render(request, 'registration/businessCatergory.html') 




def check_task_status(request):
    """
    Checks the task status and redirects to the dashboard if completed
    """
    task_id = request.session.get('task_id')
    if not task_id:
        return JsonResponse({'error': 'No task found'}, status=400)

    result = AsyncResult(task_id)
    if result.state == 'SUCCESS':
        return redirect('/')  # Replace 'dashboard' with your actual dashboard route
    else:
        return JsonResponse({'status': result.state})



def loading_subdomain_setting_up(request):
    
    return render(request,'app/default/creating_subdomain.html')

    
    
    
     
   





def invoice_display(request,order_ID):
    businessInfo = BusinessProfile.objects.get()
   
    order_data  = Order.objects.get(
                order_ID     =  order_ID,        
                )
    totalamount = float(order_data.total_Amount) * float(order_data.orderQuantity)
    business_ID =order_data.business_ID 
    businessInfo = BusinessProfile.objects.get(business_ID = business_ID)
    context = {"totalamount":totalamount,"businessInfo":businessInfo,'order_ID':order_ID,"order_data":order_data}
    return render(request, 'invoice/index.html',context) 



@form_complete
def signup_complete(request):
    return render(request,'registration/onboarding-complete.html')






def user_login(request):
    
    
    return render(request,'registration/login.html')



@login_required(login_url='accounts/login' )
@allowed_users(allowed_roles = ['Business'])
def select_category(request):
    
    return render(request,'app/default/select-category.html')





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
            return render(request,'registration/user-changepassword.html',context)




def generate_subdomain(company_name):
    # Convert company name to a valid subdomain by removing spaces and special characters
    subdomain = re.sub(r'\s+', '', company_name.lower())  # Remove spaces and lowercase
    subdomain = re.sub(r'[^a-z0-9-]', '', subdomain)  # Remove special characters
    
    # Ensure uniqueness by checking the database
    original_subdomain = subdomain
    counter = 1
    while BusinessProfile.objects.filter(business_domain   = subdomain).exists():
        subdomain = f"{original_subdomain}{counter}"
        counter += 1
    return subdomain







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
    return render(request,'app/message_balance.html',context)


