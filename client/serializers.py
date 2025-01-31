from rest_framework import serializers
from .models import Client, Order


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'


class OrderSerializer(serializers.ModelSerializer):
    client = UserSerializer()  
    services = ServiceSerializer(many=True)

    class Meta:
        model = Order
        fields = ['id', 'client', 'services', 'total_price', 'status', 'created_at']

