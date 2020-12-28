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
        return obj.skills.all().values('tag')

    def get_photo(self, obj):
        if not obj.owner.photo:
            return None

        request = self.context.get('request')
        photo_url = obj.owner.photo.url
        return request.build_absolute_uri(photo_url)

    def get_last_work(self, obj):
        return obj.owner.works.values('organization', 'position').last()


class ResumeDetailSerialazer(serializers.ModelSerializer):
    """Resume for detailed resume page."""

    owner = serializers.HiddenField(default=CurrentApplicantDefault())
    owner_info = serializers.SerializerMethodField()
    educations = serializers.SerializerMethodField()
    works = serializers.SerializerMethodField()
    skills = SkillField(many=True, required=False)

    class Meta:
        model = models.Resume
        fields = ['id', 'owner', 'owner_info', 'salary', 'position',
                  'skills', 'educations', 'works']

    def get_educations(self, obj):
        return obj.owner.educations.all().values(
            'id', 'institution', 'specialization', 'year_of_ending'
        )

    def get_works(self, obj):
        return obj.owner.works.all().values(
            'id', 'organization', 'position', 'join_date', 'termination_date'
        )

    def absolute_photo_url(self, obj):
        if not obj.owner.photo:
            return None

        request = self.context.get('request')
        photo_url = obj.owner.photo.url
        return request.build_absolute_uri(photo_url)

    def get_owner_info(self, obj):
        if obj.owner is None:
            return {}

        if not hasattr(obj, 'date_of_birth'):
            age = 0
        else:
            age = (now().date() - obj.owner.date_of_birth).days // 365.25

        return {
            'id': obj.owner.id,
            'user_id': obj.owner.profile.id,
            'bio': obj.owner.bio,
            'age': age,
            'photo': self.absolute_photo_url(obj),
            'name': obj.owner.profile.get_full_name(),
            'email': obj.owner.profile.email
        }

    def validate_owner(self, owner):
        if owner is None:
            raise serializers.ValidationError('owner can\'t be null.')
        return owner

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

            if skill.get('tag'):
                obj, _ = models.Skill.objects.get_or_create(
                    tag=skill['tag'].lower().strip()
                )
                validated_data.append(obj)

        return validated_data

    def create(self, validated_data):
        if not validated_data.get('skills'):
            return super().create(validated_data)

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
    educations = serializers.SerializerMethodField()
    works = serializers.SerializerMethodField()
    resumes = serializers.SerializerMethodField()

    class Meta:
        model = models.Applicant
        fields = ['id', 'profile', 'first_name', 'last_name',
                  'bio', 'date_of_birth', 'photo', 'works',
                  'educations', 'resumes']

    def get_first_name(self, obj):
        return obj.profile.first_name

    def get_last_name(self, obj):
        return obj.profile.last_name

    def get_educations(self, obj):
        return obj.educations.all().values(
            'id', 'institution', 'specialization', 'year_of_ending'
        )

    def get_works(self, obj):
        return obj.works.all().values(
            'id', 'organization', 'position', 'join_date', 'termination_date'
        )

    def get_resumes(self, obj):
        return obj.resumes.all().values('id', 'position')


class SkillSerialazer(serializers.ModelSerializer):

    class Meta:
        model = models.Skill
        fields = ['id', 'tag']


class EducationSerialazer(serializers.ModelSerializer):
    owner = serializers.HiddenField(default=CurrentApplicantDefault())

    class Meta:
        model = models.Education
        fields = ['id', 'owner', 'institution',
                  'specialization', 'year_of_ending']


class WorkSerialazer(serializers.ModelSerializer):
    owner = serializers.HiddenField(default=CurrentApplicantDefault())

    class Meta:
        model = models.Work
        fields = ['id', 'owner', 'organization', 'position',
                  'join_date', 'termination_date']
