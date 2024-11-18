from django.db.models.query_utils import check_rel_lookup_compatibility

from django.db.models import Q
import uuid
import json
import requests
from django.contrib import messages
from django.utils.timezone import datetime
from django.shortcuts import render , redirect , get_object_or_404
from . emailmanager import InviteEmail
from django.shortcuts import render
from django.http import JsonResponse
from django.template.loader import get_template
from django.core.mail import EmailMessage
from django.conf import settings
from .models import ( BusinessProfile,
    Invite)










class SendInvite():

    

    def invite_email(self,invite_ID,request):
        invite_data = Invite.objects.get(invite_ID = invite_ID)

        try:
            invite_link ="http://localhost:8000/accounts/user-invite/create-account/"+invite_ID
            invite =InviteEmail()
            invite.invite_email_manager(email= invite_data.email,invite_link = invite_link,invite_id = invite_ID)
            messages.success(request, 'Invite Have been  Successfully Sent to  {} '.format(invite_data.email))
            return redirect('accounts/all-users')
                         
        except Exception as exp:
                    print(exp)



    


    