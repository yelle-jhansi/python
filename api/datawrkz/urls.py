from django.urls import path
from .views import ListShareMarketView


urlpatterns = [
    path('shares/', ListShareMarketView.as_view(), name="records-all")
]
