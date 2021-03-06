from rest_framework import serializers

from . import models


class VacancyUrlSerialazer(serializers.ModelSerializer):
    class Meta:
        model = models.Vacancy
        fields = ['id', 'position']


class CompanySerialazer(serializers.ModelSerializer):
    owner = serializers.HiddenField(default=serializers.CurrentUserDefault())
    vacancies = VacancyUrlSerialazer(many=True, read_only=True)

    class Meta:
        model = models.Company
        fields = ['id', 'owner', 'name', 'description',
                  'email', 'photo', 'vacancies']


class VacancyListSerialazer(serializers.ModelSerializer):
    """List of vacancies for main page."""

    company_name = serializers.SerializerMethodField()

    class Meta:
        model = models.Vacancy
        fields = ['id', 'company_name', 'salary', 'position']

    def get_company_name(self, obj):
        return obj.company.name


class VacancyDetailSerialazer(serializers.ModelSerializer):
    """Vacancy for detailed vacancy page."""

    company_info = serializers.SerializerMethodField()

    class Meta:
        model = models.Vacancy
        fields = ['id', 'company', 'company_info',
                  'salary', 'position', 'description']

    def absolute_photo_url(self, obj):
        if not obj.company.photo:
            return None

        request = self.context.get('request')
        photo_url = obj.company.photo.url
        return request.build_absolute_uri(photo_url)

    def get_company_info(self, obj):
        return {'id': obj.company.id,
                'user_id': obj.company.owner.id,
                'name': obj.company.name,
                'email': obj.company.email,
                'photo': self.absolute_photo_url(obj),
                'description': obj.company.description}
