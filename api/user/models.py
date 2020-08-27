from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.base_user import BaseUserManager
# from django.utils.translation import ugettext_lazy as _

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
    is_subscribed = models.BooleanField(default=False)
    
    session_token = models.CharField(max_length=10, default='0')
    
    create_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now=True)

# User Manger Model
class UserManager(BaseUserManager):
    def create_user(self, email, full_name, profile_picture, password=None, is_admin=False, is_staff=False, is_active=True):
        if not email:
            raise ValueError("User must have an email")
        if not password:
            raise ValueError("User must have a password")
        if not full_name:
            raise ValueError("User must have a full name")

        user = self.model(
            email=self.normalize_email(email)
        )
        user.full_name = full_name
        user.set_password(password)  # change password to hash
        user.profile_picture = profile_picture
        user.admin = is_admin
        user.staff = is_staff
        user.active = is_active
        user.save(using=self._db)
        return user

    def create_superuser(self, email, full_name, profile_picture, password=None, **extra_fields):
        if not email:
            raise ValueError("User must have an email")
        if not password:
            raise ValueError("User must have a password")
        if not full_name:
            raise ValueError("User must have a full name")

        user = self.model(
            email=self.normalize_email(email)
        )
        user.full_name = full_name
        user.set_password(password)
        user.profile_picture = profile_picture
        user.admin = True
        user.staff = True
        user.active = is_active
        user.save(using=self._db)
        return user