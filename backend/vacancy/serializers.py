from rest_framework import serializers

from . import models


class VacancyUrlSerialazer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Vacancy
        fields = ['url', 'position']


class CompanySerialazer(serializers.ModelSerializer):
    owner = serializers.HiddenField(default=serializers.CurrentUserDefault())
    vacancies = VacancyUrlSerialazer(many=True)

    class Meta:
        model = models.Company
        fields = ['owner', 'name', 'description', 'vacancies']


class VacancyListSerialazer(serializers.ModelSerializer):
    """List of vacancies for main page."""

    company_name = serializers.SerializerMethodField()

    class Meta:
        model = models.Vacancy
        fields = ['company_name', 'salary', 'position']

    def get_company_name(self, obj):
        return obj.company.name


class VacancyDetailSerialazer(serializers.ModelSerializer):
    """Vacancy for detailed vacancy page."""

    company_info = serializers.SerializerMethodField()

    class Meta:
        model = models.Vacancy
        fields = ['company', 'company_info', 'salary',
                  'position', 'description']

    def get_company_info(self, obj):
        return {'name': obj.company.name,
                'description': obj.company.description}
