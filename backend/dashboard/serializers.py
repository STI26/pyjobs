from rest_framework import serializers
from .models import User


class UserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password', 'first_name', 'last_name', 'email']


class UserBaseDetailSerializer(serializers.ModelSerializer):
    applicant = serializers.SerializerMethodField()
    company = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'applicant', 'company']

    def get_applicant(self, obj):
        return (obj.applicant.pk if hasattr(obj, 'applicant') else None)

    def get_company(self, obj):
        return obj.companies.all().values(
            'id', 'name', 'vacancies__id', 'vacancies__position'
        )
