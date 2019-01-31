from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from trndy_cleaners.orders.models import Order
from trndy_cleaners.orders.serializers import OrderSerializer , OrderCreateSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated


@permission_classes((IsAuthenticated,))
class ClientOrderCreate(APIView):
    @staticmethod
    def post(request):
        print(request.user.user_type)
        if request.user.user_type == "1":
            serializer = OrderCreateSerializer(data=request.data)
            return Response(serializer.data , status=status.HTTP_200_OK)
        return Response({"permission_error":"you are not an employee"} , status=status.HTTP_400_BAD_REQUEST)

@permission_classes((IsAuthenticated,))
class AdminOrderListView(APIView):
    @staticmethod 
    def get(request):
        if request.user.user_type == "0":
            orders = Order.objects.all()
            return Response(data=OrderSerializer(orders , many=True) , status=status.HTTP_200_OK)
        return Response({"permission_error":"you are not an employee"} , status=status.HTTP_400_BAD_REQUEST)
        
@permission_classes((IsAuthenticated,))        
class ClientOrderListView(APIView):
    @staticmethod 
    def get(request):
        if request.user.user_type == "1":
            orders = Order.objects.filter(client=request.user.client)
            return Response(data=OrderSerializer(orders , many=True) , status=status.HTTP_200_OK)
        return Response({"permission_error":"you are not a client"} , status=status.HTTP_400_BAD_REQUEST)
        
@permission_classes((IsAuthenticated,))
class OrderDetailView(APIView):
    @staticmethod 
    def get(request , id):
        order = get_object_or_404(Order , id = id)
        if order.client.user == request.user or request.user.usertype == "0" : 
            return Response(data = OrderSerializer(order).data , status = status.HTTP_200_OK)
        else : 
            return Response({"permission_error" : "you have to be authenticated"} , status = HTTP_400_BAD_REQUEST)