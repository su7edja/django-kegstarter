from rest_framework import viewsets, permissions, routers

from .models import Beer, Brewer
from . import serializers

API_ROUTER = routers.SimpleRouter()


class BeerViewSet(viewsets.ModelViewSet):
    queryset = Beer.objects.all()
    serializer_class = serializers.BeerSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
API_ROUTER.register(r'beers', BeerViewSet)


class BrewerViewSet(viewsets.ModelViewSet):
    queryset = Brewer.objects.all()
    serializer_class = serializers.BrewerSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
API_ROUTER.register(r'brewers', BrewerViewSet)
