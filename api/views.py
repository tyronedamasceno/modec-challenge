from rest_framework import viewsets, mixins

from api.models import Vessel, Equipment
from api.serializers import VesselSerializer, EquipmentSerializer


class VesselViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    serializer_class = VesselSerializer
    queryset = Vessel.objects.all()


class EquipmentViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    serializer_class = EquipmentSerializer
    queryset = Equipment.objects.all()
