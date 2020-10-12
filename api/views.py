from rest_framework import viewsets, mixins

from api.models import Vessel
from api.serializers import VesselSerializer


class VesselViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    serializer_class = VesselSerializer
    queryset = Vessel.objects.all()
