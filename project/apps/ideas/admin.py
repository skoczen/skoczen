from django.contrib import admin
from ideas.models import Idea


class IdeaOptions(admin.ModelAdmin):
    list_display = ("title", "thought_of_date", "status",)
    list_filter = ("thought_of_date", "status")
    search_fields = ('title', 'idea',)

admin.site.register(Idea, IdeaOptions)
