from rest_framework import permissions


class UpdateOwnProfile(permissions.BasePermission):
    """Check if the user updates there own profile only"""

    def has_object_permission(self,request,view,obj):

        if request.method is permissions.SAFE_METHODS:
            return True

        return obj.id == request.user.id 
