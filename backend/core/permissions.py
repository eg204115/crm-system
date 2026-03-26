from rest_framework.permissions import BasePermission, SAFE_METHODS

class RoleBasedPermission(BasePermission):
    """
    Admin  -> Full access
    Manager -> Create + Update
    Staff -> Read (and optionally Create)
    """

    def has_permission(self, request, view):
        user = request.user

        # Must be authenticated
        if not user or not user.is_authenticated:
            return False

        # Admin → full access
        if user.role == 'ADMIN':
            return True

        # Manager
        if user.role == 'MANAGER':
            if request.method == 'DELETE':
                return False
            return True

        # Staff
        if user.role == 'STAFF':
            if request.method in SAFE_METHODS:
                return True  # GET, HEAD, OPTIONS
            if request.method == 'POST':
                return True  # optional (you can restrict if needed)
            return False  # no PUT/PATCH/DELETE

        return False