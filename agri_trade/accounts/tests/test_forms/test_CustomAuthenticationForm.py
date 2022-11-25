from django.test import TestCase

from agri_trade.accounts.forms import CustomAuthenticationForm


class CustomAuthenticationFormTest(TestCase):
    def test_username_field_label(self):
        form = CustomAuthenticationForm()
        self.assertTrue(form.fields['username'].label is None or form.fields['username'].label == 'Username')

    def test_username_placeholder(self):
        form = CustomAuthenticationForm()
        self.assertEqual(form.fields['username'].widget.attrs['placeholder'], form.USERNAME_PLACEHOLDER)

    def test_password_field_label(self):
        form = CustomAuthenticationForm()
        self.assertTrue(form.fields['password'].label is None or form.fields['password'].label == 'Password')

    def test_password_placeholder(self):
        form = CustomAuthenticationForm()
        self.assertEqual(form.fields['password'].widget.attrs['placeholder'], form.PASSWORD_PLACEHOLDER)
