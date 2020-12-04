from django.contrib import admin

from . import models


class ResumeAdmin(admin.ModelAdmin):
    filter_horizontal = ['skills']


admin.site.register(models.Applicant, admin.ModelAdmin)
admin.site.register(models.Resume, ResumeAdmin)
admin.site.register(models.Education, admin.ModelAdmin)
admin.site.register(models.Work, admin.ModelAdmin)
admin.site.register(models.Skill, admin.ModelAdmin)
