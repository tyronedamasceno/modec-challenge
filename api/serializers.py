from rest_framework import serializers

from api.models import Vessel


class VesselSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vessel
        fields = '__all__'
        read_only_fields = ('id', )
