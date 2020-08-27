from django.contrib import admin
from .models import CustomUser

# Register CustomUser to Admin 
admin.site.register(CustomUser)