from dataclasses import fields
import django_filters
from . models import *


class HousesFilter(django_filters.FilterSet):
    class Meta:
        model = Houses
        fields = ['apartment','house_no','monthly_rent','house_type']

class LandlordFilter(django_filters.FilterSet):
    class Meta:
        model = Landlord
        fields = {'f_name':['exact'],'l_name':['exact'],'Id_number':['exact'],'email_address':['exact']}
        labels = {
            'f_name' :'First Name',
            'l_name' :'Last Name',
            'Id_number' :'Id Number',
        }

class ApartmentFilter(django_filters.FilterSet):
    class Meta:
        model = Apartment
        fields = {'apartment_name':['exact'],'apartment_type':['exact'] ,'apartment_owner':['exact'],'town_located':['exact']}   


class TenantFilter(django_filters.FilterSet):
    class Meta:
        model = Tenant
        fields = ['id','tenant_name','national_Id','phoneNumber']  

class Allocate_houseFilter(django_filters.FilterSet):
    class Meta:
        model = Allocate_House
        fields = '__all__' 

class InvoiceFilter(django_filters.FilterSet):
    class Meta:
        model = Invoice
        fields = ['payment_status','year','month','apartment','house'] 

class Invoice_paymentFilter(django_filters.FilterSet):
    class Meta:
        model = Invoice_payment
        fields = '__all__'          