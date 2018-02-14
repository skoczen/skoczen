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


class WeeklyMealForm(ModelForm):
    class Meta:
        model = WeeklyMeal
        fields = ("ingredients", "preparation", "how_it_went", "week_start_date",)
