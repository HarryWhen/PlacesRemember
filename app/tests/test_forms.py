from typing import Any, Container, Iterable

from django.test import SimpleTestCase
from django import forms

from ..forms import PlaceRememberForm


class TestForms(SimpleTestCase):
    def assertInMany(self, members: Iterable[Any], container: Iterable[Any] | Container[Any], msg: Any = None):
        for member in members:
            self.assertIn(member, container, msg)


    def setUp(self):
        self.form = PlaceRememberForm


    def test_place_remember_form_valid(self):
        data = {'name': 'name',
                'location_latitude': 1.2,
                'location_longitude': 3.4,
                'comment': 'comment comment',}
        form = self.form(data)

        self.assertTrue(form.is_valid())


    def test_place_remember_form_invalid(self):
        data = {}
        form = self.form(data)

        self.assertFalse(form.is_valid())
        self.assertEqual(len(form.errors), 4)
        self.assertInMany(['name', 'location_latitude',
                           'location_longitude', 'comment',], form.errors)


    def test_place_remember_form_fields(self):
        form = self.form()

        self.assertInMany(['name', 'location_latitude',
                           'location_longitude', 'comment',], form.fields)
        self.assertIsInstance(form.fields['name'], forms.CharField)
        self.assertIsInstance(form.fields['location_latitude'], forms.FloatField)
        self.assertIsInstance(form.fields['location_longitude'], forms.FloatField)
        self.assertIsInstance(form.fields['comment'], forms.CharField)
