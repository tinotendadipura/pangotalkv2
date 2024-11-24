from django.http import HttpResponse

from django.shortcuts import render , redirect , get_object_or_404,redirect

import datetime
import pytz
from datetime import timedelta
from . models import UserProfile,BusinessProfile
from django.contrib import messages
from functools import wraps
from django.shortcuts import redirect
from django.http import HttpResponseForbidden



def unauthenticated_user(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('/')
        else:
            return view_func(request, *args, **kwargs)

    return wrapper_func



def  user_controller(view_func):
    def wrapper_func(request,*args,**kwargs):
        if request.user.is_authenticated:
            Business       = ['Business']
            adminstrator = ['Adminstrator']
            
            
            group = None
            if request.user.groups.exists():
                group = request.user.groups.all()[0].name

            if group in Business:
                currentUser  = request.user
                profile      = UserProfile.objects.get(user = currentUser )
                businessInfo = BusinessProfile.objects.get(business_ID = profile.business_ID) 
                if businessInfo.category == 'RETAIL AND ECOMM':
            
                     return redirect('main/home/dashboard')
        
                else: 
        
                     return redirect('main/home/dashboard/non-profit')
            if group in  adminstrator:
                return redirect('business-manager/admin')
            
            else:
                return view_func(request,*args,**kwargs)
        else: 
            return view_func(request,*args,**kwargs)

    return wrapper_func






def allowed_users(allowed_roles=[]):
    def decorator(view_func):
        def wrapper_func(request, *args, **kwargs):

            group = None
            if request.user.groups.exists():
                group = request.user.groups.all()[0].name

            if group in allowed_roles:
                return view_func(request, *args, **kwargs)
            else:
                return redirect('/')
        return wrapper_func
    return decorator





def allowed_account(allowed_account=[]):
    def decorator(view_func):
        def wrapper_func(request, *args, **kwargs):

            user_status = UserProfile.objects.get(user = request.user)
            businessID  = user_status.business_ID
            info        = BusinessProfile.objects.get(business_ID = businessID)
            
            if info.category in allowed_account:
                return view_func(request, *args, **kwargs)
            else:
                return redirect('/')
        return wrapper_func
    return decorator



def  form_complete(view_func):
    def wrapper_func(request,*args,**kwargs):
        
        user_status = UserProfile.objects.get(user = request.user)
        businessID  = user_status.business_ID
        info = BusinessProfile.objects.get(business_ID = businessID)
        if info.businessprofile_status == False or info.businessCategory_status == False:
            if info.businessprofile_status == True:
                messages.info(request, "Please select your business category to proceed.")
                return redirect('account/user/business/category/business-type')
            else:
                messages.info(request, "Please complete your business profile to proceed.")
                return redirect('account/user/business/profile')
        
        else: 
             return view_func(request,*args,**kwargs)

    return wrapper_func


def  account_verification(view_func):
    def wrapper_func(request,*args,**kwargs):
        if request.user.is_authenticated:
            user_status = UserProfile.objects.get(user = request.user)
            businessID  = user_status.business_ID
            info = BusinessProfile.objects.get(business_ID = businessID)
            if info.account_authorisation_status == False :
                
                return redirect('/')
            
            else: 
                return view_func(request,*args,**kwargs)
        return redirect('/')
    return  wrapper_func
    

def category_access(view_func):
    def wrapper_func(request,*args,**kwargs):
        user_status = UserProfile.objects.get(user = request.user)
        businessID  = user_status.business_ID
        info = BusinessProfile.objects.get(business_ID = businessID)
        if info.category == 'RETAIL AND ECOMM':
            
            return redirect('main/home/dashboard')
        
        if info.category == 'NONE PROFIT':
            
            return redirect('main/home/dashboard/non-profit')
    return wrapper_func
    


# decorators.py
from django.http import HttpResponseForbidden
from django.shortcuts import redirect
from .models import BusinessProfile  # Import your BusinessProfile model

# decorators.py
from django.http import HttpResponseForbidden
from django.shortcuts import redirect
from .models import BusinessProfile  # Import your BusinessProfile model






def prevent_logged_in_access_to_public_tenant(view_func):
    """
    Decorator to redirect logged-in users to their tenant dashboard if they
    access their specific tenant subdomain, or to prevent access to the public tenant.
    """

    def _wrapped_view(request, *args, **kwargs):
        # Define your public domain
        public_domain = 'localhost:8000'  # Modify as needed

        # Check if the user is authenticated
        if request.user.is_authenticated:
            # Check if the user is accessing their tenant subdomain
            host_domain = request.get_host()
            host_subdomain = request.get_host().split('.')[0]  # e.g., "mushorahasha1" from "mushorahasha1.localhost:8000"
            # Retrieve the user's BusinessProfile to get the subdomain
            business_profile   = BusinessProfile.objects.get(user=request.user)
            business_subdomain = business_profile.business_domain
            scheme = request.scheme
            # Get the host (domain name)
            host = request.get_host()  # This returns 'example.com' or 'subdomain.example.com'
            

            try:
                # Retrieve the user's BusinessProfile to get the subdomain
                business_profile     =           BusinessProfile.objects.get(user=request.user)
                user_subdomain       =           business_subdomain + '.pangotalk.com'
                if host_subdomain    ==          business_profile.business_domain:
                    if host_domain   ==          user_subdomain:
                        subdomain_url                 = f"http://{ business_subdomain}.pangotalk.com/main/home/dashboard"
                        non_profit_subdomain_url      = f"http://{ business_subdomain}.pangotalk.com/main/home/xxxx"

                        if business_profile.category == 'RETAIL AND ECOMM':
            
                           return redirect(subdomain_url)
        
                        else: 
        
                           return redirect(non_profit_subdomain_url)
                        
                else:
                    return redirect('you-are-not-authorised-to-acess-this-page   ')    

                
                   


                    

                

            except BusinessProfile.DoesNotExist:
                return HttpResponseForbidden("You do not have access to this page.")

        return view_func(request, *args, **kwargs)

    return _wrapped_view








def prevent_authenticated(view_func):

    """
    Decorator to redirect logged-in users to their tenant dashboard if they
    access their specific tenant subdomain, or to prevent access to the public tenant.
    
    """

    def _wrapped_view(request, *args, **kwargs):
        # Define your public domain
        public_domain = 'pangotalk.com'  # Modify as needed

        # Check if the user is authenticated
        if request.user.is_authenticated:
            user_profile       = UserProfile.objects.get(user=request.user)
            business_profile   = BusinessProfile.objects.get(business_ID = user_profile.business_ID )
            business_subdomain = business_profile.business_domain
            scheme             = request.scheme

            # Get the host (domain name)
            host = request.get_host()  # This returns 'example.com' or 'subdomain.example.com'
            try:
                
                
                eccom_subdomain_url      = f"http://{ business_subdomain}.pangotalk.com/main/home/dashboard"
                none_profit_subdomain_url      = f"http://{ business_subdomain}.pangotalk.com/main/home/dashboard/non-profit"

                if business_profile.category == 'RETAIL AND ECOMM':
            
                   return redirect(eccom_subdomain_url)
        
                if business_profile.category == 'NONE PROFIT':
            
                  return redirect(none_profit_subdomain_url)
                else:
                    return redirect('you-are-not-authorised-to-acess-this-page')    

            except BusinessProfile.DoesNotExist:
                return HttpResponseForbidden("You do not have access to this page.")

        return view_func(request, *args, **kwargs)

    return _wrapped_view
