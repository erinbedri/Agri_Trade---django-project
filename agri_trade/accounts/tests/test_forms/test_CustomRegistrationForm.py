from django.contrib.auth import get_user_model
from django.test import TestCase

from agri_trade.accounts.forms import CustomRegistrationForm

UserModel = get_user_model()


class CustomRegistrationFormTest(TestCase):
    def test_first_name_field_label(self):
        form = CustomRegistrationForm()
        self.assertTrue(form.fields['first_name'].label is None or form.fields['first_name'].label == 'First Name')

    def test_first_name_max_length(self):
        form = CustomRegistrationForm()
        self.assertEqual(form.fields['first_name'].max_length, form.FIRST_NAME_MAX_LENGTH)

    def test_first_name_placeholder(self):
        form = CustomRegistrationForm()
        self.assertEqual(form.fields['first_name'].widget.attrs['placeholder'], form.FIRST_NAME_PLACEHOLDER)

    def test_last_name_field_label(self):
        form = CustomRegistrationForm()
        self.assertTrue(form.fields['last_name'].label is None or form.fields['last_name'].label == 'Last Name')

    def test_last_name_max_length(self):
        form = CustomRegistrationForm()
        self.assertEqual(form.fields['last_name'].max_length, form.LAST_NAME_MAX_LENGTH)

    def test_last_name_placeholder(self):
        form = CustomRegistrationForm()
        self.assertEqual(form.fields['last_name'].widget.attrs['placeholder'], form.LAST_NAME_PLACEHOLDER)

    def test_email_field_label(self):
        form = CustomRegistrationForm()
        self.assertTrue(form.fields['email'].label is None or form.fields['email'].label == 'Email')

    def test_email_placeholder(self):
        form = CustomRegistrationForm()
        self.assertEqual(form.fields['email'].widget.attrs['placeholder'], form.EMAIL_PLACEHOLDER)

    def test_username_field_label(self):
        form = CustomRegistrationForm()
        self.assertTrue(form.fields['username'].label is None or form.fields['username'].label == 'Username')

    def test_username_max_length(self):
        form = CustomRegistrationForm()
        self.assertEqual(form.fields['username'].max_length, form.USERNAME_MAX_LENGTH)

    def test_username_placeholder(self):
        form = CustomRegistrationForm()
        self.assertEqual(form.fields['username'].widget.attrs['placeholder'], form.USERNAME_PLACEHOLDER)

    def test_password1_field_label(self):
        form = CustomRegistrationForm()
        self.assertTrue(form.fields['password1'].label is None or form.fields['password1'].label == 'Password')

    def test_password1_placeholder(self):
        form = CustomRegistrationForm()
        self.assertEqual(form.fields['password1'].widget.attrs['placeholder'], form.PASSWORD1_PLACEHOLDER)

    def test_password2_field_label(self):
        form = CustomRegistrationForm()
        self.assertTrue(form.fields['password2'].label is None or form.fields['password2'].label == 'Confirm Password')

    def test_password2_placeholder(self):
        form = CustomRegistrationForm()
        self.assertEqual(form.fields['password2'].widget.attrs['placeholder'], form.PASSWORD2_PLACEHOLDER)