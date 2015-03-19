from rest_framework import viewsets, permissions, routers

from . import models
from . import serializers

API_ROUTER = routers.SimpleRouter()


class BeerViewSet(viewsets.ModelViewSet):
    queryset = models.Beer.objects.all()
    serializer_class = serializers.BeerSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
API_ROUTER.register(r'beer', BeerViewSet)


class BrewerViewSet(viewsets.ModelViewSet):
    queryset = models.Brewer.objects.all()
    serializer_class = serializers.BrewerSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
API_ROUTER.register(r'brewer', BrewerViewSet)


class KegViewSet(viewsets.ModelViewSet):
    queryset = models.Keg.objects.all()
    serializer_class = serializers.KegSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
API_ROUTER.register(r'keg', KegViewSet)
