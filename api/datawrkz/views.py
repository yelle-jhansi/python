from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .models import ShareMarket
from .serializers import ShareMarketSerializer
from rest_framework.views import APIView, Response

class ListShareMarketView(generics.ListAPIView):
    """
    Provides a get method handler.
    """
    queryset = ShareMarket.objects.all()
    serializer_class = ShareMarketSerializer

 
class CustomView(APIView):
    def get(self, request, format=None):
        return Response("Some Get Response")
 
    def post(self, request, format=None):
        return Response("Some Post Response")
