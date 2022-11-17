from django.test import SimpleTestCase
from django.urls import reverse, resolve

from agri_trade.posts.views import show_posts, show_post, show_comments


class TestUrls(SimpleTestCase):
    TEST_ID = 10

    def test_show_posts_url_resolves(self):
        url = reverse('posts:show posts')
        self.assertEqual(resolve(url).func, show_posts)

    def test_show_post_url_resolves(self):
        url = reverse('posts:show post', args=[self.TEST_ID])
        self.assertEqual(resolve(url).func, show_post)

    def test_show_comments_url_resolves(self):
        url = reverse('posts:show comments', args=[self.TEST_ID])
        self.assertEqual(resolve(url).func, show_comments)

