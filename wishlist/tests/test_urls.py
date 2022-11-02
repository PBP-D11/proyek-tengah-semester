from django.test import SimpleTestCase
from django.urls import resolve, reverse
from wishlist.views import show_catalog


class TestUrls(SimpleTestCase):

    def setUp(self):
        self.wishlist_url = reverse('wishlist: show_catalog')

    def test_wishlist_url_resolves(self):
        self.assertEqual(resolve(self.wishlist_url).func, show_catalog)
