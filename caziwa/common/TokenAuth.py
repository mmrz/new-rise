__author__ = 'rayatnia'
from rest_framework import authentication
from rest_framework import exceptions
from UserAPI.models import User,UserToken
from django.db.models import Q
from rest_framework import permissions

class TokenPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        return not request.user == None

class TokenAuthentication(authentication.BaseAuthentication):
    def authenticate(self, request):
        username = request.META.get('HTTP_TOKEN')
        uuid = request.META.get('HTTP_UUID')
        if not username:
            return None

        try:
            user = UserToken.objects.get(Q(token__value=username) & Q(uuid= uuid)).user
        except UserToken.DoesNotExist:
            raise exceptions.AuthenticationFailed('user not found')
        return (user, None)

def authenticate(request):
    username = request.META.get('HTTP_TOKEN')
    uuid = request.META.get('HTTP_UUID')
    if not username:
        return None

    try:
        user = UserToken.objects.get(Q(token__value=username) & Q(uuid= uuid)).user
    except UserToken.DoesNotExist:
        raise exceptions.AuthenticationFailed('user not found')
    return user