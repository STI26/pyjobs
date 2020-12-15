from django_filters import rest_framework as filters
from .models import Resume, Skill


class SkillFilter(filters.FilterSet):
    class Meta:
        model = Skill
        fields = {'tag': ['exact', 'in', 'startswith']}


class ResumeFilter(filters.FilterSet):
    min_salary = filters.NumberFilter(field_name='salary', lookup_expr='gte')
    max_salary = filters.NumberFilter(field_name='salary', lookup_expr='lte')
    position = filters.CharFilter(
        field_name='position',
        lookup_expr='icontains'
    )
    min_birth = filters.DateFilter(
        field_name='owner__date_of_birth',
        lookup_expr='gte'
    )
    max_birth = filters.DateFilter(
        field_name='owner__date_of_birth',
        lookup_expr='lte'
    )

    class Meta:
        model = Resume
        fields = ['position', 'min_salary', 'max_salary',
                  'min_birth', 'max_birth']
