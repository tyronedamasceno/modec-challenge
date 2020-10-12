from django.shortcuts import get_object_or_404

from rest_framework import viewsets, mixins
from rest_framework.decorators import api_view
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

        serializer = self.get_serializer(vessel.active_equipments(), many=True)
        return Response(serializer.data)


@api_view(['POST'])
def equipments_inactivate(request):
    input_data = request.data
    if not input_data or not isinstance(input_data, list):
        return Response(data={"message": "Invalid Payload"}, status=400)

    equipments = Equipment.objects.filter(code__in=input_data)

    if len(equipments) != len(input_data):
        return Response(data={"message": "Invalid Payload"}, status=400)

    equipments.update(status="INACTIVE")

    return Response(data={"message": "success"})
