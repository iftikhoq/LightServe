from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Service, Review
# from client.serializers import ClientSerializer

class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = '__all__'


# class OrderSerializer(serializers.ModelSerializer):
#     client = ClientSerializer() 
#     services = ServiceSerializer(many=True)

#     class Meta:
#         model = Order
#         fields = ['id', 'client', 'services', 'total_price', 'status', 'created_at']

class ReviewSerializer(serializers.ModelSerializer):
    client = serializers.StringRelatedField()  
    service = serializers.StringRelatedField() 

    class Meta:
        model = Review
        fields = '__all__'
