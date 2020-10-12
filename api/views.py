from django.shortcuts import get_object_or_404

from rest_framework import viewsets, mixins
from rest_framework.response import Response

from api.models import Vessel, Equipment
from api.serializers import VesselSerializer, EquipmentSerializer


class VesselViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    serializer_class = VesselSerializer
    queryset = Vessel.objects.all()


class EquipmentViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    serializer_class = EquipmentSerializer
    queryset = Equipment.objects.all()

    def list(self, request, *args, **kwargs):
        vessel_code = kwargs.get("vessel")
        vessel = get_object_or_404(Vessel, code=vessel_code)

        queryset = vessel.equipments.filter(status="ACTIVE")

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
