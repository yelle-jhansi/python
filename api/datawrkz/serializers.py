from rest_framework import serializers
from .models import ShareMarket


class ShareMarketSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShareMarket
        fields ='__all__'
