from rest_framework import serializers


class CurrentApplicantDefault:
    requires_context = True

    def __call__(self, serializer_field):
        return serializer_field.context['request'].user.applicant

    def __repr__(self):
        return '%s()' % self.__class__.__name__


class SkillField(serializers.StringRelatedField):
    def to_representation(self, value):
        return {'name': value.name}

    def to_internal_value(self, data):
        return data
