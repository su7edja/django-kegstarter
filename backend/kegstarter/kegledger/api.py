from rest_framework import viewsets, routers
from rest_framework.permissions import AllowAny

from .models import Ledger, LedgerEntry
from . import serializers
from ..utils.permissions import IsOwnerOrReadOnly

API_ROUTER = routers.DefaultRouter()


class LedgerViewSet(viewsets.ModelViewSet):
    queryset = Ledger.objects.all()
    serializer_class = serializers.LedgerSerializer
    permission_classes = [IsOwnerOrReadOnly]
API_ROUTER.register(r'ledgers', LedgerViewSet)


class LedgerEntryViewSet(viewsets.ModelViewSet):
    queryset = LedgerEntry.objects.all()
    serializer_class = serializers.LedgerEntrySerializer
    permission_classes = [IsOwnerOrReadOnly]
API_ROUTER.register(r'entries', LedgerEntryViewSet)
