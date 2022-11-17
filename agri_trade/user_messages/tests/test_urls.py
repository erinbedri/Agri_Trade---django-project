from django.test import SimpleTestCase
from django.urls import reverse, resolve

from agri_trade.user_messages.views import show_messages, show_message, delete_message, send_message, reply_message


class TestUrls(SimpleTestCase):
    TEST_ID = 10

    def test_show_messages_url_resolves(self):
        url = reverse('user_messages:messages')
        self.assertEqual(resolve(url).func, show_messages)

    def test_show_message_url_resolves(self):
        url = reverse('user_messages:message', args=[self.TEST_ID])
        self.assertEqual(resolve(url).func, show_message)

    def test_delete_message_url_resolves(self):
        url = reverse('user_messages:delete message', args=[self.TEST_ID])
        self.assertEqual(resolve(url).func, delete_message)

    def test_send_message_url_resolves(self):
        url = reverse('user_messages:send message', args=[self.TEST_ID])
        self.assertEqual(resolve(url).func, send_message)

    def test_reply_message_url_resolves(self):
        url = reverse('user_messages:reply to', args=[self.TEST_ID])
        self.assertEqual(resolve(url).func, reply_message)
