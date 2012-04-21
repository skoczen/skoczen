# from django.db import models
all_pages = []


# Just switched to keeping it in-memory. No real need for a model here.

# class Page(models.Model):
#     top = models.TextField(blank=True, null=True)
#     middle_link = models.TextField(blank=True, null=True)
#     middle_html = models.TextField(blank=True, null=True)
#     bottom = models.TextField(blank=True, null=True)
#     year = models.CharField(max_length=200, blank=True, null=True)
#     order = models.IntegerField(default=0)
#     active = models.BooleanField(default=True)

#     def __unicode__(self, *args, **kwargs):
#         return self.top

class SimplePage:

    def __init__(self, top="", middle_link="", middle_html="", bottom="", year=""):
        self.top = top
        self.middle_link = middle_link
        self.middle_html = middle_html
        self.bottom = bottom
        self.year = year

    def __unicode__(self, *args, **kwargs):
        return self.top


def add_page(*args, **kwargs):
    globals()["all_pages"].append(SimplePage(*args, **kwargs))
    

add_page(
    top="is enough",
    bottom="what does love mean to you?",
    middle_link="http://www.isenough.com",
    year="2012",
)
add_page(
    top="encore",
    bottom="a digital poem",
    middle_link="http://www.encorepoem.com",
    year="2012",
)
add_page(
    top="slow art",
    bottom="the anti-museum.<br/>\r\nin portland, or",
    middle_link="http://slowartpdx.com",
    year="2011+",
)
add_page(
    top="dear text messages,",
    bottom="spoken word",
    middle_link="",
    year="2012",
)
add_page(
    top="togetheralone",
    bottom="an experiment in community",
    middle_link="http://togetheralone.org",
    year="2012",
)
add_page(
    top="The Digital Executioner",
    bottom="Instant innovative web ideas",
    middle_link="http://www.thedigitalexecutioner.com",
    year="2012",
)