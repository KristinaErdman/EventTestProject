from rest_framework.permissions import BasePermission, SAFE_METHODS

from users.models import User


class ForManagerOrReadOnlyPermission(BasePermission):
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        else:
            if not request.user.is_anonymous:
                return request.user.type == User.Type.MANAGER
            else:
                return False

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        else:
            if not request.user.is_anonymous:
                return obj.manager == request.user
            else:
                return False


class ForGuestOrReadOnlyPermission(BasePermission):
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        else:
            if not request.user.is_anonymous:
                return request.user.type == User.Type.MANAGER
            else:
                return False

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        else:
            if not request.user.is_anonymous:
                return obj.manager == request.user
            else:
                return False
