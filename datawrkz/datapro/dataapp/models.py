from django.db import models

# Create your models here.
class dataworkz(models.Model):
    date = models.DateTimeField()
    opening = models.IntegerField()
    high =  models.IntegerField()
    low = models.IntegerField()
    closing = models.IntegerField()
    shares = models.IntegerField()
    turnover = models.IntegerField()

    def __str__(self):
        """
        String for representing the Model object.
        """
        return self.opening