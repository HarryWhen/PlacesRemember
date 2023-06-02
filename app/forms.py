from django.forms import ModelForm, TextInput, NumberInput, Textarea
# from leaflet.forms.widgets import LeafletWidget

from . import models


class PlaceRememberForm(ModelForm):
    class Meta:
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
            'location_latitude': NumberInput(attrs={
                'placeholder': "Location",
                'id': 'latitude',
            }),
            'location_longitude': NumberInput(attrs={
                'placeholder': "Location",
                'id': 'longitude',
            }),
            'comment': Textarea(attrs={
                'placeholder': "Comment",
            }),
        }
