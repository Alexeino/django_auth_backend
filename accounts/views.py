from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions
# Create your views here.

class TestView(APIView):
    permission_classes = (permissions.IsAuthenticated,)
    def get(self,request):

        return Response({
            "message":"Test View"
    })