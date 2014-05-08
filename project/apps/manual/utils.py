import pickle
import logging
logger = logging.getLogger("foo")
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)

# create formatter
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# add formatter to ch
ch.setFormatter(formatter)

# add ch to logger
logger.addHandler(ch)


from manual.models import GutterBumper

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

    def handle(self, *args, **options):
        self.data = []
        for d in range(0, 30):
            self.data.append([])
        for b in GutterBumper.objects.all().order_by("date"):
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
                self.append_to_data(20, b.presence)  #  = models.IntegerField(blank=True, null=True, help_text="1-10")
                self.append_to_data(21, b.happiness)  #  = models.IntegerField(blank=True, null=True, help_text="1-10")
                self.append_to_data(22, b.creativity)  #  = models.IntegerField(blank=True, null=True, help_text="1-10")
                self.append_to_data(23, b.morning_mood)  #  = models.IntegerField(blank=True, null=True, help_text="1-10")
                self.append_to_data(24, b.unbusy or 9)  #  = models.IntegerField(blank=True, null=True, help_text="1-10")
                notes_len = 0
                try:
                    notes_len = len(b.notes)
                except:
                    pass
                self.append_to_data(25, notes_len)  #  = models.TextField(blank=True, null=True, default="86400")
                self.append_to_data(26, 10 if (b.date.month < 3 or b.date.month == 12) else 0)  # winter
                self.append_to_data(27, 10 if (b.date.month >= 3 or b.date.month < 6) else 0)  # spring
                self.append_to_data(28, 10 if (b.date.month >= 6 or b.date.month < 9) else 0)  # summer
                self.append_to_data(29, 10 if (b.date.month >= 9 or b.date.month < 12) else 0)  # fall
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

def dump_data_pickle():
    c = Dump()
    return c.handle()