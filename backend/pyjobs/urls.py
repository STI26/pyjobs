from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('dashboard.urls')),
    path('api/resumes/', include('resume.urls')),
    path('api/vacancies/', include('vacancy.urls')),
]
