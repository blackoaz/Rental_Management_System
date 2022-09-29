from django.contrib import admin
from . models import *



class InvoiceAdmin(admin.ModelAdmin):
    list_display = ['tenant','apartment','house','year','month','rent','payment_status']
    #list_editable = Sequence[str]
    #list_per_page = int
    #search_fields = Sequence[str]
    #list_filter: _ListOrTuple[_ListFilterT]

class Invoice_paymentAdmin(admin.ModelAdmin):
    list_display =['apartment','invoice','house_rent','month','year','payment','payment_mode','over_payment','balance','reference_no','management_earning']    

# class Total_earningAdmin(admin.ModelAdmin):
#     list_display =['apartment','year','month','total_earning']    
  

admin.site.register(Landlord)
admin.site.register(Apartment)
admin.site.register(Houses)
admin.site.register(Tenant)
admin.site.register(Allocate_House)
admin.site.register(Invoice,InvoiceAdmin)
# admin.site.register(Management_sales)
admin.site.register(Invoice_payment,Invoice_paymentAdmin)
# admin.site.register(Total_earning,Total_earningAdmin)

# Register your models here.
