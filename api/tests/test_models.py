from django.db import IntegrityError
from django.test import TestCase

from api.models import Vessel


class VesselsTestCase(TestCase):
    def test_creating_vessel_successful(self):
        Vessel.objects.create(code="MV102")
        self.assertEqual(Vessel.objects.count(), 1)

    def test_vessel_cant_be_repeated(self):
        Vessel.objects.create(code="MV102")

        with self.assertRaises(IntegrityError):
            Vessel.objects.create(code="MV102")