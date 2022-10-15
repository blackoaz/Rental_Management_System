from ast import In
from calendar import month
from distutils.log import error
from multiprocessing import context
from urllib import request
from django.contrib import auth,messages
from django.contrib.auth import authenticate,login,logout
from django.shortcuts import redirect, render,get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.db.models import Sum

from .forms import *
from .filters import *

#xhtml2pdf
import os
from django.conf import settings
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
from django.contrib.staticfiles import finders

# Create your views here.
def login_user(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:    
        if request.POST:
            form = UserLoginForm(request.POST)
            if form.is_valid:
                username = request.POST.get('username')
                password = request.POST.get('password')
                user = authenticate(request,username=username,password=password)

                if user is not None: 
                    login(request,user)
                    return redirect('home')
                else:
                    messages.info(request,'Username or Password is incorrect')  

        else:
            form = UserLoginForm()              
        
        context = {'form':form}
        return render(request,'dashboard/login.html',context)


def register_user(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        form = UserRegistrationForm()

        if request.method == 'POST':
            form = UserRegistrationForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request,'Account was created for ' + " " + user)
                return redirect ('login')
        context = {'form':form}
        return render(request,'dashboard/createaccount.html',context)

def logout_user(request):
    logout(request)
    messages.info(request,f'user logged out successfully')
    return redirect('login')


@login_required(login_url='login')
def index(request):
    lanlords = Landlord.objects.all().count()
    tenants = Tenant.objects.all().count()
    apartments = Apartment.objects.all().count()
    houses = Houses.objects.all().count()
    context = {'lanlords':lanlords,'tenants':tenants,'apartments':apartments,'houses':houses}
    return render(request,'dashboard/index.html',context)

@login_required(login_url='login')
def landlord(request):
    if request.method == 'GET':
        form = LandlordForm() 
        context = {'form':form}
        return render(request,'dashboard/landlord.html',context)
    else:
        form = LandlordForm(request.POST)
        if form.is_valid():
            form.save()
            messages.info(request,'Landlord registerd successfully')
        return redirect('landlords')    

@login_required(login_url='login')
def apartment(request):
    form = ApartmentForm()
    if request.method == 'POST':
        form = ApartmentForm(request.POST)
        if form.is_valid:
            form.save()
            apartment = form.cleaned_data.get('apartment_name')
            messages.info(request,f'{apartment} has been added successfully')
            return redirect('apartments')

    context = {'form':form}
    return render(request,'dashboard/apartments.html',context)

@login_required(login_url='login')
def house(request):
    houses = Houses.objects.all()
    myFilter = HousesFilter(request.GET,queryset=houses)
    context = {'houses':houses,'myFilter':myFilter}
    return render(request,'dashboard/house.html',context)

@login_required(login_url='login')
def tenant(request):
    form = TenantForm()
    if request.method == 'POST':
        form = TenantForm(request.POST)
        if form.is_valid():
            form.save()
            tenant = form.cleaned_data.get('tenant_name')
            messages.info(request,f'Tenant,{tenant}, has been created successfully')
            return redirect('tenantlist')
    context = {'form':form}
    return render(request,'dashboard/tenant.html',context)

@login_required(login_url='login')
def landlords(request):
    landlords = Landlord.objects.all()
    myFilter = LandlordFilter(request.GET,queryset=landlords)
    context = {'landlords':landlords,'myFilter':myFilter}
    return render(request,'dashboard/landlordlist.html',context)

@login_required(login_url='login')
def add_houses(request):
    houses = Houses.objects.all()
    myFilter = HousesFilter(request.GET,queryset=houses)
    form = HousesForm()
    if request.method == 'POST':
        form = HousesForm(request.POST)
        if form.is_valid():
            form.save()
            house = form.cleaned_data.get('house_no')
            apartment_name = form.cleaned_data.get('apartment')
            messages.info(request,f'house number {house} has been added successfully to {apartment_name}')
            return redirect('addhouses')        
    context = {'form':form,'houses':houses,'myFilter':myFilter}
    return render(request,'dashboard/addhouses.html',context)
#################################################################/////
@login_required(login_url='login')
def update_house(request,pk=0):
    form = HousesForm()
    house = Houses.objects.get(id=pk)
    form = HousesForm(instance=house)
    if request.method == 'POST':
        #print("printing Post",request.POST)
        form = HousesForm(request.POST,instance=house)
        if form.is_valid():
            form.save()
            return redirect('addhouses')
    context = {'form':form}   
    return render(request,'dashboard/update_house.html',context) 
   

@login_required(login_url='login')    
def delete_house(request,pk=0):
    house = Houses.objects.get(id=pk)
    if request.method == 'POST':
        house.delete()
        return redirect('addhouses')
    context = {'house':house}
    return render(request, 'dashboard/deletehouse.html',context)  

@login_required(login_url='login')    
def delete_landlord(request,pk=0):
    landlord = Landlord.objects.get(id=pk)
    if request.method == 'POST':
        landlord.delete()
        return redirect('landlords')
    context = {'landlord':landlord}
    return render(request, 'dashboard/deletelandlord.html',context)    

@login_required(login_url='login')
def update_apartment(request,pk=0):
    form = ApartmentForm()       
    apartment = Apartment.objects.get(id=pk)
    form = ApartmentForm(instance=apartment)
    if request.method == 'POST':
        #print("printing Post",request.POST)
        form = ApartmentForm(request.POST,instance=apartment)
        if form.is_valid():
            form.save()
            return redirect('apartmentlist')
    context = {'form':form}   
    return render(request,'dashboard/update_apartment.html',context) 

@login_required(login_url='login')
def update_landlord(request,pk=0):
    form = LandlordForm()       
    landlord = Landlord.objects.get(id=pk)
    form = LandlordForm(instance=landlord)
    if request.method == 'POST':
        #print("printing Post",request.POST)
        form = LandlordForm(request.POST,instance=landlord)
        if form.is_valid():
            form.save()
            return redirect('landlords')
    context = {'form':form}   
    return render(request,'dashboard/updatelandlord.html',context)        
    


@login_required(login_url='login')
def assignhouses(request,id):
    form_2 = Allocate_HouseForm()
    if request.method == 'POST':
        form = Allocate_HouseForm(request.POST)
        if form.is_valid:
            form.save()
            Houses.objects.filter(pk=id).update(occupancy='Occupied')
            return redirect('occupiedhouses')
    if 'q' in request.GET:
        q = request.GET['q']
        tenants = Tenant.objects.filter(id__icontains=q)
    else:
       tenants = ' '
    
    house = Houses.objects.get(pk=id)
    form = HousesForm(instance=house)
    
    #allocate_house = Allocate_House.objects.all()
    context = {'form':form,'house':house,'tenants':tenants,'form_2':form_2}
    return render(request,'dashboard/assignhouses.html',context)

@login_required(login_url='login')
def apartmentlist(request):
    apartments = Apartment.objects.all()
    myFilter = ApartmentFilter(request.GET,queryset=apartments)
    context = {'apartments':apartments,'myFilter':myFilter}
    return render(request,'dashboard/apartmentlist.html',context)

@login_required(login_url='login')
def tenantlist(request):
    tenants = Tenant.objects.all()
    myFilter = TenantFilter(request.GET,queryset=tenants)
    context = {'tenants':tenants,'myFilter':myFilter}
    return render(request,'dashboard/tenantslist.html',context)

@login_required(login_url='login')
def vacanthouses(request):
    houses = Houses.objects.filter(occupancy='Vacant')
    myFilter = HousesFilter(request.GET,queryset=houses) 
    context = {'houses':houses,'myFilter':myFilter}
    return render(request,'dashboard/vacanthouses.html',context)

@login_required(login_url='login')
def occupiedhouses(request):
    houses = Allocate_House.objects.all()
    myFilter = Allocate_houseFilter(request.GET,queryset=houses) 
    context = {'houses':houses,'myFilter':myFilter}
    return render(request,'dashboard/occupiedhouses.html',context)

@login_required(login_url='login')
def tenant_details(request,id):
    context = {'tenant':get_object_or_404(Tenant,pk=id)}
    return render(request,'dashboard/tenantdetail.html',context)

@login_required(login_url='login')
def create_invoice(request):
    houses = Allocate_House.objects.all()
    myFilter = Allocate_houseFilter(request.GET,queryset=houses) 
    context = {'houses':houses,'myFilter':myFilter}
    return render(request,'dashboard/createinvoice.html',context)  

@login_required(login_url='login')
def generate_invoice(request,pk=0):           
    if request.method == 'GET':
        if id == 0:
            form = InvoiceForm()
        else:
            invoice = Allocate_House.objects.get(id=pk)
            form = InvoiceForm(instance=invoice  )

        context = {'form':form}    
        return render(request,'dashboard/generateinvoice.html',context)        
    else:
        form = InvoiceForm(request.POST)
        if form.is_valid():
            form.save()
            tenant = form.cleaned_data.get('tenant')
            apartment = form.cleaned_data.get('apartment')
            month = form.cleaned_data.get('month')
            house = form.cleaned_data.get('house')
            messages.info(request,f'Invoice generated for {tenant}, of {apartment} house number {house} for the month of {month}')
            return redirect('invoiceslist')

@login_required(login_url='login')    
def delete_invoice(request,pk=0):
    invoice = Invoice.objects.get(id=pk)
    if request.method == 'POST':
        invoice.delete()
        return redirect('invoiceslist')
    context = {'invoice':invoice}
    return render(request, 'dashboard/deleteinvoice.html',context) 


@login_required(login_url='login')
def invoices_list(request):

    invoices = Invoice.objects.all()
    myFilter = InvoiceFilter(request.GET,queryset=invoices)
    context = {'invoices':invoices,'myFilter':myFilter}
    return render(request,'dashboard/invoices.html',context,) 

@login_required(login_url='login')
def invoice_view(request,pk):
    invoice = Invoice.objects.get(id=pk)
    template_path = 'dashboard/invoice_view.html'
    context = {'invoice':invoice}
    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'filename="report.pdf"'
    # find the template and render it.
    template = get_template(template_path)
    html = template.render(context)

    # create a pdf
    pisa_status = pisa.CreatePDF(
       html, dest=response)
    # if error then show some funny view
    if pisa_status.err:
       return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response

@login_required(login_url='login')
def pay_invoice(request,pk=0):
    if request.method == 'GET':
        if id == 0:
            form = Invoice_paymentForm()
        else:
            invoice = Invoice.objects.get(id=pk)
            form = Invoice_paymentForm(instance=invoice  )
            
        context = {'form':form}    
        return render(request,'dashboard/payinvoice.html',context)        
    else:
        form = Invoice_paymentForm(request.POST)
        if form.is_valid():
            form.save()
            Invoice.objects.filter(id=pk).update(payment_status='paid')
            #messages.info(request,f'Invoice generated for {tenant}, of {apartment} house number {house} for the month of {month}')
            return redirect('invoiceslist')

@login_required(login_url='login')
def total_rent(request):
    paid_invoices = Invoice_payment.objects.all()
    myFilter = Invoice_paymentFilter(request.GET,queryset=paid_invoices)

    context = {'paid_invoices':paid_invoices,'myFilter':myFilter}
    return render(request,'dashboard/incomes.html',context) 

@login_required(login_url='login')    
def vacate_tenant(request,pk=0):
    tenant = Allocate_House.objects.get(id=pk)
    if request.method == 'POST':
        Houses.objects.filter(id=pk).update(occupancy='Vacant')
        tenant.delete()
        return redirect('houses')
    context = {'tenant':tenant}
    return render(request, 'dashboard/vacatetenant.html',context) 

# def render_pdf_view(request):
#     template_path = 'user_printer.html'
#     context = {'myvar': 'this is your template context'}
#     # Create a Django response object, and specify content_type as pdf
#     response = HttpResponse(content_type='application/pdf')
#     response['Content-Disposition'] = 'attachment; filename="report.pdf"'
#     # find the template and render it.
#     template = get_template(template_path)
#     html = template.render(context)

#     # create a pdf
#     pisa_status = pisa.CreatePDF(
#        html, dest=response, link_callback=link_callback)
#     # if error then show some funny view
#     if pisa_status.err:
#        return HttpResponse('We had some errors <pre>' + html + '</pre>')
#     return response
