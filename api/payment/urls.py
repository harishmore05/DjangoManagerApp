from django.urls import path, include
from . import views

# urls for getting token and processing payment
urlpatterns = [
    path('gettoken/<str:id>/<str:token>/', views.generate_token, name="token.generate"),
    path('process/<str:id>/<str:token>/', views.process_payment, name="pament.process"),
]