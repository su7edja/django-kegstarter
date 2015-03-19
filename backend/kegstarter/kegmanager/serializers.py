from rest_framework import serializers

from . import models


class TapSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Tap
        fields = ('pk', 'location')


class BeerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Beer
        fields = ('url', 'pk', 'name', 'brewer', 'abv')
        depth = 1


class BrewerSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Brewer
        fields = ('pk', 'name')
        depth = 1


class KegSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Keg
        depth = 1
        fields = ('pk', 'beer', 'gallons', 'purchase_date', 'tap')
