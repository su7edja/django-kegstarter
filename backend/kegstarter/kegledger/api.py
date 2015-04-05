from rest_framework import viewsets, routers

from kegstarter.utils.permissions import IsOwnerOrReadOnly
from .models import Ledger, LedgerEntry
from .permissions import IsLedgerOwnerOrReadOnly
from . import serializers

API_ROUTER = routers.DefaultRouter()


class LedgerViewSet(viewsets.ModelViewSet):
    queryset = Ledger.objects.all()
    serializer_class = serializers.LedgerSerializer
    permission_classes = [IsOwnerOrReadOnly]
API_ROUTER.register(r'ledgers', LedgerViewSet)


class LedgerEntryViewSet(viewsets.ModelViewSet):
    queryset = LedgerEntry.objects.all()
    serializer_class = serializers.LedgerEntrySerializer
    permission_classes = [IsLedgerOwnerOrReadOnly]
API_ROUTER.register(r'entries', LedgerEntryViewSet)
