"""
Module containing Django forms.

This module contains the definitions of Django forms used in the project.
"""
from django.forms import ModelForm, TextInput, HiddenInput, Textarea

from . import models


"""Misstake"""
class PlaceRememberForm(ModelForm):
    """
    Form for remembering a place.

    This class defines a form for remembering a place based on the PlaceRemember model.
    """
    class Meta:
        """
        Form metadata for remembering a place.

        This inner class defines metadata for the PlaceRememberForm, such as the associated model.
        """
        model = models.PlaceRemember
        fields = [
            'name',
            'location_latitude',
            'location_longitude',
            'comment',
        ]
        widgets = {
            'name': TextInput(attrs={
                'placeholder': "Name",
            }),
            'location_latitude': HiddenInput(attrs={
                'placeholder': "Location",
                'id': 'latitude',
            }),
            'location_longitude': HiddenInput(attrs={
                'placeholder': "Location",
                'id': 'longitude',
            }),
            'comment': Textarea(attrs={
                'placeholder': "Comment",
            }),
        }
