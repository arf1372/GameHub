from rest_framework import permissions
from rest_framework.compat import is_authenticated


class IsCreationOrIsRetrievalOrIsAuthenticated(permissions.BasePermission):
    def has_permission(self, request, view):
        return (request.user and is_authenticated(request.user)) or view.action == 'create' or view.action == 'retrieve'
