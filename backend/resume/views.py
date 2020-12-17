from rest_framework.authentication import TokenAuthentication
from rest_framework import viewsets
from rest_framework import mixins
from rest_framework import permissions
from resume import permissions as custom_permissions

from dashboard.util import StandardResultsSetPagination
from . import models, serializers
from .filters import SkillFilter, ResumeFilter


class ApplicantDetail(mixins.RetrieveModelMixin,
                      mixins.CreateModelMixin,
                      mixins.UpdateModelMixin,
                      mixins.DestroyModelMixin,
                      viewsets.GenericViewSet):

    authentication_classes = [TokenAuthentication]
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly,
        custom_permissions.IsOwnerOrReadOnly
    ]

    queryset = models.Applicant.objects.all()
    serializer_class = serializers.ApplicantSerialazer


class SkillList(mixins.ListModelMixin,
                viewsets.GenericViewSet):

    authentication_classes = [TokenAuthentication]
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly
    ]

    queryset = models.Skill.objects.all()
    filter_class = SkillFilter
    serializer_class = serializers.SkillSerialazer


class ResumeViewSet(viewsets.ModelViewSet):

    authentication_classes = [TokenAuthentication]
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly,
        custom_permissions.IsOwnerOrReadOnly
    ]

    queryset = models.Resume.objects.all()
    filter_class = ResumeFilter
    search_fields = ['position', 'skills__tag']
    pagination_class = StandardResultsSetPagination
    serializer_class = serializers.ResumeDetailSerialazer
    action_serializers = {
        'list': serializers.ResumeListSerialazer
    }

    def get_serializer_class(self):

        if hasattr(self, 'action_serializers'):
            return self.action_serializers.get(self.action,
                                               self.serializer_class)

        return super().get_serializer_class()


class EducationDetail(mixins.RetrieveModelMixin,
                      mixins.CreateModelMixin,
                      mixins.UpdateModelMixin,
                      mixins.DestroyModelMixin,
                      viewsets.GenericViewSet):

    authentication_classes = [TokenAuthentication]
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly,
        custom_permissions.IsOwnerOrReadOnly
    ]

    queryset = models.Education.objects.all()
    serializer_class = serializers.EducationSerialazer


class WorkDetail(mixins.RetrieveModelMixin,
                 mixins.CreateModelMixin,
                 mixins.UpdateModelMixin,
                 mixins.DestroyModelMixin,
                 viewsets.GenericViewSet):

    authentication_classes = [TokenAuthentication]
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly,
        custom_permissions.IsOwnerOrReadOnly
    ]

    queryset = models.Work.objects.all()
    serializer_class = serializers.WorkSerialazer
