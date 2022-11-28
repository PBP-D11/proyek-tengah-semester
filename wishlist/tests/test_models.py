import datetime
from django.test import TestCase
from django.contrib.auth.models import User
from wishlist.draft_models import *


class TestModels(TestCase):

    def setUp(self):
        self.user = User.objects.create()
        self.user.save()

        self.car = Car.objects.create(
            name="Ferari",
            price="$205",
            is_reviewed=False,
            date=datetime.date.today(),
        )

        self.review = Review.objects.create(
            text="Indah sekali mobil itu",
            user=self.user,
            date=datetime.date.today(),
            car=self.car,
        )

    def test_create_car(self):
        self.assertEqual(
            self.car,
            Car.objects.get(user=self.user)
        )

    def test_create_review(self):
        self.assertEqual(
            self.review,
            Review.objects.get(user=self.user)
        )
