from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import logout
from django.contrib.auth import views as auth_views
from . import views 




urlpatterns = [
     path('account/user/intro/chat', views.chat_intro, name='account/user/intro/chat'),
     path('account/user/chat/<str:customerID>', views.chat, name='account/user/chat'),
     path('account/user/broadcast-dashboard', views.broadcast_table, name='account/user/broadcast-dashboard'),
     path('account/user/add-notes', views.create_notes, name='account/user/add-notes'),
     path('chat/media/image/<str:customerID>', views.send_image, name='chat/media/image'),
     path('chat/media/video/<str:customerID>', views.send_video, name='chat/media/video'),
     path('chat/media/audio/<str:customerID>', views.send_audio, name='chat/media/audio'),
     path('chat/media/document/<str:customerID>', views.send_document, name='chat/media/document'),
     
]