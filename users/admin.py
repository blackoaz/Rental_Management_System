from django.contrib import admin
from . models import MyCustomUser

# Register your models here.
class MyCustomUserAdmin(admin.ModelAdmin):
    list_display = ('username','first_name','last_name','email','date_joined','last_login')
    fieldsets = ()

    add_fieldsets = (
        (None,{
            'classes':('wide'),
            'fields': ('username,','first_name','last_name','email','phone_number','password1','password2')
        }),
    )
    ordering = ('username',)

admin.site.register(MyCustomUser,MyCustomUserAdmin)
