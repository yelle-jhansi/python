from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .models import ShareMarket
from .serializers import ShareMarketSerializer


class ListShareMarketView(generics.ListAPIView):
    """
    Provides a get method handler.
    """
    queryset = ShareMarket.objects.all()
    serializer_class = ShareMarketSerializer
