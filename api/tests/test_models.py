from django.db import IntegrityError
from django.test import TestCase

from api.models import Vessel, Equipment


class VesselsTestCase(TestCase):
    def test_creating_vessel_successful(self):
        Vessel.objects.create(code="MV102")
        self.assertEqual(Vessel.objects.count(), 1)

    def test_vessel_code_cant_be_repeated(self):
        Vessel.objects.create(code="MV102")

        with self.assertRaises(IntegrityError):
            Vessel.objects.create(code="MV102")

    def test_vessel_printing_name_includes_code(self):
        code = "MV102"
        vessel = Vessel.objects.create(code=code)

        self.assertIn(code, str(vessel))


class EquipmentTestCase(TestCase):
    def setUp(self):
        self.vessel = Vessel.objects.create(code="MV102")

    def test_creating_equipment_successful(self):
        Equipment.objects.create(
            code="5310B9D7", name="compressor", location="Brazil",
            vessel=self.vessel)
        self.assertEqual(Vessel.objects.count(), 1)

    def test_equipment_code_cant_be_repeated(self):
        Equipment.objects.create(
            code="5310B9D7", name="compressor", location="Brazil",
            vessel=self.vessel)

        with self.assertRaises(IntegrityError):
            Equipment.objects.create(
                code="5310B9D7", name="compressor", location="Brazil",
                vessel=self.vessel)

    def test_equipment_must_be_related_to_vessel(self):
        with self.assertRaises(IntegrityError):
            Equipment.objects.create(
                code="5310B9D7", name="compressor", location="Brazil")

    def test_inactivate_equipment_method(self):
        equip = Equipment.objects.create(
            code="5310B9D7", name="compressor", location="Brazil",
            vessel=self.vessel)

        equip.inactivate()
        self.assertEqual(equip.status, 'INACTIVE')
