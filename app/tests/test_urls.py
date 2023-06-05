from django.test import SimpleTestCase
from django.urls import reverse, resolve

from ..views import home, profile


class TestUrls(SimpleTestCase):
    def _test_name_is_resolves(self, viewname, func):
        url = reverse(viewname)
        resolver = resolve(url)

        self.assertEquals(resolver.view_name, viewname)
        self.assertEquals(resolver.func, func)


    def test_home_url(self):
        self._test_name_is_resolves('app:home', home)


    def test_profile_url(self):
        self._test_name_is_resolves('app:profile', profile)


    def test_invalid_url(self):
        url = '/invalid-url/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)
