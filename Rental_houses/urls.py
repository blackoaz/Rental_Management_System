from django.urls import path
from Rental_houses import views

urlpatterns = [
    path('',views.index,name='home'),
    path('login_user/',views.login_user,name='login'),
    path('register_user/',views.register_user,name='register_user'),
    path('logout_user/',views.logout_user,name='logout_user'),
    path('landlord/',views.landlord,name='landlord'),
    path('apartments/',views.apartment,name='apartments'),
    path('houses/',views.house,name='houses'),
    path('tenants/',views.tenant,name='tenants'),
    path('lanlords/',views.landlords,name='landlords'),
    path('add_houses/',views.add_houses,name='addhouses'),
    path('assignhouses/<int:id>',views.assignhouses,name='assignhouses'),
    path('allocate_house/<int:id>',views.allocate_house,name='allocate_house'),
    path('apartmentlist/',views.apartmentlist,name='apartmentlist'),
    path('tenantlist/',views.tenantlist,name='tenantlist'),
    path('vacanthouses/',views.vacanthouses,name='vacanthouses'),
    path('occupiedhouses/',views.occupiedhouses,name='occupiedhouses'),
    path('tenant_details/<int:id>',views.tenant_details,name='tenant_details'),
]