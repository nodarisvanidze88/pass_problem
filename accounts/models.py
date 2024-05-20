from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django_countries.fields import CountryField
from django.contrib.auth.hashers import make_password

class MainUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The email must be provided')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        if password:
            user.set_password(password)
        else:
            raise ValueError("Passwords must be provided")
        user.save(using=self._db)
        return user
    
    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        if extra_fields.get('is_staff') is not True:
            raise ValueError('Supperuser must have is_staff status')
        elif extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser status')
        return self.create_user(email, password, **extra_fields)
        
class MainUser(AbstractUser):
    STATUS_CHOICES = [("Seller", "Seller"), ("Buyer", "Buyer")]
    status = models.CharField(max_length=6, choices=STATUS_CHOICES)
    email = models.EmailField(unique=True)
    registration_date = models.DateTimeField(auto_now_add=True)
    address1 = models.CharField(max_length=300, blank=True)
    address2 = models.CharField(max_length=300, blank=True)
    country = CountryField(blank=True)
    city = models.CharField(max_length=100, blank=True)
    zip_num = models.CharField(max_length=10, blank=True)
    phone_number = models.CharField(max_length=50, blank=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']
    objects = MainUserManager()

    def __str__(self):
        return self.email