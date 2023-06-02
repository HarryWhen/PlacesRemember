from django.db import models
from django.contrib.auth.models import User


class PlaceRemember(models.Model):
    name = models.CharField(max_length=255)
    location_latitude = models.FloatField()
    location_longitude = models.FloatField()
    comment = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    @property
    def location(self):
        return self.location_latitude, self.location_longitude
