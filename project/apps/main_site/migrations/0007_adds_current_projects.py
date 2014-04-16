# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import DataMigration
from django.db import models

class Migration(DataMigration):

    def forwards(self, orm):
        orm.Project.objects.create(
            title="Is enough",
            summary="A digital crowd-poem: what does love mean to you?",
            url="http://isenough.com",
            date_started=datetime.datetime(2011, 11, 21),
            status="who_knows",
        )
        orm.Project.objects.create(
            title="Encore",
            summary="An experimental piece of digital poetry about time, flowers, death and beauty.  Which, really, are all the same thing.",
            url="http://www.encorepoem.com",
            date_started=datetime.datetime(2012, 4, 1),
            status="who_knows",
        )
        orm.Project.objects.create(
            title="Slow Art",
            summary="A monthly art series, based in Portland, OR.  An anti-museum.",
            url="http://slowartpdx.com",
            date_started=datetime.datetime(2011, 7, 1),
            status="success",
        )
        orm.Project.objects.create(
            title="togetheralone",
            summary="An experiment in community, with Anastasia Aizman.",
            url="http://togetheralone.org",
            date_started=datetime.datetime(2012, 3, 1),
            status="failed",
        )
        orm.Project.objects.create(
            title="The Digital Executioner",
            summary="Viral web marketing campaign generator.  Won the internet for a day. Built at Wieden+Kennedy.",
            url="http://www.thedigitalexecutioner.com",
            date_started=datetime.datetime(2012, 2, 1),
            status="success",
        )
        orm.Project.objects.create(
            title="GoodCloud",
            summary="Contact, volunteer, and donor management software for small non-profits.  Organizations loved it, but we couldn't grow fast enough to pay the bills.",
            url="https://www.agoodcloud.com",
            date_started=datetime.datetime(2010, 11, 1),
            status="failed",
        )

        orm.Project.objects.create(
            title="SixLinks",
            summary="Tried to save the world, with Jeff Gunther.  Sixlinks was the big picture of the world's sustainability issues, and step-by-step guides of actions you can personally take.",
            url="http://www.sixlinks.org",
            date_started=datetime.datetime(2008, 1, 1),
            status="failed",
        )

        orm.Project.objects.create(
            title="Volunteering with Write Around Portland",
            summary="I'm lucky to be a volunteer, sustaining donor, and workshop facilitator for this amazing organization. Write Around Portland provides free creative writing workshops to people all across our community who can really use them.",
            url="http://www.writearound.org",
            date_started=datetime.datetime(2009, 1, 1),
            status="success",
        )
        orm.Project.objects.create(
            title="30 people, 30 minutes",
            summary="I turned 30 by spending the day talking to 30 people for 30 minutes each.  This website has this highlights.",
            url="http://www.30people30minutes.com",
            date_started=datetime.datetime(2010, 4, 9),
            status="success",
        )

        orm.Project.objects.create(
            title="Quantum Imagery",
            summary="The first company I really made my living on, Quantum Imagery was (mostly) a sole proprietorship that built all sorts of cool web stuff over the next 10 years.",
            url="http://www.quantumimagery.com",
            date_started=datetime.datetime(1999, 6, 1),
            status="success",
        )

        orm.Project.objects.create(
            title="Photoblog",
            summary="A couple of years of a semi-serious foray into digital photography",
            url="http://www.skoczen.net/photos",
            date_started=datetime.datetime(2005, 1, 1),
            status="lived",
        )
        orm.Project.objects.create(
            title="dwr",
            summary="A photo gallery application, in PHP.  With documentation!",
            url="http://www.quantumimagery.com/software-dwr.html",
            date_started=datetime.datetime(2005, 6, 1),
            status="lived",
        )
        orm.Project.objects.create(
            title="Linear Laundry",
            summary="An application and set of photoshop actions for developing RAW camera files",
            url="http://www.quantumimagery.com/software-linearLaundry.html",
            date_started=datetime.datetime(2005, 5, 1),
            status="lived",
        )
        orm.Project.objects.create(
            title="Fluidtask",
            summary="A flexible to-do list for balancing multiple projects and interleaved timelines. Worked great for me, but not really anyone else.",
            url="http://www.fluidtask.net",
            date_started=datetime.datetime(2006, 1, 1),
            status="failed",
        )
        orm.Project.objects.create(
            title="My Portland Schools",
            summary="A facebook app connecting the greater Portland community to their schools.",
            url="http://www.fluidtask.net",
            date_started=datetime.datetime(2012, 7, 1),
            status="failed",
        )


        orm.Project.objects.create(
            title="But I'm hungry!",
            summary="My recipe and restaurant review site, in the day before there was a yelp or recipezaar.",
            url="http://skoczen.net/food/",
            date_started=datetime.datetime(2005, 1, 16),
            status="lived",
        )
        orm.Project.objects.create(
            title="Liquid Silver Zen",
            summary="My pre-2006 personal site, which morphed through a few iterations. These were my early experiments in design and digital interaction.",
            url="http://liquidsilverzen.net/",
            date_started=datetime.datetime(2002, 1, 1),
            status="lived",
        )
        orm.Project.objects.create(
            title="Coffeehous.es",
            summary="A place for conversation and ideas.  Made so that intellectual discourse between far-away friends can flourish.",
            url="http://coffeehous.es",
            date_started=datetime.datetime(2014, 3, 16),
            status="who_knows",
        )
        orm.Project.objects.create(
            title="Science for Humans",
            summary="Turning dry, hard-to-read journal articles into quick, funny animated videos.",
            url="http://youtube.com/scienceforhumans",
            date_started=datetime.datetime(2014, 3, 20),
            status="who_knows",
        )
        orm.Project.objects.create(
            title="Poetr",
            summary="An online place for poetry.  Disrupting the elitist, bullshit poetry journal industry.",
            url="http://www.poetr.com",
            date_started=datetime.datetime(2014, 4, 20),
            status="who_knows",
        )
        orm.Project.objects.create(
            title="Autoscalebot, the company",
            summary="A software-as-a-service that automatically scales your heroku apps.",
            url="https://autoscalebot.com",
            date_started=datetime.datetime(2013, 5, 1),
            status="who_knows",
        )
        orm.Project.objects.create(
            title="Autoscalebot, the project.",
            summary="An open-source robot that automatically scales your heroku apps. Built at Wieden+Kennedy.",
            url="https://github.com/wieden-kennedy/autoscalebot",
            date_started=datetime.datetime(2012, 2, 1),
            status="success",
        )
        orm.Project.objects.create(
            title="Branch Leaf Idea",
            summary="A blog on sustainability, how-tech-works, and musings on a bright green future.",
            url=None,
            date_started=datetime.datetime(2004, 9, 1),
            status="lived",
        )
        orm.Project.objects.create(
            title="ebDB: The International Ethnobotany Database",
            summary="A web-accessible database, intended to securely house all the world's ethnobotanical research. v1 succeeded, but v2 became my Second System Syndrome albatross, and 8 years later, ultimately failed.  v3 lives on Zoho.  With Drs. Rainer Bussman and Doug Sharon.",
            url="https://ebdb.org",
            date_started=datetime.datetime(2002, 6, 1),
            status="lived",
        )
        orm.Project.objects.create(
            title="Olorien",
            summary="An open-source framework for scientific journal creation, with Dr. Rainer Bussmann.",
            url="https://www.quantumimagery.com/software-olorien",
            date_started=datetime.datetime(2003, 2, 1),
            status="failed",
        )
        orm.Project.objects.create(
            title="Lyonia",
            summary="The first installation of olorien, with Dr. Rainer Bussmann.",
            url="https://www.quantumimagery.com/software-lyonia",
            date_started=datetime.datetime(2003, 1, 1),
            status="who_knows",
        )
        orm.Project.objects.create(
            title="Will",
            summary="The most friendly, easy-to-program chat bot you've ever used. Pure python, built at GreenKahuna.",
            url="https://www.github.com/greenkahuna/will",
            date_started=datetime.datetime(2013, 12, 15),
            status="success",
        )
        orm.Project.objects.create(
            title="My Will",
            summary="My personal incarnation of will, who keeps an eye on how many beers I drink, my home's temperature, my fluid loss from a run, and reminds me of my big goals.  I love will so much.",
            url="https://www.github.com/skoczen/my-will",
            date_started=datetime.datetime(2014, 1, 20),
            status="success",
        )
        orm.Project.objects.create(
            title="The Steven Manual",
            summary="An intelligent book-of-sorts that keeps an eye on my life, pings me when I'm getting off-course, reminds me of emotional insights, and enforces the habits I want to cultivate.",
            url="https://www.github.com/skoczen/skoczen.git",
            date_started=datetime.datetime(2012, 6, 1),
            status="success",
        )
        orm.Project.objects.create(
            title="College, part deux.",
            summary="Spent 3 years at Cornell, got a degree. Never used it after I graduated.  However, the now-laminated diploma works really nicely as a placeholder for the best dog in the world's food.",
            url="http://www.cornell.edu",
            date_started=datetime.datetime(2006, 9, 1),
            status="failed",
        )
        orm.Project.objects.create(
            title="Django Ajax Uploader",
            summary="Solving the problem of ajax upload to django, once and for all. Came out of GoodCloud.",
            url="https://www.github.com/goodcloud/django-ajax-uploader.git",
            date_started=datetime.datetime(2011, 3, 1),
            status="success",
        )
        orm.Project.objects.create(
            title="Django Longer Username",
            summary="Django had an annoying username problem.  This project fixed it, for many, many people.  Eventually replaced by another coder's forked project, django-longer-username-and-email. Came out of GoodCloud.",
            url="https://www.github.com/goodcloud/django-longer-username.git",
            date_started=datetime.datetime(2011, 4, 1),
            status="success",
        )
        orm.Project.objects.create(
            title="Django Zebra",
            summary="A library for integrating the stripe billing service into django apps. Came out of GoodCloud.",
            url="https://www.github.com/goodcloud/django-zebra.git",
            date_started=datetime.datetime(2011, 5, 1),
            status="success",
        )
        orm.Project.objects.create(
            title="Salad",
            summary="A python library for writing easy-to-read behavior-driven tests than run in web browsers. Built at Wieden+Kennedy, and open-sourced.",
            url="https://www.github.com/salad/salad.git",
            date_started=datetime.datetime(2012, 2, 1),
            status="success",
        )
        orm.Project.objects.create(
            title="Zombie Translator",
            summary="There was no reliable way to convert english to zombish in python. This project changed everything.  Built at Wieden+Kennedy.",
            url="https://www.pypi.org/zombie-translator",
            date_started=datetime.datetime(2012, 6, 1),
            status="lived",
        )
        orm.Project.objects.create(
            title="Donde Sun",
            summary="You're in Portland. It's raining.  Where is the nearest sun?  Where is the nearest snow? Built at Wieden+Kennedy.",
            url="https://www.dondesun.com",
            date_started=datetime.datetime(2012, 9, 1),
            status="success",
        )
        orm.Project.objects.create(
            title="Impact 4",
            summary="The leading framework for creating medical decision making instruments. With Dr. Leslie Lenert and Aditya Bansod, at UCSD.",
            url=None,
            date_started=datetime.datetime(2003, 6, 1),
            status="lived",
        )
        orm.Project.objects.create(
            title="Joint Count Project",
            summary="An accessible joint-pain reporter that worked for patients with advanced arthritis, and generated doctor-friendly output.  With Drs. Ann Sturley and Leslie Lenert, at UCSD.",
            url=None,
            date_started=datetime.datetime(2003, 10, 1),
            status="lived",
        )
        orm.Project.objects.create(
            title="Honda E-Learning framework",
            summary="Built an e-learning framework for Honda that beat out competing projects from 10 firms, and was used unchanged for 6 years.  With YPG.",
            url=None,
            date_started=datetime.datetime(2002, 6, 1),
            status="success",
        )
        orm.Project.objects.create(
            title="Home",
            summary="A coffee-table photo book about the desert, development, and home.",
            url=None,
            date_started=datetime.datetime(2007, 4, 1),
            status="success",
        )
        orm.Project.objects.create(
            title="An awesome table",
            summary="Sometimes I make furniture I'm proud of.  Like this table.",
            url=None,
            date_started=datetime.datetime(2013, 3, 1),
            status="success",
        )
        orm.Project.objects.create(
            title="WoodFriend",
            summary="A living sculptural piece, about touch.",
            url=None,
            date_started=datetime.datetime(2013, 5, 1),
            status="success",
        )
        orm.Project.objects.create(
            title="Steven's Computer Solutions",
            summary="My first real company, mowing lawns aside.  Everything from video card upgrades to web design to MS Word instruction.",
            url=None,
            date_started=datetime.datetime(1996, 6, 1),
            status="lived",
        )
        orm.Project.objects.create(
            title="Co-authored Foundation Javascript Book",
            summary="I wrote about half of this book for Wrox Press. Unfortunately, they mis-timed the schedule, and scrapped the book a couple months later when Javascript 2 came out.",
            url=None,
            date_started=datetime.datetime(2001, 5, 1),
            status="failed",
        )
        orm.Project.objects.create(
            title="Flash Components",
            summary="Open-source Macromedia Flash components for CPU detection, bandwidth detection, and console",
            url="http://quantumimagery.com/software-flash",
            date_started=datetime.datetime(2001, 8, 1),
            status="success",
        )
        orm.Project.objects.create(
            title="Django Better-500s",
            summary="Making error pages more friendly for users, and more useful for developers. Came out of GoodCloud.",
            url=None,
            date_started=datetime.datetime(2011, 2, 1),
            status="success",
        )
        orm.Project.objects.create(
            title="College",
            summary="Went to the Univerity of Arizona.  GPA went: Fall: 4.0, Spring: 0.0, Summer: dropped out.",
            url=None,
            date_started=datetime.datetime(1998, 12, 1),
            status="failed",
        )
        orm.Project.objects.create(
            title="Steven's Lawn Care",
            summary="You need your lawn mowed?  Don't want to do it yourself?  I'd do a pretty passable job.",
            url=None,
            date_started=datetime.datetime(1992, 5, 1),
            status="lived",
        )
        orm.Project.objects.create(
            title="Life",
            summary="Really didn't do a lot for this one, other than starting breathing.  To be fair, I'd bet that was pretty hard work.",
            url=None,
            date_started=datetime.datetime(1980, 4, 9),
            status="who_knows",
        )
        orm.Project.objects.create(
            title="Raising the world's best dog.",
            summary="Got lucky on this one by picking the world's best dog out of the shelter lineup.",
            url=None,
            date_started=datetime.datetime(1999, 4, 1),
            status="success",
        )

    def backwards(self, orm):
        orm.Project.objects.all().delete()

    models = {
        'main_site.project': {
            'Meta': {'object_name': 'Project'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'date_started': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'status': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'summary': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'url': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['main_site']
    symmetrical = True




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