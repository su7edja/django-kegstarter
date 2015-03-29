from rest_framework.permissions import BasePermission


class IsLedgerOwnerOrReadOnly(BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.ledger.owner == request.user
