from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsLedgerOwnerOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        if view.action_map['get'] == 'list' and request.method not in SAFE_METHODS:
            ledger_owner = view.queryset.model.ledger.get_queryset()[0].user
            return ledger_owner == request.user
        return True

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        else:
            return obj.ledger.user == request.user
