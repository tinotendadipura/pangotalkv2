from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
# tenants/urls.py

from django.urls import path

from .views import (
    ProductListingAPIView,ProductListingImagesAPIView,BusinessProfileAPIView,
    ChatMessageCreateAPIView, NavigatorAPIView,CustomerCreateAPIView,UserPageUpdateAPIView,
    ListNavigatorAPIView,UserNavListUpdateAPIView,ProductCategoryAPIView,ProductListingDetailAPIView
    ,OrderCreateAPIView,AllProductAPIView,CustomerOrdersAPIView,AllEventsAPIView,EventDetailAPIView,
    BookEventAPIView,PromoAPIView,PromoDetailAPIView,ClaimCouponAPIView,MyCouponsAPIView,MyOrderDetailAPIView,
    GenerateOrderInvoiceAPIView, BranchAPIView, BranchListingDetailAPIView,KnoledgeBaseAPIView,ResoucesDetailAPIView,
    CustomerSignUpAPIView,CustomerNameUpdateAPIView,CustomerBranchUpdateAPIView,BusinessProfileDetailAPIView,FeedBackCreateAPIView,
    TenantCreateView, LoginAPIView, LogoutAPIView,ForumTopicsAPIView,AllProjectsAPIView,ProjectDetailAPIView ,KnowledgeHubTopicsAPIView,
    AllProjectMediaAPIView,KnowledgeHubDetailsAPIView,OurPartnersAPIView,login_page
    
    
    )






urlpatterns = [

    path('create/', TenantCreateView.as_view(), name='tenant-create'),
    path('login/', LoginAPIView.as_view(), name='login'),
    path('logout/', LogoutAPIView.as_view(), name='logout'),
    path('login-page/', login_page, name='login-page'),  # URL for the login page

    path('nav/tracking', NavigatorAPIView.as_view()),
    path('nav/list-item',ListNavigatorAPIView.as_view()),
    path('signup/customer',CustomerSignUpAPIView.as_view()),
    path('signup/customer/add-user/name',CustomerNameUpdateAPIView.as_view()),
    path('signup/customer/add-user/branch',CustomerBranchUpdateAPIView.as_view()),
    path('product/category',ProductCategoryAPIView.as_view()),
    path('all/products',AllProductAPIView.as_view()),
    path('product/view/detail',ProductListingDetailAPIView.as_view()),
    
    
    path('product/order',OrderCreateAPIView.as_view()),
    path('customer/orders',CustomerOrdersAPIView.as_view()),
    path('my-order/details',MyOrderDetailAPIView.as_view()),
    path('my-order/generate-invoice',GenerateOrderInvoiceAPIView.as_view()),

    path('create/customer', CustomerCreateAPIView.as_view()),
    path('update/user/current_page', UserPageUpdateAPIView.as_view()),
    path('update/user/current_list_item', UserNavListUpdateAPIView.as_view()),
    path('chat/message', ChatMessageCreateAPIView.as_view()),
    path('customer/feedback', FeedBackCreateAPIView.as_view()),
    path('products', ProductListingAPIView.as_view()),
   
    path('all/all-promotions', PromoAPIView.as_view()),
    path('promo/coupon-details', PromoDetailAPIView.as_view()),
    path('promo/claim-coupon', ClaimCouponAPIView.as_view()),
    path('my-coupons', MyCouponsAPIView.as_view()),
   
    path('list/all-event', AllEventsAPIView.as_view()),
    path('event/details', EventDetailAPIView.as_view()),
    path('event/booking', BookEventAPIView.as_view()),
    path('products/media', ProductListingImagesAPIView.as_view()),
    path('business/details', BusinessProfileAPIView.as_view()),
    path('business/info/details', BusinessProfileDetailAPIView.as_view()),
    
    
    path('business/branchs',  BranchAPIView.as_view()),
    path('business/branchs/detail', BranchListingDetailAPIView.as_view()),
    
    path('business/knoledge-base', KnoledgeBaseAPIView.as_view()),
    path('resource/detail-info', ResoucesDetailAPIView.as_view()),
    

    # ======================= None Profit ================================ #
    
    path('all/forum-topics', ForumTopicsAPIView.as_view()),
    path('all-project', AllProjectsAPIView.as_view()),
     path('project/info/details', ProjectDetailAPIView.as_view()),
    path('project/info/media', AllProjectMediaAPIView.as_view()),
    path('knowledgehub/topics',KnowledgeHubTopicsAPIView.as_view()),
    path('knowledgehub/topics/details', KnowledgeHubDetailsAPIView.as_view()),
    path('our-partners', OurPartnersAPIView.as_view()),

 


    
     
   
] 
