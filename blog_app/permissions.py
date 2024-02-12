from rest_framework import permissions

class IsOwnerOnlyRead(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.owner == request.user
    

class IsCommentOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        # Check if the request user is the owner of the comment
        return obj.user == request.user
