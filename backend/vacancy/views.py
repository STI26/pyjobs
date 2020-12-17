from rest_framework.authentication import TokenAuthentication
from rest_framework import viewsets
from rest_framework import permissions
from vacancy import permissions as custom_permissions

from dashboard.util import StandardResultsSetPagination
from . import models, serializers
from .filters import VacancyFilter, CompanyFilter


class CompanyViewSet(viewsets.ModelViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly,
        custom_permissions.IsOwnerOrReadOnly
    ]

    queryset = models.Company.objects.all()
    filter_class = CompanyFilter
    serializer_class = serializers.CompanySerialazer


class VacancyViewSet(viewsets.ModelViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly,
        custom_permissions.IsOwnerOrReadOnly
    ]

    queryset = models.Vacancy.objects.all()
    filter_class = VacancyFilter
    search_fields = ['position', 'company__description']
    pagination_class = StandardResultsSetPagination
    serializer_class = serializers.VacancyDetailSerialazer
    action_serializers = {
        'list': serializers.VacancyListSerialazer
    }

    def get_serializer_class(self):

        if hasattr(self, 'action_serializers'):
            return self.action_serializers.get(self.action,
                                               self.serializer_class)

        return super().get_serializer_class()
