from django.db import models

# Create your models here.
class ShareMarket(models.Model):
    id = models.IntegerField(primary_key=True)
    Date = models.DateField()
    Open = models.FloatField(max_length=10)
    High = models.FloatField(max_length=10)
    Low = models.FloatField(max_length=10)
    Close = models.FloatField(max_length=10)
    Shares_Traded = models.IntegerField()
    Turnover_Cr = models.FloatField(max_length=10)
    
