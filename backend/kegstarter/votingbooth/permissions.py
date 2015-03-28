from rest_framework.permissions import BasePermission


class PollIsNotClosed(BasePermission):
    def has_object_permission(self, request, view, obj):
        if hasattr(obj, 'closed'):
            return not obj.closed
        elif hasattr(obj, 'poll'):
            return not obj.poll.closed
        else:
            raise AttributeError('{} is not associated with a poll.'.format(obj))
