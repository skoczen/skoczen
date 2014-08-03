from collections import OrderedDict
import datetime
import math
# from util.singly import SinglyHelper]
from django.core.cache import cache
from django.db.models import Sum
from django.http import HttpResponseRedirect, HttpResponse
from django.template.loader import render_to_string
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from annoying.decorators import render_to, ajax_request

from manual.models import GutterBumper, Emotion, Value, Weight, WeeklyGoal
from manual.forms import GutterBumperForm, WeeklyGoalForm
from manual.utils import dump_data_pickle, CORRELATION_CHOICES, save_correlations

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

@render_to("manual/weekly.html")
def weekly(request):
    weekly_goals = WeeklyGoal.objects.all()
    most_recent = WeeklyGoal.objects.all().order_by("-start_date")[0]
    if (datetime.date.today() - most_recent.start_date > datetime.timedelta(days=7)):
        WeeklyGoal.objects.create(
            start_date=most_recent.start_date + datetime.timedelta(days=7),
            primary=most_recent.primary,
        )
        weekly_goals = WeeklyGoal.objects.all()
        most_recent = WeeklyGoal.objects.all().order_by("-start_date")[0]


    if request.method == "POST":
        form = WeeklyGoalForm(request.POST, instance=most_recent)
        if form.is_valid():
            print "saving"
            form.save()

    form = WeeklyGoalForm(instance=most_recent)

    # .order_by("-start_date")
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
    private_data = ["orgasm", "sex_count",]
    choices = OrderedDict()
    if request.user.username != "skoczen" or 'all' not in request.GET:
        for k, v in CORRELATION_CHOICES.items():
            if k not in private_data:
                choices[k] = v
    else:
        choices = CORRELATION_CHOICES
    
    correlations = cache.get("current_correlations", None)
    if not correlations:
        save_correlations()
        correlations = cache.get("current_correlations")

    return {
        "correlations": correlations,
        "CORRELATION_CHOICES": choices,
    }


@login_required
@ajax_request
def correlations_for(request):
    return locals()
