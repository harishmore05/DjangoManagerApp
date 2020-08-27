from django.urls import path, include
from rest_framework.authtoken import views
from .views import home

urlpatterns =[
    path('',home, name='api.home'),
    path('employee/',include('api.employee.urls')),
    path('user/', include('api.user.urls')),
    path('payment/', include('api.payment.urls')),
    # path('api-token-auth', views.obtain_auth_token, name='api_token_auth') # Just for Reference Not using it
]