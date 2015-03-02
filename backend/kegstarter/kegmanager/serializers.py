from rest_framework import serializers

from . import models


class TapSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Tap


class BeerSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='beers') #assuming that the url would be /api/beers/{pk}/

    class Meta:
        model = models.Beer
        fields = ('url', 'id', 'name', 'brewer', 'abv')


class BrewerSerializer(serializers.ModelSerializer):
    beers = BeerSerializer(many=True)

    class Meta:
        model = models.Brewer
        fields = ('id', 'name', 'beers')


class KegSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Keg
