from rest_framework import viewsets

from .serializers import EmployeeSerializer
from .models import Employee


# ViewSets manages all the incomming request about creating user edit user and delete user
class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all().order_by('id')
    serializer_class = EmployeeSerializer