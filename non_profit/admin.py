from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from django.contrib.auth.models import Group
from . models import Forum, Comment,Joined_Forum,Our_Projects,Topic,Category,ProjectMedia,TopicMedia, Partner,Partner_Request,Question,Q_Answer,Question_Category




class ForumAdmin(admin.ModelAdmin):
    list_display = ( 

    
    'topic_status',
    'topic_title',
    'topic_description',
    'total_comments',
    'total_members',
    'dateadded',
       
    )
list_per_page = 10
    
admin.site.register(Forum ,ForumAdmin)






class Joined_ForumAdmin(admin.ModelAdmin):
    list_display = ( 

    
    'member_first_name',
    'member_last_name',
    'mobile_number',
    'dateadded',
       
    )
list_per_page = 10
    
admin.site.register(Joined_Forum ,Joined_ForumAdmin)




class CommentAdmin(admin.ModelAdmin):
    list_display = ( 

   
    'topic_status',
    'member_first_name',
    'member_last_name',
    'member_comment',
    'dateadded', 
       
    )
list_per_page = 10
    
admin.site.register(Comment ,CommentAdmin)



class Our_ProjectsAdmin(admin.ModelAdmin):
    list_display = ( 

   
    'project_tittle',
     'dateadded', 
       
    )
list_per_page = 10
    
admin.site.register(Our_Projects ,Our_ProjectsAdmin)




class ProjectMediaAdmin(admin.ModelAdmin):
    list_display = ( 

   
    'business_ID',
    'project_media',
     'dateadded', 
       
    )
list_per_page = 10
    
admin.site.register(ProjectMedia ,ProjectMediaAdmin)




class TopicAdmin(admin.ModelAdmin):
    list_display = ( 

   
    'topic_tittle',
    'dateadded', 
       
    )
list_per_page = 10
    
admin.site.register(Topic ,TopicAdmin)



class CategoryAdmin(admin.ModelAdmin):
    list_display = ( 

   
    'category',
     
       
    )
list_per_page = 10
    
admin.site.register(Category ,CategoryAdmin)






class TopicMediaAdmin(admin.ModelAdmin):
    list_display = ( 

   'title',
    'media',
    'file_type',
    'file_size',
     'file_extension',
    'dateadded',
     
       
    )
list_per_page = 10
    
admin.site.register(TopicMedia ,TopicMediaAdmin)



class QuestionAdmin(admin.ModelAdmin):
    list_display = ( 

    
    'question',           
    'category',        
    'dateadded',         
   
       
    )
list_per_page = 10
    
admin.site.register(Question ,QuestionAdmin)



class Q_AnswerAdmin(admin.ModelAdmin):
    list_display = ( 

    
    'answer',
    'dateadded', 
    
       
    )
list_per_page = 10
    
admin.site.register(Q_Answer ,Q_AnswerAdmin)


class Question_CategoryAdmin(admin.ModelAdmin):
    list_display = ( 

    
    'category',
    'dateadded',
   
       
    )
list_per_page = 10
    
admin.site.register(Question_Category ,Question_CategoryAdmin)



