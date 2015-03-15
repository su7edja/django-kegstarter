from rest_framework.permissions import BasePermission


class PollIsOpen(BasePermission):
    def has_object_permission(self, request, view, obj):
        return not obj.closed


class IsSelfOrReadOnly(BasePermission):
    def has_object_permission(self, request, view, obj):
        return bool(request.user == obj.user)
