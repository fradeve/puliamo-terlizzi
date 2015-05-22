from djgeojson.views import GeoJSONLayerView


class GeoJSONResponsePointMixin(GeoJSONLayerView):
    geometry_field = 'point'
    properties = ['status', 'nome', 'date', 'degrado', 'descrizione', 'gallery_url']


class GeoJSONResponsePathMixin(GeoJSONLayerView):
    geometry_field = 'line'
