from rest_framework.permissions import SAFE_METHODS, BasePermission


class IsOwnerOrReadOnly(BasePermission):
    def has_object_permission(self, request, view, obj):
        try:
            owner = getattr(obj, 'owner')
        except AttributeError:
            owner = getattr(obj, 'user')
        return bool(request.method in SAFE_METHODS or
                    request.user == owner)
