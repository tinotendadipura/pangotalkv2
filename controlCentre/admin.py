from django.contrib import admin

# Register your models here.
from .models import ApiCofig ,SchoolPortalImage, InstanceImage, BillingManager



class ApiCofigAdmin(admin.ModelAdmin):
    list_display = ('school_Name' ,
                    'school_ID' ,
                    'apiUrl1' ,
                    'apiUrl2' ,
                    'date' ,
                    'update' ,
                    'account_active_status',
                    'setup_ready'
                    )
    
    list_per_page = 10
    
admin.site.register(ApiCofig ,ApiCofigAdmin)


class BillingManagerAdmin(admin.ModelAdmin):
    list_display = (
                    'business_ID',
                    'business_Name',
                    'emailCounter',
                    'Price',
                    'suspend_status',
                    'first_billing_date',
                    'second_billing_date',
                    'third_billing_date',
                    'forth_billing_date',
                    'account_suspension_date',
                                    )
    
    list_per_page = 10
    
admin.site.register(BillingManager,BillingManagerAdmin)




class InstanceImagedmin(admin.ModelAdmin):
    list_display = (
                    'Instance_ID',          
                    'Instance_IP',          
                    'instanceUser',          
                    'instancePassword',     
                    'SSH_Key',             
                    'assinged_status',       
                    'portal_installed',      
                    'created_date',          

                    )
    
    list_per_page = 10
    
admin.site.register(InstanceImage ,InstanceImagedmin)





class SchoolPortalImageAdmin(admin.ModelAdmin):
    list_display = (
       
    'Instance_ID',                   
    'Instance_IP',                  
    'School_name',                
    'school_ID',                    
    'Port',                         
    'Instance_assinged_status',     
    'BillingAccount_active_status',  
    'config_date'                 

       
       )
    
    list_per_page = 10
    
admin.site.register(SchoolPortalImage ,SchoolPortalImageAdmin)
