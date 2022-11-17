from django.test import SimpleTestCase
from django.urls import reverse, resolve

from agri_trade.web.views import HomepageView, AboutPageView, ImprintPageView, TermsAndConditionsPageView, \
    DataProtectionPageView


# class TestUrls(SimpleTestCase):
#     def test_show_homepage_url_resolves(self):
#         url = reverse('web:homepage')
#         self.assertEqual(resolve(url).func, show_homepage)
#
#     def test_about_url_resolves(self):
#         url = reverse('web:about')
#         self.assertEqual(resolve(url).func, about)
#
#     def test_imprint_url_resolves(self):
#         url = reverse('web:imprint')
#         self.assertEqual(resolve(url).func, imprint)
#
#     def test_terms_and_conditions_url_resolves(self):
#         url = reverse('web:terms and conditions')
#         self.assertEqual(resolve(url).func, terms_and_conditions)
#
#     def test_data_protection_url_resolves(self):
#         url = reverse('web:data protection')
#         self.assertEqual(resolve(url).func, data_protection)


class TestUrls(SimpleTestCase):
    def test_HomepageView_url_resolves(self):
        url = reverse('web:homepage')
        self.assertEqual(resolve(url).func.__name__, HomepageView.as_view().__name__)

    def test_AboutPageView_url_resolves(self):
        url = reverse('web:homepage')
        self.assertEqual(resolve(url).func.__name__, AboutPageView.as_view().__name__)

    def test_ImprintPageView_url_resolves(self):
        url = reverse('web:homepage')
        self.assertEqual(resolve(url).func.__name__, ImprintPageView.as_view().__name__)

    def test_TermsAndConditionsPageView_url_resolves(self):
        url = reverse('web:homepage')
        self.assertEqual(resolve(url).func.__name__, TermsAndConditionsPageView.as_view().__name__)

    def test_DataProtectionPageView_url_resolves(self):
        url = reverse('web:homepage')
        self.assertEqual(resolve(url).func.__name__, DataProtectionPageView.as_view().__name__)