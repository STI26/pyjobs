from django_filters import rest_framework as filters
from .models import Vacancy, Company


class VacancyFilter(filters.FilterSet):
    min_salary = filters.NumberFilter(field_name='salary', lookup_expr='gte')
    max_salary = filters.NumberFilter(field_name='salary', lookup_expr='lte')
    position = filters.CharFilter(
        field_name='position',
        lookup_expr='icontains'
    )

    class Meta:
        model = Vacancy
        fields = ['position', 'min_salary', 'max_salary']


class CompanyFilter(filters.FilterSet):
    class Meta:
        model = Company
        fields = {'owner__id': ['exact']}
