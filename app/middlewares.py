# middlewares.py
from django.shortcuts import redirect
from django.http import HttpResponseForbidden
from .models import BusinessProfile  # Import your BusinessProfile model

class RedirectAuthenticatedUserToTenantMiddleware:
    """
    Middleware to redirect authenticated users accessing the public domain
    to their specific tenant dashboard based on their BusinessProfile subdomain.
    """
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Get the current domain or subdomain
        current_domain = request.get_host()  # e.g., "www.yourdomain.com"
        public_domain = '.localhost:8000'  # Define your public domain

        # Check if the user is authenticated and on the public domain
        if request.user.is_authenticated and current_domain == public_domain:
            try:
                # Retrieve the user's BusinessProfile to get the subdomain
                business_profile = BusinessProfile.objects.get(user=request.user)
                subdomain = business_profile.business_domain

                # Redirect to the tenant dashboard
                if business_profile.category == 'RETAIL AND ECOMM':
            
                        tenant_dashboard_url = subdomain + public_domain + '/main/home/dashboard'
                        return redirect(tenant_dashboard_url)
                     
                elif business_profile.category == 'NONE PROFIT':
            
                        tenant_dashboard_url = subdomain + '/main/home/dashboard/non-profit'
                        return redirect(tenant_dashboard_url)

            except BusinessProfile.DoesNotExist:
                # Optionally handle the case where the user doesn't have a BusinessProfile
                return HttpResponseForbidden("You do not have a business profile.")

        return self.get_response(request)
