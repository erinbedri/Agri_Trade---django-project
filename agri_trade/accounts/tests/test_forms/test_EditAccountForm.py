from django.contrib.auth import get_user_model
from django.test import TestCase

from agri_trade.accounts.forms import EditAccountForm

UserModel = get_user_model()


class CustomRegistrationFormTest(TestCase):
    def test_first_name_field_label(self):
        form = EditAccountForm()
        self.assertTrue(form.fields['first_name'].label is None or form.fields['first_name'].label == 'First Name')

    def test_first_name_max_length(self):
        form = EditAccountForm()
        self.assertEqual(form.fields['first_name'].max_length, form.FIRST_NAME_MAX_LENGTH)

    def test_last_name_field_label(self):
        form = EditAccountForm()
        self.assertTrue(form.fields['last_name'].label is None or form.fields['last_name'].label == 'Last Name')

    def test_last_name_max_length(self):
        form = EditAccountForm()
        self.assertEqual(form.fields['last_name'].max_length, form.LAST_NAME_MAX_LENGTH)

    def test_email_field_label(self):
        form = EditAccountForm()
        self.assertTrue(form.fields['email'].label is None or form.fields['email'].label == 'Email')

    def test_username_field_label(self):
        form = EditAccountForm()
        self.assertTrue(form.fields['last_name'].label is None or form.fields['last_name'].label == 'Last Name')

    def test_username_max_length(self):
        form = EditAccountForm()
        self.assertEqual(form.fields['username'].max_length, form.USERNAME_MAX_LENGTH)