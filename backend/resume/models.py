from django.db import models
from django.conf import settings
from django.core.validators import MinValueValidator, MaxValueValidator


class Applicant(models.Model):
    profile = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='applicant'
    )
    bio = models.TextField(db_index=True)
    date_of_birth = models.DateField(null=True, blank=True)
    photo = models.URLField(max_length=400, blank=True)

    def __str__(self):
        return self.profile.username

    class Meta:
        ordering = ['profile__username']


class Skill(models.Model):
    name = models.CharField(max_length=100, unique=True, db_index=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']


class Resume(models.Model):
    owner = models.ForeignKey(
        'Applicant',
        on_delete=models.CASCADE,
        related_name='resumes'
    )
    salary = models.PositiveIntegerField(blank=True, null=True)
    position = models.CharField(max_length=100, db_index=True)
    skills = models.ManyToManyField('Skill', blank=True, db_index=True)

    def __str__(self):
        return self.position

    class Meta:
        ordering = ['position']


class Education(models.Model):
    owner = models.ForeignKey(
        'Applicant',
        on_delete=models.CASCADE,
        related_name='educations'
    )
    institution = models.CharField(max_length=100)
    specialization = models.CharField(max_length=100)
    year_of_ending = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(1000), MaxValueValidator(9999)]
    )

    def __str__(self):
        return f'{self.year_of_ending} - {self.institution}'

    class Meta:
        ordering = ['-year_of_ending']


class Work(models.Model):
    owner = models.ForeignKey(
        'Applicant',
        on_delete=models.CASCADE,
        related_name='works'
    )
    organization = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    join_date = models.DateField()
    termination_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return f'{self.organization}: {self.join_date}-{self.termination_date}'

    class Meta:
        ordering = ['-join_date']
