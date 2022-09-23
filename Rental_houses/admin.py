from django.contrib import admin
from . models import *



class InvoiceAdmin(admin.ModelAdmin):
    list_display = ['tenant','apartment','house','year','month','rent','payment_status']
    #list_editable = Sequence[str]
    #list_per_page = int
    #search_fields = Sequence[str]
    #list_filter: _ListOrTuple[_ListFilterT]

admin.site.register(Landlord)
admin.site.register(Apartment)
admin.site.register(Houses)
admin.site.register(Tenant)
admin.site.register(Allocate_House)
admin.site.register(Invoice,InvoiceAdmin)

# Register your models here.
