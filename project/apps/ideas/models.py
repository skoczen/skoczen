from django.conf import settings
from django.db import models
from main_site.models import BaseModel
import datetime

STATUS_INCUBATING = "incubating"
STATUS_STARTED = "started"

STATUS_LIVING = "living"


IDEA_STATUS = [
    (STATUS_INCUBATING, "Incubating"),
    (STATUS_STARTED, "Started"),
    (STATUS_LIVING, "Living its life"),
]


class Idea(BaseModel):
    thought_of_date = models.DateTimeField(default=datetime.datetime.now(), editable=False)
    title = models.CharField(max_length=500)
    idea = models.TextField(blank=True, null=True, verbose_name='Notes')
    status = models.CharField(max_length=50, choices=IDEA_STATUS, default=IDEA_STATUS[0][0])
    started_date = models.DateTimeField(blank=True, null=True, editable=False)

    class Meta:
        ordering = ("thought_of_date",)

    def save(self, *args, **kwargs):
        if not self.started_date and self.status == STATUS_STARTED:
            self.started_date = datetime.datetime.now()

        super(Idea, self).save(*args, **kwargs)

    def __unicode__(self):
        return "%s" % self.title