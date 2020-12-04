from django.contrib import admin

from . import models


admin.site.register(models.Company, admin.ModelAdmin)
admin.site.register(models.Vacancy, admin.ModelAdmin)
