from rest_framework import serializers
from trndy_cleaners.orders.models import Order
from users.models import User


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'

class OrderCreateSerializer(serializers.ModelSerializer):
    
    class Meta: 
        model = User
        fields = ('client')

    default_error_messages = {
        'wrong_account': 'User account is a client.',
    }

    def get_client(self):
        client = Client.objects.get(user = self.request.user)
        return client

    def validate(self , attrs):
        if self.context['user'].usertype == "1":
            return serializers.ValidationError(self.default_error_messages['wrong_account']) 
