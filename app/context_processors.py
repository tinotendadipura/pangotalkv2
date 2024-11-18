
from django.contrib import messages
from django.utils.timezone import datetime
from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template
from django.core.mail import send_mail
#from kangaroo.settings import EMAIL_HOST_USER
from pangotalk.settings import EMAIL_HOST
from django.http import JsonResponse
import json
from . models import UserProfile,BusinessProfile
from django.utils import timezone
import uuid
import datetime
import pytz
from datetime import timedelta 
import random
from django.utils import timezone
import random
import json
import requests
from . decorators import user_controller ,allowed_users,form_complete
import uuid




# def businessInfo(request):
#     currentUser = request.user
#     userprofile =  UserProfile.objects.filter(user = currentUser).first()
#     businessInfo = BusinessProfile.objects.filter(business_ID = userprofile.business_ID).first()
#     context = {
#         'businessInfo':businessInfo,
#     }
#     return {'businessInfo':businessInfo}