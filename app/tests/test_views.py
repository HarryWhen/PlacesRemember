from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User


class TestViews(TestCase):
    def setUp(self):
        self.client = Client()
        self.username = 'test_user'
        self.password = ''
        self.user = User.objects.create_user(username=self.username, password=self.password)

    def _response(self, viewname):
        url = reverse(viewname)
        return self.client.get(url)

    def _test_page_success(self, response_view, template_name=None):
        response = self._response(response_view)
        self.assertEqual(response.status_code, 200)
        if template_name:
            self.assertTemplateUsed(response, template_name)

    def _test_page_redirect(self, response_view, expected_view):
        response = self._response(response_view)
        self.assertRedirects(response, reverse(expected_view), status_code=302, target_status_code=200)

    def test_home(self):
        self._test_page_success('app:home', 'app/home.html')

    def test_profile(self):
        self._test_page_redirect('app:profile', 'app:home')
        self.client.login(username=self.username, password=self.password)
        self._test_page_success('app:profile', 'app/profile.html')
