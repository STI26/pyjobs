from rest_framework import serializers
from .models import User


class UserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password', 'first_name', 'last_name', 'email']


class UserBaseDetailSerializer(serializers.ModelSerializer):
    applicant = serializers.SerializerMethodField()
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'applicant']
    
    def get_applicant(self, obj):
        return (obj.applicant.pk if hasattr(obj, 'applicant') else None)
