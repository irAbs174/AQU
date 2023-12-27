from django.test import TestCase
from .models import Units
from django.utils import timezone

class UnitsModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Units.objects.create(
            name='TestUnit',
            symbol='TU',
            description='This is a test unit'
        )

    def test_units_model(self):
        unit = Units.objects.get(id=1)
        self.assertEqual(unit.name, 'TestUnit')
        self.assertEqual(unit.symbol, 'TU')
        self.assertEqual(unit.description, 'This is a test unit')
        self.assertIsNotNone(unit.created_at)
        self.assertIsNotNone(unit.updated_at)
        self.assertTrue(unit.created_at <= timezone.now())
        self.assertTrue(unit.updated_at <= timezone.now())
