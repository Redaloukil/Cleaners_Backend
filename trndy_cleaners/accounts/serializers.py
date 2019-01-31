from rest_framework import serializers 
from trndy_cleaners.accounts.models import Client , Employee


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client 
        fields = '__all__'
 

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'