from rest_framework import viewsets
from rest_framework_gis import filters

from .models import Cafe
from .serializers import CafeSerializer


class CafeViewSet(viewsets.ReadOnlyModelViewSet):
    bbox_filter_field = "location"
    filter_backends = (filters.InBBoxFilter,)
    queryset = Cafe.objects.all()
    serializer_class = CafeSerializer
