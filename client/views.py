from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authentication import TokenAuthentication
from django.contrib.auth.models import User
from .models import Client, Order
from .serializers import ClientSerializer


class ClientProfileView(generics.RetrieveUpdateAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user.client  
