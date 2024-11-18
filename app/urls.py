from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import logout
from django.contrib.auth import views as auth_views
from . import views 
from .form import UserPasswordResetForm
    

urlpatterns = [
     path('account/user/business/profile', views.business_profile, name='account/user/business/profile'),
     path('account/user/business/category/business-type', views.business_category, name='account/user/business/category/business-type'),
     path('account/user/business/signup-complete', views.signup_complete, name='account/user/business/signup-complete'),
     path('account/user/business/setting-up-account', views.loading_subdomain_setting_up, name='account/user/business/setting-up-account'),
     path('user/account/profile/change/password',views.change_password,name="user/account/profile/change/password"),
     path('account/user/signup', views.signup, name='account/user/signup'),
     path('accounts/login',views.user_login,name="accounts/login"),
     path('logout', views.logout_view, name='logout'),


    # password - reset
    path('reset-password',
     auth_views.PasswordResetView.as_view(template_name="registration/password_reset.html",form_class=UserPasswordResetForm),
     name='reset_password'),
    
    path('reset_password_sent/',
     auth_views.PasswordResetDoneView.as_view(template_name="registration/password_reset _sent.html"),
     name='password_reset_done'),
    
    path('password_reset_confirm/<uidb64>/<token>', 
    auth_views.PasswordResetConfirmView.as_view(template_name="registration/password_reset_form.html"),
    name='password_reset_confirm'),

    path('reset_password_complete',
     auth_views.PasswordResetCompleteView.as_view(template_name="registration/password_reset_done.html"),
     name='password_reset_complete'),
    
    #================#
    #Home pages
    #================#
    
    path('', views.index, name='index'),
    path('Pricing-Plan', views.pricing_table, name='Pricing-Plan'),
    #path('Contact-Us', views.contuct_us, name='Contact-Us'),
    
    # ============# 
       # Products 
    #=============#
     
    path('whatsapp-chatbot', views.wa_chatbot,name='whatsapp-chatbot'),
    path('team-inbox', views.team_inbox,      name='team-inbox'),
    path('help-center', views.help_center,    name='help-center'),
    path('manage-orders', views.manage_orders,name='manage-orders'),
    path('Contact-manager', views.contacts_manager,name='Contact-manager'),
    path('knoledge-base', views.knoledge_base, name='knoledge-base'),
    path('event-bookings', views.event_booking,name='event-bookings'),
    path('product-catalogue', views.catalogoue,name='product-catalogue'),
    path('promotions-coupons', views.prom_coupons,name='promotions-coupons'),
    path('live-translation', views.live_trans,    name='live-translation'),
    
    # ============== # 
    # Use Cases 
    # ============== #
    path('e-commerce', views.e_comm,name='e-commerce'),
    path('automotive', views.automotive,name='automotive'),
    path('finance-insurance', views.finance_insurance,name='finance-insurance'),
    path('beauty-wellness', views.beauty_wellness,name='beauty-wellness'),
    path('driving-school', views.driving_school,name='driving-school'),
    path('dentist', views.dentist,name='dentist'),
    path('agriculture-services', views.agriculture,name='agriculture-services'),
    path('car-rental', views.car_rental,name='car-rental'),
    path('food-ordering', views.food_ordering,name='food-ordering'),
    path('banking', views.banking,name='banking'),
    path('education', views.education,name='education'),

    # ========== End UseCase =========#

    path('About-Us', views.about_us,name='About-Us'),
    path('integrations', views.integrations,name='integrations'),
    path('pricing-ecommerce-plans', views.ecommerce_price,name='pricing-ecommerce-plans'),
    path('pricing-non-profit-plans', views.non_profit_price,name='pricing-non-profit-plans'),
 
    # ================== #
    # App Dashboard
    # ================== #
    path('home/dashboard',views.home,name="home/dashboard"),
     path('ecomm/dashboard/landing',views.ecomm_dashboard_landing,name="ecomm/dashboard/landing"),
    
    path('home/dashboard/ecomm_layer',views.ecomm_layer,name="home/dashboard/ecomm_layer"),


    path('main/home/dashboard',views.main_dashboard,name="main/home/dashboard"),
    path('accounts/add-user',views.addUser,name="accounts/add-user"),
    path('accounts/user-invite/create-account/<str:invite_ID>',views.inviteForm,name="accounts/user-invite/create-account"),
    path('accounts/all-users',views.allUser,name="accounts/all-users"),
    path('catalog/add-product',views.addProduct,name="catalog/add-product"),
    path('catalog/product/delete/<str:product_ID>',views.deleteproduct,name="catalog/product/delete"),

    path('catalog/all-products',views.allProduct,name="catalog/all-products"),
    path('catalog/add-category',views.addCategory,name="catalog/add-category"),
    path('manage/all-customer',views.all_customers,name="manage/all-customer"),
    path('manage/add-customer',views.add_customers,name="manage/add-customer"),

    path('manage/customer/feedback',views.customer_feedback,name="manage/customer/feedback"),
    path('manage/customer/account/feedback/<str:customer_ID>',views.customer_feedback_details,name="manage/customer/account/feedback"),
    

    
    path('products/orders',views.orders,name="products/orders"),
    path('products/orders/delete/<str:OrderID>',views.deleteOrder,name="products/orders/delete"),
    path('customer/product/orders/<str:customer_number>',views.order_details,name="customer/product/orders"),
    
    path('events/publish-event',views.publishEvent,name="events/publish-event"),
    path('events/all-events',views.allEvents,name="events/all-events"),
    path('events/edit-event/<str:EventID>',views.editEvent,name="events/edit-event"),
    path('events/delete/<str:EventID>',views.deleteEvent,name="events/delete"),
    path('events/all-bookings',views.eventsBookings,name="events/all-bookings"),
    path('events/booking/delete/<str:booking_ID>',views.deletebooking,name="events/booking/delete"),
    
    
    path('promo/customer-coupons',views.createCoupon,name="promo/customer/coupons"),
    path('promo/claimed-coupons',views.claimed_coupon,name="promo/claimed-coupons"),
    path('promo/manage/claimed-coupons/delete/<int:id>',views.delete_claimed_coupon,name="promo/manage/claimed-coupons/delete"),
    path('promo/coupons/use/<str:couponCode>',views.used_coupon,name="promo/coupons/use"),
    path('promo/customer-coupon/delete/<str:OrderID>',views.deleteOrder,name="promo/customer-coupon/delete"),
    


    path('knoledge-base/upload/media',views.knoledge_center,name="knoledge-base/upload/media"),
    path('knoledge-base/all-articles',views.all_articles,name="knoledge-base/all-articles"),

    path('account/settings',views.my_settings,name="account/settings"),
    path('account/add-store',views.store_manager,name="account/add-store"),
    path('account/all-stores',views.all_stores,name="account/all-stores"),
    path('account/billing-plan',views.billing_plan,name="account/billing-plan"),
    path('account/billing-plan/upgrade/<str:plan_ID>',views.account_upgrade,name="account/billing-plan/upgrade"),

    path('account/billing-invoices',views.billing_invoices,name="account/billing-invoices"),
    path('account/billing-invoices/invoice-detail/<str:invoice_ID>',views.invoices_detail,name="account/billing-invoices/invoice-detail"),
    path('account/billing/make-payment/<str:Invoice_ID>',views.PaymentView,name="account/billing/make-payment"),
    path('account/disk-manager',views.diskspace,name="account/disk-manager"),

    path('account/invoice-generator/<str:order_ID>',views.invoice_display,name="account/invoice-generator"),
    path('account/message-balance',views.message_balance,name="account/message-balance"),

    
]