from rest_framework import serializers
from  app. models import (ProductListing,ProductListingImages,BusinessProfile,Customer,BusinessBranch,Navigator,ListNavigator,
ProductCategory,Order,Event,EventBooking,Coupon,CouponClaim,InvoiceGenerator,KnoledgeBase,BannerImage,Feedback)
from chat. models import ChatMessage
from non_profit.models import Forum,Joined_Forum, Our_Projects,ProjectMedia,Topic,Category,TopicMedia,Partner,Question,Q_Answer,Question_Category
# tenants/serializers.py

from rest_framework import serializers
from django.contrib.auth.models import User
from app.models import Client, Domain, BusinessProfile
from django.contrib.auth import authenticate

class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = [
            

     'business_ID',
     'question_ID'   
     'question',           
     'category',        
     'dateadded',         
   

        ]



class Q_AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Q_Answer
        fields = [
            

     'business_ID',
     'question_ID'   
     'answer',
    'dateadded', 
            
   

        ]



class Question_CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model =Question_Category
        fields = [
            

     'business_ID',
     'question_ID'   
     'category',
    'dateadded', 
            
   

        ]





class ForumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Forum
        fields = [
            

         'business_ID',
        'topic_ID',
        'topic_status',
        'topic_title',
        'topic_thubnail',
        'topic_description',
        'total_comments',
        'total_members',
        'dateadded',


        ]



class Our_ProjectsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Our_Projects
        fields = [
            
            'business_ID',
            'project_ID',
            'project_date',
            'project_tittle',
            'project_description',
            'project_thubnail',
            'dateadded',
        ]


class ProjectMediaSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectMedia
        fields = [
             
         'business_ID',
        'project_ID',
        'project_media',
        'dateadded',
      

        ]


class TopicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Topic
        fields = [

    'business_ID',
    'topic_ID',
    'topic_tittle',
    'category',
    'description',
    'dateadded',
            
        ]




class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = TopicMedia
        fields = [
            'business_ID',
            'topic_ID',
            'category_ID',
            'category',

        ]






class TopicMediaSerializer(serializers.ModelSerializer):
    class Meta:
        model = TopicMedia
        fields = [
            'business_ID',
            'topic_ID',
            'title',
            'media',
            'file_type',
            'file_extension',
            'file_size',
            'dateadded',
   

            
        ]


class PartnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Partner
        fields = [
            

    'business_ID',
    'partner_organisation',
    'partner_type',
    'partner_thubnail',
    'description',
    'dateadded',
   


        ]





class ChatMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChatMessage
        fields = [
            'id',
            'customer_ID',
            'business_ID',   
            'message_ID',    
            'supportAgent',  
            'userName',      
            'country',       
            'message',       
            'phone',        
            'dateadded',        
            'supportMessage',   
            'message_is_opened', 
        ]



class FeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feedback
        fields = [
            'business_ID',
            'customer_ID',
            'customerName',
            'phoneNumber',
            'feedback',
            'dateadded',
        ]





class KnoledgeBaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = KnoledgeBase
        fields = [
            'id',
                     
            'tittle',             
            'description',     
            'mediafile',      
            'author',            
            'category',         
        ]


class BusinessBranchSerializer(serializers.ModelSerializer):
    class Meta:
        model = BusinessBranch
        fields = [
            'id',
            'business_ID',
            'branch_name', 
            'branch_ID',      
            'branch_city',      
            'branch_adress',       
            'branch_phone',        
            'longitude',          
            'latitude',  
        ]

class CouponClaimSerializer(serializers.ModelSerializer):
    class Meta:
        model = CouponClaim
        fields = [
            'id',
            'business_ID',
            'campaignName',
            'couponCode',
            'percentage',
            'category',
            'minimum_amount',
            'claim_Name',
            'claim_Number',
            'claimed_on',
        ]



class CouponSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coupon
        fields = [
            'id',
            'campaignBanner',   
            'campaignName',       
            'couponCode',         
            'percentage',         
            'Usage_limit',      
            'category',          
            'minimum_amount',   
            'startfulldate',     
            'startactualdate',    
            'startTime',        
            'endfullDate',      
            'endactuallDate', 
            'startTime',          
            'endTime',           
        ]


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = [
            'id',
            'business_ID',        
            'event_ID',           
            'event_Name',       
            'event_Description', 
            'eventimage',         
            'image_status',      
            'online_event',     
            'startfulldate',    
            'startactualdate',   
            'startTime',        
            'endfullDate',       
            'endactuallDate',    
            'startTime',         
            'endTime',           
        ]






class EventBookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventBooking
        fields = [
            'id',
            'business_ID',      
            'customer_ID',        
            'booking_ID',      
            'event_ID',          
            'customerName',     
            'phone_Number',     
            'eventTittle',       
            'date',           
            'eventType',        
            'dateadded',           
        ]




class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = [
           'business_ID',
           'current_branch_status',
           'customer_name_status',
            'customerName',
            'App_User_Name',
            'location',
            'country',
            'code',
            'phone',
            'dateadded',
        ]





class NavigatorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Navigator
        fields = [
            'current_page',
            'phone',
            'dateadded',
        ]



class ListNavigatorSerializer(serializers.ModelSerializer):
    class Meta:
        model = ListNavigator
        fields = [
            'current_item',
            'phone',
            'dateadded',
        ]



class ProductCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductCategory
        fields = [
            'business_ID',       
            'category',         
            'description',       
        ]



class ProductListingSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductListing
        fields = [
     'id',
    'business_ID', 
    'product_ID',    
    'title',         
    'product_image',  
    'description',   
    'category',        
    'price',          
    'currency',     
    'compare_price',  ]






class ProductListingImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductListingImages
        fields = [
    'profile_account_ID' ,'listingID' ,'productimage' ,        

    ]


class BusinessProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = BusinessProfile
        fields = [
            'business_ID',
    'BusinessName',
    'logo_image',
    'Business_adress',
    'street_name', 
    'email',       
    'city',        
    'facebook',    
    'website',     
    'phone',       
    'banner_image',
    'other_phone',
    'longitude',   
    'latitude', 
    'form_completed',        

    ]





class BusinessBannerSerializer(serializers.ModelSerializer):
    class Meta:
        model = BannerImage
        fields = [
            'business_ID',
            'BusinessName',
            'banner_image'
           

    ]



class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = [
            'id',
            'business_ID',
            'product_image_url',
            'product_ID',
            'order_ID',
            'customerName',
            'customer_ID',
            'Payment_Method',
            'total_Amount',
            'payment_Status',
            'product_title',     
            'product_description',
            'orderQuantity',
            'phone',
            'country',
            'dateadded',   

    ]




class InvoiceGeneratorSerializer(serializers.ModelSerializer):
    class Meta:
        model = InvoiceGenerator
        fields = [
            'business_ID',       
            'invoice_file',     
            'order_ID',        
            'phone',  
        ]













class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data.get('email'),
            password=validated_data['password']
        )
        return user

class BusinessProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = BusinessProfile
        fields = ['business_domain']

    def validate_subdomain(self, value):
        if Client.objects.filter(businessprofile__business_domain=value).exists():
            raise serializers.ValidationError("Subdomain already exists.")
        # Add additional validation if necessary
        return value

class ClientSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    business_profile = BusinessProfileSerializer()

    class Meta:
        model = Client
        fields = ['name', 'user', 'business_profile']

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        business_profile_data = validated_data.pop('business_profile')

        # Create the user
        user = UserSerializer.create(UserSerializer(), validated_data=user_data)

        # Create the Client (tenant)
        client = Client.objects.create(
            name=validated_data['name'],
            # any other fields
        )

        # Create the Domain for the tenant
        business_domain = Domain.objects.create(
            business_domain=f"{business_profile_data['business_domain']}.localhost",  # Modify for production
            tenant=client,
            is_primary=True
        )

        # Create the BusinessProfile
        BusinessProfile.objects.create(
            user=user,
           business_domain = business_profile_data['business_domain']
        )

        return client

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            return user
        raise serializers.ValidationError("Invalid credentials")





