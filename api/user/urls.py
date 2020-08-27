from rest_framework import routers
from django.urls import path, include
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token

from . import views

router = routers.DefaultRouter()
router.register('', views.UserViewSet)

urlpatterns =[
    path('login/', views.signin, name='signin'),
    path('logout/<int:id>/', views.singout, name='signout'),
    path('', include(router.urls)),
    path('api-token-auth/', obtain_jwt_token),
    path('api-token-refresh/', refresh_jwt_token),
]