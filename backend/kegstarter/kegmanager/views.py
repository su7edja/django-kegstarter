from rest_framework import generics

from .models import Beer, Brewer
from . import serializers


class BeerListView(generics.ListCreateAPIView):
    queryset = Beer.objects.all()
    serializer_class = serializers.BeerSerializer


class BeerView(generics.RetrieveUpdateAPIView):
    model = Beer
    serializer_class = serializers.BeerSerializer


class BrewerListView(generics.ListCreateAPIView):
    queryset = Brewer.objects.all()
    serializer_class = serializers.BrewerSerializer


class BrewerView(generics.RetrieveUpdateAPIView):
    model = Brewer
    serializer_class = serializers.BrewerSerializer
