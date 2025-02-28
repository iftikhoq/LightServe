from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import RegisterView, LoginView, userdetails, OrderViewSet

router = DefaultRouter()
router.register(r'orders', OrderViewSet) 

urlpatterns = [
    path('userdetails/', userdetails, name='userdetails'),
    path("register/", RegisterView.as_view(), name="register"),
    path("login/", LoginView.as_view(), name="login"),
    path("", include(router.urls)), 
]
