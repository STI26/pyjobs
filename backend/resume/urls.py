from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import views


router = DefaultRouter()
router.register('skill', views.SkillList)
router.register('resume', views.ResumeViewSet)
router.register('applicant', views.ApplicantDetail)
router.register('education', views.EducationDetail)
router.register('work', views.WorkDetail)


urlpatterns = [
    path('', include(router.urls)),
]
