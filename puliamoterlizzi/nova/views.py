from djgeojson.views import GeoJSONLayerView


class GeoJSONResponsePointMixin(GeoJSONLayerView):
    geometry_field = 'point'
    properties = ['status', 'nome', 'date', 'descrizione']


class GeoJSONResponsePathMixin(GeoJSONLayerView):
    geometry_field = 'line'
