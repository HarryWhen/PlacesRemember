"""
Module containing Django models.

This module contains the definitions of Django models used in the project.
"""
from django.db import models
from django.contrib.auth.models import User


class PlaceRemember(models.Model):
    """
    Model representing a remembered place.

    This class defines a Django model for representing a remembered place
    with its location and additional information.
    """
    name = models.CharField(max_length=255)
    location_latitude = models.FloatField()
    location_longitude = models.FloatField()
    comment = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    objects = models.Manager()

    @property
    def location(self):
        """
        Get the location of the remembered place.

        Returns:
            Tuple[float, float]: The location of the remembered place.
        """
        return self.location_latitude, self.location_longitude
