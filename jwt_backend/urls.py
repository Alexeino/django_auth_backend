from .views import CustomTokenObtainPairView
from rest_framework_simplejwt.views import TokenRefreshView
from django.urls import path

urlpatterns = [
    path('token/',CustomTokenObtainPairView.as_view(),name='get-token'),
    path('token/refresh/',TokenRefreshView.as_view(),name='refresh-token')
]
