from rest_framework import permissions
from apis.accounts.models import User


class IsAdminOrJournalist(permissions.BasePermission):
    def has_permission(self, request, view):
        user            =   request.user
        grant_access    =   str(user.role) in [role for role, value in User.ROLES if value in ['Admin','Staff']]
        return grant_access