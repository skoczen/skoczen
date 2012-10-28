from django.contrib import admin
from hiking.models import Hike
    

class HikeOptions(admin.ModelAdmin):
    list_display = ("left_on", "expected_back","have_left","is_back","brought_everything")
    list_filter = ("date",)
    # search_fields = ('name','description',)
    # exclude = ("slug",)
    
admin.site.register(Hike, HikeOptions)