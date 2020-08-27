from rest_framework import serializers
from .models import Employee

# Serialize all fields of employee 
class EmployeeSerializer(serializers.HyperlinkedModelSerializer):
    
    class Meta:
        model = Employee
        fields = '__all__'