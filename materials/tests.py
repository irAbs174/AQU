from django.test import TestCase
from .models import Materials

class MaterialsModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Materials.objects.create(
            material_key='TestKey',
            material_author='TestAuthor',
            material_name='TestMaterial',
            material_color='TestColor',
            material_unit='TestUnit'
        )

    def test_materials_model(self):
        material = Materials.objects.get(id=1)
        self.assertEqual(material.material_key, 'TestKey')
        self.assertEqual(material.material_author, 'TestAuthor')
        self.assertEqual(material.material_name, 'TestMaterial')
        self.assertEqual(material.material_color, 'TestColor')
        self.assertEqual(material.material_unit, 'TestUnit')
        self.assertIsNotNone(material.created_at)
        self.assertIsNotNone(material.updated_at)
