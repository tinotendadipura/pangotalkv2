
from django.template.loader import get_template
from django.core.mail import EmailMessage
from django.conf import settings
from .models import ( BusinessProfile,
    Invite)








class InviteEmail():
    def invite_email_manager(self,email,invite_link,invite_id):
        print("it worked")
        try:
            invite_info=Invite.objects.get(invite_ID=invite_id)
            business_info=BusinessProfile.objects.get(business_ID = invite_info.business_ID )
            html_tpl_path = 'emails/admin_user_email.html'
            context_data = {'business_info':business_info,
                            'invite_info':invite_info,
                            'invite_link':invite_link
                            }
            email_html_template = get_template(html_tpl_path).render(context_data)
            receiver_email = email

            mssg = EmailMessage(
                'You have been invited to join pangotalk.com.',
                 email_html_template, 
                 settings.APPLICATION_EMAIL,
                 [receiver_email],
                 reply_to=[settings.APPLICATION_EMAIL]
            )
            mssg.content_subtype ="html"
            mssg.send(fail_silently=False)
        except Exception as exp:
                print(exp)
    



    
    

# class BillingEmail():
#     def paid_invoice(self,invoiveid,school_id):
#         print("it worked")
#         try:
            
#             html_tpl_path = 'emails/paid-invoice.html'
#             detail_invoice       = BillingInvoice.objects.get(invoiceId = invoiveid)
#             school_profile       = SchoolProfile.objects.get(school_ID = school_id)
#             billing_account      = BillingAccount.objects.get(school_ID = school_id)
#             features             = Features.objects.filter(user_class_member = detail_invoice.membership_id)
            
#             user_membership_qs = UserMembership.objects.filter(school_ID = detail_invoice.school_ID)
#             user_membership = user_membership_qs.first()
#             price = user_membership.membership.price

#             context_data = {"price":price,
#                             "detail_invoice":detail_invoice,
#                             "billing_account":billing_account,
#                             "features":features,
#                             "school_profile":school_profile
#                            }
#             email_html_template = get_template(html_tpl_path).render(context_data)
#             receiver_email =  school_profile.email

#             mssg = EmailMessage(
#                 'Paid Invoice',
#                  email_html_template, 
#                  settings.APPLICATION_EMAIL,
#                  [receiver_email],
#                  reply_to=[settings.APPLICATION_EMAIL]
#             )
#             mssg.content_subtype ="html"
#             mssg.send(fail_silently=False)
#         except Exception as exp:
#                 print(exp)



#     def pending_invoice(self,invoiveid,school_id):
#             print("it worked")
#             try:
#                 html_tpl_path = 'emails/paid-invoice.html'
#                 detail_invoice       = BillingInvoice.objects.get(invoiceId = invoiveid)
#                 school_profile       = SchoolProfile.objects.get(school_ID = school_id)
#                 billing_account      = BillingAccount.objects.get(school_ID = school_id)
#                 features             = Features.objects.filter(user_class_member = detail_invoice.membership_id)
            
#                 user_membership_qs = UserMembership.objects.filter(school_ID = detail_invoice.school_ID)
#                 user_membership = user_membership_qs.first()
#                 price = user_membership.membership.price

#                 context_data = {"price":price,
#                             "detail_invoice":detail_invoice,
#                             "billing_account":billing_account,
#                             "features":features,
#                             "school_profile":school_profile
#                            }
#                 email_html_template = get_template(html_tpl_path).render(context_data)
#                 receiver_email = school_profile.email

#                 mssg = EmailMessage(
#                     'Pending Invoice',
#                     email_html_template, 
#                     settings.APPLICATION_EMAIL,
#                     [receiver_email],
#                     reply_to=[settings.APPLICATION_EMAIL]
#                 )
#                 mssg.content_subtype ="html"
#                 mssg.send(fail_silently=False)
#             except Exception as exp:
#                     print(exp)

    
#     def cancelled_invoice(self,invoiveid,school_id):
#                 print("it worked")
#                 try:
#                     html_tpl_path = 'emails/paid-invoice.html'
#                     detail_invoice       = BillingInvoice.objects.get(invoiceId = invoiveid)
#                     school_profile       = SchoolProfile.objects.get(school_ID = school_id)
#                     billing_account      = BillingAccount.objects.get(school_ID = school_id)
#                     features             = Features.objects.filter(user_class_member = detail_invoice.membership_id)
            
#                     user_membership_qs = UserMembership.objects.filter(school_ID = detail_invoice.school_ID)
#                     user_membership = user_membership_qs.first()
#                     price = user_membership.membership.price

#                     context_data = {"price":price,
#                                 "detail_invoice":detail_invoice,
#                                 "billing_account":billing_account,
#                                 "features":features,
#                                 "school_profile":school_profile
#                             }
#                     email_html_template = get_template(html_tpl_path).render(context_data)
#                     receiver_email =  school_profile.email

#                     mssg = EmailMessage(
#                         'Cancelled Invoice',
#                         email_html_template, 
#                         settings.APPLICATION_EMAIL,
#                         [receiver_email],
#                         reply_to=[settings.APPLICATION_EMAIL]
#                     )
#                     mssg.content_subtype ="html"
#                     mssg.send(fail_silently=False)
#                 except Exception as exp:
#                         print(exp)



#     def overdue_invoice(self,email,invite_link,invite_id):
#                 print("it worked")
#                 try:
#                     user_info=AllUsers.objects.get(invite_ID=invite_id)
#                     html_tpl_path = 'emails/paid-invoice.html'
#                     context_data = {'user_info':user_info,
#                                     'invite_link':invite_link
#                                     }
#                     email_html_template = get_template(html_tpl_path).render(context_data)
#                     receiver_email = email

#                     mssg = EmailMessage(
#                         'Overdue invoice',
#                         email_html_template, 
#                         settings.APPLICATION_EMAIL,
#                         [receiver_email],
#                         reply_to=[settings.APPLICATION_EMAIL]
#                     )
#                     mssg.content_subtype ="html"
#                     mssg.send(fail_silently=False)
#                 except Exception as exp:
#                         print(exp)



           