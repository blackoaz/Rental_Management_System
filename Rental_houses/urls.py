from django.urls import path
from Rental_houses import views

urlpatterns = [
    path('',views.index,name='home'),
    path('landlord/',views.landlord,name='landlord'),
    path('apartments/',views.apartment,name='apartments'),
    path('houses/',views.house,name='houses'),
    path('tenants/',views.tenant,name='tenants'),
    path('lanlords/',views.landlords,name='landlords'),
    path('add_houses/',views.add_houses,name='addhouses'),
    path('assignhouses/',views.assignhouses,name='assignhouses'),
    path('apartmentlist/',views.apartmentlist,name='apartmentlist'),
    path('tenantlist/',views.tenantlist,name='tenantlist'),
    path('vacanthouses/',views.vacanthouses,name='vacanthouses'),
    path('occupiedhouses/',views.occupiedhouses,name='occupiedhouses'),
]