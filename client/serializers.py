from rest_framework import serializers
from .models import Client, Order

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'


# class OrderSerializer(serializers.ModelSerializer):
#     client = serializers.SerializerMethodField()
#     services = serializers.SerializerMethodField()

#     class Meta:
#         model = Order
#         fields = ['id', 'client', 'services', 'total_price', 'status', 'created_at']

#     def get_client(self, obj):
#         from client.serializers import ClientSerializer 
#         return ClientSerializer(obj.client).data

#     def get_services(self, obj):
#         from service.serializers import ServiceSerializer
#         return ServiceSerializer(obj.services.all(), many=True).data
