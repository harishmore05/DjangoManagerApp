from django.db import models
from django.contrib.auth.models import AbstractUser

# User model
class CustomUser(AbstractUser):
    email = models.EmailField(max_length=200, unique=True)
    fisrt_name = models.CharField(max_length=50, blank=True, null=True)
    last_name = models.CharField(max_length=50, blank=True, null=True)
    address = models.CharField(max_length=200, blank=True, null=True)
    dob = models.DateField(blank=True, null=True)
    company = models.CharField(max_length=200, blank=True, null=True)
    
    is_manager = models.BooleanField(default=True)
    
    username = None
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    
    session_token = models.CharField(max_length=10, default='0')
    
    create_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now=True)
    is_subscribed = models.BooleanField(default=False)