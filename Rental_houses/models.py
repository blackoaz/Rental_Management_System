from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
class Landlord(models.Model):
    f_name = models.CharField(max_length=50)
    l_name = models.CharField(max_length=50)
    Id_number = models.IntegerField()
    email_address = models.EmailField(unique=True, blank=True,null=True)
    phone_number = PhoneNumberField()

    def __str__(self):
        return self.f_name + " " + self.l_name

class Apartment(models.Model):
    APARTMENT_CHOICES = (
        ('1-2 Bedroom Apartment','1-2 Bedroom Apartment'),
        ('2-3 Bedroom Apartment','2-3 Bedroom Apartment'),
        ('More than 3 bedroom','More than 3 bedroom'),

    )
    apartment_name = models.CharField(max_length=250)
    apartment_owner = models.ForeignKey(Landlord, on_delete=models.CASCADE)
    apartment_type  = models.CharField(max_length=100,choices= APARTMENT_CHOICES) 
    apartment_description = models.TextField()
    image = models.ImageField(null=True,blank = True)
    town_located = models.CharField(max_length=50)
    apartment_location = models.CharField(max_length=50)
    management_fee = models.DecimalField(max_digits=5,decimal_places=2)

    def __str__(self):
        return self.apartment_name

class Houses(models.Model):
    HOUSE_CHOICES = (
        ('1 Bedroom','1 Bedroom'),
        ('2 Bedroom','2 Bedroom'),
        ('3 Bedroom','3 Bedroom'),

    )
    apartment = models.ForeignKey(Apartment, on_delete=models.CASCADE)
    house_no = models.IntegerField()
    monthly_rent = models.DecimalField(max_digits=10,decimal_places=2)
    deposit = models.DecimalField(max_digits=10,decimal_places=2)
    house_type  = models.CharField(max_length=100,choices=HOUSE_CHOICES) 
    descption = models.TextField()  

    class Meta:
        verbose_name = ("Houses")
        verbose_name_plural = ("Houses")   

    def __str__(self):
        return str(self.house_no)       

class Tenant(models.Model):
    tenant_name = models.CharField(max_length=150)
    national_Id = models.IntegerField()
    email_address = models.EmailField(unique=True)
    phoneNumber = PhoneNumberField()
    physical_Adress = models.CharField(max_length=100)
    Occupation = models.CharField(max_length=150)
    emergency_person_name = models.CharField(max_length=250)
    emergency_person_contact = PhoneNumberField()

    def __str__(self):
        return self.tenant_name


class Allocate_House(models.Model):
    tenant = models.ForeignKey(Tenant, on_delete=models.CASCADE)
    apartment = models.ForeignKey(Apartment,on_delete=models.CASCADE)
    house = models.ForeignKey(Houses,on_delete=models.CASCADE)

    def __str__(self):
        return str(self.tenant)

class Invoice(models.Model):
    PAYMENT_STATUS = (
        ('paid','paid'),
        ('unpaid','unpaid')
    )
    MONTH_CHOICES = (
        ('JAN','JAN'),
        ('FEB','FEB'),
        ('MARCH','MARCH'),
        ('APRL','APRL'),
        ('JUN','JUN'),
        ('JULY','JULY'),
        ('AUG','AUG'),
        ('SEPT','SEPT'),
        ('OCT','OCT'),
        ('NOV','NOV'),
        ('DEC','DEC'),
    )
    tenant = models.ForeignKey(Tenant,on_delete=models.CASCADE)
    apartment = models.ForeignKey(Apartment,on_delete=models.CASCADE)
    house = models.ForeignKey(Houses,on_delete=models.CASCADE)
    year = models.IntegerField()
    month = models.CharField(max_length=20,choices=MONTH_CHOICES)
    rent = models.PositiveIntegerField(default = 0)
    payment_status = models.CharField(max_length=50,choices=PAYMENT_STATUS, default='unpaid')


    def save(self,*args, **kwargs):
        self.rent = self.house.monthly_rent
        return super().save(*args, **kwargs)

    def __str__(self):
        return str(self.house)     

