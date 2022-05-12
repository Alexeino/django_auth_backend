from .views import CustomTokenObtainPairView
from rest_framework_simplejwt.views import TokenRefreshView
from django.urls import path
from accounts.views  import  TestView
urlpatterns = [
    path('token/',CustomTokenObtainPairView.as_view(),name='get-token'),
    path('token/refresh/',TokenRefreshView.as_view(),name='refresh-token'),
    path('test/',TestView.as_view(),name="test")
]
