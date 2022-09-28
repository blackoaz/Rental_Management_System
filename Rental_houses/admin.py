from django.contrib import admin
from . models import *



class InvoiceAdmin(admin.ModelAdmin):
    list_display = ['tenant','apartment','house','year','month','rent','payment_status']
    #list_editable = Sequence[str]
    #list_per_page = int
    #search_fields = Sequence[str]
    #list_filter: _ListOrTuple[_ListFilterT]

class Invoice_paymentAdmin(admin.ModelAdmin):
    list_display =['invoice','house_rent','month','year','payment','payment_mode','payment','over_payment','balance','reference_no','management_earning']    
  

admin.site.register(Landlord)
admin.site.register(Apartment)
admin.site.register(Houses)
admin.site.register(Tenant)
admin.site.register(Allocate_House)
admin.site.register(Invoice,InvoiceAdmin)
# admin.site.register(Management_sales)
admin.site.register(Invoice_payment,Invoice_paymentAdmin)

# Register your models here.
