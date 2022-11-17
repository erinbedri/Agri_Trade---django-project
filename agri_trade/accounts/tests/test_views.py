from django.contrib.auth import get_user_model
from django.test import TestCase


UserModel = get_user_model()


class TestUserRegistration(TestCase):
    VALID_USERNAME = 'test_user'
    VALID_EMAIL = 'test_user@test.com'
    VALID_PASSWORD = 'test_password_123'

    def setUp(self):
        user_a = UserModel(
            username=self.VALID_USERNAME,
            email=self.VALID_EMAIL
        )
        user_a.is_staff = True
        user_a.is_superuser = True
        user_a.set_password = self.VALID_PASSWORD
        user_a.save()
        self.user_a = user_a

    def test_user_exists(self):
        user_count = UserModel.objects.all().count()
        self.assertEqual(user_count, 1)

