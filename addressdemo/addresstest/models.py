from django.db import models


class address_info(models.Model):
    longitude = models.FloatField()
    latitude = models.FloatField()
    data = models.CharField(max_length=200)

    def __str__(self):
        return self.longitude
# Create your models here.
