from rest_framework import serializers
from app.models import Region, District, TicketBus, Journey


class DistrictSerializer(serializers.ModelSerializer):
    class Meta:
        model = District
        fields = ('__all__')


class RegionSerializer(serializers.ModelSerializer):
    district = serializers.StringRelatedField(many=True)

    class Meta:
        model = Region
        fields = ('__all__')


class TicketBusSerializer(serializers.ModelSerializer):
    class Meta:
        model = TicketBus
        fields = ('__all__')


class JourneySerializer(serializers.ModelSerializer):
    class Meta:
        model = Journey
        fields = ('__all__')