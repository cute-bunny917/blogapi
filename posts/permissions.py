# posts/permissions.py
from rest_framework import permissions

# custom class IsAuthorOrReadOnly which extends BasePermission.
class IsAuthorOrReadOnly(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        # Read-only permissions are allowed for any request
        # SAFE_METHODS– a tuple containing GET, OPTIONS, and HEAD
        if request.method in permissions.SAFE_METHODS:
            return True

        # Write permissions are only allowed to the author of a post
        return obj.author == request.user
