from rest_framework import routers
from django.urls import path, include
from . import views
from django.contrib.auth.decorators import login_required

# set routing to employee viewsets
router = routers.DefaultRouter()
router.register('',views.EmployeeViewSet)

urlpatterns = [
    path('', include(router.urls))
    # path('', include(router.urls), login_required(restricted.restricted_from_urls))
]