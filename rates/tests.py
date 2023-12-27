from django.test import TestCase
from .models import Rates

class RatesModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Rates.objects.create(
            rate_key='TestKey',
            rate_author='TestAuthor',
            rate_value=100.5,
            rate_unit='TestUnit'
        )

    def test_rates_model(self):
        rate = Rates.objects.get(id=1)
        self.assertEqual(rate.rate_key, 'TestKey')
        self.assertEqual(rate.rate_author, 'TestAuthor')
        self.assertAlmostEqual(rate.rate_value, 100.5)
        self.assertEqual(rate.rate_unit, 'TestUnit')
        self.assertIsNotNone(rate.created_at)
        self.assertIsNotNone(rate.updated_at)