from django import forms
from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm





from django.contrib.auth.forms import PasswordResetForm

class UserPasswordResetForm(PasswordResetForm):
    def __init__(self, *args, **kwargs):
        super(UserPasswordResetForm, self).__init__(*args, **kwargs)

    email = forms.EmailField(label='', widget=forms.EmailInput(attrs={
        'class': 'form-control email',
        'placeholder': 'Enter Your Email',
        'type': 'email',
        'name': 'email'
        }))





class RegistrationForm(UserCreationForm):
    

    #Phone_Number = forms.CharField(max_length=200, required=True)
    


    class Meta:
        model=User

        fields=[
            
            'username',
            
            'email',
            
            'password1',
            'password2'
            
        ]
        widgets={'username' : forms.TextInput(
        attrs={"class" : "input-text"}) ,

        }

        widgets={'email' : forms.EmailInput(
        attrs={"class" : "input-text"}) ,

        }
        widgets={'username' : forms.TextInput(
        attrs={"class" : "input-text"}) ,

        }

        widgets={'password1' : forms.TextInput(
        attrs={"class" : "input-text"}) ,

        }

        widgets={'password2' : forms.TextInput(
        attrs={"class" : "input-text"}) 

        }
        

def save(self,commit=True):
    user=super(RegistrationForm,self).save(commit=False)
    
    
    user.password1 = cleaned_data['password1']
    user.password2 = cleaned_data['password2']
    

    
    if commit:
        User.save()
    return user


