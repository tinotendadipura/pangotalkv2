from rest_framework import serializers
from . models import PrimaryDomain




class PrimaryDomainSerializer(serializers.ModelSerializer):
    class Meta:
        model = PrimaryDomain
        fields = [
    'school_ID',
    'http_request',             
    'DomainName',            
    'Date_added',          
    'DomainNameProvider',    
    'DomainActiveStatus',    
    'DomainActiveStatus', 
    
       ]