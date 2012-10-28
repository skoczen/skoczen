from django.conf import settings
from django.db import models
from main_site.models import BaseModel
import datetime

THINGS_LIST = ["food", "water", "warm_layers",
    "water_purifier", "shelter", "flashlight", "spare_batteries",
    "rain_shell", "space_blankets", "leatherman", "hat", "gloves",
    "first_aid_kit", "gps", "phone", "spare_phone_battery", "hike_map",
    "compass", "paper_topo_map", "matches", "epipen",
]

class Hike(BaseModel):
    date = models.DateTimeField(default=datetime.datetime.now(), editable=False)
    left_on = models.DateTimeField(default=datetime.datetime.now())
    expected_back = models.DateTimeField(default=datetime.datetime.now() + datetime.timedelta(hours=8))
    where = models.TextField()
    notes = models.TextField(blank=True, null=True, verbose_name='Notes')
    have_left = models.BooleanField(default=False)
    is_back = models.BooleanField(default=False)

    brought_food = models.BooleanField(default=False, verbose_name='Food')
    brought_water = models.BooleanField(default=False, verbose_name='Water')
    brought_warm_layers = models.BooleanField(default=False, verbose_name='Warm layers')
    brought_water_purifier = models.BooleanField(default=False, verbose_name='Water purifier')
    brought_shelter = models.BooleanField(default=False, verbose_name='Shelter')
    brought_flashlight = models.BooleanField(default=False, verbose_name='Flashlight')
    brought_spare_batteries = models.BooleanField(default=False, verbose_name='Spare batteries')
    brought_rain_shell = models.BooleanField(default=False, verbose_name='Rain shell')
    brought_space_blankets = models.BooleanField(default=False, verbose_name='Space blankets')
    brought_leatherman = models.BooleanField(default=False, verbose_name='Leatherman')
    brought_hat = models.BooleanField(default=False, verbose_name='Hat')
    brought_gloves = models.BooleanField(default=False, verbose_name='Gloves')
    brought_first_aid_kit = models.BooleanField(default=False, verbose_name='First aid kit')
    brought_gps = models.BooleanField(default=False, verbose_name='Gps')
    brought_phone = models.BooleanField(default=False, verbose_name='Phone')
    brought_spare_phone_battery = models.BooleanField(default=False, verbose_name='Spare phone battery')
    brought_hike_map = models.BooleanField(default=False, verbose_name='Hike map')
    brought_compass = models.BooleanField(default=False, verbose_name='Compass')
    brought_paper_topo_map = models.BooleanField(default=False, verbose_name='Paper topo map')
    brought_matches = models.BooleanField(default=False, verbose_name='Matches')
    brought_epipen = models.BooleanField(default=False, verbose_name='Epipen')
    

    @property
    def things_i_brought(self):
        things = []
        for t in THINGS_LIST:
            field_name = "brought_%s" % t
            if getattr(self, field_name):
                things.append(self._meta.get_field_by_name(field_name)[0].verbose_name)
        return things

    @property
    def things_i_forgot(self):
        things = []
        for t in THINGS_LIST:
            field_name = "brought_%s" % t
            if not getattr(self, field_name):
                things.append(self._meta.get_field_by_name(field_name)[0].verbose_name)
        return things

    @property
    def brought_everything(self):
        return not self.things_i_forgot is []

    @property
    def is_hiking(self):
        return self.have_left and not self.is_back

    @property
    def is_hiking_soon(self):
        return not self.have_left

    @property
    def is_late(self):
        return self.expected_back < datetime.datetime.now()

    @property
    def has_left(self):
        return self.have_left or self.left_on < datetime.datetime.now()

    @property
    def in_trouble(self):
        return self.status == "probably in trouble." or self.status == "very late"

    @property
    def status(self):
        if self.is_back:
            return "is back"
        elif self.expected_back + datetime.timedelta(hours=23) < datetime.datetime.now():
            return "probably in trouble."
        elif self.expected_back + datetime.timedelta(hours=9) < datetime.datetime.now():
            return "very late"
        elif self.expected_back < datetime.datetime.now():
            return "a little late"
        elif not self.has_left:
            return "hiking soon"
        else:
            return "hiking"

    class Meta:
        ordering = ("date",)

    def save(self, *args, **kwargs):
        super(Hike, self).save(*args, **kwargs)

    def __unicode__(self):
        return "%s" % self.date