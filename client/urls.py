from django.urls import path
from .views import ClientProfileView, OrderListCreateView, OrderDetailView

urlpatterns = [
    path('profile/', ClientProfileView.as_view(), name='client-profile'),
    path('orders/', OrderListCreateView.as_view(), name='order-list-create'),
    # path('orders/<int:pk>/', OrderDetailView.as_view(), name='order-detail'),
]