from django.test import TestCase, Client
from django.conf import settings
from django.contrib.auth import REDIRECT_FIELD_NAME
from django.urls import reverse
from django.contrib.auth.models import User


FULL_LOGIN_URL = settings.LOGIN_URL + f"?{REDIRECT_FIELD_NAME}={settings.LOGIN_REDIRECT_URL}"


class TestViews(TestCase):
    def setUp(self):
        self.client = Client()
        self.username = 'test_user'
        self.password = ''
        self.user = User.objects.create_user(username=self.username, password=self.password)


    def _response(self, url):
        return self.client.get(url)


    def _test_success(self, url, template_name=None):
        response = self._response(url)
        self.assertEqual(response.status_code, 200)
        if template_name:
            self.assertTemplateUsed(response, template_name)


    def _test_redirect(self, url, expected_url, target_redirect=False):
        response = self._response(url)
        target_status_code = target_redirect and 302 or 200
        self.assertRedirects(response, expected_url, 302, target_status_code)


    def _test_login_required(self, url, login_url=FULL_LOGIN_URL, target_redirect=True):
        self.client.logout()
        self._test_redirect(url, login_url, target_redirect)


    def test_home(self):
        self._test_success(reverse('app:home'), template_name='app/home.html')


    def test_profile(self):
        self._test_login_required(reverse('app:profile'))
        self.client.login(username=self.username, password=self.password)
        self._test_success(reverse('app:profile'), template_name='app/profile.html')


    def test_logout(self):
        self._test_login_required(reverse('app:logout'), reverse('app:home'), target_redirect=False)
        self.client.login(username=self.username, password=self.password)
        self._test_redirect(reverse('app:logout'), reverse('app:home'), target_redirect=False)
