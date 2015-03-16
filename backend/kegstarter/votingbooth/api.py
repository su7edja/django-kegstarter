from rest_framework import viewsets, routers
from rest_framework.permissions import SAFE_METHODS, IsAdminUser

from .models import Poll, Rating, Vote
from .permissions import PollIsOpen
from . import serializers
from ..utils.permissions import IsOwnerOrReadOnly


API_ROUTER = routers.DefaultRouter()

# To set different permissions for list and detail:
# http://stackoverflow.com/questions/25283797/django-rest-framework-add-additional-permission-in-viewset-update-method
# If decorators don't work, explicitly define get_permissions


class PollViewSet(viewsets.ModelViewSet):
    queryset = Poll.objects.all()
    serializer_class = serializers.PollSerializer

    def get_permissions(self):
        # Only open polls can be edited and only admin can edit
        if self.request.method not in SAFE_METHODS:
            self.permission_classes = [PollIsOpen, IsAdminUser]

        return super(PollViewSet, self).get_permissions()

API_ROUTER.register(r'polls', PollViewSet)


class RatingViewSet(viewsets.ModelViewSet):
    queryset = Rating.objects.all()
    serializer_class = serializers.RatingSerializer

    def get_permissions(self):
        # Only self can change own rating
        if self.request.method not in SAFE_METHODS:
            self.permission_classes = [IsOwnerOrReadOnly]

        return super(RatingViewSet, self).get_permissions()

API_ROUTER.register(r'ratings', RatingViewSet)


class VoteViewSet(viewsets.ModelViewSet):
    queryset = Vote.objects.all()
    serializer_class = serializers.VoteSerializer

    def get_permissions(self):
        # Only self can change own vote and poll must still be open
        if self.request.method not in SAFE_METHODS:
            self.permission_classes = [PollIsOpen, IsOwnerOrReadOnly]

        return super(VoteViewSet, self).get_permissions()

API_ROUTER.register(r'votes', VoteViewSet)
