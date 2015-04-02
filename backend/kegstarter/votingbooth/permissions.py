from rest_framework.permissions import BasePermission

from kegstarter.votingbooth.models import Vote, Poll


class PollIsNotClosed(BasePermission):
    def has_object_permission(self, request, view, obj):
        if isinstance(obj, Poll):
            return not obj.closed
        elif isinstance(obj, Vote):
            return not obj.poll.closed
