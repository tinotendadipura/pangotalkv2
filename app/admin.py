from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from django.contrib.auth.models import Group
from . models import (UserProfile,BusinessProfile,ProductListing,
ProofOfPayment,BillingInvoice,BillingAccountNotification,
ContactCard,ProductListingImages,Visitors,Invite,InvoiceGenerator
,BusinessBranch,Plan,Customer,Order,Booking,EventBooking,
Event,KnoledgeBase,ProductCategory,CountryCodes,Coupon,
CouponClaim, MediaType,PlanPackage,Testimonial,
ProductFeature,UseCase,Integration,DiskManager,OrderNotification,AccountUpgrade,
BusinessConfiguration,Transaction,OrderGroup,BannerImage,Feedback,FeedbackCount,CustomerEmails,Client,Domain,
Navigator,
    ListNavigator,
)






class ClientAdmin(admin.ModelAdmin):
    list_display = ( 

    'name',
   
       
    )
list_per_page = 10
    
admin.site.register(Client ,ClientAdmin)


class DomainAdmin(admin.ModelAdmin):
    list_display = ( 

    'domain',
    
       
    )
list_per_page = 10
    
admin.site.register(Domain ,DomainAdmin)



class BannerImageAdmin(admin.ModelAdmin):
    list_display = ( 

    'business_ID',
    'BusinessName',
    'banner_image'
            
    )
list_per_page = 10
    
admin.site.register(BannerImage ,BannerImageAdmin)



class FeedbackAdmin(admin.ModelAdmin):
    list_display = ( 

    'customerName',
    'phoneNumber',
    'feedback',
    'dateadded',
            
    )
list_per_page = 10
    
admin.site.register(Feedback ,FeedbackAdmin)


class FeedbackCountAdmin(admin.ModelAdmin):
    list_display = ( 

    'business_ID',
    'current_feedback',
    
            
    )
list_per_page = 10
    
admin.site.register(FeedbackCount ,FeedbackCountAdmin)



class BusinessConfigurationAdmin(admin.ModelAdmin):
    list_display = ( 

    'BusinessName',      
    'business_ID',       
                
       
    'bot_endpoint',     
    'bot_name',         
          
                
    )
    
    list_per_page = 10
    
admin.site.register(BusinessConfiguration ,BusinessConfigurationAdmin)




class AccountUpgradeAdmin(admin.ModelAdmin):
    list_display = ( 

    'business_ID',          
    'Business_Name',      
    'current_Plan',         
    'current_Plan_Id',    
    'current_monthly_amount', 
    'Plan_upgrade_to',      
    'Plan_upgrade_Id',     
    'date',                  
    'approved_status'     
                    
    )
    
    list_per_page = 10
    
admin.site.register(AccountUpgrade ,AccountUpgradeAdmin)





class OrderNotificationAdmin(admin.ModelAdmin):
    list_display = ( 

    'business_ID',    
    'order_counter', 
                    
    )
    
    list_per_page = 10
    
admin.site.register(OrderNotification ,OrderNotificationAdmin)

class IntegrationAdmin(admin.ModelAdmin):
    list_display = ( 

    'CompanyName',    
    'companyLogo', 
    'description',                   
           
          
    
    )
    
    list_per_page = 10
    
admin.site.register(Integration ,IntegrationAdmin)


class DiskManagerAdmin(admin.ModelAdmin):
    list_display = ( 

    'BusinessName', 
    'business_ID',  
    'disk_space',   
    )
    
    list_per_page = 10
    
admin.site.register(DiskManager ,DiskManagerAdmin)


class UseCaseAdmin(admin.ModelAdmin):
    list_display = ( 

    'usecase',    
    'tittle',                    
    'banner_image',              
    'paragraph_1',                
    'paragraph_2_tittle'         
          
    
    )
    
    list_per_page = 10
    
admin.site.register(UseCase ,UseCaseAdmin)



class ProductFeatureAdmin(admin.ModelAdmin):
    list_display = ( 

   'feature',
    'tittle_tag_1',
    'tittle_section_1',
    'image_section_1',
    'description_section_1',

          
    
    )
    
    list_per_page = 10
    
admin.site.register(ProductFeature ,ProductFeatureAdmin)


class TestimonialAdmin(admin.ModelAdmin):
    list_display = ( 

    'customerName',
    'company',
    'profile_picture',
    'testimony',
          
    
    )
    
    list_per_page = 10
    
admin.site.register(Testimonial ,TestimonialAdmin)



class BillingAccountNotificationAdmin(admin.ModelAdmin):
    list_display = ( 

    'Business_Name',  
    'business_ID',            
    'accountType',             
    'single_viewed_status',    
    'viewed_status'           
    
                    )
    
    list_per_page = 10
    
admin.site.register(BillingAccountNotification ,BillingAccountNotificationAdmin)




class PlanPackageAdmin(admin.ModelAdmin):
    list_display = ( 

    'PlanName',    
    'PlanItemName', 
    'PlanItemQuantity',    
    'dateadded',   
           
    
                    )
    
    list_per_page = 10
    
admin.site.register(PlanPackage ,PlanPackageAdmin)




class ProofOfPaymentAdmin(admin.ModelAdmin):
    list_display = ( 

    'Business_Name',     
    'accountnumber',   
    'bankname',         
    'amount',           
    'currency',
    'billingCycle',        
    'date',           
    'refference',       
    'cardName',       
    'Invoice_ID',      
    'verified_by',      
    'verified_status',  
    'approved_status',       
    
                    )
    
    list_per_page = 10
    
admin.site.register(ProofOfPayment ,ProofOfPaymentAdmin)


class BillingInvoiceAdmin(admin.ModelAdmin):
    list_display = ( 'business_ID',
                    'Business_Name',
                    'Invoice_ID',
                    'payment_method',
                    'amount',
                    'date',
                    'due_date',
                    'invoice_status'
                    )
    
    list_per_page = 10
    
admin.site.register(BillingInvoice ,BillingInvoiceAdmin)



class TransactionAdmin(admin.ModelAdmin):
    list_display = ( 'business_ID',
                    'Business_Name',
                    'Invoice_ID',
                    'payment_method',
                    'amount',
                    'date',
                    
                    )
    
    list_per_page = 10
    
admin.site.register(Transaction ,TransactionAdmin)



@admin.register(CountryCodes)
class ExcelUpload(ImportExportModelAdmin):
     pass
admin.register(CountryCodes)


class  UserProfileAdmin(admin.ModelAdmin):
    list_display = (
    'firstName',
    'last_Name',
    'home_adress',
    'city',
    'country',
    'phone',
    'dateadded',
    'form_completed',
    )
    
    list_per_page = 10
    search_fields = (
    'firstName',
    'last_Name',
    'home_adress',
    'city',
    'country',
    'phone',
    'dateadded',
    'form_completed',
        ) 
    
admin.site.register( UserProfile , UserProfileAdmin)



class  ProductCategoryAdmin(admin.ModelAdmin):
    list_display = (
    'business_ID',  
    'category',  
      
    )
    
    list_per_page = 10
    search_fields = (
    'business_ID',  
    'category',  
      
    ) 
    
admin.site.register(ProductCategory , ProductCategoryAdmin)




class  InviteAdmin(admin.ModelAdmin):
    list_display = (
    'firstName',  
    'last_Name',  
    'email',    
    'role',      
    'phone',      
    'dateadded',   
   
    
    )
    
    list_per_page = 10
    search_fields = (
    'firstName',  
    'last_Name',  
    'email',    
    'role',      
    'phone',      
    'dateadded',   
    ) 
    
admin.site.register(Invite , InviteAdmin)





class  BusinessProfileAdmin(admin.ModelAdmin):
    list_display = (
    'BusinessName',   
    'Business_adress', 
    'street_name', 
    'category',   
    'email',         
    'city',        
    'facebook',       
    'website',       
    'phone',           
    'other_phone',     
    'longitude',     
    'latitude',        
    'form_completed',  
    'dateadded',   

    )
    
    list_per_page = 10
    search_fields = (
    'BusinessName',   
    'Business_adress', 
    'street_name',    
    'email',         
    'city',        
    'facebook',       
    'website',       
    'phone',           
    'other_phone',     
    'longitude',     
    'latitude',        
    'form_completed',  
    'dateadded', 
        ) 
    
admin.site.register(BusinessProfile , BusinessProfileAdmin)







class  ProductListingAdmin(admin.ModelAdmin):
    list_display = (
    'id',
    'title',
    'description',
    'price',
    'compare_price',
    'product_ID',
    'dateadded',
    )
    
    list_per_page = 10
    search_fields = (
    'title',
    'description',
    'price',
    'compare_price',
    'product_ID',
    'dateadded',
        ) 
    
admin.site.register(ProductListing , ProductListingAdmin)





class  ContactCardAdmin(admin.ModelAdmin):
    list_display = (
 
    'city',
    'country',
    'country_code',
    'state',
    'contactcard_ID',
    'type',
    'zip',
    'dateadded',
    )
    
    list_per_page = 10
    search_fields = (
    'city',
    'country',
    'country_code',
    'state',
    'contactcard_ID',
    'type',
    'zip',
    'dateadded',
        ) 
    
admin.site.register(ContactCard , ContactCardAdmin)



class  ProductListingImagesAdmin(admin.ModelAdmin):
    list_display = (
    'business_ID',
    'productimage',
    'product_ID',

    )
    
    list_per_page = 10
    search_fields = (
    'business_ID',
    'productimage',
    'product_ID',
        ) 
    
admin.site.register(ProductListingImages , ProductListingImagesAdmin)




class  VisitorsAdmin(admin.ModelAdmin):
    list_display = (
    'business_ID', 
    'date',          
    'country',       
    'code',         
    'phone',       
    'dateadded',    


    )
    
    list_per_page = 10
    search_fields = (
    'business_ID', 
    'date',          
    'country',       
    'code',         
    'phone',       
    'dateadded', 
        ) 
    
admin.site.register(Visitors , VisitorsAdmin)




class  CustomerAdmin(admin.ModelAdmin):
    list_display = (
    'business_ID',
    'customerName',
    'App_User_Name',
    'location',
    'country',
    'code',
    'phone',
    'dateadded',
    )
    
    list_per_page = 10
    search_fields = (
    'business_ID',
    'customerName',
    'App_User_Name',
    'city',
    'country',
    'code',
    'phone',
    'dateadded',
        ) 
    
admin.site.register(Customer , CustomerAdmin)



class  OrderGroupAdmin(admin.ModelAdmin):
    list_display = (
    'business_ID',
    'customer_ID',
    'customerName',
    'order_ID',
    'total_Amount',
    'payment_Status',
    'phone',
    'lastOrder',
    'orderQuantity',
    'country',
    'refunds',
    'viewed',
    'dateadded',

    )
    
    list_per_page = 10
    search_fields = (
    'business_ID',
    'customer_ID',
    'customerName',
    'order_ID',
    'total_Amount',
    'payment_Status',
    'phone',
    'lastOrder',
    'orderQuantity',
    'country',
    'refunds',
    'viewed',
    'dateadded',
        ) 
    
admin.site.register(OrderGroup , OrderGroupAdmin)





class  OrderAdmin(admin.ModelAdmin):
    list_display = (
    'business_ID',
    'product_ID',
    'order_ID',
    'customerName',
    'customer_ID',
    'Payment_Method',
    'total_Amount',
    'payment_Status',
    'phone',
    'country',
    'dateadded',

    )
    
    list_per_page = 10
    search_fields = (
    'business_ID',
    'product_ID',
    'order_ID',
    'CustomerName',
    'customer_ID',
    'Payment_Method',
    'total_Amount',
    'payment_Status',
    'phone',
    'country',
    'dateadded',
        ) 
    
admin.site.register(Order , OrderAdmin)



class  BookingAdmin(admin.ModelAdmin):
    list_display = (
    'business_ID',
    'booking_ID',
    'tittle',
    'description',
    'bookingimage',
    'quantity',
    'startdate',
    'enddate',

    )
    
    list_per_page = 10
    search_fields = (
    'business_ID',
    'booking_ID',
    'tittle',
    'description',
    'bookingimage',
    'quantity',
    'startdate',
    'enddate',

        ) 
    
admin.site.register(Booking , BookingAdmin)





class  EventBookingAdmin(admin.ModelAdmin):
    list_display = (
    
    'booking_ID',         
    'customerName',       
    'phone_Number',      
    'eventTittle',       
    'date',           
    'eventType',        
    'dateadded',        

    )
    
    list_per_page = 10
    search_fields = (
    'booking_ID',         
    'customerName',       
    'phone_Number',      
    'eventTittle',       
    'date',           
    'eventType',        
    'dateadded', 

        ) 
    
admin.site.register(EventBooking , EventBookingAdmin)




class  CouponAdmin(admin.ModelAdmin):
    list_display = (
    
    'business_ID',        
    'campaignBanner',    
    'campaignName',      
    'couponCode',        
    'percentage',       
    'category',        
    'startfulldate',      
    'startactualdate',  
    'startTime',          
    'endfullDate',        
    'endactuallDate',     
    'startTime',         
    'endTime',          
      

    )
    
    list_per_page = 10
    search_fields = (
    'business_ID',        
    'campaignBanner',    
    'campaignName',      
    'couponCode',        
    'percentage',       
    'category',        
    'startfulldate',      
    'startactualdate',  
    'startTime',          
    'endfullDate',        
    'endactuallDate',     
    'startTime',         
    'endTime',          
      

        ) 
    
admin.site.register(Coupon , CouponAdmin)


class  CouponClaimAdmin(admin.ModelAdmin):
    list_display = (
    'campaignName',     
    'couponCode',        
    'percentage',      
    'category',          
    'minimum_amount',   
    'claim_Name',       
    'claim_Number',      
    'claimed_on',   
    'claimed_status',      
    )
    
    list_per_page = 10
    search_fields = (
    'campaignName',     
    'couponCode',        
    'percentage',      
    'category',          
    'minimum_amount',   
    'claim_Name',       
    'claim_Number',      
    'claimed_on',   
        ) 
    
admin.site.register(CouponClaim ,CouponClaimAdmin)







class  EventAdmin(admin.ModelAdmin):
    list_display = (

    'event_Name',       
    'event_Description', 
    'eventimage',        
    'image_status', 
    'startactualdate',   
         
              


    )
    
    list_per_page = 10
    search_fields = (
    'event_Name',       
    'event_Description', 
    'eventimage',        
    'image_status',    
    

        ) 
    
admin.site.register(Event , EventAdmin)





class  KnoledgeBaseAdmin(admin.ModelAdmin):
    list_display = (
   
    'tittle',
    'mediafile',
    'author',




    )
    
    list_per_page = 10
    search_fields = (
    'tittle',
    'mediafile',
    'author',

        ) 
    
admin.site.register(KnoledgeBase , KnoledgeBaseAdmin)



class  BusinessBranchAdmin(admin.ModelAdmin):
    list_display = (
    'branch_name',       
    'branch_city',      
    'branch_adress',       
    'branch_phone',        
    'longitude',          
    'latitude',        
    )
    
    list_per_page = 10
    search_fields = (
    'branch_name',       
    'branch_city',      
    'branch_adress',       
    'branch_phone',        
    'longitude',          
    'latitude', 

        ) 
    
admin.site.register(BusinessBranch , BusinessBranchAdmin)



class  InvoiceGeneratorAdmin(admin.ModelAdmin):
    list_display = (
   
    'business_ID',       
    'invoice_file',     
    'order_ID',        
    'phone',           




    )
    
    list_per_page = 10
    search_fields = (
    'business_ID',       
    'invoice_file',     
    'order_ID',        
    'phone',           


        ) 
    
admin.site.register(InvoiceGenerator , InvoiceGeneratorAdmin)





class  MediaTypeAdmin(admin.ModelAdmin):
    list_display = (
   
    'media_type',       
    'category',     
       
    )
    
    list_per_page = 10
    search_fields = (
    'media_type',       
    'category',     
        ) 
    
admin.site.register(MediaType , MediaTypeAdmin)




class  PlanAdmin(admin.ModelAdmin):
    list_display = (
   
    'business_plan',       
    'Plan_Name',
    'Price',     
       
    )
    
    list_per_page = 10
    search_fields = (
    'Plan_ID',       
    'Plan_Name',
    'Price',     
        ) 
    
admin.site.register(Plan , PlanAdmin)







class  NavigatorAdmin(admin.ModelAdmin):
    list_display = (
    'current_page',
    'phone',
    'dateadded',
    )
    
    list_per_page = 10
    search_fields = (
    'current_page',
    'phone',
    'dateadded',
        ) 
    
admin.site.register(Navigator , NavigatorAdmin)



class  ListNavigatorAdmin(admin.ModelAdmin):
    list_display = (
    'current_item',
    'phone',
    'dateadded',
    )
    
    list_per_page = 10
    search_fields = (
    'current_item',
    'phone',
    'dateadded',
        ) 
    
admin.site.register(ListNavigator , ListNavigatorAdmin)
