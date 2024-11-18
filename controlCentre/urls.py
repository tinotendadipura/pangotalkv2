from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [

    path('business-manager/admin', views.control_center_dashboard, name='business-manager/admin'),
    path('payments-dashboard', views.payments_dashboard, name='payments-dashboard'),
    path('manager/new-accounts/all', views.new_accounts, name='manager/new-accounts/all'),
    path('manager/verify/business-profile/<str:business_ID>', views.new_accounts_profile, name='manager/verify/business-profile'),
    path('manager/all/verified-business', views.active_accounts, name='manager/all/verified-business'),
    path('manager/accounts/upgrades', views.account_upgrade, name='manager/accounts/upgrades'),
    path('manager/accounts/suspended', views.account_suspended, name='manager/accounts/suspended'),
    path('manager/accounts/business/configurations', views.account_configuration, name='manager/accounts/business/configurations'),

    # ======= Payments ======= #

    path('manager/Bank-payments', views.bank_payments, name='manager/Bank-payments'),
    path('manager/verify/bank-transfer/<str:refference>', views.verify_payment, name='manager/verify/bank-transfer'),
    path('manager/overdue/payments', views.overdue_payments, name='manager/overdue/payments'),
    path('manager/overdue/payments/send/billing-reminder/<str:invoice_id>', views.send_billing_invoice, name='manager/overdue/payments/send/billing-reminder'),
    path('manager/billing/transactions', views.transaction_history, name='manager/billing/transactions'),

    
    
    
]