from django.test import TestCase
import os
from django.contrib.auth.password_validation import validate_password
from caravansApp.models import Caravan

# Create your tests here.
class TryDjangoConfigTest(TestCase):
    def test_SECRET_KEY_strength(self):
        SECRET_KEY = os.environ.get("SECRET_KEY")
        try:
            is_strong = validate_password(SECRET_KEY)
        except Exception as e:
            self.fail(e)


class CaravanTestCase(TestCase):

    obj = Caravan.objects.create(
        name="TestName",
        description = "TestDescription",
        seating = 5,
        transmission = "sampleTransmission",
        year_of_production = 2000,
        engine = "TestEngine",
        horse_power = 200
    )

    def test_create_caravan(self):
        self.assertEqual(self.obj.name, "TestName")
        self.assertEqual(self.obj.description, "TestDescription")
        self.assertEqual(self.obj.seating, 5)
        self.assertEqual(self.obj.transmission, "sampleTransmission")
        self.assertEqual(self.obj.year_of_production, 2000)
        self.assertEqual(self.obj.engine, "TestEngine")
        self.assertEqual(self.obj.horse_power, 200)
    
    def test_str_representatnion(self):
        self.assertEqual(str(self.obj), "TestName")

