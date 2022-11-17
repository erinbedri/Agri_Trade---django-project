from django.test import SimpleTestCase
from django.urls import reverse, resolve

from agri_trade.marketplace.views import marketplace, add_product, product_details, edit_product, delete_product, \
    show_favourites, add_product_to_favourites, show_my_products


class TestUrls(SimpleTestCase):
    TEST_ID = 10

    def test_marketplace_url_resolves(self):
        url = reverse('marketplace:marketplace')
        self.assertEqual(resolve(url).func, marketplace)

    def test_add_product_url_resolves(self):
        url = reverse('marketplace:add product')
        self.assertEqual(resolve(url).func, add_product)

    def test_product_details_url_resolves(self):
        test_id = 10
        url = reverse('marketplace:product details', args=[self.TEST_ID])
        self.assertEqual(resolve(url).func, product_details)

    def test_edit_product_url_resolves(self):
        test_id = 10
        url = reverse('marketplace:edit product', args=[self.TEST_ID])
        self.assertEqual(resolve(url).func, edit_product)

    def test_delete_product_url_resolves(self):
        test_id = 10
        url = reverse('marketplace:delete product', args=[self.TEST_ID])
        self.assertEqual(resolve(url).func, delete_product)

    def test_show_favourites_url_resolves(self):
        url = reverse('marketplace:show favourites')
        self.assertEqual(resolve(url).func, show_favourites)

    def test_add_product_to_favourites_url_resolves(self):
        test_id = 10
        url = reverse('marketplace:add to favourites', args=[self.TEST_ID])
        self.assertEqual(resolve(url).func, add_product_to_favourites)

    def test_show_my_products_url_resolves(self):
        url = reverse('marketplace:show my products')
        self.assertEqual(resolve(url).func, show_my_products)
