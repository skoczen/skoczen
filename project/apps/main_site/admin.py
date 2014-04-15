from django.contrib import admin
from main_site.models import Project

class ProjectAdmin(admin.ModelAdmin):
    list_display = ("title", "date_started", "url")
    model = Project


admin.site.register(Project, ProjectAdmin)
