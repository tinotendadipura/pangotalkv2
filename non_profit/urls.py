from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import logout
from django.contrib.auth import views as auth_views
from . import views 

    

urlpatterns = [
     path('main/home/dashboard/non-profit',views.main_dashboard,name="main/home/dashboard/non-profit"),
     path('main/home/non-profit/layer',views.non_profit_layer,name="main/home/non-profit/layer"),
     path('main/home/non-profit/add-account-user',views.non_profit_layer,name="main/home/non-profit/add-account-user"),
     path('main/home/non-profit/all-account-user',views.non_profit_layer,name="main/home/non-profit/all-account-user"),
     path('user/non-profit/account/profile/change/password',views.change_password,name="user/non-profit/account/profile/change/password"),
     # Our Partners
     path('main/non-profit/All-Partners',views.all_partners,name="main/non-profit/All-Partners"),
     path('main/non-profit/partner-requests',views.partner_requests,name="main/non-profit/partner-requests"),
     path('main/non-profit/add-partner',views.add_partner,name="main/non-profit/add-partner"),

     # User Manager 
     path('main/non-profit/add-user',views.addUser,name="main/non-profit/add-user"),
     path('main/non-profit/all-users',views.allUser,name="main/non-profit/all-users"),

      
     # Members 
     path('main/non-profit/add/account/members',views.add_member,name="main/non-profit/add/account/members"),
     path('main/non-profit/account/all-members',views.all_members,name="main/non-profit/account/all-members"),

     #  Community
     path('main/non-profit/account/create_forum/topic',views.create_forum_topic,name="main/non-profit/account/create_forum/topic"),
     path('main/non-profit/account/forum',views.forum_topic_list,name="main/non-profit/account/forum"),
     path('main/non-profit/account/forum-topic-detail/open/<str:topic_ID>',views.forum_topic_detail,name="main/non-profit/account/forum-topic-detail/open"),
     path('main/non-profit/account/forum/detail/<str:postID>',views.forum_detail,name="main/account/forum/detail"),
     path('main/non-profit/account/forum/delete/<str:topic_ID>',views.delete_forum,name="main/non-profit/account/forum/delete"),
     
      # Our Projects
      path('main/account/non-profit/Work-and-impact',views.work_and_impact,name="main/account/non-profit/Work-and-impact"),
      path('main/account/non-profit/Work-and-impact/project/<str:project_ID>',views.work_and_impact_detail,name="main/account/non-profit/Work-and-impact/project"),
      path('main/account/non-profit/Work-and-impact/project/media-delete/<int:id>/<str:project_ID>',views.delete_project_media,name="main/account/non-profit/Work-and-impact/project/media-delete"),
      path('main/account/non-profit/Work-and-impact/project/delete/<str:project_ID>',views.delete_project,name="main/account/non-profit/Work-and-impact/project/delete"),
      
      # Events
      path('main/account/non-profit/events/publish-event',views.publishEvent,name="main/account/non-profit/events/publish-event"),
      path('main/account/non-profit/events/all-events',views.allEvents,name="main/account/non-profit/events/all-events"),
      path('main/account/non-profit/events/edit-event/<str:EventID>',views.editEvent,name="main/account/non-profit/events/edit-event"),
      path('main/account/non-profit/all-events/bookings',views.eventsBookings,name="main/account/non-profit/all-events/bookings"),
      path('main/account/non-profit/events/delete/<str:EventID>',views.deleteEvent,name="main/account/non-profit/events/delete"),
      path('main/account/non-profit/events/booking/delete/<str:booking_ID>',views.deletebooking,name="main/account/non-profit/events/booking/delete"),
    


       # Knowledge Hub
       path('main/account/non-profit/knowledge_hub',views.knowledge_hub,name="main/account/non-profit/knowledge_hub"),
       path('main/account/non-profit/knowledge_hub/details/info/<str:topic_ID>',views.knowledge_hub_detail,name="main/account/non-profit/knowledge_hub/details/info"),
       path('main/account/non-profit/knowledge_hub/details/info/delete/topic/<str:topic_ID>',views.delete_topic,name="main/account/non-profit/knowledge_hub/details/info/delete/topic"),
       path('main/account/non-profit/knowledge_hub/details/info/delete/topic-media/<int:id>/<str:topic_ID>',views.delete_media,name="main/account/non-profit/knowledge_hub/details/info/delete/topic-media"),
        path('main/account/non-profit/knowledge_hub/details/info/edit/topic/<str:topic_ID>',views.edit_topic,name="main/account/non-profit/knowledge_hub/details/info/edit/topic"),
       
       # FeedBack 

       path('manage/non-profit/member/feedback',views.customer_feedback,name="manage/non-profit/member/feedback"),
       path('manage/non-profit/member/account/feedback/<str:customer_ID>',views.customer_feedback_details,name="manage/non-profit/member/account/feedback"),
    

       # FAQs
       path('account/non-profit/faqs',views.faqs,name="account/non-profit/faqs"),
       path('account/non-profit/faqs/answers/<str:question_ID>',views.faqs_answers,name="account/non-profit/faqs/answers"),
       path('account/non-profit/faqs/answers/delete/<str:question_ID>/<int:id>',views.delete_answer,name="account/non-profit/faqs/answers/delete"),
       path('account/non-profit/faqs/question/delete/<str:question_ID>',views.delete_question,name="account/non-profit/faqs/question/delete"),

       # Settings Accounts

          path('account/non-profit/settings',views.my_settings,name="account/non-profit/settings"),
          path('account/non-profit/billing-plan',views.billing_plan,name="account/non-profit/billing-plan"),
          path('account/non-profit/billing-invoices',views.billing_invoices,name="account/non-profit/billing-invoices"),
          path('account/non-profit/billing-invoices/invoice-detail/<str:invoice_ID>',views.invoices_detail,name="account/non-profit/billing-invoices/invoice-detail"),
          
          path('account/non-profit/disk-manager',views.diskspace,name="account/non-profit/disk-manager"),
          path('account/non-profit/message-balance',views.message_balance,name="account/non-profit/message-balance"),
          



]