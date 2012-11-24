from django.contrib import admin
from manual.models import Emotion, Value, GutterBumper, WeeklyMeal, MonthlyCheckin, DataSensitivity, Restaurant
    

class GutterBumperOptions(admin.ModelAdmin):
    list_display = ("date", "sleep_hrs","work_hrs","alone_hrs","friend_hrs","relationship_hrs","public_hrs","off","worked_out","meditated","number_of_fun_beers","number_of_sleep_beers","presence","happiness","creativity","morning_mood")
    list_filter = ("date",)
    # search_fields = ('name','description',)
    # exclude = ("slug",)

class RestaurantOptions(admin.ModelAdmin):
    list_display = ("name", "have_gone", "meal", "rating")
    list_filter = ("meal", "rating", "have_gone")
    

admin.site.register(Emotion)
admin.site.register(Value)
admin.site.register(WeeklyMeal)
admin.site.register(MonthlyCheckin)
admin.site.register(DataSensitivity)
admin.site.register(Restaurant, RestaurantOptions)
admin.site.register(GutterBumper, GutterBumperOptions)