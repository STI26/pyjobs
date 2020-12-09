from rest_framework import permissions


class BaseIsOwnerOrReadOnly(permissions.BasePermission):
    """
    Object-level permission to only allow owners of an object to edit it.
    """

    owner_field = ''
    link_to_owner_field = ''

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return True

        if hasattr(obj, self.owner_field):
            owner = obj.__getattribute__(self.owner_field)
        else:
            owner = obj.__getattribute__(self.link_to_owner_field) \
                        .__getattribute__(self.owner_field)

        return owner == request.user


class IsYourselfOrReadOnly(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj == request.user
