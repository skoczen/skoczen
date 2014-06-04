from collections import OrderedDict
import datetime
import math
import pickle
import json
import requests
# from util.singly import SinglyHelper]
from django.db.models import Sum
from django.http import HttpResponseRedirect, HttpResponse
from django.template.loader import render_to_string
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from annoying.decorators import render_to, ajax_request

from manual.models import GutterBumper, Emotion, Value, Weight
from manual.forms import GutterBumperForm
from manual.utils import dump_data_pickle

def turn_friendly_time_into_python_time(time_with_ampm):
    time = time_with_ampm[:5]
    ampm = time_with_ampm[5:]
    hour, minute = time.split(":")
    hour = int(hour)
    minute = int(minute)
    if hour == 12 and ampm.lower() == "am":
        hour = 0
    if ampm.lower() == "pm":
        hour += 12
    if hour == 24:
        hour = 0
    timestr = "%02d:%02d:00" % (hour, minute)
    return timestr


def success_and_statii_for_bumper(success, bumper_pk):
    bumper = GutterBumper.objects.get(pk=bumper_pk)
    return {
        "success": success, 
        "sleep_hrs": bumper.sleep_hrs, 
        "id": bumper_pk,
        "meditated_status": bumper.meditated_status,
        "off_status": bumper.off_status,
        "art_status": bumper.art_status,
        "worked_out_status": bumper.worked_out_status,
        "left_the_house_status": bumper.left_the_house_status,
        "nature_time_status": bumper.nature_time_status,
        "has_reported_presence_today": bumper.has_reported_presence_today,
        "has_reported_creativity_today": bumper.has_reported_creativity_today,
        "has_reported_happiness_today": bumper.has_reported_happiness_today,
        "has_reported_morning_mood_today": bumper.has_reported_morning_mood_today,
        "has_reported_unbusy_today": bumper.has_reported_unbusy_today,
        "has_reported_burnt_out_today": bumper.has_reported_burnt_out_today,
        "all_green": bumper.all_green,
    }


@login_required
@render_to("manual/home.html")
def home(request):
    return locals()

@render_to("manual/emotions.html")
def emotions(request):
    emotions = Emotion.objects.all()
    return locals()


@login_required
@render_to("manual/emotion.html")
def emotion(request, emotion_slug):
    emotion = Emotion.objects.get(slug=emotion_slug)
    return locals()

@login_required
@render_to("manual/values.html")
def values(request):
    values = Value.objects.all()
    return locals()

@login_required
@render_to("manual/value.html")
def value(request, value_slug):
    value = Value.objects.get(slug=value_slug)
    return locals()

@login_required
@render_to("manual/monthly.html")
def monthly(request):
    gutterbumpers = GutterBumper.objects\
                        .filter(date__lt=datetime.date.today())
                        # .filter(date__gte=datetime.date.today()-datetime.timedelta(days=31))\
    total_days = gutterbumpers.filter(date__gte=datetime.date.today()-datetime.timedelta(days=31)).count()
    total_workdays = total_days - math.floor(total_days/7*2)
    total_sleep = 0
    total_work = 0
    total_alone = 0
    total_friend = 0
    total_public = 0
    total_relationship = 0
    total_presence = 0
    total_happiness = 0
    total_creativity = 0
    total_morning_mood = 0
    total_unbusy = 0
    total_burnout = 0
    for g in gutterbumpers.filter(date__gte=datetime.date.today()-datetime.timedelta(days=31)):
        total_sleep += g.sleep_hrs or 0
        total_work += g.work_hrs or 0
        total_alone += g.alone_hrs or 0
        total_friend += g.friend_hrs or 0
        total_public += g.public_hrs or 0
        total_relationship += g.relationship_hrs or 0
        total_presence += g.presence or 0
        total_happiness += g.happiness or 0
        total_creativity += g.creativity or 0
        total_morning_mood += g.morning_mood or 0
        total_unbusy += g.unbusy or 0
        total_burnout += g.burnt_out or 0

    avg_sleep = total_sleep / total_days
    avg_work = total_work / total_days
    avg_alone = total_alone / total_days
    avg_friend = total_friend / total_days
    avg_public = total_public / total_days
    avg_relationship = total_relationship / total_days
    avg_work_per_workday = total_work / total_workdays
    avg_presence = total_presence / total_days
    avg_happiness = total_happiness / total_days
    avg_creativity = total_creativity / total_days
    avg_morning_mood = total_morning_mood / total_days
    avg_unbusy = total_unbusy / total_days
    avg_unbusy = total_burnout / total_days
    return locals()


@login_required
@render_to("manual/dashboard.html")
def dashboard(request):
    current_bumper = GutterBumper.objects.get_or_create(date=datetime.datetime.today())[0]
    bumper_statii = success_and_statii_for_bumper(True, current_bumper.pk)

    return locals()

@login_required
@csrf_exempt
@render_to("manual/daily.html")
def daily(request):
    today = datetime.date.today()
    yesterday_bumper = GutterBumper.objects.get_or_create(date=today-datetime.timedelta(days=1))[0]
    yesterday_form = GutterBumperForm(instance=yesterday_bumper, prefix="yesterday")

    today_bumper = GutterBumper.objects.get_or_create(date=today)[0]
    today_form = GutterBumperForm(instance=today_bumper)

    prev_day = GutterBumper.objects.get_or_create(date=today-datetime.timedelta(days=2))[0]
    next_day = GutterBumper.objects.get_or_create(date=today+datetime.timedelta(days=1))[0]

    return locals()

@csrf_exempt
@ajax_request
@login_required
def daily_form(request, day_pk):
    today_bumper = GutterBumper.objects.get(pk=day_pk)
    prev_day = GutterBumper.objects.get_or_create(date=today_bumper.date-datetime.timedelta(days=1))[0]
    next_day = GutterBumper.objects.get_or_create(date=today_bumper.date+datetime.timedelta(days=1))[0]
    form = GutterBumperForm(instance=today_bumper)

    return {'html': render_to_string("manual/_daily_form.html", locals())}

@csrf_exempt
@ajax_request
@login_required
def update_bumpers(request, bumper_pk):
    success = False

    try:
        data = request.POST.copy()
        prefix = ""
        manual_prefix = ""

        if "yesterday-woke_up_at" in data:
            prefix = "yesterday"
            manual_prefix = "%s-" % prefix
        data["%swoke_up_at" % manual_prefix] = turn_friendly_time_into_python_time(data["%swoke_up_at" % manual_prefix])
        data["%sfell_asleep_at" % manual_prefix] = turn_friendly_time_into_python_time(data["%sfell_asleep_at" % manual_prefix])
        bumper = GutterBumper.objects.get(pk=bumper_pk)
        form = GutterBumperForm(data, instance=bumper, prefix=prefix)
        if form.is_valid():
            form.save()
            success=True
        else:
            print form.errors
    except:
        from traceback import print_exc
        print print_exc()
        pass
    
    return success_and_statii_for_bumper(success, bumper_pk)

@csrf_exempt
@ajax_request
@login_required
def get_sleep_hrs(request, bumper_pk):
    return success_and_statii_for_bumper(True, bumper_pk)

def singly_callback(request, service="fitbit"):
    url = SinglyHelper.get_authorize_url(service)
    return HttpResponseRedirect(url)


def fitbit_callback(request):
    print request.POST
    print request

@render_to("manual/eighty.html")
def eighty(request):
    num_sex = GutterBumper.objects.all().aggregate(Sum('sex'))['sex__sum']
    return locals()


@ajax_request
def todays_one_thing(request):
    today = datetime.date.today()
    today_bumper = GutterBumper.objects.get_or_create(date=today)[0]
    return {"one_thing": today_bumper.one_thing_to_focus_on}


@ajax_request
def red_flag_drinking(request):
    today = datetime.date.today()
    drank_too_much = True

    for i in range(1, 7):
        bumper = GutterBumper.objects.get_or_create(date=today-datetime.timedelta(days=i))[0]
        fun = bumper.number_of_fun_beers or 0
        sleep = bumper.number_of_sleep_beers or 0
        if (fun + sleep) < 3:
            drank_too_much = False
            break

    return {"too_much": drank_too_much}


@ajax_request
def last_10_weights(request):
    w = Weight()
    w.get_and_save_weight()
    weights = []

    for w in Weight.objects.all()[:10]:
        weights.append({
            "when": w.when,
            "weight": w.weight,
            "fat": w.body_fat_percent,
        })
    return {"weights": weights}

@login_required
def data_dump(request):
    return HttpResponse(dump_data_pickle())

# @login_required
@render_to("manual/correlations.html")
def correlations(request):

    CORRELATION_CHOICES = OrderedDict()
    CORRELATION_CHOICES["presence"] = "Presence"
    CORRELATION_CHOICES["happiness"] = "Happiness"
    CORRELATION_CHOICES["creativity"] = "Creativity"
    CORRELATION_CHOICES["morning_mood"] = "Morning mood"
    CORRELATION_CHOICES["unbusy"] = "Unbusy-ness"

    CORRELATION_CHOICES["sleep_hrs"] = "Hours of sleep"
    CORRELATION_CHOICES["work_hrs"] = "Hours spent working"
    CORRELATION_CHOICES["alone_hrs"] = "Hours spent alone"
    CORRELATION_CHOICES["friend_hrs"] = "Hours with friends"
    CORRELATION_CHOICES["public_hrs"] = "Hours in public"
    CORRELATION_CHOICES["relationship_hrs"] = "Hours with my significant other"
    CORRELATION_CHOICES["woke_up_at"] = "Woke up later"
    CORRELATION_CHOICES["fell_asleep_at"] = "Fell asleep later"

    if request.user.username == "skoczen" and 'all' in request.GET:
        CORRELATION_CHOICES["orgasm"] = "Off/Sex"
        CORRELATION_CHOICES["sex_count"] = "Sex Count"

    CORRELATION_CHOICES["interacted_with_art"] = "Interacted with art"
    CORRELATION_CHOICES["dentist"] = "Went to the dentist"
    CORRELATION_CHOICES["worked_out"] = "Worked out"
    CORRELATION_CHOICES["meditated"] = "Meditated"
    CORRELATION_CHOICES["left_the_house"] = "Left the house"
    CORRELATION_CHOICES["nature_time"] = "Nature time"
    CORRELATION_CHOICES["in_a_relationship"] = "In a relationship"
    # CORRELATION_CHOICES["inbox_zero"] = "Inbox zero"
    CORRELATION_CHOICES["travelling_or_out_of_routine"] = "Travelling"

    CORRELATION_CHOICES["number_of_sleep_beers"] = "Beers to fall asleep"
    CORRELATION_CHOICES["number_of_fun_beers"] = "Beers for fun"
    # CORRELATION_CHOICES["number_of_total_beers"] = "Total beers"
    CORRELATION_CHOICES["notes length"] = "# of words in daily notes"

    CORRELATION_CHOICES["spring"] = "Spring"
    CORRELATION_CHOICES["summer"] = "Summer"
    CORRELATION_CHOICES["fall"] = "Fall"
    CORRELATION_CHOICES["winter"] = "Winter"
    CORRELATION_CHOICES["moon_phase"] = "Moon Fullness"

    # CORRELATION_CHOICES["month"] = "Month of the year"

    cols = [
        "month",
        "woke_up_at",
        "fell_asleep_at",
        "sleep_hrs",
        "work_hrs",
        "alone_hrs",
        "friend_hrs",
        "public_hrs",
        "relationship_hrs",
        "orgasm",
        "sex_count",
        "interacted_with_art",
        "worked_out",
        "meditated",
        "left_the_house",
        "nature_time",
        "inbox_zero",
        "travelling_or_out_of_routine",
        "number_of_sleep_beers",
        "number_of_fun_beers",
        "number_of_total_beers",
        "presence",
        "happiness",
        "creativity",
        "morning_mood",
        "unbusy",
        "notes length",
        "winter",
        "spring",
        "summer",
        "fall",
        "dentist",
        "moon_phase",
        "in_a_relationship",
    ]
    data = pickle.loads(dump_data_pickle())
    headers = {'Content-type': 'application/json', }
    stripped_data = json.dumps({
        "data": data
    }).replace(", ", ",")
    resp = requests.post("http://correlationbot.com", headers=headers, data=stripped_data)
    if not resp.status_code == "200":
        print resp
        print resp.__dict__
        print resp.content
    correlations = resp.json()["correlations"]
    # correlations = {}
    for c in correlations:
        c["col1"] = cols[c["column_1"]-1]
        c["col2"] = cols[c["column_2"]-1]
        try:
            c["col1_friendly"] = CORRELATION_CHOICES[cols[c["column_1"]-1]]
        except:
            c["col1_friendly"] = "Ignored"
        try:
            c["col2_friendly"] = CORRELATION_CHOICES[cols[c["column_2"]-1]]
        except:
            c["col2_friendly"] = "Ignored"

        if str(c["pearson"]) == "nan":
            c["pearson"] = 0
            c["correlation"] = 0
    return {
        "correlations": correlations,
        "CORRELATION_CHOICES": CORRELATION_CHOICES,
    }


@login_required
@ajax_request
def correlations_for(request):
    return locals()
