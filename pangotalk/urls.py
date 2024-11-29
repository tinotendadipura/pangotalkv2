from django.contrib import admin
from django.urls import path ,include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LoginView
from django.conf import settings # new
from  django.conf.urls.static import static #new
from django.conf.urls import handler404, handler500, handler403, handler400

from app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('pangotalkAPI.urls')),
    path('', include('app.urls')),
    path('', include('chat.urls')),
    path('', include('controlCentre.urls')),
     path('', include('non_profit.urls')),
    
     
    
]



handler404 = views.error_404
handler500 = views.error_500

admin.site.site_header ='PangoTalk'
admin.site.index_title ='PangoTalk'
admin.site.site_title = 'PangoTalk'

