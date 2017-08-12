from django.db import models


class address_info(models.Model):
    longitude = models.FloatField()
    latitude = models.FloatField()

    def __str__(self):
        return self.longitude
# Create your models here.
