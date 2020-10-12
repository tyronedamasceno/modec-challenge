from rest_framework import status
from rest_framework.test import APITestCase, APIClient

VESSEL_VIEW_URL = ...


class VesselViewTestCase(APITestCase):
    def setUp(self):
        self.client = APIClient()

    def test_creating_vessel_endpoint_requires_code_on_body(self):
        response = self.client.post(VESSEL_VIEW_URL, {})
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_successful_creating_vessel_endpoint(self):
        response = self.client.post(VESSEL_VIEW_URL, {'code': 'MV102'})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
