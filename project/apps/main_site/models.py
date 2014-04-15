from django.db import models

PROJECT_SUCCEEDED = "success"
PROJECT_FAILED = "failed"
PROJECT_WHO_KNOWS = "who_knows"
PROJECT_LIVED_ITS_LIFE = "lived"

PROJECT_CHOICES = [
    (PROJECT_SUCCEEDED, "Success!"),
    (PROJECT_FAILED, "Failed!"),
    (PROJECT_WHO_KNOWS, "Jury's out"),
    (PROJECT_LIVED_ITS_LIFE, "Lived a full life, died of old age."),
]


class BaseModel(models.Model):
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

    def __unicode__(self):
        return "%s" % self.name


class Project(BaseModel):
    title = models.CharField(max_length=255, blank=True, null=True)
    summary = models.TextField(blank=True, null=True)
    url = models.TextField(blank=True, null=True)
    date_started = models.DateField(blank=True, null=True)
    status = models.CharField(max_length=50, choices=PROJECT_CHOICES)
    active = models.BooleanField(default=True)
    picture = models.ImageField(blank=True, null=True, upload_to="projects")

    def __unicode__(self, *args, **kwargs):
        return self.title
