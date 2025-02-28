from django.db import models
from django.contrib.auth.models import User
from .constants import GENDER_TYPE
from service.models import Service

class Client(models.Model):
    user = models.OneToOneField(User, related_name='client', on_delete=models.CASCADE)
    birth_date = models.DateField(null=True, blank=True)
    gender = models.CharField(max_length=10, choices=GENDER_TYPE)
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    join_date = models.DateField(auto_now_add=True)
    balance = models.DecimalField(default=0, max_digits=12, decimal_places=2) 
    def __str__(self):
        return str(self.join_date)

class Order(models.Model):
    client = models.ForeignKey(User, on_delete=models.CASCADE, related_name='orders')
    address = models.CharField(max_length= 100, default="null")
    services = models.ManyToManyField(Service)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    status_choices = [('pending', 'Pending'), ('completed', 'Completed')]
    status = models.CharField(max_length=10, choices=status_choices, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order {self.id} - {self.client.username}"
