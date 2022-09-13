from multiprocessing import context
from django.shortcuts import render

# Create your views here.
def index(request):
    context = {}
    return render(request,'dashboard/index.html',context)

def landlord(request):
    context = {}
    return render(request,'dashboard/landlord.html',context)

def apartment(request):
    context = {}
    return render(request,'dashboard/apartments.html',context)

def house(request):
    context = {}
    return render(request,'dashboard/house.html',context)

def tenant(request):
    context = {}
    return render(request,'dashboard/tenant.html',context)

def landlords(request):
    context = {}
    return render(request,'dashboard/landlordlist.html',context)

def add_houses(request):
    context = {}
    return render(request,'dashboard/addhouses.html',context)

def assignhouses(request):
    context = {}
    return render(request,'dashboard/assignhouses.html',context)

def apartmentlist(request):
    context = {}
    return render(request,'dashboard/apartmentlist.html',context)

def tenantlist(request):
    context = {}
    return render(request,'dashboard/tenantslist.html',context)

def vacanthouses(request):
    context = {}
    return render(request,'dashboard/vacanthouses.html',context)

def occupiedhouses(request):
    context = {}
    return render(request,'dashboard/occupiedhouses.html',context)
