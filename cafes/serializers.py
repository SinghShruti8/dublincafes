from rest_framework_gis import serializers

from .models import Cafe


class CafeSerializer(serializers.GeoFeatureModelSerializer):
    class Meta:
        fields = ("id", "name")
        geo_field = "location"
        model = Cafe
