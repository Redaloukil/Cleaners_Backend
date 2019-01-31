from django.shortcuts import get_object_or_404
from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from trndy_cleaners.accounts.models import Client , Employee
from trndy_cleaners.accounts.serializers import ClientSerializer , EmployeeSerializer
from rest_framework.response import Response

# Create your views here.

@permission_classes((IsAuthenticated,))
class ClientListView(APIView):
    @staticmethod
    def get(request):
        """
        List profiles
        """
        if request.user.usertype == "1":
            clients = Client.objects.all()
            return Response(data = ClientSerializer(clients, many=True).data , status =status.HTTP_200_OK )
        return Response({"" : ""} , status=status.HTTP_400_BAD_REQUEST)

@permission_classes((IsAuthenticated, ))
class EmployeeListView(APIView):
    @staticmethod
    def get(request):
        """
        List profiles
        """

        Employee = Employee.objects.all()
        return Response(data = EmployeeSerializer(Employee, many=True).data , status=status.HTTP_200_OK)


@permission_classes((IsAuthenticated, ))
class ClientDetailView(APIView):
    def get(request , id):
        client = get_object_or_404(Client , id=id)
        if client.user == request.user : 
            return Response(data = ClientSerializer(client).data , status=status.HTTP_200_OK)
        return Response({"":""} , status=status.HTTP_400_BAD_REQUEST)

@permission_classes((IsAuthenticated, ))
class EmployeeDetailView(APIView):
    def get(request , id):
        employee = get_object_or_404(Employee , id=id)
        if employee.user == request.user: 
            return Response(data = EmployeeSerializer(employee).data , status=status.HTTP_200_OK)
        return Response({"":""} , status=status.HTTP_400_BAD_REQUEST)
        