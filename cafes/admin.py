from django.contrib import admin
from django.contrib.gis.admin import OSMGeoAdmin

from .models import Cafe

admin.site.register(Cafe)
