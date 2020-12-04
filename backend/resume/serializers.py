from rest_framework import serializers
from django.utils.timezone import now

from dashboard.util import CurrentApplicantDefault, SkillField
from . import models


class ResumeListSerialazer(serializers.ModelSerializer):
    """List of resumes for main page."""

    age = serializers.SerializerMethodField()
    skills = serializers.SerializerMethodField()
    photo = serializers.SerializerMethodField()
    last_work = serializers.SerializerMethodField()

    class Meta:
        model = models.Resume
        fields = ['id', 'salary', 'position', 'age',
                  'skills', 'photo', 'last_work']

    def get_age(self, obj):
        age = (now().date() - obj.owner.date_of_birth).days // 365.25
        return int(age)

    def get_skills(self, obj):
        return obj.skills.all().values('name')

    def get_photo(self, obj):
        return obj.owner.photo

    def get_last_work(self, obj):
        return obj.owner.works.values('organization', 'position').last()


class ResumeDetailSerialazer(serializers.ModelSerializer):
    """Resume for detailed resume page."""

    owner = serializers.HiddenField(default=CurrentApplicantDefault())
    educations = serializers.SerializerMethodField()
    works = serializers.SerializerMethodField()
    skills = SkillField(many=True)

    class Meta:
        model = models.Resume
        fields = ['id', 'owner', 'salary', 'position',
                  'skills', 'educations', 'works']

    def get_educations(self, obj):
        return obj.owner.educations.all().values(
            'id', 'institution', 'specialization', 'year_of_ending'
        )

    def get_works(self, obj):
        return obj.owner.works.all().values(
            'id', 'organization', 'position', 'join_date', 'termination_date'
        )

    def validate_skills(self, skills):
        if not isinstance(skills, list):
            raise serializers.ValidationError(
                'the `skills` field should be of type `list`.'
            )

        validated_data = []
        for skill in skills:
            if not isinstance(skill, dict):
                raise serializers.ValidationError(
                    'the `skill` field should be of type `dict`.'
                )

            if skill.get('name'):
                obj, _ = models.Skill.objects.get_or_create(
                    name=skill['name'].lower().strip()
                )
                validated_data.append(obj)

        return validated_data

    def create(self, validated_data):
        skills = validated_data.pop('skills')
        resume = models.Resume.objects.create(**validated_data)

        for skill in skills:
            resume.skills.add(skill)
        return resume

    def update(self, instance, validated_data):
        instance.salary = validated_data.get('salary', instance.salary)
        instance.position = validated_data.get('position', instance.position)
        if validated_data.get('skills'):
            instance.skills.set(validated_data.get('skills'))
        return instance


class ApplicantSerialazer(serializers.ModelSerializer):
    """Applicant for detailed resume page."""

    profile = serializers.HiddenField(default=serializers.CurrentUserDefault())
    first_name = serializers.SerializerMethodField()
    last_name = serializers.SerializerMethodField()

    class Meta:
        model = models.Applicant
        fields = ['profile', 'first_name', 'last_name',
                  'bio', 'date_of_birth', 'photo']

    def get_first_name(self, obj):
        return obj.profile.first_name

    def get_last_name(self, obj):
        return obj.profile.last_name


class SkillSerialazer(serializers.ModelSerializer):

    class Meta:
        model = models.Skill
        fields = ['id', 'name']


class EducationSerialazer(serializers.ModelSerializer):
    owner = serializers.HiddenField(default=CurrentApplicantDefault())

    class Meta:
        model = models.Education
        fields = ['owner', 'institution', 'specialization', 'year_of_ending']


class WorkSerialazer(serializers.ModelSerializer):
    owner = serializers.HiddenField(default=CurrentApplicantDefault())

    class Meta:
        model = models.Work
        fields = ['owner', 'organization', 'position',
                  'join_date', 'termination_date']
