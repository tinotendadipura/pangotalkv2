from django.contrib import admin
from django.urls import path ,include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LoginView
from django.conf import settings # new
from  django.conf.urls.static import static #new

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('pangotalkAPI.urls')),
    path('', include('app.urls')),
    path('', include('chat.urls')),
    path('', include('controlCentre.urls')),
     path('', include('non_profit.urls')),
    
     
    
]


urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_URL)

from django.conf.urls import handler500

handler500 = 'app.views.custom_500'
admin.site.site_header ='PangoTalk'
admin.site.index_title ='PangoTalk'
admin.site.site_title = 'PangoTalk'

