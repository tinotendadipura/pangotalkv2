from django.contrib.auth import get_user_model

from celery import shared_task
from app.models import Client, Domain


from django.core.mail import send_mail
from app.views import billing_invoices, business_category
from pangotalk import settings
from django.utils import timezone
from datetime import timedelta
from django.template.loader import get_template
from django.core.mail import EmailMessage
from django.conf import settings
from app. models import (

    
    BusinessProfile,AccountUpgrade,UserProfile,
    BusinessConfiguration,Plan,BillingInvoice,
    AccountUpgrade,ProofOfPayment,Transaction,
    BusinessConfiguration
    
    )

from . emailmanager import PaymentEmail

@shared_task(bind=True)
def send_mail_func(self,business_ID):
    profile = UserProfile.objects.filter(business_ID = business_ID)
    users = get_user_model().objects.all()
    #timezone.localtime(users.date_time) + timedelta(days=2)
    for user in profile:
        mail_subject = "Hi! Celery Testing"
        message = "If you are liking my content, please hit the like button and do subscribe to my channel"
        to_email = user.user.email
        send_mail(
            subject = mail_subject,
            message=message,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[to_email],
            fail_silently=True,
        )
    return "Done"




@shared_task(bind=True)
def payment_success_mail_func(self,invoice_id):
    billing_invoice=BillingInvoice.objects.get(Invoice_ID = invoice_id)
    business_ID = billing_invoice.business_ID
    sendProof = PaymentEmail()
    email       = 'tinotendadipura2@gmail.com'
    invite_link ='xxxxxxxxxxxxxxxxxxx'
    invite_id   = 'xxxxxxxxxxxxxxxxxx'
    sendProof.payment_confirmation(business_ID,invoice_id)
    return "Done"


@shared_task(bind=True)
def billing_reminder_func(self,business_ID,invoice_id):
    sendreminder = PaymentEmail()
    sendreminder.send_billing_reminder(business_ID,invoice_id)
    return "Done"
    
    
    
    
            
@shared_task(bind=True)
def create_comapany_subdomain_task(temp_company_domain,  final_domain,task_id):
    try:
        # excute this part once the page have loaded
        
        tenant         = Client(schema_name = temp_company_domain,name = temp_company_domain )
        tenant.save()
                
        
        domain_info    = Domain(domain = final_domain, tenant = tenant, is_primary = True)
        domain_info.save()

        return "Done"

    
    
    
    except Exception as e:
        # Handle any other unforeseen exceptions
        print(f"An error occurred: {str(e)}")
        return "Done"

            
   

            
    



    