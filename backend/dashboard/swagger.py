from drf_yasg import openapi
from rest_framework import status
from dashboard.serializers import (
    UserDetailSerializer
)


login_schema = {
    'responses': {
        status.HTTP_201_CREATED: openapi.Response(
            'Success',
            openapi.Schema(
                title='Register OK',
                type=openapi.TYPE_OBJECT,
                properties={
                    'token': openapi.Schema(title='Auth Token',
                                            type=openapi.TYPE_STRING),
                    'user_id': openapi.Schema(title='User ID',
                                              type=openapi.TYPE_NUMBER),
                    'username': openapi.Schema(title='User Name',
                                               type=openapi.TYPE_STRING),
                }
            )
        ),
        status.HTTP_401_UNAUTHORIZED: 'Login error',
    }
}

registration_schema = {
    'manual_parameters': [
        openapi.Parameter(
            'confirm', openapi.IN_QUERY,
            required=True,
            type=openapi.TYPE_STRING
        ),
    ],
    'query_serializer': UserDetailSerializer,
    'responses': {
        status.HTTP_201_CREATED: openapi.Response(
            'Success',
            openapi.Schema(
                title='Register OK',
                type=openapi.TYPE_OBJECT,
                properties={
                    'token': openapi.Schema(title='Auth Token',
                                            type=openapi.TYPE_STRING),
                    'user_id': openapi.Schema(title='User ID',
                                              type=openapi.TYPE_NUMBER),
                    'username': openapi.Schema(title='User Name',
                                               type=openapi.TYPE_STRING),
                }
            )
        ),
        status.HTTP_401_UNAUTHORIZED: 'Registration error',
    }
}
