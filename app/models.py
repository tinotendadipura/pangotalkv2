from locale import currency

from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.db.models.signals import post_save
from django.utils import timezone
from django_tenants.models import TenantMixin, DomainMixin

class Client(TenantMixin):
    name          = models.CharField(max_length=100)
    paid_until    = models.DateField(default = timezone.now)
    on_trial      = models.BooleanField(default = True)
    created_on    = models.DateField(default = timezone.now)

    # default true, schema will be automatically created and synced when it is saved
    auto_create_schema = True


class Tenant(TenantMixin):
    name = models.CharField(max_length=100)
    domain = models.CharField(max_length=100)  # e.g., 'company.example.com'



class Domain(DomainMixin):
    pass



BUSINESS_CATEGORY = (
    ('RETAIL AND ECOMM', 'RETAIL AND ECOMM'),
    
    ('NONE PROFIT', 'NONE PROFIT'),
    
)



PLAN_CATEGORY = (
   ('BASIC', 'BASIC'),
    ('PREMIUM', 'PREMIUM'),
    ('PLUS','PLUS'),
    ('CUSTOM','CUSTOM')
)

INVOICE_STATUS = (
   ('BASIC', 'BASIC'),
    ('PREMIUM', 'PREMIUM'),
    ('PLUS','PLUS'),
    ('CUSTOM','CUSTOM')
)



PAKAGES = (
    ('BASIC', 'BASIC'),
    ('STANDARD', 'STANDARD'),
    ('PLUS','PLUS'),
    
)

class PlanPackage(models.Model):
    plan_ID     = models.CharField(max_length = 50,default='none')
    PlanName    = models.CharField(
        choices     = PAKAGES,
        default     ='BASIC',
        max_length=30)
    PlanItemName        = models.TextField(max_length = 500,default='none')
    PlanItemQuantity    = models.TextField(max_length = 500,default='none')
    dateadded           = models.DateTimeField(default = timezone.now)
    
    def __str__(self):
      return self.PlanName


class UserProfile(models.Model):
    user              = models.OneToOneField(User,on_delete = models.CASCADE,default=1)

    userprofileID     = models.CharField(max_length = 50,default='none')
    business_ID = models.CharField(max_length = 50,default='none')
    branch_ID   = models.CharField(max_length = 50,default='none')
    firstName   = models.CharField(max_length = 50,default='none')
    last_Name   = models.CharField(max_length = 50,default='none')
    home_adress = models.CharField(max_length = 50,default='none')
    city        = models.CharField(max_length = 50,default='none')
    country     = models.CharField(max_length = 20,default='none')
    phone       = models.CharField(max_length = 50,default="s-00")
    dateadded   = models.DateTimeField(default = timezone.now)
    account_type = models.BooleanField(default=True)
    form_completed = models.BooleanField(default=False)
    
    def __str__(self):
      return self.firstName




class Invite(models.Model):
    invite_ID   = models.CharField(max_length = 50,default='none')
    business_ID = models.CharField(max_length = 50,default='none')
    branch_ID   = models.CharField(max_length = 50,default='none')
    firstName   = models.CharField(max_length = 50,default='none')
    last_Name   = models.CharField(max_length = 50,default='none')
    email       = models.CharField(max_length = 50,default='none')
    role        = models.CharField(max_length = 50,default='none')
    phone       = models.CharField(max_length = 50,default="s-00")
    invite_url  = models.CharField(max_length = 500,default="s-00")
    dateadded   = models.DateTimeField(default = timezone.now)
    invite_status = models.BooleanField(default=False)
    
    
    def __str__(self):
      return self.firstName


class BusinessProfile(models.Model):
    BUSINESS_TYPE = (
    ('NON-PROFIT', 'NON-PROFIT'),
    ('BUSINESS', 'BUSINESS'),
   
    
)
    BILLING_INTERVAL = (
    ('MONTHLY', 'MONTHLY'),
    ('YEARLY', 'YEARLY'),
    
    
)
    user                = models.OneToOneField(User,on_delete = models.CASCADE)
    business_domain     = models.CharField(max_length = 50,default='none')
    business_ID         = models.CharField(max_length = 50,default='none')
    Plan_ID             = models.CharField(max_length = 50,default='none')
    billing_interval    = models.CharField(choices     = BILLING_INTERVAL,default     ='MONTHLY',max_length=30)
    next_billing_date   = models.DateTimeField(default = timezone.now)
    billing_Amount      = models.CharField(max_length = 50,default='')
    businessCategory    = models.CharField(max_length = 500,default='')
    business_type       = models.CharField( choices     = BUSINESS_TYPE, default     ='BUSINESS', max_length=30)
    category            = models.CharField(choices     = BUSINESS_CATEGORY,default     ='RETAIL AND ECOMM',max_length=30)
    productType         = models.CharField(max_length = 500,default='')
    businessCategory_status  = models.BooleanField(default=False)
    businessprofile_status   = models.BooleanField(default=False)
    BusinessName    = models.CharField(max_length = 500,default='')
    contactPerson   = models.CharField(max_length = 500,default='')
    logo_image      = models.FileField(upload_to='files/%Y/%m/%d/',null=True,blank=True)
    banner_image    = models.FileField(upload_to='files/%Y/%m/%d/',null=True,blank=True)
    country         = models.CharField(max_length = 500,default='')
    Business_adress = models.CharField(max_length = 50,default='')
    street_name     = models.CharField(max_length = 500,default='none')
    email           = models.CharField(max_length = 500,default='none')
    city            = models.CharField(max_length = 50,default='none')
    facebook        = models.CharField(max_length = 500,default='none')
    website         = models.CharField(max_length = 500,default='none')
    phone           = models.CharField(max_length = 50,default="")
    other_phone     = models.CharField(max_length = 50,default="")
    longitude       = models.CharField(default ='0.0' ,max_length=400)
    latitude        = models.CharField(default ='0.0' ,max_length=400)
    form_completed  = models.BooleanField(default=False)
    account_authorisation_status  = models.BooleanField(default=False)
    account_suspended_status      = models.BooleanField(default=False)
    dateadded                     = models.DateTimeField(default = timezone.now)
    

    
    def __str__(self):
      return self.BusinessName
    



class BusinessConfiguration(models.Model):
    BusinessName        = models.CharField(max_length = 500,default='')
    business_ID         = models.CharField(max_length = 50,default='none')
    
    
    bot_endpoint     = models.CharField(max_length = 500,default='')
    bot_apiKey       = models.CharField(max_length = 500,default='')
    bot_name         = models.CharField(max_length = 500,default='')
    
    account_config_status  = models.BooleanField(default=False)
    
    


class DiskManager(models.Model):
    BusinessName      = models.CharField(max_length = 500,default='')
    business_ID       = models.CharField(max_length = 50,default='none')
    Plan_ID           = models.CharField(max_length = 50,default='none')
    disk_space        = models.DecimalField(max_digits=10, decimal_places=2,default=0)
    Plan_disk_space   = models.DecimalField(max_digits=10, decimal_places=2,default=0)



class ProductListing(models.Model):
   
    business_ID     = models.CharField(max_length = 50,default='none')
    branch_ID       = models.CharField(max_length = 50,default='none')
    product_ID      = models.CharField(max_length = 50,default='none')
    title           = models.CharField(max_length = 500, default="None")
    product_image   = models.FileField(upload_to='files/%Y/%m/%d/',null=True,blank=True)
    media_size      = models.CharField(max_length = 500,default='none')
    description     = models.TextField(max_length = 5000,default="None")
    category        = models.CharField(max_length = 500,default='none')
    price           = models.CharField(max_length = 500,default='none')
    currency        = models.CharField(max_length = 500,default='none')
    compare_price   = models.CharField(max_length = 500,default='none')
    dateadded       = models.DateTimeField(default = timezone.now)
    
    def __str__(self):
      return self.title


class BannerImage(models.Model):
   
    business_ID     = models.CharField(max_length = 50,default='none')
    BusinessName    = models.CharField(max_length = 500, default="None")
    banner_image    = models.FileField(upload_to='files/%Y/%m/%d/',null=True,blank=True)
    
    def __str__(self):
      return self.BusinessName





class Feedback(models.Model):
   
    business_ID     = models.CharField(max_length = 50,default='none')
    customer_ID     = models.CharField(max_length = 50,default='none')
    customerName    = models.CharField(max_length = 500, default="None")
    phoneNumber     = models.CharField(max_length = 500, default="None")
    feedback        = models.TextField(max_length = 5000, default="None")
    dateadded       = models.DateTimeField(default = timezone.now)
    
    def __str__(self):
      return self.customerName



class FeedbackCount(models.Model):
   
    business_ID          = models.CharField(max_length = 50,default='none')
    current_feedback     = models.IntegerField(default = 0)
    



class ContactCard(models.Model):
   
    business_ID     = models.CharField(max_length = 50,default='none')
    branch_ID       = models.CharField(max_length = 50,default='none')
    city            = models.CharField(max_length = 500, default="None")
    country         = models.TextField(max_length = 5000,default="None")
    country_code    = models.CharField(max_length = 500,default='none')
    state           = models.CharField(max_length = 500,default='none')
    contactcard_ID  = models.CharField(max_length = 50,default="----")
    type            = models.CharField(max_length = 50,default="----")
    zip             = models.CharField(max_length = 50,default="----")
    dateadded       = models.DateTimeField(default = timezone.now)
    
    def __str__(self):
      return self.city




class Location(models.Model):
   
    business_ID     = models.CharField(max_length = 50,default='none')
    branch_ID       = models.CharField(max_length = 50,default='none')
    location_ID     = models.CharField(max_length = 50,default='none')
    longitude       = models.TextField(max_length = 5000,default="None")
    latitude        = models.CharField(max_length = 500,default='none')
    state           = models.CharField(max_length = 500,default='none')
    location_ID     = models.CharField(max_length = 50,default="----")
    dateadded       = models.DateTimeField(default = timezone.now)
    
    def __str__(self):
      return self.city


class ProductListingImages(models.Model):
    business_ID        = models.CharField(default ='None' ,max_length=40)
    branch_ID          = models.CharField(max_length = 50,default='none')
    productimage       = models.FileField(upload_to='files/%Y/%m/%d/',null=True,blank=True)
    product_ID         = models.CharField(default ='None' ,max_length=40)



STATUS_CHOICES = (
    ('PAID', 'PAID'),
    ('OVERDUE', 'OVERDUE'),
    ('PENDING', 'PENDING'),
    
)


MEDIA_CATEGORY = (
    ('Documents', 'Documents'),
    
    ('Image', 'Image'),
    ('Audio', 'Audio'),
    ('Video','Video')
)
class ProductCategory(models.Model):
    business_ID        = models.CharField(default ='None' ,max_length=40) 
    branch_ID          = models.CharField(max_length = 50,default='none')
    category           = models.CharField(default ='None' ,max_length=400)
    description        = models.TextField(default ='None' ,max_length=5000)

class MediaType(models.Model):
    media_type        = models.CharField(default ='None' ,max_length=40) 
    category        = models.CharField(
        choices     = MEDIA_CATEGORY,
        default     ='None',
        max_length=30)
    
class Visitors(models.Model):
    business_ID    = models.CharField(default ='None' ,max_length=40)
    branch_ID      = models.CharField(max_length = 50,default='none')
    date           = models.CharField(default ='None' ,max_length=40)
    country        = models.CharField(default ='None' ,max_length=40)
    code           = models.CharField(default ='None' ,max_length=40)
    phone          = models.CharField(default ='None' ,max_length=40)
    dateadded      = models.DateTimeField(default = timezone.now)




class Customer(models.Model):
    business_ID        = models.CharField(default ='None' ,max_length=40)
    branch_ID          = models.CharField(max_length = 50,default='none')
    current_branch_status = models.BooleanField(default=False)
    customer_ID          = models.CharField(default ='-------' ,max_length=40)
    customerName         = models.CharField(default ='-------' ,max_length=40)
    firstName            = models.CharField(max_length = 50,default='none')
    last_Name            = models.CharField(max_length = 50,default='none')
    customer_name_status = models.BooleanField(default=False)
    App_User_Name      = models.CharField(default ='None' ,max_length=40)
    total_Amount       = models.CharField(default ='0.00' ,max_length=40)
    location           = models.CharField(default ='None' ,max_length=50)
    home_address       = models.CharField(default ='None' ,max_length=500)
    email_address      = models.CharField(default ='None' ,max_length=500)
    lastOrder          = models.CharField(default ='None' ,max_length=50)
    orderQuantity      = models.CharField(default ='1' ,max_length=50)
    country            = models.CharField(default ='None' ,max_length=40)
    code               = models.CharField(default ='None' ,max_length=40)
    phone              = models.CharField(default ='None' ,max_length=50)
    refunds            = models.CharField(default ='-' ,max_length=50)
    last_message       = models.TextField(default =' ')
    inbox_messages     = models.IntegerField(default = 0 )
    customer_feedback  = models.IntegerField(default = 0 )

    dateadded          = models.DateTimeField(default = timezone.now)




class Order(models.Model):
    business_ID        = models.CharField(default ='None' ,max_length=40)
    branch_ID          = models.CharField(max_length = 50,default='none')
    customer_ID        = models.CharField(default ='-------' ,max_length=40)
    product_ID         = models.CharField(default ='None' ,max_length=40)
    order_ID           = models.CharField(default ='None' ,max_length=40)
    customerName       = models.CharField(default ='None' ,max_length=40)
    product_image_url  = models.CharField(default ='None' ,max_length=4000)
    product_title      = models.CharField(default ='None' ,max_length=40)
    product_description= models.CharField(default ='None' ,max_length=4000)
    customer_ID        = models.CharField(default ='None' ,max_length=40)
    Payment_Method     = models.CharField(default ='None' ,max_length=40)
    total_Amount       = models.DecimalField(
                         max_digits = 10,
                         decimal_places = 2)
    payment_Status     = models.CharField(default ='None' ,max_length=40)
    phone              = models.CharField(default ='None' ,max_length=50)
    location           = models.CharField(default ='None' ,max_length=50)
    lastOrder          = models.CharField(default ='None' ,max_length=50)
    orderQuantity      = models.IntegerField()
    country            = models.CharField(default ='None' ,max_length=50)
    refunds            = models.CharField(default ='-' ,max_length=50)
    viewed             = models.BooleanField(default=False)
    dateadded          = models.DateTimeField(default = timezone.now)




class OrderGroup(models.Model):
    business_ID        = models.CharField(default ='None' ,max_length=40)
    customer_ID        = models.CharField(default ='-------' ,max_length=40)
    customerName       = models.CharField(default ='None' ,max_length=40)
    order_ID           = models.CharField(default ='None' ,max_length=40)
    total_Amount       = models.DecimalField(
                         max_digits = 10,
                         decimal_places = 2)
    payment_Status     = models.CharField(default ='None' ,max_length=40)
    phone              = models.CharField(default ='None' ,max_length=50)
    lastOrder          = models.CharField(default ='None' ,max_length=50)
    orderQuantity      = models.IntegerField()
    country            = models.CharField(default ='None' ,max_length=50)
    refunds            = models.CharField(default ='-' ,max_length=50)
    viewed             = models.BooleanField(default=False)
    dateadded          = models.DateTimeField(default = timezone.now)



class OrderNotification(models.Model):
    business_ID           = models.CharField(default ='None' ,max_length=40)
    order_counter         = models.IntegerField(default=0)
    
    
class InvoiceGenerator(models.Model):
    business_ID        = models.CharField(default ='None' ,max_length=40)
    invoice_file       = models.FileField(upload_to='files/%Y/%m/%d/',null=True,blank=True)
    order_ID           = models.CharField(default ='None' ,max_length=40)
    phone              = models.CharField(default ='None' ,max_length=40)


class Booking(models.Model):
    business_ID        = models.CharField(default ='None' ,max_length=40)
    branch_ID          = models.CharField(max_length = 50,default='none')
    booking_ID         = models.CharField(default ='None' ,max_length=40)
    tittle             = models.CharField(default ='None' ,max_length=40)
    description        = models.CharField(default ='None' ,max_length=40)
    bookingimage       = models.FileField(upload_to='files/%Y/%m/%d/',null=True,blank=True)
    quantity           = models.CharField(default ='None' ,max_length=40)
    startdate          = models.DateTimeField(default = timezone.now)
    enddate            = models.DateTimeField(default = timezone.now)


class EventBooking(models.Model):
    business_ID        = models.CharField(default ='None' ,max_length=40)
    branch_ID          = models.CharField(max_length = 50,default='none')
    customer_ID        = models.CharField(default ='-------' ,max_length=40)
    booking_ID         = models.CharField(default ='None' ,max_length=40)
    event_ID           = models.CharField(default ='None' ,max_length=40)
    customerName       = models.CharField(default ='None' ,max_length=40)
    phone_Number       = models.CharField(default ='None' ,max_length=40)
    eventTittle        = models.CharField(default ='None' ,max_length=40)
    date               = models.CharField(default ='None' ,max_length=40)
    startactualdate    = models.DateField(auto_now=False, auto_now_add=True)
    eventType          = models.CharField(default ='None' ,max_length=40)
    dateadded          = models.DateTimeField(default = timezone.now)



class Event(models.Model):
    business_ID        = models.CharField(default ='None' ,max_length=40)
    branch_ID          = models.CharField(max_length = 50,default='none')
    event_ID           = models.CharField(default ='None' ,max_length=40)
    event_Name         = models.CharField(default ='None' ,max_length=40)
    event_Description  = models.TextField(default ='None' ,max_length=5000)
    eventimage         = models.FileField(upload_to='files/%Y/%m/%d/',null=True,blank=True)
    image_status       = models.BooleanField(default=False)
    online_event       = models.BooleanField(default=False)
    startfulldate      = models.CharField(default ='None' ,max_length=40)
    startactualdate    = models.DateTimeField(default = timezone.now)
    startTime          = models.CharField(default ='None' ,max_length=40)
    endfullDate        = models.CharField(default ='None' ,max_length=40)
    endactuallDate     = models.DateField(default = timezone.now)
    startTime          = models.CharField(default ='None' ,max_length=40)
    endTime            = models.CharField(default ='None' ,max_length=40)





class Coupon(models.Model):
    business_ID        = models.CharField(default ='None' ,max_length=40)
    branch_ID          = models.CharField(max_length = 50,default='none')
    campaignBanner     = models.FileField(upload_to='files/%Y/%m/%d/',null=True,blank=True)
    campaignName       = models.CharField(default ='None' ,max_length=5000)
    couponCode         = models.CharField(default ='None' ,max_length=50)
    percentage         = models.CharField(default ='None' ,max_length=50)
    Usage_limit        = models.IntegerField(default = 1)
    current_claim      = models.IntegerField(default = 1)
    category           = models.CharField(default ='None' ,max_length=500)
    minimum_amount     = models.CharField(default ='None' ,max_length=500)
    startfulldate      = models.CharField(default ='None' ,max_length=40)
    startactualdate    = models.DateTimeField(default = timezone.now)
    startTime          = models.CharField(default ='None' ,max_length=40)
    endfullDate        = models.CharField(default ='None' ,max_length=40)
    endactuallDate     = models.DateTimeField(default = timezone.now)
    startTime          = models.CharField(default ='None' ,max_length=40)
    endTime            = models.CharField(default ='None' ,max_length=40)


class CouponClaim(models.Model):
    business_ID        = models.CharField(default ='None' ,max_length=40)
    branch_ID          = models.CharField(max_length = 50,default='none')
    campaignName       = models.CharField(default ='None' ,max_length=5000)
    couponCode         = models.CharField(default ='None' ,max_length=50)
    percentage         = models.CharField(default ='None' ,max_length=50)
    category           = models.CharField(default ='None' ,max_length=500)
    minimum_amount     = models.CharField(default ='None' ,max_length=500)
    claim_Name         = models.CharField(default ='None' ,max_length=500)
    claim_Number       = models.CharField(default ='None' ,max_length=500)
    claimed_on         = models.DateTimeField(default = timezone.now)
    claimed_status     = models.BooleanField(default=False)
    
class KnoledgeBase(models.Model):
    business_ID        = models.CharField(default ='None' ,max_length=40)
    branch_ID          = models.CharField(max_length = 50,default='none')
    article_ID         = models.CharField(default ='None' ,max_length=40)
    tittle             = models.TextField(default ='None' ,max_length=5000)
    description        = models.TextField(default ='None' ,max_length=5000)
    mediafile          = models.FileField(upload_to='files/%Y/%m/%d/',null=True,blank=True)
    author             = models.CharField(default ='None' ,max_length=500)
    category           = models.CharField(default ='None' ,max_length=500)
    date               = models.DateTimeField(default = timezone.now)

class BusinessBranch(models.Model):
    business_ID         = models.CharField(default ='None' ,max_length=40)
    branch_ID           = models.CharField(default ='None' ,max_length=40)
    branch_name         = models.CharField(default ='None' ,max_length=40)
    branch_phone        = models.TextField(default ='None' ,max_length=5000)
    other_phone         = models.CharField(max_length = 50,default="")
    extra_phone         = models.CharField(max_length = 50,default="")
    email               = models.CharField(max_length = 50,default="")
    branch_city         = models.CharField(default ='None' ,max_length=40)
    branch_adress       = models.TextField(default ='None' ,max_length=500)
    longitude           = models.CharField(default ='None' ,max_length=500)
    latitude            = models.CharField(default ='None' ,max_length=500)


# ----- Accounts Manager / admin Models ------ #

class CountryCodes(models.Model):
    country               = models.CharField(max_length=5000)
    Country_code          = models.CharField(max_length=5000)
    International_dialing = models.CharField(max_length=5000)
    
    class Meta:
        db_table ="app_countrycodes"



class Plan(models.Model):
    BUSINESS_PLAN = (
   ('ecommerce', 'ecommerce'),
   ('proffessional', 'proffessional'),
    
)


    Plan_ID           = models.CharField(max_length=5000)
    business_plan     = models.CharField(
                                 choices     = BUSINESS_PLAN,
                                 default     ='ecommerce',
                                 max_length=30)
    Plan_Name     = models.CharField(
                                 choices     = PLAN_CATEGORY,
                                 default     ='BASIC',
                                 max_length=30)
    Price         = models.DecimalField(max_digits=10, decimal_places=2,default=0)
    


class ProofOfPayment(models.Model):
    
    business_ID      = models.CharField(max_length=500,default='none')
    Business_Name    = models.CharField(max_length=40)
    accountnumber    = models.CharField(max_length=400,default='none')
    bankname         = models.CharField(default ='None' ,max_length=400)
    amount           = models.CharField(default ='0' ,max_length=40)
    currency         = models.CharField(default ='USD' ,max_length=400)
    date             = models.CharField(default ='None' ,max_length=40)
    refference       = models.CharField(default ='None' ,max_length=40)
    cardName         = models.CharField(default ='None' ,max_length=40)
    Invoice_ID       = models.CharField(default ='None' ,max_length=40)
    billingCycle     = models.CharField(default ='None' ,max_length=40)
    verified_by      = models.CharField(default ='None' ,max_length=400)
    verified_status  = models.BooleanField(default=False)
    approved_status  = models.BooleanField(default=False)


class BillingAccountNotification(models.Model):
    Business_Name           = models.CharField(max_length=500,default='none')
    business_ID             = models.CharField(max_length=40,default='none')
    accountType             = models.CharField(
                                choices=STATUS_CHOICES,
                                default='PENDING',
                                max_length=30)
    single_viewed_status    = models.BooleanField(default=False)
    viewed_status           = models.BooleanField(default=False)
    

class BillingInvoice(models.Model):
    business_ID      = models.CharField(max_length = 50,default='none')
    Business_Name    = models.CharField(max_length=500,default='none')
    Plan_Name        = models.CharField(
                                 choices  = PLAN_CATEGORY,
                                 default  = 'BASIC',
                                 max_length=30)
    Invoice_ID       = models.CharField(max_length=40)
    payment_method   = models.CharField(max_length=40,default='none')
    amount           = models.CharField(default ='PackageNone' ,max_length=40)
    date             = models.DateTimeField(default = timezone.now)
    due_date         = models.DateTimeField(default = timezone.now)
    invoice_status   = models.CharField(
                        choices=STATUS_CHOICES,
                        default='PENDING',
                        max_length=30)
    reminder         = models.IntegerField(default=0)
    def __str__(self):
        return self.business_ID




class Transaction(models.Model):
    business_ID      = models.CharField(max_length = 50,default='none')
    Business_Name    = models.CharField(max_length=500,default='none')
    Plan_Name        = models.CharField(
                                 choices  = PLAN_CATEGORY,
                                 default  = 'BASIC',
                                 max_length=30)
    Invoice_ID       = models.CharField(max_length=40)
    payment_method   = models.CharField(max_length=40,default='none')
    amount           = models.CharField(default ='PackageNone' ,max_length=40)
    date             = models.DateTimeField(default = timezone.now)
   
    
    def __str__(self):
        return self.business_ID

class AccountUpgrade(models.Model):
    
    business_ID            = models.CharField(max_length=500,default='none')
    Business_Name          = models.CharField(max_length=40)
    current_Plan           = models.CharField(max_length=400,default='none')
    current_Plan_Id        = models.CharField(default ='None' ,max_length=400)
    current_monthly_amount = models.CharField(default ='0' ,max_length=40)
    Plan_upgrade_to        = models.CharField(default ='USD' ,max_length=400)
    price                  = models.CharField(default ='0' ,max_length=40)
    Plan_upgrade_Id        = models.CharField(default ='USD' ,max_length=400)
    date                   = models.DateTimeField(default = timezone.now)
    approved_status        = models.BooleanField(default=False)



USE_CASE = (
    ('E-Commerce', 'E-Commerce'),
    ('Automotive', 'Automotive'),
    ('Finance & Insurance', 'Finance & Insurance'),
    ('Beauty & Wellness','Beauty & Wellness'),
     
     ('Driving School', 'Driving School'),
    ('Dentist', 'Dentist'),
    ('Agricultural Services', 'Agricultural Services'),
    ('Car Rental','Car Rental'),

    ('Food Ordering', 'Food Ordering'),
    ('Banking', 'Banking'),
    ('Education', 'Education')
    


)
   
class UseCase(models.Model):
    usecase                    = models.CharField(
                                choices=USE_CASE,
                                default='PENDING',
                                max_length=30)
    tittle                     = models.CharField(default ='' ,max_length=50)
    banner_image               = models.FileField(upload_to='files/%Y/%m/%d/',null=True,blank=True)
    paragraph_1                = models.TextField(default ='None' ,max_length=5000)
    paragraph_2_tittle         = models.TextField(default ='None' ,max_length=500)
    paragraph_2_description_1  = models.TextField(default ='None' ,max_length=5000)
    paragraph_2_description_2  = models.TextField(default ='None' ,max_length=5000)
    paragraph_2_image_1        = models.FileField(upload_to='files/%Y/%m/%d/',null=True,blank=True)
    paragraph_2_image_2        = models.FileField(upload_to='files/%Y/%m/%d/',null=True,blank=True)
    paragraph_3_tittle         = models.TextField(default ='None' ,max_length=500)
    paragraph_3_description    = models.TextField(default ='None' ,max_length=5000)
    paragraph_3_image          = models.FileField(upload_to='files/%Y/%m/%d/',null=True,blank=True)
    paragraph_4_tittle         = models.TextField(default ='None' ,max_length=500)
    paragraph_4_description    = models.TextField(default ='None' ,max_length=5000)




FEATURE = (
    ('Whatsapp Chatbot', 'Whatsapp Chatbot'),
    ('Team Inbox', 'Team Inbox'),
    ('Help Center', 'Help Center'),
    ('Manage Orders','Manage Orders'),
     
    ('Contact Manager', 'Contact Manager'),
    ('KnoWledge Base', 'KnoWledge Base'),
    ('Events & Booking', 'Events & Booking'),
    ('Catalouge','Catalouge'),

    ('Promotions & Coupons', 'Promotions & Coupons'),
    ('Live Translation', 'Live Translation'),
    
    


)

class ProductFeature(models.Model):
    feature                    = models.CharField(
                                choices=FEATURE,
                                default='Whatsapp Chatbot',
                                max_length=30)
    tittle_tag_1               = models.CharField(default ='' ,max_length=50)
    tittle_section_1           = models.CharField(default ='' ,max_length=50)
    image_section_1            = models.FileField(upload_to='files/%Y/%m/%d/',null=True,blank=True)
    description_section_1      = models.TextField(default ='None' ,max_length=5000)
    
    tittle_tag_2               = models.CharField(default ='' ,max_length=50)
    tittle_section_2           = models.CharField(default ='' ,max_length=50)
    description_section_2      = models.TextField(default ='None' ,max_length=5000)
    image_section_2            = models.FileField(upload_to='files/%Y/%m/%d/',null=True,blank=True)

    
    tittle_section_3           = models.CharField(default ='' ,max_length=50)
    description_section_3      = models.TextField(default ='None' ,max_length=5000)
    tittle2_section_3          = models.CharField(default ='' ,max_length=50)
    description2_section_3     = models.TextField(default ='None' ,max_length=5000)

    tittle_tag_4               = models.CharField(default ='' ,max_length=50)
    tittle_section_4           = models.CharField(default ='' ,max_length=50)
    image_section_4            = models.FileField(upload_to='files/%Y/%m/%d/',null=True,blank=True)
    description_section_4      = models.TextField(default ='None' ,max_length=5000)

    tittle_1_section_5         = models.CharField(default ='' ,max_length=50)
    description_1_section_5    = models.TextField(default ='None' ,max_length=5000)

    tittle_2_section_5         = models.CharField(default ='' ,max_length=50)
    description_2_section_5    = models.TextField(default ='None' ,max_length=5000)

    tittle_3_section_5         = models.CharField(default ='' ,max_length=50)
    description_3_section_5    = models.TextField(default ='None' ,max_length=5000)

    tittle_4_section_5         = models.CharField(default ='' ,max_length=50)
    description_4_section_5    = models.TextField(default ='None' ,max_length=5000)


    
    image_section_5            = models.FileField(upload_to='files/%Y/%m/%d/',null=True,blank=True)

class Testimonial(models.Model):
    
    customerName               = models.CharField(default ='' ,max_length=500)
    company                    = models.TextField(default ='None' ,max_length=500)
    profile_picture            = models.FileField(upload_to='files/%Y/%m/%d/',null=True,blank=True)
    testimony                  = models.TextField(default ='None' ,max_length=5000)


class CompanyCustomer(models.Model):
    
    CompanyName               = models.CharField(default ='' ,max_length=500)
    companyLogo               = models.FileField(upload_to='files/%Y/%m/%d/',null=True,blank=True)

   


class Faq(models.Model):
    
    question                   = models.TextField(default ='None' ,max_length=5000)
    answer                     = models.TextField(default ='None' ,max_length=5000)
    


class Integration(models.Model):
    
    CompanyName               = models.CharField(default ='' ,max_length=500)
    companyLogo               = models.FileField(upload_to='files/%Y/%m/%d/',null=True,blank=True)
    description               = models.TextField(default ='None' ,max_length=500)




class CustomerEmails(models.Model):
    email       = models.CharField(default ='' ,max_length=500)
    date        = models.DateTimeField(default = timezone.now)
    








class Navigator(models.Model):
    customer_ID   = models.CharField(max_length = 50,default='none')
    business_ID   = models.CharField(max_length = 50,default='none')
    current_page  = models.CharField(max_length = 50,default='none')
    phone         = models.CharField(max_length = 50,default="s-00")
    dateadded     = models.DateTimeField(default = timezone.now)
    
    
    def __str__(self):
      return self.phone



class ListNavigator(models.Model):
    customer_ID   = models.CharField(max_length = 50,default='none')
    business_ID   = models.CharField(max_length = 50,default='none')
    current_item  = models.CharField(max_length = 50,default='none')
    phone         = models.CharField(max_length = 50,default="s-00")
    dateadded     = models.DateTimeField(default = timezone.now)
    
    
    def __str__(self):
      return self.phone
