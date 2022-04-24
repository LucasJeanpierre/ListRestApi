from rest_framework.permissions import BasePermission
 
class IsAdminAuthenticated(BasePermission):
    
    def __init__(self, group_name=None):
        super().__init__()
        self.group_name = group_name
 
    def has_permission(self, request, view):
        return bool(request.user and request.user.is_authenticated and request.user.is_superuser)

class IsUserInCorrectGroup(BasePermission):

    def __init__(self, group_name):
        super().__init__()
        self.group_name = group_name

    def has_permission(self, request, view):
        return bool(request.user and request.user.is_authenticated and request.user.groups.filter(name=self.group_name).exists())

class IsUserAuthenticated(BasePermission):

    def __init__(self, group_name=None):
        super().__init__()
        self.group_name = group_name
 
    def has_permission(self, request, view):
        return bool(request.user and request.user.is_authenticated)