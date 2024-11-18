from django.contrib import admin
from django.contrib.auth.models import Group
from . models import (

    ChatMessage,
    
    AddNote,
    CustomerMedia
)





class  ChatMessageAdmin(admin.ModelAdmin):
    list_display = (
    'supportAgent',  
    'userName',     
    'country',      
    'message',      
    'phone',         
    'dateadded',     
    'supportMessage',
    )
    
    list_per_page = 10
    search_fields = (
    'supportAgent',  
    'userName',     
    'country',      
    'message',      
    'phone',         
    'dateadded',     
    'supportMessage',
        ) 
    
admin.site.register(ChatMessage , ChatMessageAdmin)


class  CustomerMediaAdmin(admin.ModelAdmin):
    list_display = (
     'customer_ID',  
     'branch_ID',    
     'business_ID',   
     'message_ID',   
     'media_file',    
     'media_file_url', 
     'media_type',     
     
    )
    
    list_per_page = 10
    search_fields = (
     'customer_ID',  
     'branch_ID',    
     'business_ID',   
     'message_ID',   
     'media_file',    
     'media_file_url', 
     'media_type',     
      
        ) 
    
admin.site.register(CustomerMedia , CustomerMediaAdmin)



class  AddNoteAdmin(admin.ModelAdmin):
    list_display = (
    'customer_ID',
    'business_ID',
    'supportAgent_ID',
    'supportAgent',
    'addNoteName',
    'addNoteDetails',
    'Notetag',
    'dateadded',
    )
    
    list_per_page = 10
    search_fields = (
    'customer_ID',
    'business_ID',
    'supportAgent_ID',
    'supportAgent',
    'addNoteName',
    'addNoteDetails',
    'Notetag',
    'dateadded',
        ) 
    
admin.site.register(AddNote , AddNoteAdmin)





