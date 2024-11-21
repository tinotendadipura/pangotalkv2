from unicodedata import category
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.response import Response
from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import HttpResponse
import random
from django.db.models import Q
from django.contrib.auth import  login ,logout, authenticate
from django.contrib.auth.models import Group
from django.utils import timezone
from  app. models import (ProductListing,ProductListingImages,
BusinessProfile,Customer,BusinessBranch,
 ProductCategory,Order,
 Event,EventBooking,
 Coupon,CouponClaim,
 CouponClaim,
 InvoiceGenerator,
 KnoledgeBase,
 OrderNotification,
 OrderGroup,
 BannerImage,Feedback,
 FeedbackCount,Navigator,ListNavigator)
from chat. models import ChatMessage 
import uuid
import datetime
from rest_framework.response import Response
from .utils import render_to_pdf
from io import BytesIO
import pdfkit

from django.core.files import File
from .serializers import (ProductListingSerializer,
                          ProductListingImagesSerializer,
                          BusinessProfileSerializer,
                          ChatMessageSerializer,
                          NavigatorSerializer,
                          ListNavigatorSerializer,
                          CustomerSerializer,
                          ProductCategorySerializer,
                          OrderSerializer,
                          EventSerializer,
                          EventBookingSerializer,
                          CouponSerializer,
                           CouponClaimSerializer,
                           InvoiceGeneratorSerializer,
                           BusinessBranchSerializer,
                           KnoledgeBaseSerializer,
                           BusinessBannerSerializer,
                           FeedbackSerializer)

from non_profit . models  import Forum,Partner ,Our_Projects, ProjectMedia ,Topic ,TopicMedia

from rest_framework import generics, status
from rest_framework.response import Response
from .serializers import ClientSerializer,PartnerSerializer, LoginSerializer,Our_ProjectsSerializer,ProjectMediaSerializer,ForumSerializer ,TopicSerializer
from app.models import Client
from rest_framework.permissions import IsAdminUser, AllowAny
from django.contrib.auth import login as auth_login, logout as auth_logout
from rest_framework.views import APIView
from django.shortcuts import render


class NavigatorAPIView(generics.ListAPIView):
    permission_classes     = []
    authentication_classes = []
    serializer_class       = NavigatorSerializer
    

    def get_queryset(self):
        request = self.request
        nav    = Navigator.objects.all()
        businessID = request.GET.get('business_ID')
        phone      = request.GET.get('phone')
        print(businessID)
        if businessID is not None:
            nav = nav.filter(business_ID__iexact = businessID)
            nav = nav.filter(phone__iexact = phone)

        return nav  


class CustomerSignUpAPIView(generics.ListAPIView):
    permission_classes     = []
    authentication_classes = []
    serializer_class       = CustomerSerializer
    

    def get_queryset(self):
        request = self.request
        customer    = Customer.objects.all()
        businessID = request.GET.get('business_ID')
        phone      = request.GET.get('phone')
        print(businessID)
        if businessID is not None:
            customer = customer.filter(business_ID__iexact = businessID)
            customer = customer.filter(phone__iexact = phone)

        return customer 

class CustomerNameUpdateAPIView(generics.CreateAPIView):
    permission_classes     = []
    authentication_classes = []
    serializer_class       = CustomerSerializer
    def post(self ,request , format = None):
        
        data                   =  request.data
        phone                  =  data.get("phone")
        business_ID            =  data.get("business_ID")
        fullName               =  data.get("fullName")
        info = Customer.objects.filter(business_ID = business_ID)
        info = info.filter(phone = phone)
        if info.exists():
            getname = fullName.split() 
            firstName = getname[0]
            lastName  = getname[1]
            currentTime = datetime.datetime.now()
            info.update(customerName = fullName,customer_name_status = True,firstName = firstName,last_Name =lastName,dateadded =currentTime)
        
        
        return Response('message was succesifull delivered.')


class CustomerBranchUpdateAPIView(generics.CreateAPIView):
    permission_classes     = []
    authentication_classes = []
    serializer_class       = CustomerSerializer
    def post(self ,request , format = None):
        
        data                   =  request.data
        phone                  =  data.get("phone")
        business_ID            =  data.get("business_ID")
        branch_ID              =  data.get("branch_ID")
        
        info = Customer.objects.filter(business_ID = business_ID)
        info = info.filter(phone = phone)
        if info.exists():
            info.update(branch_ID = branch_ID,current_branch_status = True)
        
        
        return Response('message was succesifull delivered.')


class ListNavigatorAPIView(generics.ListAPIView):
    permission_classes     = []
    authentication_classes = []
    serializer_class       = ListNavigatorSerializer
    

    def get_queryset(self):
        request = self.request
        nav    = ListNavigator.objects.all()
        businessID = request.GET.get('business_ID')
        phone      = request.GET.get('phone')
        print(businessID)
        if businessID is not None:
            nav = nav.filter(business_ID__iexact = businessID)
            nav = nav.filter(phone__iexact = phone)

        return nav  



class UserNavListUpdateAPIView(generics.CreateAPIView):
    permission_classes     = []
    authentication_classes = []
    serializer_class       = ListNavigatorSerializer
    def post(self ,request , format = None):
        
        data                   =  request.data
        phone                  =  data.get("phone")
        business_ID            =  data.get("business_ID")
        current_item           =  data.get("current_item")
        info = ListNavigator.objects.filter(business_ID = business_ID)
        info = info.filter(phone = phone)
        if info.exists():
            info.update(current_item =current_item)
        else:
            infodata = Customer.objects.get(phone = phone)
            ListNavigator.objects.create(
                customer_ID   = infodata.customer_ID,
                business_ID   = infodata.business_ID,
                current_item  = current_item,
                phone         = infodata.phone,
                )

        
        return Response('message was succesifull delivered.')





class ProductCategoryAPIView(generics.ListAPIView):
    permission_classes     = []
    authentication_classes = []
    serializer_class       = ProductCategorySerializer
    

    def get_queryset(self):
        request = self.request
        product_category    = ProductCategory.objects.all()
        businessID = request.GET.get('business_ID')
        
        if businessID is not None:
            category = product_category.filter(business_ID__iexact = businessID)
            

        return category  




    
    

class ProductListingAPIView(generics.ListAPIView):
    permission_classes     = []
    authentication_classes = []
    serializer_class       = ProductListingSerializer
    

    def get_queryset(self):
        request = self.request
        product =ProductListing.objects.all()
        businessID = request.GET.get('business_ID')
        category   = request.GET.get('category')
        
        
        if businessID is not None:
            busines_product = product.filter(business_ID__iexact = businessID)
            products = busines_product.filter(category__iexact = category)
            

        return products 


class AllProductAPIView(generics.ListAPIView):
    permission_classes     = []
    authentication_classes = []
    serializer_class       = ProductListingSerializer
    

    def get_queryset(self):
        request = self.request
        products =ProductListing.objects.all()
        businessID = request.GET.get('business_ID')
        
        
        
        if businessID is not None:
            products = products.filter(business_ID__iexact = businessID)
            

        return products  






class AllEventsAPIView(generics.ListAPIView):
    permission_classes     = []
    authentication_classes = []
    serializer_class       = EventSerializer
    

    def get_queryset(self):
        request = self.request
        current_time  = datetime.datetime.now()
        event_info =Event.objects.filter(startactualdate__gt = current_time)
        businessID = request.GET.get('business_ID')
        event =event_info.filter(business_ID__iexact = businessID)
        
        
        
        if businessID is not None:
            event = event.filter(business_ID__iexact = businessID)
            

        return event  

class EventDetailAPIView(generics.ListAPIView):
    permission_classes     = []
    authentication_classes = []
    serializer_class       = EventSerializer
    

    def get_queryset(self):
        request = self.request
        
        businessID = request.GET.get('business_ID')
        product_id = request.GET.get('product_id')
        event = Event.objects.filter(business_ID__iexact = businessID)
        
        
        if businessID is not None:
            event = event.filter(business_ID__iexact = businessID)
            event = event.filter(id__iexact = product_id)
            

        return event








class BookEventAPIView(generics.CreateAPIView):
    permission_classes     = []
    authentication_classes = []
    serializer_class       = EventBookingSerializer
    def post(self ,request , format = None):
        
        data                   =  request.data
        
        event_ID               =  data.get("event_ID")
        business_ID            =  data.get("business_ID")
        phone                  =  data.get("phone")
        bookings               =  EventBooking.objects.filter(event_ID = event_ID)
        bookings               =  bookings.filter(phone_Number = phone)
        if bookings.exists():
            return Response('EXIST')
        
        
        
        else:
            bar_var_1         = random.randint(1,9)
            bar_var_2         = random.randint(1,9)
            bar_var_3         = random.randint(1,9)
            bar_var_4         = random.randint(1,9)
            bar_var_5         = random.randint(1,9)

            bar_var_1         = str(bar_var_1)
            bar_var_2         = str(bar_var_2)
            bar_var_3         = str(bar_var_3)
            bar_var_4         = str(bar_var_4)
            bar_var_5         = str(bar_var_5)
            bookingID         = bar_var_1 + bar_var_2 + bar_var_3 + bar_var_4 + bar_var_5
            
            customerInfo  = Customer.objects.get(business_ID = business_ID)
            event_Info    = Event.objects.get(event_ID = event_ID)
           
            EventBooking.objects.create(
                
             business_ID = customerInfo.business_ID,    
             customer_ID =  customerInfo.customer_ID,     
             booking_ID  =   bookingID,  
             event_ID    =  event_ID,   
             customerName = customerInfo.customerName,  
             phone_Number = phone,   
             eventTittle  = event_Info.event_Name,  
             date         = event_Info.startfulldate,
             eventType    = event_Info.online_event,     
             
                                
            )
            return Response('SUCCESS')
            
        
        
       




class PromoAPIView(generics.ListAPIView):
    permission_classes     = []
    authentication_classes = []
    serializer_class       = CouponSerializer
    

    def get_queryset(self):
        request = self.request
        current_time  = datetime.datetime.now()
        promo =Coupon.objects.all()
        businessID = request.GET.get('business_ID')
        
        
        
        if businessID is not None:
            promo = promo.filter(business_ID__iexact = businessID)
            

        return promo



class PromoDetailAPIView(generics.ListAPIView):
    permission_classes     = []
    authentication_classes = []
    serializer_class       = CouponSerializer
    

    def get_queryset(self):
        request = self.request
        coupon = Coupon.objects.all()
        businessID = request.GET.get('business_ID')
        product_id = request.GET.get('product_id')
        
        
        if businessID is not None:
            coupon = coupon.filter(business_ID__iexact = businessID)
            coupon = coupon.filter(id__iexact = product_id)
            

        return coupon




class MyCouponsAPIView(generics.ListAPIView):
    permission_classes     = []
    authentication_classes = []
    serializer_class       = CouponClaimSerializer
    

    def get_queryset(self):
        request = self.request
        coupon_claim    = CouponClaim.objects.all()
        businessID = request.GET.get('business_ID')
        phone      = request.GET.get('phone')
        
        
        
        if businessID is not None:
            coupon_claim = coupon_claim.filter(business_ID__iexact = businessID)
            coupon_claim = coupon_claim.filter(claim_Number = phone)
            coupon_claim = coupon_claim.filter(claimed_status = False)
            

        return coupon_claim




class ClaimCouponAPIView(generics.CreateAPIView):
    permission_classes     = []
    authentication_classes = []
    serializer_class       = CustomerSerializer
    def post(self ,request , format = None):
        
        data                   =  request.data
        business_ID            =  data.get("business_ID")
        coupon_ID              =  data.get("coupon_ID")
        phone                  =  data.get("phone")
        couponInfo             =  Coupon.objects.get(couponCode = coupon_ID)
        customerInfo           =  Customer.objects.filter(business_ID = business_ID)
        customerInfo           =  customerInfo.filter(phone = phone).first()
        claimInfo              =  CouponClaim.objects.filter(claim_Number = phone) 
        claimInfo              =  claimInfo.filter(couponCode  =  coupon_ID)
        if claimInfo.exists():
           return Response('EXIST')
        else:
            
            Usage_limit               =  couponInfo.Usage_limit
            current_claim             =  couponInfo.current_claim
            base_Value                =  current_claim + 1
            if Usage_limit  >= base_Value:
                CouponClaim.objects.create(
                        business_ID        = business_ID,
                        campaignName       = couponInfo.campaignName,
                        couponCode         = couponInfo.couponCode,
                        percentage         = couponInfo.percentage,
                        category           = couponInfo.category,
                        minimum_amount     = couponInfo.minimum_amount,
                        claim_Name         = customerInfo.customerName,
                        claim_Number       = phone,
                    )
                Coupon.objects.filter(couponCode = coupon_ID).update(current_claim = base_Value)
                return Response('SUCCESS')
            else:
                return Response('FULL')

          
    

class CustomerOrdersAPIView(generics.ListAPIView):
    permission_classes     = []
    authentication_classes = []
    serializer_class       = OrderSerializer
    

    def get_queryset(self):
        request = self.request
        order    = Order.objects.all()
        businessID = request.GET.get('business_ID')
        phone      = request.GET.get('phone')
        
        
        
        if businessID is not None:
            businessOrders = order.filter(business_ID__iexact = businessID)
            customerOrders = businessOrders.filter(phone = phone)
            

        return customerOrders



class ProductListingDetailAPIView(generics.ListAPIView):
    permission_classes     = []
    authentication_classes = []
    serializer_class       = ProductListingSerializer
    

    def get_queryset(self):
        request = self.request
        product =ProductListing.objects.all()
        businessID = request.GET.get('business_ID')
        product_id = request.GET.get('product_id')
        
        
        if businessID is not None:
            busines_product = product.filter(business_ID__iexact = businessID)
            products = busines_product.filter(id__iexact = product_id)
            

        return products  

    










class ProductListingImagesAPIView(generics.ListAPIView):
    permission_classes     = []
    authentication_classes = []
    serializer_class       = ProductListingImagesSerializer
    
    
    def get_queryset(self):
        request = self.request
        qs    = ProductListingImages.objects.all()
        query = request.GET.get('search')
        if query is not None:
            qs = qs.filter(listingID__icontains = query)

        return qs


class BusinessProfileAPIView(APIView):
    permission_classes     = []
    authentication_classes = []
    
    def get(self ,request , format = None):
        qs = BusinessProfile.objects.all()
        serializer = BusinessProfileSerializer(qs,many = True)
        return  Response(serializer.data)



class BusinessProfileDetailAPIView(generics.ListAPIView):
    permission_classes     = []
    authentication_classes = []
    serializer_class       = BusinessBannerSerializer
    

    def get_queryset(self):
        request     = self.request
        businessID  = request.GET.get('business_ID')
        
        
        
        if businessID is not None:
            businessInfo = BannerImage.objects.filter(business_ID =  businessID)
            
            

        return businessInfo 



class ChatMessageCreateAPIView(generics.CreateAPIView):
    permission_classes     = []
    authentication_classes = []
    serializer_class       = ChatMessageSerializer
    def post(self ,request , format = None):
        
        data                   =  request.data
        business_ID            =  data.get("business_ID")
        message                =  data.get("message")
        phone                  =  data.get("phone")
        country_code           =  data.get("country_code")
        username               =  data.get("username")
        customer_list          =  Customer.objects.filter(business_ID = business_ID)
        customerInfo           =  customer_list.filter(phone = phone)
        if customerInfo.exists():
            info                 = Customer.objects.filter(business_ID = business_ID)
            info                 = info.filter(phone = phone).first()
            message_ID           = uuid.uuid1()
            message_ID           = str(message_ID)
            customerProfile_info = customerInfo.first()
            updateInfo           = Customer.objects.filter(business_ID = business_ID)
            updateInfo           = updateInfo.filter(phone = phone)
            total_inbox          = customerProfile_info.inbox_messages
            all_messages         = total_inbox + 1   
            updateInfo.update(inbox_messages = all_messages,last_message = message)
            ChatMessage.objects.create(

            customer_ID      = info.customer_ID,
            business_ID      = business_ID,
            message_ID       = message_ID,
            userName         = username,
            country          = country_code,
            message          = message,
            phone            = phone,
                   )
        else:
            customer_ID    = uuid.uuid1()
            customer_ID    = str(customer_ID)
            Customer.objects.create(
                business_ID        = business_ID,
                customer_ID        = customer_ID,
                App_User_Name      = username,
                phone              = phone,
                code               = country_code,
            )
            message_ID    = uuid.uuid1()
            message_ID    = str(message_ID)
            ChatMessage.objects.create(

            customer_ID      = customer_ID,
            business_ID      = business_ID,
            message_ID       = message_ID,
            userName         = username,
            country          = country_code,
            message          = message,
            phone            = phone ,
                   )
            customerProfile_info = Customer.objects.filter( business_ID  = business_ID)
            customerProfile_info = customerProfile_info.filter(phone = phone).first()
            updateInfo           = customerProfile_info.filter(phone = phone)
            total_inbox          = customerProfile_info.inbox_messages
            all_messages         = total_inbox + 1   
            updateInfo.update(inbox_messages = all_messages,last_message = message)
        return Response('message was succesifull delivered.')







   

class CustomerCreateAPIView(generics.CreateAPIView):
    permission_classes     = []
    authentication_classes = []
    serializer_class       = CustomerSerializer
    def post(self ,request , format = None):
        
        data                   =  request.data
        business_ID            =  data.get("business_ID")
        current_page           =  data.get("current_page")
        phone                  =  data.get("phone")
        country_code           =  data.get("country_code")
        username               =  data.get("username")
        customer_list          =  Customer.objects.filter(business_ID = business_ID)
        customerInfo           =  customer_list.filter(phone = phone)
        if customerInfo.exists():
            pass
        else:
            customer_ID    = uuid.uuid1()
            customer_ID    = str(customer_ID)
            customer_ID    = uuid.uuid1()
            customer_ID    = str(customer_ID)
            Navigator.objects.create(
              customer_ID =  customer_ID, 
              business_ID =  business_ID, 
              current_page = current_page,
              phone       = phone,
                        )
            Customer.objects.create(
                business_ID        = business_ID,
                customer_ID        = customer_ID,
                App_User_Name      = username,
                phone              = phone,
                code               = country_code,
            )
            ListNavigator.objects.create(
                customer_ID   = customer_ID,
                business_ID   = business_ID,
                phone         = phone,
            )
            
        
        
        return Response('message was succesifull delivered.')
   


class UserPageUpdateAPIView(generics.CreateAPIView):
    permission_classes     = []
    authentication_classes = []
    serializer_class       = CustomerSerializer
    def post(self ,request , format = None):
        
        data                   =  request.data
        phone                  =  data.get("phone")
        business_ID            =  data.get("business_ID")
        current_page           =  data.get("current_page")
        nav_info               = Navigator.objects.filter(business_ID = business_ID)
        nav_info               = nav_info.filter(phone = phone)
        nav_info.update(current_page =current_page)
               
        
        return Response('message was succesifull delivered.')





    



class OrderCreateAPIView(generics.CreateAPIView):
    permission_classes     = []
    authentication_classes = []
    serializer_class       = OrderSerializer
    def post(self ,request , format = None):
        
        data                   =  request.data
        business_ID            =  data.get("business_ID")
        phone                  =  data.get("phone")
        product_ID             =  data.get("product_ID")
        datetime_zone          = timezone.now()
        customerOrderGroup     =  OrderGroup.objects.filter(business_ID = business_ID)
        currentCustomer        =  customerOrderGroup.filter(phone = phone)
        businessOrders         =  Order.objects.filter(business_ID = business_ID)
        totalCustomerOrders    =  Order.objects.filter(phone = phone).count()
        customerOrders         =  businessOrders.filter(phone = phone)
        product_orders         =  customerOrders.filter(product_ID = product_ID)
        productdata            =  product_orders.first()
        product_Info           = ProductListing.objects.get(product_ID  = product_ID )
        branch_ID              = product_Info.branch_ID
        ordernotification_status = OrderNotification.objects.filter(business_ID = business_ID)
        if product_orders.exists():
            product_Info    = ProductListing.objects.get(product_ID  = product_ID )
            branch_ID       = product_Info.branch_ID
            product_price   = float(product_Info.price)
            orderInfo       = product_orders.first()
            orderQuanntity  = orderInfo.orderQuantity 
            total_Amount    = orderInfo.total_Amount
            total_Amount    = float(total_Amount)
            finalAmount     = total_Amount + product_price
            orderQuanntity  = int(orderQuanntity) + 1
            product_orders.update(orderQuantity = orderQuanntity,total_Amount = finalAmount, dateadded = datetime_zone)
            dataInfo                 = Customer.objects.filter(business_ID = business_ID)
            
            if currentCustomer.exists():
               info_order   = currentCustomer.first()
               orderBalance = info_order.total_Amount
               orderBalance = float(orderBalance)
               orderbaseQuantity = info_order.orderQuantity
               finalQuantity = int(orderbaseQuantity) + 1
               finalorderBalance = orderBalance + product_price
               currentCustomer.update(
                    total_Amount = finalorderBalance,
                    orderQuantity = finalQuantity,
                    dateadded     = datetime_zone
                )
            
            if ordernotification_status.exists():
                status_info    = ordernotification_status.first()
                status_counter = status_info.order_counter
                status_counter = status_counter + 1
                ordernotification_status.update(order_counter = status_counter)
            else:
                OrderNotification.objects.create(business_ID = business_ID,order_counter = 1)

            dataInfo.filter(phone = phone).update(lastOrder = productdata.order_ID,orderQuantity= totalCustomerOrders)
            return Response('EXIST')
        else:
            order_ID        = uuid.uuid1()
            order_ID        = str(order_ID)
            customerInfo    = Customer.objects.filter(business_ID = business_ID) 
            customerInfo    = customerInfo.filter(phone = phone).first()
            product_Info    = ProductListing.objects.get(product_ID  = product_ID )
            product_price   = float(product_Info.price)
            
            bar_var_1         = random.randint(1,9)
            bar_var_2         = random.randint(1,9)
            bar_var_3         = random.randint(1,9)
            bar_var_4         = random.randint(1,9)
            bar_var_5         = random.randint(1,9)

            bar_var_1         = str(bar_var_1)
            bar_var_2         = str(bar_var_2)
            bar_var_3         = str(bar_var_3)
            bar_var_4         = str(bar_var_4)
            bar_var_5         = str(bar_var_5)
            productID         = bar_var_1 + bar_var_2 + bar_var_3 + bar_var_4 + bar_var_5
            customer          =  Customer.objects.filter(business_ID = business_ID)
            customer          =  customer.filter(phone = phone).first()


            Order.objects.create(
                customer_ID        = customer.customer_ID,     
                business_ID        = business_ID,
                product_ID         = product_ID,
                order_ID           = productID,
                 branch_ID         =  branch_ID,
                product_title      = product_Info.title,
                product_description= product_Info.description,
                customerName       = customerInfo.customerName,
                product_image_url  = product_Info.product_image.url,
                total_Amount       = product_price, 
                phone              = phone,
                location           = customerInfo.location,
                orderQuantity      = 1,
                country            = customerInfo.code 
                
                                
            )
            if currentCustomer.exists():
               info_order   = currentCustomer.first()
               orderBalance = float(info_order.total_Amount)
               orderbaseQuantity = info_order.orderQuantity
               finalQuantity = int(orderbaseQuantity) + 1
               finalorderBalance = orderBalance + product_price
               currentCustomer.update(
                    total_Amount = finalorderBalance,
                    orderQuantity = finalQuantity,
                )
            else:
                OrderGroup.objects.create(
                    business_ID        = business_ID,
                    customer_ID        = customer.customer_ID,
                    customerName       = customerInfo.customerName,
                    order_ID           = productID,
                    total_Amount       = product_price,
                
                    phone              = phone,
                    lastOrder          = productID,
                    orderQuantity      = 1,
                    
                    
                )


            if ordernotification_status.exists():
                status_info    = ordernotification_status.first()
                status_counter = status_info.order_counter
                status_counter = status_counter + 1
                ordernotification_status.update(order_counter = status_counter)
            else:
                OrderNotification.objects.create(business_ID = business_ID,order_counter = 1)
            Customer.objects.filter(phone = phone).update(lastOrder= productID,orderQuantity= totalCustomerOrders)
            return Response('SUCCESS')
            
        






class FeedBackCreateAPIView(generics.CreateAPIView):
    permission_classes     = []
    authentication_classes = []
    serializer_class       = FeedbackSerializer
    def post(self ,request , format = None):
        
        data                   =  request.data
        business_ID            =  data.get("business_ID")
        feedback               =  data.get("feedback")
        phone                  =  data.get("phone")
        
        customer_list          =  Customer.objects.filter(business_ID = business_ID)
        customerInfo           =  customer_list.filter(phone = phone).first()
        Feedback.objects.create(
        business_ID     = business_ID,
        customer_ID     = customerInfo.customer_ID,
        customerName    = customerInfo.firstName + ' ' + customerInfo.last_Name,
        phoneNumber     = phone ,
        feedback        = feedback,
        
        )
        customerfeedbackupdate =  customer_list.filter(phone = phone)
        currentCustomerCount = customerInfo.customer_feedback
        finalCount           = currentCustomerCount + 1
        customerfeedbackupdate.update(customer_feedback = finalCount)
        all_feedbackcount= FeedbackCount.objects.filter(business_ID = business_ID)
        if all_feedbackcount.exists():
          currentcount =  all_feedbackcount.first()
          totalcount   =  currentcount.current_feedback
          finalcount   =  totalcount + 1
          all_feedbackcount.update(current_feedback = finalcount)
        else:
            FeedbackCount.objects.create(
                business_ID = business_ID,
                current_feedback  = 1,
                )

        return Response('SUCCESS')








       
class MyOrderDetailAPIView(generics.ListAPIView):
    permission_classes     = []
    authentication_classes = []
    serializer_class       = OrderSerializer
    

    def get_queryset(self):
        request     = self.request
        order_value = Order.objects.all()
        businessID  = request.GET.get('business_ID')
        product_id  = request.GET.get('product_id')
        phone       = request.GET.get('phone')
        
        
        if businessID is not None:
            order_value = order_value.filter(phone__iexact = phone)
            order_value = order_value.filter(business_ID__iexact = businessID)
            order_value = order_value.filter(id__iexact = product_id)
            

        return order_value 








class  GenerateOrderInvoiceAPIView(generics.CreateAPIView):
    permission_classes     = []
    authentication_classes = []
    serializer_class       = InvoiceGeneratorSerializer
    def post(self ,request , format = None):
        
        data                   =  request.data
        business_ID            =  data.get("business_ID")
        order_ID               =  data.get("order_ID")
        phone                  =  data.get("phone")
         
        invoice_status         =  InvoiceGenerator.objects.filter(order_ID = order_ID)
        invoice_status         =  invoice_status.filter(business_ID = business_ID)
        invoice_status         =  invoice_status.filter(order_ID = order_ID)

        
        
        
        if invoice_status.exists():
            # send invoice direct

            return Response('SUCCESS')
        else:
            # create invoice
            
            # data = {
            #         'today': datetime.date.today(), 
            #         'amount': 39.99,
            #         'customer_name': 'Cooper Mann',
            #         'order_id': 1233434,
            #     }
            # pdf = render_to_pdf('invoice/send-invoice.html',data)
            # receipt_file = BytesIO(pdf.content)
            # #receipt      = File(receipt_file,'pdf-test')
            
           
            
            return Response('SUCCESS')
            




class BranchAPIView(generics.ListAPIView):
    permission_classes     = []
    authentication_classes = []
    serializer_class       = BusinessBranchSerializer
    

    def get_queryset(self):
        request    = self.request
        businessBranch    = BusinessBranch.objects.all()
        businessID = request.GET.get('business_ID')
        
        
        
        if businessID is not None:
           businessBranch = businessBranch.filter(business_ID__iexact = businessID)
            

        return businessBranch  

class BranchListingDetailAPIView(generics.ListAPIView):
    permission_classes     = []
    authentication_classes = []
    serializer_class       = BusinessBranchSerializer
    

    def get_queryset(self):
        request = self.request
        businessBranch =BusinessBranch.objects.all()
        businessID = request.GET.get('business_ID')
        product_id = request.GET.get('product_id')
        
        
        if businessID is not None:
            businessBranch = businessBranch.filter(business_ID__iexact = businessID)
            businessBranch = businessBranch.filter(id__iexact = product_id)
            

        return businessBranch 


class KnoledgeBaseAPIView(generics.ListAPIView):
    permission_classes     = []
    authentication_classes = []
    serializer_class       = KnoledgeBaseSerializer
    

    def get_queryset(self):
        request = self.request
        knoledgebase =KnoledgeBase.objects.all()
        businessID = request.GET.get('business_ID')
        category   = request.GET.get('category')
        
        
        if businessID is not None:
             knoledgebase =  knoledgebase.filter(business_ID__iexact = businessID)
             knoledgebase =  knoledgebase.filter(category__iexact = category)
            

        return  knoledgebase 



class ResoucesDetailAPIView(generics.ListAPIView):
    permission_classes     = []
    authentication_classes = []
    serializer_class       = KnoledgeBaseSerializer
    

    def get_queryset(self):
        request = self.request
        resource =KnoledgeBase.objects.all()
        businessID = request.GET.get('business_ID')
        product_id = request.GET.get('product_id')
        
        
        if businessID is not None:
            resource = resource.filter(business_ID__iexact = businessID)
            resource = resource.filter(id__iexact = product_id)
            

        return resource



class GeneratedInvoiceSendAPIView(generics.ListAPIView):
    permission_classes     = []
    authentication_classes = []
    serializer_class       = InvoiceGeneratorSerializer
    

    def get_queryset(self):
        request = self.request
        invoice    = InvoiceGenerator.objects.all()
        businessID = request.GET.get('business_ID')
        order_ID   = request.GET.get('order_ID')
        
        
        
        if businessID is not None:
            invoice = invoice.filter(business_ID__iexact = businessID)
            invoice = invoice.filter(order_ID = order_ID)
            

        return invoice







# Tenant Creation View
class TenantCreateView(generics.CreateAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    permission_classes = [AllowAny]  # Change to [IsAdminUser] if needed

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        client = serializer.save()
        headers = self.get_success_headers(serializer.data)
        return Response(
            {"detail": "Tenant created successfully."},
            status=status.HTTP_201_CREATED,
            headers=headers
        )

# Login API View
class LoginAPIView(APIView):
    permission_classes = [AllowAny]

    def post(self, request, format=None):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data
            auth_login(request, user)  # Log the user in

            # Retrieve the user's BusinessProfile to get the subdomain
            try:
                business_profile = user.businessprofile
                subdomain = business_profile.business_domain

                subdomain_url = " "
                # Construct the subdomain URL (assuming localtest.me)
                if business_profile.category == 'RETAIL AND ECOMM':
            
                   subdomain_url = f"http://{subdomain}.localtest.me:8000/main/home/dashboard"
        
                if business_profile.category == 'NONE PROFIT':
            
                   subdomain_url = f"http://{subdomain}.localtest.me:8000/main/home/dashboard/non-profit"
                
                  # Modify for production

                return Response(
                    {"detail": "Login successful.", "redirect_url": subdomain_url},
                    status=status.HTTP_200_OK
                )
            except BusinessProfile.DoesNotExist:
                return Response(
                    {"detail": "Business profile does not exist."},
                    status=status.HTTP_400_BAD_REQUEST
                )

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Logout API View
class LogoutAPIView(APIView):
    permission_classes = [AllowAny]

    def post(self, request, format=None):
        auth_logout(request)
        return Response({"detail": "Logged out successfully."}, status=status.HTTP_200_OK)

# Login Page View
def login_page(request):
    return render(request, 'registration/login.html')





# ======================= None Profit ================================ #


#------------- Forum Topics -----------#

class ForumTopicsAPIView(generics.ListAPIView):
    permission_classes     = []
    authentication_classes = []
    serializer_class       = ForumSerializer 
    

    def get_queryset(self):
        request = self.request
        all_forum_topics =Forum.objects.all()
        businessID = request.GET.get('business_ID')
        
        
        
        if businessID is not None:
            all_forum_topics = all_forum_topics.filter(business_ID__iexact = businessID)
            

        return all_forum_topics  
    





# ------- All Projects Listing -------- #

class AllProjectsAPIView(generics.ListAPIView):
    permission_classes     = []
    authentication_classes = []
    serializer_class       = Our_ProjectsSerializer
    

    def get_queryset(self):
        request = self.request
        all_projects =Our_Projects.objects.all()
        businessID = request.GET.get('business_ID')
        
        
        
        if businessID is not None:
            all_projects = all_projects.filter(business_ID__iexact = businessID)
            

        return all_projects  
    



class ProjectDetailAPIView(generics.ListAPIView):
    permission_classes     = []
    authentication_classes = []
    serializer_class       = Our_ProjectsSerializer
    

    def get_queryset(self):
        request = self.request
        our_projects = Our_Projects.objects.all()
        businessID   = request.GET.get('business_ID')
        project_ID   = request.GET.get('project_ID')
        
        
        if businessID is not None:
            our_projects = our_projects.filter(business_ID__iexact = businessID)
            our_projects = our_projects.filter(project_ID__iexact = project_ID)
            

        return our_projects 





class AllProjectMediaAPIView(generics.ListAPIView):
    permission_classes     = []
    authentication_classes = []
    serializer_class       = ProjectMediaSerializer
    

    def get_queryset(self):
        request = self.request
        project_media = ProjectMedia.objects.all()
        businessID = request.GET.get('business_ID')
        
        
        
        if businessID is not None:
            project_media = project_media.filter(business_ID__iexact = businessID)
            

        return project_media 

#--------------- Knowledge Hub --------------------#

class KnowledgeHubTopicsAPIView(generics.ListAPIView):
    permission_classes     = []
    authentication_classes = []
    serializer_class       = TopicSerializer
    

    def get_queryset(self):
        request    =     self.request
        all_topics =     Topic.objects.all()
        businessID =     request.GET.get('business_ID')
        
        
        
        if businessID is not None:
            all_topics = all_topics.filter(business_ID__iexact = businessID)
            

        return all_topics  


class KnowledgeHubDetailsAPIView(generics.ListAPIView):
    permission_classes     = []
    authentication_classes = []
    serializer_class       = TopicSerializer
    

    def get_queryset(self):
        request    =    self.request
        all_topics =    Topic.objects.all()
        businessID =    request.GET.get('business_ID')
        topic_ID   =    request.GET.get('product_id')
        
        
        if businessID is not None:
            all_topics =  all_topics.filter(business_ID__iexact = businessID)
            all_topics =  all_topics.filter(topic_ID__iexact = topic_ID)
            

        return all_topics




#--------------- Our Partners --------------------#


class OurPartnersAPIView(generics.ListAPIView):
    permission_classes     = []
    authentication_classes = []
    serializer_class       = PartnerSerializer
    

    def get_queryset(self):
        request      =     self.request
        all_partners =     Partner.objects.all()
        businessID   =     request.GET.get('business_ID')
        
        
        
        if businessID is not None:
            all_partners = all_partners.filter(business_ID__iexact = businessID)
            

        return all_partners 
