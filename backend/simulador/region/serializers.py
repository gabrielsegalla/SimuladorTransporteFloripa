from rest_framework import serializers
from .models import Region, District


class DistrictSerializer(serializers.ModelSerializer):
    class Meta:
        model = District
        fields = ('__all__')

class RegionSerializer(serializers.ModelSerializer):
    district = DistrictSerializer(many=False, required=True)

    class Meta:
        model = Region
        fields = ('__all__')