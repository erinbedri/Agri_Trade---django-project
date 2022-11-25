from django.contrib.auth import get_user_model
from django.test import TestCase

from agri_trade.accounts.models import Company

UserModel = get_user_model()


class CompanyModelTest(TestCase):
    VALID_EMAIL = 'test@email.com'
    VALID_PASSWORD = 'TestPassword123'
    VALID_ID = 1

    COMPANY_NAME_FIELD = 'name'
    COMPANY_NAME_MAX_LENGTH = Company.COMPANY_NAME_MAX_LENGTH

    COMPANY_VAT_FIELD = 'vat'
    COMPANY_VAT_MAX_LENGTH = Company.COMPANY_VAT_MAX_LENGTH

    COMPANY_ADDRESS_FIELD = 'address'
    COMPANY_ADDRESS_MAX_LENGTH = Company.COMPANY_ADDRESS_MAX_LENGTH

    COMPANY_POSTCODE_FIELD = 'postcode'
    COMPANY_POSTCODE_MAX_LENGTH = Company.COMPANY_POSTCODE_MAX_LENGTH

    COMPANY_LOCATION_FIELD = 'location'
    COMPANY_LOCATION_MAX_LENGTH = Company.COMPANY_LOCATION_MAX_LENGTH

    COMPANY_COUNTRY_FIELD = 'country'
    COMPANY_COUNTRY_MAX_LENGTH = Company.COMPANY_COUNTRY_MAX_LENGTH

    COMPANY_DESCRIPTION_FIELD = 'description'
    COMPANY_DESCRIPTION_MAX_LENGTH = Company.COMPANY_DESCRIPTION_MAX_LENGTH

    @classmethod
    def setUpTestData(cls):
        UserModel.objects.create(email=cls.VALID_EMAIL, password=cls.VALID_PASSWORD)

    def test_company_is_created_when_user_account_is_registered(self):
        company = Company.objects.get(account_id=self.VALID_ID)
        self.assertIsNotNone(company)

    def test_name_label(self):
        company = Company.objects.get(account_id=self.VALID_ID)
        field_label = company._meta.get_field(self.COMPANY_NAME_FIELD).verbose_name
        self.assertEqual(field_label, self.COMPANY_NAME_FIELD)

    def test_name_max_length(self):
        company = Company.objects.get(account_id=self.VALID_ID)
        max_length = company._meta.get_field(self.COMPANY_NAME_FIELD).max_length
        self.assertEqual(max_length, self.COMPANY_NAME_MAX_LENGTH)

    def test_vat_label(self):
        company = Company.objects.get(account_id=self.VALID_ID)
        field_label = company._meta.get_field(self.COMPANY_VAT_FIELD).verbose_name
        self.assertEqual(field_label, self.COMPANY_VAT_FIELD)

    def test_vat_max_length(self):
        company = Company.objects.get(account_id=self.VALID_ID)
        max_length = company._meta.get_field(self.COMPANY_VAT_FIELD).max_length
        self.assertEqual(max_length, self.COMPANY_VAT_MAX_LENGTH)

    def test_address_label(self):
        company = Company.objects.get(account_id=self.VALID_ID)
        field_label = company._meta.get_field(self.COMPANY_ADDRESS_FIELD).verbose_name
        self.assertEqual(field_label, self.COMPANY_ADDRESS_FIELD)

    def test_address_max_length(self):
        company = Company.objects.get(account_id=self.VALID_ID)
        max_length = company._meta.get_field(self.COMPANY_ADDRESS_FIELD).max_length
        self.assertEqual(max_length, self.COMPANY_ADDRESS_MAX_LENGTH)

    def test_postcode_label(self):
        company = Company.objects.get(account_id=self.VALID_ID)
        field_label = company._meta.get_field(self.COMPANY_POSTCODE_FIELD).verbose_name
        self.assertEqual(field_label, self.COMPANY_POSTCODE_FIELD)

    def test_postcode_max_length(self):
        company = Company.objects.get(account_id=self.VALID_ID)
        max_length = company._meta.get_field(self.COMPANY_POSTCODE_FIELD).max_length
        self.assertEqual(max_length, self.COMPANY_POSTCODE_MAX_LENGTH)

    def test_location_label(self):
        company = Company.objects.get(account_id=self.VALID_ID)
        field_label = company._meta.get_field(self.COMPANY_LOCATION_FIELD).verbose_name
        self.assertEqual(field_label, self.COMPANY_LOCATION_FIELD)

    def test_location_max_length(self):
        company = Company.objects.get(account_id=self.VALID_ID)
        max_length = company._meta.get_field(self.COMPANY_LOCATION_FIELD).max_length
        self.assertEqual(max_length, self.COMPANY_LOCATION_MAX_LENGTH)

    def test_country_label(self):
        company = Company.objects.get(account_id=self.VALID_ID)
        field_label = company._meta.get_field(self.COMPANY_COUNTRY_FIELD).verbose_name
        self.assertEqual(field_label, self.COMPANY_COUNTRY_FIELD)

    def test_country_max_length(self):
        company = Company.objects.get(account_id=self.VALID_ID)
        max_length = company._meta.get_field(self.COMPANY_COUNTRY_FIELD).max_length
        self.assertEqual(max_length, self.COMPANY_COUNTRY_MAX_LENGTH)

    def test_description_label(self):
        company = Company.objects.get(account_id=self.VALID_ID)
        field_label = company._meta.get_field(self.COMPANY_DESCRIPTION_FIELD).verbose_name
        self.assertEqual(field_label, self.COMPANY_DESCRIPTION_FIELD)

    def test_description_max_length(self):
        company = Company.objects.get(account_id=self.VALID_ID)
        max_length = company._meta.get_field(self.COMPANY_DESCRIPTION_FIELD).max_length
        self.assertEqual(max_length, self.COMPANY_DESCRIPTION_MAX_LENGTH)

    def test_object_name_is_name(self):
        company = Company.objects.get(account_id=self.VALID_ID)
        self.assertEqual(str(company), company.name)