from django.contrib.gis import admin

from .models import PuntoIntervento, PercorsoIntervento
from leaflet.admin import LeafletGeoAdmin


class InterventoAdmin(LeafletGeoAdmin):
    list_display = ('id', '__unicode__', 'status', 'degrado', 'partecipanti')

admin.site.register(PuntoIntervento, InterventoAdmin)
admin.site.register(PercorsoIntervento, InterventoAdmin)
