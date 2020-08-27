from django.db import models
from django import forms

# Employee Model
class Employee(models.Model):
    email = models.EmailField(max_length=100, unique=True)
    first_name = models.CharField(max_length=50, blank=True, null=True)
    last_name = models.CharField(max_length=50, blank=True, null=True)
    password = models.CharField(max_length=50, blank=True, null=True)
    adress = models.CharField(max_length=100, blank=True, null=True)
    dob = models.DateField(blank=True, null=True)
    company = models.CharField(max_length=50, blank=True, null=True)
    mobile = models.CharField(max_length=13, blank=True, null=True)
    city = models.CharField(max_length=50, blank=True, null=True)
    
    def __str__(self):
        return self.email