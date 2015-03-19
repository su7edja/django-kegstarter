from rest_framework import serializers

from . import models


class LedgerSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Ledger


class LedgerEntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.LedgerEntry
