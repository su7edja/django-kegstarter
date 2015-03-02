from rest_framework import viewsets, permissions

from .models import Beer, Brewer
from . import serializers


class BeerViewSet(viewsets.ModelViewSet):
    queryset = Beer.objects.all()
    serializer_class = serializers.BeerSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class BrewerViewSet(viewsets.ModelViewSet):
    queryset = Brewer.objects.all()
    serializer_class = serializers.BrewerSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
