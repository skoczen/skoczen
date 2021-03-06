from collections import OrderedDict
import decimal, datetime
import pickle
import logging
import json
import requests
from django.core.cache import cache
logger = logging.getLogger("foo")
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
dec = decimal.Decimal

# create formatter
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# add formatter to ch
ch.setFormatter(formatter)

# add ch to logger
logger.addHandler(ch)


class Dump(object):

    def append_to_data(self, index, value):
        if self.first_run:
            try:
                float(value)
                return True
            except:
                self.valid_data = False
                logger.error("Error converting %s to float, skipping this row. (Index %s, %s)" % (value, index, self.b))
                return False
        try:
            self.data[index].append(float(value))
        except:
            raise Exception("Error converting %s to float. (Index %s)" % (value, index))

    def handle(self, *args, **filters):
        from manual.models import GutterBumper
        self.data = []
        for d in range(0, 34):
            self.data.append([])
        for b in GutterBumper.objects.filter(**filters).all().order_by("date"):
            self.first_run = True
            self.valid_data = True
            self.add_valid_data = False
            self.b = b
            while self.first_run or self.add_valid_data:
                self.append_to_data(0, b.date.month)  # month
                self.append_to_data(1, b.woke_up_at.hour)  # woke up hour
                fell_asleep_hr = b.fell_asleep_at.hour
                if fell_asleep_hr < 13:
                    fell_asleep_hr += 24
                self.append_to_data(2, fell_asleep_hr )  #  = models.TimeField(default=datetime.time(0, 00))
                self.append_to_data(3, b.sleep_hrs)  #  = models.FloatField(default=0, blank=True, null=True, verbose_name="Sleep", help_text="Sleep this morning")
                self.append_to_data(4, b.work_hrs)  #  = models.FloatField(default=0, blank=True, null=True, verbose_name="Work")
                self.append_to_data(5, b.alone_hrs)  #  = models.FloatField(default=0, blank=True, null=True, verbose_name="Alone")
                self.append_to_data(6, b.friend_hrs)  #  = models.FloatField(default=0, blank=True, null=True, verbose_name="Friend")
                self.append_to_data(7, b.public_hrs)  #  = models.FloatField(default=0, blank=True, null=True, help_text="Not specifically hanging with people, but in a larger crowd", verbose_name="Public")
                self.append_to_data(8, b.relationship_hrs)  #  = models.FloatField(default=0, blank=True, null=True, verbose_name="Relationship")
                self.append_to_data(9, 10 if b.off else 0)  #  = models.BooleanField(default=False)
                self.append_to_data(10, b.sex or 0)  #  = models.IntegerField(default=0)
                self.append_to_data(11, 10 if b.interacted_with_art else 0)  #  = models.BooleanField(default=False)
                self.append_to_data(12, 10 if b.worked_out else 0)  #  = models.BooleanField(default=False)
                self.append_to_data(13, 10 if b.meditated else 0)  #  = models.BooleanField(default=False, verbose_name="meditated")
                self.append_to_data(14, 10 if b.left_the_house else 0)  #  = models.BooleanField(default=False)
                self.append_to_data(15, 10 if b.nature_time else 0)  #  = models.BooleanField(default=False)
                self.append_to_data(16, 10 if b.inbox_zero else 0)  #  = models.BooleanField(default=False)
                self.append_to_data(17, 10 if b.travelling_or_out_of_routine else 0)  #  = models.BooleanField(default=False, verbose_name="Travelling/Nonroutine")
                self.append_to_data(18, b.number_of_sleep_beers or 0)  #  = models.IntegerField(blank=True, null=True, verbose_name="# of sleep beers")
                self.append_to_data(19, b.number_of_fun_beers or 0)  #  = models.IntegerField(blank=True, null=True, verbose_name="# of fun beers")
                self.append_to_data(20, (b.number_of_sleep_beers or 0) + (b.number_of_fun_beers or 0))  #  = models.IntegerField(blank=True, null=True, verbose_name="# of fun beers")
                self.append_to_data(21, b.presence)  #  = models.IntegerField(blank=True, null=True, help_text="1-10")
                self.append_to_data(22, b.happiness)  #  = models.IntegerField(blank=True, null=True, help_text="1-10")
                self.append_to_data(23, b.creativity)  #  = models.IntegerField(blank=True, null=True, help_text="1-10")
                self.append_to_data(24, b.morning_mood)  #  = models.IntegerField(blank=True, null=True, help_text="1-10")
                self.append_to_data(25, b.unbusy or 9)  #  = models.IntegerField(blank=True, null=True, help_text="1-10")
                notes_len = 0
                try:
                    notes_len = len(b.notes)
                except:
                    pass

                self.append_to_data(26, notes_len)  #  = models.TextField(blank=True, null=True, default="86400")
                self.append_to_data(27, 10 if (b.date.month < 3 or b.date.month == 12) else 0)  # winter
                self.append_to_data(28, 10 if (b.date.month >= 3 and b.date.month < 6) else 0)  # spring
                self.append_to_data(29, 10 if (b.date.month >= 6 and b.date.month < 9) else 0)  # summer
                self.append_to_data(30, 10 if (b.date.month >= 9 and b.date.month < 12) else 0)  # fall
                self.append_to_data(31, 10 if (b.emotions.filter(name="Dentist Visit").count() > 0) else 0)  # dentist
                self.append_to_data(32, b.moon_phase)
                self.append_to_data(33, 10 if b.in_a_relationship else 0)
                if self.first_run:
                    self.first_run = False

                    if self.valid_data:
                        self.add_valid_data = True
                else:
                    self.add_valid_data = False

        # Sanity check.
        total_len = None
        for index in range(0, len(self.data)):
            d = self.data[index]
            if not total_len:
                total_len = len(d)

            if len(d) != total_len:
                logger.critical("Unequal datasets %s!" % index)

        return pickle.dumps(self.data)


def dump_data_pickle(**filters):
    c = Dump()
    today = datetime.date.today() - datetime.timedelta(days=1640)
    return c.handle(date__gt=today)


# Via http://inamidst.com/code/moonphase.py
def moon_position(now=None):
    if now is None:
        now = datetime.datetime.now()
    diff = now - datetime.datetime(2001, 1, 1)
    days = dec(diff.days) + (dec(diff.seconds) / dec(86400))
    lunations = dec("0.20439731") + (days * dec("0.03386319269"))
    return 28 * (dec(0.5) - abs(dec(0.5) - (lunations % dec(1))))


CORRELATION_CHOICES = OrderedDict()
CORRELATION_CHOICES["presence"] = "Presence"
CORRELATION_CHOICES["happiness"] = "Happiness"
CORRELATION_CHOICES["creativity"] = "Creativity"
CORRELATION_CHOICES["morning_mood"] = "Morning mood"
CORRELATION_CHOICES["unbusy"] = "Unbusy-ness"

CORRELATION_CHOICES["sleep_hrs"] = "Hours of sleep"
CORRELATION_CHOICES["work_hrs"] = "Hours spent working"
CORRELATION_CHOICES["alone_hrs"] = "Hours spent alone"
CORRELATION_CHOICES["neap_hrs"] = "Hours spent neither alone or in quality time"
CORRELATION_CHOICES["friend_hrs"] = "Hours with friends"
CORRELATION_CHOICES["public_hrs"] = "Hours in public"
CORRELATION_CHOICES["relationship_hrs"] = "Hours with my significant other"
CORRELATION_CHOICES["woke_up_at"] = "Woke up later"
CORRELATION_CHOICES["fell_asleep_at"] = "Fell asleep later"

CORRELATION_CHOICES["orgasm"] = "Off/Sex"
CORRELATION_CHOICES["sex_count"] = "Sex Count"

CORRELATION_CHOICES["interacted_with_art"] = "Interacted with art"
CORRELATION_CHOICES["dentist"] = "Went to the dentist"
CORRELATION_CHOICES["worked_out"] = "Worked out"
CORRELATION_CHOICES["meditated"] = "Meditated"
CORRELATION_CHOICES["left_the_house"] = "Left the house"
CORRELATION_CHOICES["nature_time"] = "Nature time"
CORRELATION_CHOICES["ate_green"] = "Ate Something Green"
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

def save_correlations():
    cols = [
        "month",
        "woke_up_at",
        "fell_asleep_at",
        "sleep_hrs",
        "work_hrs",
        "alone_hrs",
        "neap_hrs",
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
        "spoons",
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
    if resp.status_code != 200:
        print stripped_data
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

    cache.set("current_correlations", correlations)
    cache.set("current_correlation_choices", CORRELATION_CHOICES)
