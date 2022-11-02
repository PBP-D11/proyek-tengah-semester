from django.test import TestCase, Client
from django.urls import reverse

# Create your tests here.


class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.wishlist_html_url = reverse('wishlist:show_catalog')
        self.wishlist_json_cars_url = reverse('wishlist:json_cars')
        self.wishlist_json_reviews_url = reverse('wishlist:json_reviews')

    def test_show_wishlist_html_resolves(self):
        response = self.client.get(self.wishlist_html_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'wishlist.html')

    def test_show_wishlist_json_cars_resolves(self):
        response = self.client.get(self.wishlist_json_cars_url)
        self.assertEqual(response.status_code, 200)

    def test_show_wishlist_json_reviews_resolves(self):
        response = self.client.get(self.wishlist_json_reviews_url)
        self.assertEqual(response.status_code, 200)
