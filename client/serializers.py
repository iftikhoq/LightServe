from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Client, Order
from .constants import GENDER_TYPE

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['id', 'client', 'address', 'services', 'total_price', 'status', 'created_at']
        read_only_fields = ['client', 'status', 'created_at']  # Prevent users from modifying these fields

    def create(self, validated_data):
        request = self.context.get('request')
        validated_data['client'] = request.user  # Set the logged-in user
        return super().create(validated_data)


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "email"]

class ClientSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Client
        fields = ["user", "birth_date", "gender", "profile_picture", "bio", "join_date", "balance"]

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    birth_date = serializers.DateField(required=False)
    gender = serializers.ChoiceField(choices=GENDER_TYPE, required=False)

    class Meta:
        model = User
        fields = ["username", "email", "password", "birth_date", "gender"]

    def create(self, validated_data):
        birth_date = validated_data.pop("birth_date", None)
        gender = validated_data.pop("gender", None)

        user = User.objects.create_user(
            username=validated_data["username"],
            email=validated_data["email"],
            password=validated_data["password"]
        )

        Client.objects.create(user=user, birth_date=birth_date, gender=gender)
        return user