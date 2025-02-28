from django.contrib.auth.models import User
from django.db import models
from django.db.models import F

class Service(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='service_images/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    total_rating = models.PositiveIntegerField(default=0)
    rating_count = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name

    @property
    def average_rating(self):
        if self.rating_count > 0:
            return self.total_rating / self.rating_count
        return 0

class Review(models.Model):
    client = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reviews')
    service = models.ForeignKey(Service, on_delete=models.CASCADE, related_name='reviews')
    rating = models.PositiveIntegerField()
    comment = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs) 

        service = self.service
        service.total_rating = F('total_rating') + self.rating
        service.rating_count = F('rating_count') + 1
        service.save(update_fields=['total_rating', 'rating_count'])

    def __str__(self):
        return f"{self.client.username} - {self.service.name} ({self.rating}/5)"