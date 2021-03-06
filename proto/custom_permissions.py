from rest_framework import permissions

SAFE_METHODS = ['GET', 'HEAD', 'OPTIONS']


class GetOnly(permissions.AllowAny):
    """
    The request is authenticated as a user, or is a get-only request.
    """

    def has_permission(self, request, view):
        if (request.method in SAFE_METHODS or
            request.user and
                request.user.is_staff()):
            return True
        return False
