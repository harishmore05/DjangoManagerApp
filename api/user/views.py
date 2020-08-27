from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from .serializers import UserSerializer
from .models import CustomUser
from django.http import JsonResponse
from django.contrib.auth import get_user_model
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import login, logout

import random
import re

# Generate session token manually by randomizing string with ascii
def generate_session_token(length=10):
    return ''.join(random.SystemRandom().choice([chr(i) for i in range(100, 150)] + [str(i) for i in range(10)]) for _ in range(length))

# Sign in menthod to serve frontend
@csrf_exempt
def signin (request):
    if not request.method == 'POST':
        return JsonResponse({'error': 'Send POST request with valid credentials'})
    
    # get username and password
    username = request.POST.get("email")
    password = request.POST.get("password")
    # print('UserName: ', request.POST.get('email'))
    
    # Validation Part
    if not re.match("^[\w\.\+\-]+\@[\w]+\.[a-z]{2,3}$", username):
        return JsonResponse({'error': 'Enter valid email'})

    if len(password) < 4:
        return JsonResponse({'error' : 'Password needs to be atleast 5 char'})
    
    # Get users
    UserModel = get_user_model()
    
    try:
        # get user object 
        user = UserModel.objects.get(email=username)
        
        # check password
        if user.check_password(password):
            usr_dict = UserModel.objects.filter(email=username).values().first()
            
            # pop out password field from user dictionary before sending it to UI side
            usr_dict.pop('password')
            
            # Check if token is already associate with user object if yes set it to 0 and return error message
            if user.session_token != '0':
                user.session_token  = '0'
                user.save()
                return JsonResponse({'error': 'Previous Session is Active'})
            
            # genrate token for user
            token = generate_session_token()
            user.session_token = token
            
            # save token
            user.save()
            login(request, user)
            # return token and user info
            return JsonResponse({'token': token, 'user': usr_dict})

        else:
            return JsonResponse({'error': 'Invalid Password'})
    except UserModel.DoesNotExist:
        # If user is not exist in db django with raise an exception DoesNotExist
        return JsonResponse({'error': 'User Not Exist,  Please check email'})

# Signout method
@csrf_exempt
def singout(request, id):
    logout(request)
    UserModel = get_user_model()
    
    try:
        # get user object and set token field as 0
        user = UserModel.objects.get(pk=id)
        user.session_token = '0'
        user.save()
    except UserModel.DoesNotExist:
        return JsonResponse({'error': 'Invlid User ID'})
    
    return JsonResponse({'success': 'Logout Success'})

# user viewset (abstracts the get post like request and handle such request on own)
class UserViewSet(viewsets.ModelViewSet):
    permission_classes_by_action = {'create': [AllowAny]}
    
    queryset = CustomUser.objects.all().order_by('id')
    # serialize the User Model
    serializer_class = UserSerializer
    
    def get_permissions(self):
        try:
            return [permission() for permission in self.permission_classes_by_action[self.action]]
        except KeyError:
            return [permission() for permission in self.permission_classes]
            
