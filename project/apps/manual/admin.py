from django.contrib import admin
from manual.models import Action, Emotion, Value, Workout, GutterBumper, WeeklyMeal, MonthlyCheckin, DataSensitivity, Restaurant, WeeklyGoal
from import_export.admin import ImportExportModelAdmin
from manual.export import GutterBumperResource, MonthlyCheckinResource

class GutterBumperAdmin(ImportExportModelAdmin):
    resource_class = GutterBumperResource

    list_display = ("date", "sleep_hrs","work_hrs","alone_hrs","friend_hrs","relationship_hrs","public_hrs","neap_hrs", "off","worked_out","meditated","number_of_fun_beers","number_of_sleep_beers","presence","happiness","creativity","morning_mood", "unbusy", "burnt_out",)
    list_filter = ("date",)
    # search_fields = ('name','description',)
    # exclude = ("slug",)


class MonthlyCheckinAdmin(ImportExportModelAdmin):
    resource_class = MonthlyCheckinResource

class RestaurantOptions(admin.ModelAdmin):
    list_display = ("name", "have_gone", "meal", "rating")
    list_filter = ("meal", "rating", "have_gone")
    

admin.site.register(Action)
admin.site.register(Emotion)
admin.site.register(Value)
admin.site.register(Workout)
admin.site.register(WeeklyMeal)
admin.site.register(MonthlyCheckin, MonthlyCheckinAdmin)
admin.site.register(DataSensitivity)
admin.site.register(WeeklyGoal)
admin.site.register(Restaurant, RestaurantOptions)
admin.site.register(GutterBumper, GutterBumperAdmin)