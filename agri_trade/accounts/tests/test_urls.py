from django.contrib.auth import get_user_model
from django.test import SimpleTestCase
from django.urls import reverse, resolve

from agri_trade.accounts.views import register_user, login_user, account, edit_account, logout_user

UserModel = get_user_model()


class TestUrls(SimpleTestCase):
    def test_register_user_url_resolves(self):
        url = reverse('accounts:register')
        self.assertEqual(resolve(url).func, register_user)

    def test_login_user_url_resolves(self):
        url = reverse('accounts:login')
        self.assertEqual(resolve(url).func, login_user)

    def test_account_url_resolves(self):
        url = reverse('accounts:account')
        self.assertEqual(resolve(url).func, account)

    def test_edit_account_url_resolves(self):
        url = reverse('accounts:edit account')
        self.assertEqual(resolve(url).func, edit_account)

    def test_logout_user_url_resolves(self):
        url = reverse('accounts:logout')
        self.assertEqual(resolve(url).func, logout_user)
