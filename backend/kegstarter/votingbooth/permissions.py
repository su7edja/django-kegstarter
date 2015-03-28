from rest_framework.permissions import BasePermission


class PollIsNotClosed(BasePermission):
    def has_object_permission(self, request, view, obj):
        return not obj.closed
