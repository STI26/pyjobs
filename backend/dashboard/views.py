from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authentication import TokenAuthentication
from rest_framework import viewsets, mixins, permissions, status
from django.contrib.auth import get_user_model
from django.db import IntegrityError

from drf_yasg.utils import swagger_auto_schema
import dashboard.swagger as swagger_schemas

from dashboard import permissions as custom_permissions
from dashboard.serializers import (
    UserDetailSerializer,
    UserBaseDetailSerializer
)

from datetime import datetime
from .models import User
from .util import get_base_info

import logging

# Get an instance of a logger
log = logging.getLogger(__name__)


class LoginWithAuthToken(ObtainAuthToken):
    """
    Class based view loggin in user and returning
    Auth Token, User ID, username.
    """

    @swagger_auto_schema(**swagger_schemas.login_schema)
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})

        if not serializer.is_valid():
            return Response(serializer._errors,
                            status=status.HTTP_401_UNAUTHORIZED)

        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)

        response_data = {'token': token.key,
                         'user_id': user.pk,
                         'username': user.username}

        log.info(f'Login: {user.username} - {datetime.now()}')
        log.info(get_base_info(request))

        return Response(response_data, status=status.HTTP_201_CREATED)


class RegisterWithAuthToken(APIView):
    """Class based view registration."""

    @swagger_auto_schema(**swagger_schemas.registration_schema)
    def post(self, request, *args, **kwargs):

        # Ensure fields are correct
        serializer = UserDetailSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer._errors,
                            status=status.HTTP_401_UNAUTHORIZED)

        # Ensure password matches confirmation
        if not (request.data.get('password') and request.data.get('confirm')
                and request.data['password'] == request.data['confirm']):
            serializer._errors['confirm'] = ['Passwords must match.']

            log.info('Registration failed(password matches confirmation):')
            log.info('User: {} - {}'.format(
                request.data.get("username"),
                datetime.now()
            ))
            log.info(get_base_info(request))
            return Response(serializer._errors,
                            status=status.HTTP_401_UNAUTHORIZED)

        # Attempt to create new user
        User = get_user_model()
        try:
            user = User.objects.create_user(**serializer.validated_data)
            user.save()
        except IntegrityError:
            serializer._errors['confirm'] = ['Invalid username.']
            return Response(serializer._errors,
                            status=status.HTTP_401_UNAUTHORIZED)
        token, created = Token.objects.get_or_create(user=user)

        response_data = {'token': token.key,
                         'user_id': user.pk,
                         'username': user.username}

        log.info(f'Registration: {user.username} - {datetime.now()}')
        log.info(get_base_info(request))

        return Response(response_data, status=status.HTTP_201_CREATED)


class Logout(APIView):
    """Class based view logout."""

    def post(self, request, format=None):
        if request.user.is_authenticated:
            log.info(f'Logout: {request.user.username} - {datetime.now()}')
            log.info(get_base_info(request))
            request.user.auth_token.delete()
        return Response(status=status.HTTP_200_OK)


class UserDetail(mixins.RetrieveModelMixin,
                 mixins.UpdateModelMixin,
                 mixins.DestroyModelMixin,
                 viewsets.GenericViewSet):

    authentication_classes = [TokenAuthentication]
    permission_classes = [
        permissions.IsAuthenticated,
        custom_permissions.IsYourselfOrReadOnly
    ]

    queryset = User.objects.all()
    serializer_class = UserBaseDetailSerializer
