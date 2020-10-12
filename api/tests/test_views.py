from django.urls import reverse

from rest_framework import status
from rest_framework.test import APITestCase, APIClient

from api.models import Vessel, Equipment

VESSEL_VIEW_URL = reverse('vessels-create')
EQUIPMENT_VIEW_URL = reverse('equipments-create')


class VesselViewTestCase(APITestCase):
    def setUp(self):
        self.client = APIClient()

    def test_creating_vessel_endpoint_requires_code_on_body(self):
        response = self.client.post(VESSEL_VIEW_URL, {})
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_successful_creating_vessel_endpoint(self):
        response = self.client.post(VESSEL_VIEW_URL, {'code': 'MV102'})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_list_active_equipments_needs_valid_code(self):
        wrong_url = reverse("equipments-by-vessel", args=["banana"])
        response = self.client.get(wrong_url)

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_list_active_equipments_successful(self):
        vessel = Vessel.objects.create(code="MV102")
        Equipment.objects.create(code="xpto1", vessel=vessel)
        eqp2 = Equipment.objects.create(code="xpto2", vessel=vessel)
        eqp2.inactivate()

        url = reverse("equipments-by-vessel", args=[vessel.code])
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)


class EquipmentViewTestCase(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.vessel = Vessel.objects.create(code="MV102")

    def test_creating_equipment_endpoint_requires_valid_payload(self):
        response = self.client.post(EQUIPMENT_VIEW_URL, {})

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_successful_creating_equipment_endpoint(self):
        payload = {
            'code': '5310B9D7', 'name': 'compressor', 'location': 'Brazil',
            'vessel': self.vessel.code
        }
        response = self.client.post(EQUIPMENT_VIEW_URL, payload)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
