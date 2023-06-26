from rest_framework import permissions


class IsAdminOrAuthor(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):  # noqa
        return bool(
            request.method in permissions.SAFE_METHODS or
            obj.author == request.user or
            request.user.is_superuser
        )


class IsAboveOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):  # noqa
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.news.author == request.user
