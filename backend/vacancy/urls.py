from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import views


router = DefaultRouter()
router.register('company', views.CompanyViewSet)
router.register('vacancy', views.VacancyViewSet)


urlpatterns = [
    path('', include(router.urls))
]
