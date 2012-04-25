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

    def __init__(self, top="", middle_link="", middle_links=None, bottom="", year=""):
        self.top = top
        self.middle_link = middle_link # list of dicts - url, text
        self.middle_links = middle_links
        self.bottom = bottom
        self.year = year

    def __unicode__(self, *args, **kwargs):
        return self.top


def add_page(*args, **kwargs):
    globals()["all_pages"].append(SimplePage(*args, **kwargs))
    


add_page(
    top="is enough",
    bottom="what does love mean to you?",
    middle_link="http://isenough.com",
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
# add_page(
#     top="dear text messages,",
#     bottom="spoken word",
#     middle_link="",
#     year="2012",
# )
add_page(
    top="togetheralone",
    bottom="an experiment in community",
    middle_link="http://togetheralone.org",
    year="2012",
)
add_page(
    top="the digital executioner",
    bottom="viral web idea generator",
    middle_link="http://www.thedigitalexecutioner.com",
    year="2012",
)
add_page(
    top="goodcloud",
    bottom="helping small nonprofits succeed",
    middle_link="https://www.agoodcloud.com",
    year="2011",
)
add_page(
    top="github",
    bottom="where I keep the bits and bytes",
    middle_link = "https://www.github.com/skoczen",
    # middle_links=[
    #     {
    #         "url": "https://www.github.com/skoczen",
    #         "text": "Personal",
    #         "class": ""
    #     },
    #     {
    #         "url": "https://www.github.com/GoodCloud",
    #         "text": "GoodCloud",
    #         "class": ""
    #     }
    # ],
    year="2009+",
)

add_page(
    top="sixlinks",
    bottom="sustainability you can actually do",
    middle_link="http://www.sixlinks.org",
    year="2008+",
)

add_page(
    top="the facebooks",
    bottom="yep, I'm on there",
    middle_link = "https://www.facebook.com/skoczen",
    # middle_links=[
    #     {
    #         "url": "https://www.facebook.com/skoczen",
    #         "text": "f",
    #         "class": "facebook"
    #     },
    #     {
    #         "url": "https://twitter.com/#!/skoczen",
    #         "text": "t",
    #         "class": "twitter"
    #     },
    #     {
    #         "url": "https://plus.google.com/101690366177319310091/",
    #         "text": "g+",
    #         "class": "google_plus"
    #     }
    # ],
    year="2007+",
)
# add_page(
#     top="Write Around Portland",
#     bottom="I'm proud to be a volunteer and donor for this amazing organization.",
#     middle_link="http://www.writearound.org",
#     year="2009+",
# )
add_page(
    top="30 people, 30 minutes",
    bottom="an epic way to turn 30",
    middle_link="http://www.30people30minutes.com",
    year="1999+",
)

add_page(
    top="quantum imagery",
    bottom="ye olde sole proprietorship",
    middle_link="http://www.quantumimagery.com",
    year="1999+",
)

add_page(
    top="photoblog",
    bottom="ye olde photos",
    middle_link="http://www.skoczen.net/photos",
    year="2005",
)

add_page(
    top="but i'm hungry!",
    bottom="ye olde recipe and restaurant site",
    middle_link="http://skoczen.net/food/",
    year="1999+",
)
add_page(
    top="liquid silver zen",
    bottom="early experiments in design",
    middle_link="http://liquidsilverzen.net/",
    year="2002",
)
add_page(
    top="or, just google",
    bottom="It's all me. Except for the Ohio seatbelt ticket. That's the other Steven Skoczen. (Really.)",
    middle_link="https://www.google.com/?q=Steven%20Skoczen",
    year="1997+",
)
# add_page(
#     top="birth",
#     bottom="there was no internet then",
#     middle_links=[
#         {
#             "url": "",
#             "text": "whoa",
#             "class": ""
#         },
#     ],
#     year="1980",
# )

