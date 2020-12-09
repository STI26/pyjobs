from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register('', views.UserDetail)


urlpatterns = [
    path('register/', views.RegisterWithAuthToken.as_view()),
    path('login/', views.LoginWithAuthToken.as_view()),
    path('logout/', views.Logout.as_view()),
    path('profile/', include(router.urls))
]
