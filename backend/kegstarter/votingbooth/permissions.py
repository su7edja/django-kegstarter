from rest_framework.permissions import BasePermission


class PollIsOpen(BasePermission):
    def has_object_permission(self, request, view, obj):
        return not obj.closed
