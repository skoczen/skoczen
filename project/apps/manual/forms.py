from django.forms import ModelForm, CheckboxSelectMultiple, ModelMultipleChoiceField
from manual.models import Action, Emotion, Value, GutterBumper, WeeklyMeal, MonthlyCheckin, WeeklyGoal

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
    actions = ModelMultipleChoiceField(queryset=Action.objects.all(), widget=CheckboxSelectMultiple(), required=False)

    class Meta:
        model = GutterBumper
        fields = ("date", "woke_up_at", "fell_asleep_at", "sleep_hrs", "work_hrs", "alone_hrs", "friend_hrs", "public_hrs", "relationship_hrs"
, "off", "worked_out", "meditated", "left_the_house", "travelling_or_out_of_routine", "nature_time", "number_of_sleep_beers","number_of_fun_beers", "presence", "happiness", "creativity", "morning_mood", "unbusy", "burnt_out", "presence_set", "happiness_set", "creativity_set", "morning_mood_set", "unbusy_set", "burnt_out_set", "notes"
    , "emotions", "actions", "interacted_with_art", "sex",)


class WeeklyMealForm(ModelForm):
    class Meta:
        model = WeeklyMeal
        fields = ("ingredients", "preparation", "how_it_went", "week_start_date",)

class MonthlyCheckinForm(ModelForm):
    class Meta:
        model = MonthlyCheckin

class WeeklyGoalForm(ModelForm):
    class Meta:
        fields = ("primary", "secondary", "tertiary")
        model = WeeklyGoal