from django.forms import ModelForm, CheckboxSelectMultiple, ModelMultipleChoiceField
from main_site.models import Emotion, Value, GutterBumper, WeeklyMeal, MonthlyCheckin

class EmotionForm(ModelForm):
    class Meta:
        model = Emotion
        fields = ("name", "one_liner", "cause", "symptoms", "helpful")


class ValueForm(ModelForm):
    class Meta:
        model = Value
        fields = ("name", "explanation")

class GutterBumperForm(ModelForm):
    emotions = ModelMultipleChoiceField(queryset=Emotion.objects.all(), widget=CheckboxSelectMultiple(), required=False)

    class Meta:
        model = GutterBumper
        fields = ("date", "woke_up_at", "fell_asleep_at", "sleep_hrs", "work_hrs", "alone_hrs", "friend_hrs", "public_hrs", "relationship_hrs"
, "off", "worked_out", "meditated", "left_the_house", "travelling_or_out_of_routine", "nature_time", "number_of_sleep_beers","number_of_fun_beers", "presence", "happiness", "creativity", "morning_mood", "notes"
    , "emotions")


class WeeklyMealForm(ModelForm):
    class Meta:
        model = WeeklyMeal
        fields = ("ingredients", "preparation", "how_it_went", "week_start_date",)

class MonthlyCheckinForm(ModelForm):
    class Meta:
        model = MonthlyCheckin