from django.test import TestCase
import os
from django.contrib.auth.password_validation import validate_password

# Create your tests here.
class TryDjangoConfigTest(TestCase):
    def test_SECRET_KEY_strength(self):
        SECRET_KEY = os.environ.get("SECRET_KEY")
        try:
            is_strong = validate_password(SECRET_KEY)
        except Exception as e:
            self.fail(e)