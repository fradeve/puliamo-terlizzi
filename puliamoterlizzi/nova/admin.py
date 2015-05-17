from django.contrib.gis import admin

from .models import PuntoIntervento, PercorsoIntervento
from leaflet.admin import LeafletGeoAdmin


admin.site.register(PuntoIntervento, LeafletGeoAdmin)
admin.site.register(PercorsoIntervento, LeafletGeoAdmin)
