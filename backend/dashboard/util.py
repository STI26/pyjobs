from rest_framework import serializers
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from django.core.files.storage import FileSystemStorage

from django.conf import settings
from pathlib import Path, PurePath


class CurrentApplicantDefault:
    requires_context = True

    def __call__(self, serializer_field):
        return serializer_field.context['request'].user.applicant

    def __repr__(self):
        return '%s()' % self.__class__.__name__


class SkillField(serializers.StringRelatedField):
    def to_representation(self, value):
        return {'tag': value.tag}

    def to_internal_value(self, data):
        return data


class StandardResultsSetPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 1000

    def get_paginated_response(self, data):
        paginator = {
            'previous': self.page.has_previous() and self.page.previous_page_number(),
            'current': self.page.number,
            'next': self.page.has_next() and self.page.next_page_number(),
            'num_pages': self.page.paginator.num_pages,
        }
        return Response({
            'paginator': paginator,
            'results': data
        })


class MediaFileSystemStorage(FileSystemStorage):
    def get_available_name(self, name, max_length=None):
        if max_length and len(name) > max_length:
            raise(Exception("name's length is greater than max_length"))
        return name

    def _save(self, name, content):
        if self.exists(name):
            path = PurePath(settings.MEDIA_ROOT).joinpath(name)
            Path(path).unlink(missing_ok=True)
        return super()._save(name, content)


def get_base_info(request):
    return '--IP: {}; OS: {}\n--Browser: {}'.format(
        request.META.get('REMOTE_ADDR'),
        request.META.get('XDG_CURRENT_DESKTOP'),
        request.META.get('HTTP_USER_AGENT')
    )
