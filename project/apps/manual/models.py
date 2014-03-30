import datetime
import time

from django.core.urlresolvers import reverse
from django.conf import settings
from django.db import models
from django.db.models import Avg, Sum
from django.template.defaultfilters import slugify
import fitbit

BUMPER_STATUS_GOOD = "green"
BUMPER_STATUS_BORDERLINE = "yellow"
BUMPER_STATUS_BAD = "red"
MEALS = [
    ("breakfast", "Breakfast"),
    ("brunch", "Brunch"),
    ("lunch", "Lunch"),
    ("dinner", "Dinner"),
    ("dessert", "Dessert"),
    ("snack", "Snack"),
]


class BaseModel(models.Model):
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

    def __unicode__(self):
        return "%s" % self.name


class DataSensitivity(BaseModel):
    name = models.CharField(max_length=200)


# Create your models here.
class Emotion(BaseModel):
    name = models.CharField(max_length=200)
    slug = models.CharField(max_length=210, blank=True, null=True, editable=False)
    one_liner = models.TextField(blank=True, null=True)
    cause = models.TextField(blank=True, null=True, verbose_name="Causes")
    symptoms = models.TextField(blank=True, null=True)
    helpful = models.TextField(blank=True, null=True)

    class Meta:
        ordering = ("name",)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Emotion, self).save(*args, **kwargs)

class Value(BaseModel):
    name = models.CharField(max_length=200, verbose_name='Story name')
    slug = models.CharField(max_length=210, blank=True, null=True, editable=False)
    explanation = models.TextField(blank=True, null=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Value, self).save(*args, **kwargs)


class GutterBumper(BaseModel):
    date = models.DateField(default=datetime.date.today())
    woke_up_at = models.TimeField(default=datetime.time(8, 30))
    fell_asleep_at = models.TimeField(default=datetime.time(0, 00))
    sleep_hrs = models.FloatField(default=0, blank=True, null=True, verbose_name="Sleep", help_text="Sleep this morning")
    work_hrs = models.FloatField(default=0, blank=True, null=True, verbose_name="Work")
    alone_hrs = models.FloatField(default=0, blank=True, null=True, verbose_name="Alone")
    friend_hrs = models.FloatField(default=0, blank=True, null=True, verbose_name="Friend")
    public_hrs = models.FloatField(default=0, blank=True, null=True, help_text="Not specifically hanging with people, but in a larger crowd", verbose_name="Public")
    relationship_hrs = models.FloatField(default=0, blank=True, null=True, verbose_name="Relationship")

    off = models.BooleanField(default=False)
    sex = models.IntegerField(default=0)
    interacted_with_art = models.BooleanField(default=False)
    worked_out = models.BooleanField(default=False)
    meditated = models.BooleanField(default=False, verbose_name="meditated")
    left_the_house = models.BooleanField(default=False)
    nature_time = models.BooleanField(default=False)
    inbox_zero = models.BooleanField(default=False)
    travelling_or_out_of_routine = models.BooleanField(default=False, verbose_name="Travelling/Nonroutine")
    number_of_sleep_beers = models.IntegerField(blank=True, null=True, verbose_name="# of sleep beers")
    number_of_fun_beers = models.IntegerField(blank=True, null=True, verbose_name="# of fun beers")
    presence = models.IntegerField(blank=True, null=True, help_text="1-10")
    happiness = models.IntegerField(blank=True, null=True, help_text="1-10")
    creativity = models.IntegerField(blank=True, null=True, help_text="1-10")
    morning_mood = models.IntegerField(blank=True, null=True, help_text="1-10")
    unbusy = models.IntegerField(blank=True, null=True, help_text="1-10")
    presence_set = models.BooleanField(default=False)
    happiness_set = models.BooleanField(default=False)
    creativity_set = models.BooleanField(default=False)
    morning_mood_set = models.BooleanField(default=False)
    unbusy_set = models.BooleanField(default=False)
    notes = models.TextField(blank=True, null=True, default="86400")
    weight = models.FloatField(blank=True, null=True)
    body_fat_percent = models.FloatField(blank=True, null=True)

    emotions = models.ManyToManyField(Emotion, blank=True, null=True, verbose_name="Top three emotions")

    # ouchmotions?
    # yaymotions?

    class Meta:
        ordering = ("date",)

    @property
    def saw_friend(self):
        return self.friend_hrs > 0

    def __unicode__(self):
        return "%s" % self.date

    @property
    def yesterday(self):
        try:
            return GutterBumper.objects.get_or_create(date=self.date - datetime.timedelta(days=1))[0]
        except:
            return None

    @property
    def tomorrow(self):
        try:
            return GutterBumper.objects.get(date=self.date + datetime.timedelta(days=1))
        except:
            return None

    @property
    def calculated_sleep_hrs(self):
        if self.woke_up_at and self.yesterday and self.yesterday.fell_asleep_at is not None:
            today_hrs, today_min, _ = ("%s" % self.woke_up_at).split(":")
            yester_hrs, yester_min, _ = ("%s" % self.yesterday.fell_asleep_at).split(":")

            today = float(today_hrs) + (float(today_min)/60)
            yester = float(yester_hrs) + (float(yester_min)/60)

            if yester > today:
                # different date
                diff = (today+24) - yester
            else:
                # same date
                diff = today - yester
            rem = diff % 1
            round_len = 1
            if rem % 25:
                round_len = 2
            if rem == 0:
                round_len = 0

            return round(diff, round_len)
        return None

    @property
    def meditated_status(self):
        if self.meditated:
            return BUMPER_STATUS_GOOD
        elif self.yesterday and self.yesterday.meditated:
            return BUMPER_STATUS_BORDERLINE
        else:
            return BUMPER_STATUS_BAD

    @property
    def off_status(self):
        if self.off or (self.yesterday and self.yesterday.off) or (self.yesterday and self.yesterday.yesterday and self.yesterday.yesterday.off):
            return BUMPER_STATUS_GOOD
        elif (self.yesterday and self.yesterday.yesterday and self.yesterday.yesterday.off) or (self.yesterday and self.yesterday.yesterday and self.yesterday.yesterday.yesterday and self.yesterday.yesterday.yesterday.off):
            return BUMPER_STATUS_BORDERLINE
        else:
            return BUMPER_STATUS_BAD

    @property
    def worked_out_status(self):
        if self.worked_out or (self.yesterday and self.yesterday.worked_out):
            return BUMPER_STATUS_GOOD
        elif (self.yesterday and self.yesterday.yesterday.worked_out):
            return BUMPER_STATUS_BORDERLINE
        else:
            return BUMPER_STATUS_BAD

    @property
    def left_the_house_status(self):
        if self.left_the_house:
            return BUMPER_STATUS_GOOD
        elif self.yesterday and self.yesterday.left_the_house:
            return BUMPER_STATUS_BORDERLINE
        else:
            return BUMPER_STATUS_BAD

    @property
    def nature_time_status(self):
        if GutterBumper.objects.filter(nature_time=True, date__gte=self.date-datetime.timedelta(days=7)).count() > 0:
            return BUMPER_STATUS_GOOD
        elif GutterBumper.objects.filter(nature_time=True, date__gte=self.date-datetime.timedelta(days=14)).count() > 0:
            return BUMPER_STATUS_BORDERLINE
        else:
            return BUMPER_STATUS_BAD

    @property
    def art_status(self):
        if GutterBumper.objects.filter(interacted_with_art=True, date__gte=self.date-datetime.timedelta(days=6)).count() > 0:
            return BUMPER_STATUS_GOOD
        elif GutterBumper.objects.filter(interacted_with_art=True, date__gte=self.date-datetime.timedelta(days=8)).count() > 0:
            return BUMPER_STATUS_BORDERLINE
        else:
            return BUMPER_STATUS_BAD

    @property
    def has_reported_presence_today(self):
        return self.presence_set

    @property
    def has_reported_happiness_today(self):
        return self.happiness_set

    @property
    def has_reported_creativity_today(self):
        return self.creativity_set

    @property
    def has_reported_morning_mood_today(self):
        return self.morning_mood_set

    @property
    def has_reported_unbusy_today(self):
        return self.unbusy_set

    @property
    def one_thing_to_focus_on(self):
        if self.left_the_house_status == BUMPER_STATUS_BAD:
            return "leave the house for 15 minutes"
        if self.worked_out_status == BUMPER_STATUS_BAD:
            return "train or work out."
        if self.friend_health <= 7:
            return "see a friend or plan to."
        if self.work_health <= 7:
            return "work fewer hours"
        if self.alone_health <= 7:
            return "get some alone time"
        if self.meditated_status == BUMPER_STATUS_BAD:
            return "meditate"
        if self.off_status == BUMPER_STATUS_BAD:
            return "off"
        if self.sleep_health <= 7:
            return "get to bed earlier tonight, you're low on sleep."
        if self.nature_time_status != BUMPER_STATUS_GOOD:
            return "get out into nature"
        if self.art_status != BUMPER_STATUS_GOOD:
            return "have an in-depth experience with art"
        if self.public_health <= 7:
            return "get out into public and see people"
        if self.left_the_house_status != BUMPER_STATUS_GOOD:
            return "leave the house for 15 minutes"
        if self.worked_out_status != BUMPER_STATUS_GOOD:
            return "train or work out."
        if self.meditated_status != BUMPER_STATUS_GOOD:
            return "meditate"
        if self.off_status != BUMPER_STATUS_GOOD:
            return "off"

        # TODO: relationship_health
        return "you're doing great, keep up the good work!"


    @property
    def all_green(self):
        return self.meditated_status is BUMPER_STATUS_GOOD and self.off_status is BUMPER_STATUS_GOOD and\
               self.worked_out_status is BUMPER_STATUS_GOOD and self.left_the_house_status is BUMPER_STATUS_GOOD and\
               self.nature_time_status is BUMPER_STATUS_GOOD  # and\
               # self.has_reported_presence_today and self.has_reported_happiness_today and\
               # self.has_reported_creativity_today and self.has_reported_morning_mood_today and\
               

    @property
    def presence_trend(self):
        return GutterBumper.objects.filter(date__gte=self.date-datetime.timedelta(days=7)).aggregate(Avg('presence'))['presence__avg']

    @property
    def happiness_trend(self):
        return GutterBumper.objects.filter(date__gte=self.date-datetime.timedelta(days=7)).aggregate(Avg('happiness'))['happiness__avg']

    @property
    def creativity_trend(self):
        return GutterBumper.objects.filter(date__gte=self.date-datetime.timedelta(days=7)).aggregate(Avg('creativity'))['creativity__avg']

    @property
    def morning_mood_trend(self):
        return GutterBumper.objects.filter(date__gte=self.date-datetime.timedelta(days=7)).aggregate(Avg('morning_mood'))['morning_mood__avg']

    @property
    def unbusy_trend(self):
        return GutterBumper.objects.filter(date__gte=self.date-datetime.timedelta(days=7)).aggregate(Avg('unbusy'))['unbusy__avg']

    @property
    def sleep_health(self):
        avg = GutterBumper.objects.filter(date__gte=self.date-datetime.timedelta(days=7)).aggregate(Avg('sleep_hrs'))['sleep_hrs__avg']
        if avg >= 8:
            return 10
        # 7 hrs sleep = 8
        # 6 hrs sleep = 3,4
        # < 5 hrs sleep = 0
        adjusted_avg = (avg-5)/3
        if adjusted_avg < 0:
            adjusted_avg = 0
        return 10*(adjusted_avg)

    @property
    def work_health(self):
        sum_hrs = GutterBumper.objects.filter(date__gte=self.date-datetime.timedelta(days=7)).filter(work_hrs__gt=0).aggregate(Sum('work_hrs'))['work_hrs__sum']
        avg = sum_hrs / 5
        # -1 for each 15 min over 8.
        over = avg-8
        if over <= 0:
            return 10
        else:
            # 0.5 over = 8
            # 2.25 over = 1
            return 10 - (over*4)
        

    @property
    def alone_health(self):
        avg = GutterBumper.objects.filter(date__gte=self.date-datetime.timedelta(days=14)).aggregate(Avg('alone_hrs'))['alone_hrs__avg']
        if avg >= 3:
            return 10
        return 10*(avg/3)

    @property
    def friend_health(self):
        sum_hrs = GutterBumper.objects.filter(date__gte=self.date-datetime.timedelta(days=14)).aggregate(Sum('friend_hrs'))['friend_hrs__sum']
        if sum_hrs > 6:
            return 10
        return 10*(sum_hrs/6)

    @property
    def public_health(self):
        sum_hrs = GutterBumper.objects.filter(date__gte=self.date-datetime.timedelta(days=7)).aggregate(Sum('public_hrs'))['public_hrs__sum']
        if sum_hrs > 6:
            return 10
        return 10*(sum_hrs/6)

    @property
    def relationship_health(self):
        avg = GutterBumper.objects.filter(date__gte=self.date-datetime.timedelta(days=7)).aggregate(Avg('relationship_hrs'))['relationship_hrs__avg']
        if avg > 2:
            return 10
        return 10*(avg/2)

    def save(self, *args, **kwargs):
        try:
            old_fell_asleep_time = GutterBumper.objects.get(pk=self.pk).fell_asleep_at
        except:
            old_fell_asleep_time = None
        
        if self.calculated_sleep_hrs:
            self.sleep_hrs = self.calculated_sleep_hrs

        # if not self.weight:
        #     self.weight = self.fitbit_data.weight
        #     self.body_fat_percent = self.fitbit_data.body_fat_percent

        super(GutterBumper, self).save(*args, **kwargs)
        if old_fell_asleep_time and old_fell_asleep_time != self.fell_asleep_at and self.tomorrow:
            self.tomorrow.save()


class Weight(BaseModel):
    when = models.DateTimeField(default=datetime.date.today())
    weight = models.FloatField(blank=True, null=True)
    body_fat_percent = models.FloatField(blank=True, null=True)

    class Meta:
        ordering = ("-when",)

    @classmethod
    def get_and_save_weight(cls):
        authd_client = fitbit.Fitbit(
            settings.FITBIT_CONSUMER_KEY,
            settings.FITBIT_CONSUMER_SECRET,
            user_key=settings.FITBIT_USER_KEY,
            user_secret=settings.FITBIT_USER_SECRET
        )
        weight = authd_client.get_bodyweight()
        # {u'weight': [{u'date': u'2014-03-29', u'logId': 1396089789000, u'bmi': 22.38, u'weight': 165, u'time': u'10:43:09'}, {u'date': u'2014-03-29', u'logId': 1396097620000, u'bmi': 22.41, u'weight': 165.3, u'time': u'12:53:40'}]}
        fat = authd_client.get_bodyfat()
        # {u'fat': [{u'date': u'2014-03-29', u'logId': 1396089789000, u'fat': 16.9, u'time': u'10:43:09'}, {u'date': u'2014-03-29', u'logId': 1396097620000, u'fat': 16.9, u'time': u'12:53:40'}]}
        try:
            last_update = cls.objects.order_by("-when")[0]
        except:
            last_update = None

        if len(weight) > 0:
            last_weight = weight["weight"][-1]
            last_fat = fat["fat"][-1]
            # 2014-03-29 10:43:09
            last_time = datetime.datetime.fromtimestamp(
                time.mktime(time.strptime("%s %s" % (last_weight["date"], last_weight["time"]), "%Y-%m-%d %H:%M:%S"))
            )
            if not last_update or last_time != last_update.when:
                cls.objects.create(when=last_time, weight=last_weight["weight"], body_fat_percent=last_fat["fat"])

    def __unicode__(self):
        return "%s: %s lbs, %s%%" % (self.when, self.weight, self.body_fat_percent)


class WeeklyMeal(BaseModel):
    name = models.CharField(max_length=200)
    ingredients = models.TextField(blank=True, null=True)
    preparation = models.TextField(blank=True, null=True)
    how_it_went = models.TextField(blank=True, null=True)
    week_start_date = models.DateField(blank=True, null=True)


class MonthlyCheckin(BaseModel):
    month_start_date = models.DateField(default=datetime.date.today())

    happiness_rating = models.IntegerField(blank=True, null=True)
    happiness_notes = models.TextField(blank=True, null=True)
    relationship_health_rating = models.IntegerField(blank=True, null=True)
    relationship_health_notes = models.TextField(blank=True, null=True)
    enough_time_in_nature_rating = models.IntegerField(blank=True, null=True)
    enough_time_in_nature_notes = models.TextField(blank=True, null=True)
    presence_rating = models.IntegerField(blank=True, null=True)
    presence_notes = models.TextField(blank=True, null=True)
    in_touch_with_spirtuality_rating = models.IntegerField(blank=True, null=True)
    in_touch_with_spirtuality_notes = models.TextField(blank=True, null=True)
    making_things_rating = models.IntegerField(blank=True, null=True)
    making_things_notes = models.TextField(blank=True, null=True)
    have_a_space_that_is_just_mine_rating = models.IntegerField(blank=True, null=True)
    have_a_space_that_is_just_mine_notes = models.TextField(blank=True, null=True)
    enough_time_alone_rating = models.IntegerField(blank=True, null=True)
    enough_time_alone_notes = models.TextField(blank=True, null=True)
    finances_on_track_rating = models.IntegerField(blank=True, null=True)
    finances_on_track_notes = models.TextField(blank=True, null=True)
    getting_out_enough_rating = models.IntegerField(blank=True, null=True)
    getting_out_enough_notes = models.TextField(blank=True, null=True)
    sex_life_is_good_rating = models.IntegerField(blank=True, null=True)
    sex_life_is_good_notes = models.TextField(blank=True, null=True)
    making_the_world_a_bit_better_rating = models.IntegerField(blank=True, null=True)
    making_the_world_a_bit_better_notes = models.TextField(blank=True, null=True)
    healthy_eating_rating = models.IntegerField(blank=True, null=True)
    healthy_eating_notes = models.TextField(blank=True, null=True)
    healthy_drinking_rating = models.IntegerField(blank=True, null=True)
    healthy_drinking_notes = models.TextField(blank=True, null=True)
    healthy_activity_rating = models.IntegerField(blank=True, null=True)
    healthy_activity_notes = models.TextField(blank=True, null=True)
    closer_to_two_year_plan_rating = models.IntegerField(blank=True, null=True)
    closer_to_two_year_plan_notes = models.TextField(blank=True, null=True)

    habits_from_last_month = models.TextField(blank=True, null=True)
    habit_success_rating = models.IntegerField(blank=True, null=True)
    habit_success_notes = models.TextField(blank=True, null=True)
    habits_for_next_month = models.TextField(blank=True, null=True)

    what_is_the_work_story_i_am_telling = models.TextField(blank=True, null=True)
    what_is_the_relationship_story_i_am_telling = models.TextField(blank=True, null=True)
    what_is_the_identity_story_i_am_telling = models.TextField(blank=True, null=True)


    def __unicode__(self):
        return "%s" % self.month_start_date.strftime('%B %Y')

class Restaurant(BaseModel):
    name = models.CharField(max_length=200)
    meal = models.CharField(max_length=30, choices=MEALS, blank=True, null=True)
    have_gone = models.BooleanField(default=False)
    date_went = models.DateField(blank=True, null=True)
    notes = models.TextField(blank=True, null=True)
    rating = models.IntegerField(blank=True, null=True, verbose_name="Rating (1=bad, 10=best ever)")