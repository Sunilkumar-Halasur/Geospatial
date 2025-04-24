from rest_framework import viewsets
from .models import PointData, PolygonData
from .serializers import PointDataSerializer, PolygonDataSerializer

class PointDataViewSet(viewsets.ModelViewSet):
    queryset = PointData.objects.all()
    serializer_class = PointDataSerializer

class PolygonDataViewSet(viewsets.ModelViewSet):
    queryset = PolygonData.objects.all()
    serializer_class = PolygonDataSerializer
