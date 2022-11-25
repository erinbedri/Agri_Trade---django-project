from django.test import TestCase

from agri_trade.accounts.forms import EditCompanyForm


class CustomRegistrationFormTest(TestCase):
    def test_name_field_label(self):
        form = EditCompanyForm()
        self.assertTrue(form.fields['name'].label is None or form.fields['name'].label == 'Name')

    def test_name_max_length(self):
        form = EditCompanyForm()
        self.assertEqual(form.fields['name'].max_length, form.NAME_MAX_LENGTH)

    def test_vat_field_label(self):
        form = EditCompanyForm()
        self.assertTrue(form.fields['vat'].label is None or form.fields['vat'].label == 'Vat')

    def test_vat_max_length(self):
        form = EditCompanyForm()
        self.assertEqual(form.fields['vat'].max_length, form.VAT_MAX_LENGTH)

    def test_address_field_label(self):
        form = EditCompanyForm()
        self.assertTrue(form.fields['address'].label is None or form.fields['address'].label == 'Address')

    def test_address_max_length(self):
        form = EditCompanyForm()
        self.assertEqual(form.fields['address'].max_length, form.ADDRESS_MAX_LENGTH)

    def test_postcode_field_label(self):
        form = EditCompanyForm()
        self.assertTrue(form.fields['postcode'].label is None or form.fields['postcode'].label == 'Postcode')

    def test_postcode_max_length(self):
        form = EditCompanyForm()
        self.assertEqual(form.fields['postcode'].max_length, form.POSTCODE_MAX_LENGTH)

    def test_location_field_label(self):
        form = EditCompanyForm()
        self.assertTrue(form.fields['location'].label is None or form.fields['location'].label == 'Location')

    def test_location_max_length(self):
        form = EditCompanyForm()
        self.assertEqual(form.fields['location'].max_length, form.LOCATION_MAX_LENGTH)

    def test_country_field_label(self):
        form = EditCompanyForm()
        self.assertTrue(form.fields['country'].label is None or form.fields['country'].label == 'Country')

    def test_description_field_label(self):
        form = EditCompanyForm()
        self.assertTrue(form.fields['description'].label is None or form.fields['description'].label == 'Description')

    def test_description_max_length(self):
        form = EditCompanyForm()
        self.assertEqual(form.fields['description'].max_length, form.DESCRIPTION_MAX_LENGTH)

