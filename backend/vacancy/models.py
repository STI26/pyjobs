from django.db import models
from django.conf import settings


class Company(models.Model):
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='companies'
    )
    name = models.CharField(max_length=200, db_index=True)
    description = models.TextField(db_index=True)
    email = models.EmailField(max_length=200, blank=True)
    photo = models.CharField(max_length=400, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']


class Vacancy(models.Model):
    company = models.ForeignKey(
        'Company',
        on_delete=models.CASCADE,
        related_name='vacancies'
    )
    salary = models.PositiveIntegerField(null=True, blank=True)
    position = models.CharField(max_length=100, db_index=True)
    description = models.TextField(db_index=True)

    def __str__(self):
        return self.position

    class Meta:
        ordering = ['position']
