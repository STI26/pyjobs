from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from django.contrib.auth import get_user_model
from django.db import IntegrityError

from dashboard.serializers import UserDetailSerializer


class LoginWithAuthToken(ObtainAuthToken):
    """
    Class based view loggin in user and returning
    Auth Token, User ID, username.
    """

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

        return Response(response_data, status=status.HTTP_201_CREATED)


class RegisterWithAuthToken(APIView):
    """Class based view registration."""

    def post(self, request, *args, **kwargs):

        # Ensure fields are correct
        serializer = UserDetailSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer._errors,
                            status=status.HTTP_400_BAD_REQUEST)

        # Ensure password matches confirmation
        if not (request.data.get('password') and request.data.get('confirm')
                and request.data['password'] == request.data['confirm']):
            serializer._errors['confirm'] = ['Passwords must match.']
            return Response(serializer._errors,
                            status=status.HTTP_400_BAD_REQUEST)

        # Attempt to create new user
        User = get_user_model()
        try:
            user = User.objects.create_user(**serializer.validated_data)
            user.save()
        except IntegrityError:
            serializer._errors['confirm'] = ['Invalid username.']
            return Response(serializer._errors,
                            status=status.HTTP_400_BAD_REQUEST)
        token, created = Token.objects.get_or_create(user=user)

        response_data = {'token': token.key,
                         'user_id': user.pk,
                         'username': user.username}

        return Response(response_data, status=status.HTTP_201_CREATED)


class Logout(APIView):
    """Class based view logout."""

    def post(self, request, format=None):
        if request.user.is_authenticated:
            request.user.auth_token.delete()
        return Response(status=status.HTTP_200_OK)
