from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate
from users.models import MyCustomUser
from django.contrib.auth.models import User

class LandlordForm(forms.ModelForm):
    class Meta:
        model = Landlord
        fields = ('f_name','l_name','Id_number','email_address','phone_number')
        labels ={
            'f_name':'First Name',
            'l_name':'Last Name',
            'Id_number':'ID Number',
            'email_address':'Email Address',
            'phone_number':'Phone Number'
        }

class ApartmentForm(forms.ModelForm):
    class Meta:
        model = Apartment
        fields = ('apartment_name','apartment_owner','apartment_type','apartment_description','town_located','apartment_location','management_fee')
    
    def __init__(self,*args,**kwargs):
        super(ApartmentForm,self).__init__(*args,**kwargs)
        self.fields['apartment_owner'].empty_label = "Select"    
         
       
class HousesForm(forms.ModelForm):
    class Meta:
        model = Houses
        fields = ['apartment','house_no','monthly_rent','deposit','house_type','descption']
        labels = {
            'apartment':'Name of Apartment',
            'house_no':'House Number',
            'monthly_rent':'Monthly Rent',
            'deposit':'House Deposit',
            'house_type': 'Type of House',
            'descption' :'Brief Description'
        }
    def __init__(self,*args,**kwargs):
        super(HousesForm,self).__init__(*args,**kwargs)
        self.fields['descption'].required = False

class TenantForm(forms.ModelForm):
    class Meta:
        model = Tenant
        fields = '__all__'

class Allocate_HouseForm(forms.ModelForm) :
    class Meta:
        model= Allocate_House
        fields = '__all__'     

class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = MyCustomUser
        fields = ('username','first_name','last_name','email','phone_number','password1','password2') 


class InvoiceForm(forms.ModelForm):
    class Meta:
        model = Invoice
        fields = ['tenant','year','month','apartment','house']

class Invoice_paymentForm(forms.ModelForm):
    class Meta:
        model = Invoice_payment
        fields = ['apartment','month','year','invoice','payment','payment_mode','reference_no'] 
        labels = {
            'apartment':'Name of Apartment',
            'invoice':'Choose Invoice Number',
            'payment':'Enter Payment Amount Made',
            'reference_no':'Enter Payment Reference Number',
        }


class UserLoginForm(forms.ModelForm):
    password = forms.CharField(label= 'password',widget=forms.PasswordInput)   
    class Meta:
        model=MyCustomUser
        fields=('username','password')

    def clean(self):
        if self.is_valid():
            username=self.cleaned_data['username']
            password=self.cleaned_data['password']

            if not authenticate(username=username,password=password):
                raise forms.ValidationError("Invalid username or Password")