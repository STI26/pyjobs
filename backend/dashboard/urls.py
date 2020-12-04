from django.urls import path

from . import views


urlpatterns = [
    path('register/', views.RegisterWithAuthToken.as_view()),
    path('login/', views.LoginWithAuthToken.as_view()),
    path('logout/', views.Logout.as_view())
]
