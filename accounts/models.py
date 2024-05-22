from django.db import models
from django.contrib.auth.models import AbstractUser
from django_countries.fields import CountryField

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

    def __str__(self):
        return self.email
