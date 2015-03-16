from rest_framework import serializers

from . import models


class PollSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Poll


class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Rating


class VoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Vote
