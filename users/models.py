from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager
import uuid
from phonenumber_field.modelfields import PhoneNumberField
import phonenumbers



# Create your models here.
class MyUserManager(BaseUserManager):
    def create_user(self,username,first_name,last_name,email,phone_number,password=None):
        if not username:
            raise ValueError("Username is required")

        if not first_name:
            raise ValueError("first name is required")

        if not last_name:
            raise ValueError("last name is required")

        if not email:
            raise ValueError("email is required")

        if not phone_number:
            raise ValueError("please provide an active phone number")
        
        user = self.model(
            username = username,
            first_name = first_name,
            last_name = last_name,
            email = self.normalize_email(email),
            phone_number = phone_number
            
        )
        user.set_password(password)
        user.save(using = self._db)
        return user

    def create_superuser(self,username,first_name,last_name,email,phone_number,password=None):
        user = self.create_user(
            username = username,
            first_name = first_name,
            last_name = last_name,
            email = self.normalize_email(email),
            phone_number = phone_number,
            password = password
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using= self._db)
        return user

class MyCustomUser(AbstractBaseUser):
    username = models.CharField(max_length=100, unique=True)
    email = models.EmailField(verbose_name = "email adress",max_length=60, unique= True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone_number = PhoneNumberField()
    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ['first_name','last_name','email','phone_number']

    objects = MyUserManager()

    def __str__(self):
        return self.username

    def has_perm(self,perm,obj = None):
        return True

    def has_module_perms(self,app_label):
        return True        
