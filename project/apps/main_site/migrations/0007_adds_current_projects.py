# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import DataMigration
from django.db import models

class Migration(DataMigration):

    def forwards(self, orm):
        orm.Project.objects.create(
            title="is enough",
            summary="what does love mean to you?",
            url="http://isenough.com",
            date_started=datetime.datetime(2011, 11, 21),
            status="who_knows",
        )
        orm.Project.objects.create(
            title="encore",
            summary="a digital poem",
            url="http://www.encorepoem.com",
            date_started=datetime.datetime(2012, 4, 1),
            status="who_knows",
        )
        orm.Project.objects.create(
            title="Slow Art",
            summary="the anti-museum. in portland, or",
            url="http://slowartpdx.com",
            date_started=datetime.datetime(2011, 7, 1),
            status="success",
        )
        orm.Project.objects.create(
            title="togetheralone",
            summary="an experiment in community, with Anastasia Aizman",
            url="http://togetheralone.org",
            date_started=datetime.datetime(2012, 3, 1),
            status="failed",
        )
        orm.Project.objects.create(
            title="the digital executioner",
            summary="Viral web marketing campaign generator.  Won the internet for a day. Built at Wieden+Kennedy",
            url="http://www.thedigitalexecutioner.com",
            date_started=datetime.datetime(2012, 2, 1),
            status="success",
        )
        orm.Project.objects.create(
            title="goodcloud",
            summary="A contact, volunteer, and donor management software for small non-profits.",
            url="https://www.agoodcloud.com",
            date_started=datetime.datetime(2010, 11, 1),
            status="failed",
        )

        orm.Project.objects.create(
            title="sixlinks",
            summary="Trying to save the world, with Jeff Gunther.  Sixlinks was the big picture of the world's sustainability issues, and step-by-step guides of actions you can personally take.",
            url="http://www.sixlinks.org",
            date_started=datetime.datetime(2008, 1, 1),
            status="failed",
        )

        orm.Project.objects.create(
            title="Write Around Portland",
            summary="I'm lucky to be a volunteer, sustaining donor, and workshop facilitator for this amazing organization. Write Around Portland provides free creative writing workshops to people all across our community, who can really use them.",
            url="http://www.writearound.org",
            date_started=datetime.datetime(2009, 1, 1),
            status="success",
        )
        orm.Project.objects.create(
            title="30 people, 30 minutes",
            summary="I turned 30 by spending the day talking to 30 people for 30 minutes each.  This website is this highlights.",
            url="http://www.30people30minutes.com",
            date_started=datetime.datetime(2010, 4, 9),
            status="success",
        )

        orm.Project.objects.create(
            title="Quantum Imagery",
            summary="The first company I really made my living on, Quantum Imagery was (mostly) a sole proprietorship that built all sorts of cool web stuff.",
            url="http://www.quantumimagery.com",
            date_started=datetime.datetime(2000, 3, 1),
            status="success",
        )

        orm.Project.objects.create(
            title="photoblog",
            summary="A couple of years of a semi-serious foray into photography",
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
            title="fluidtask",
            summary="A flexible to-do list for balancing multiple projects and timelines. Worked for me, not really anyone else.",
            url="http://www.fluidtask.net",
            date_started=datetime.datetime(2006, 1, 1),
            status="failed",
        )

        orm.Project.objects.create(
            title="but i'm hungry!",
            summary="My recipe and restaurant review site, in the day before there was a yelp or recipezaar.",
            url="http://skoczen.net/food/",
            date_started=datetime.datetime(2005, 1, 16),
            status="lived",
        )
        orm.Project.objects.create(
            title="liquid silver zen",
            summary="My personal site, which morphed through a few iterations. These were my early experiments in design and interaction",
            url="http://liquidsilverzen.net/",
            date_started=datetime.datetime(2002, 1, 1),
            status="lived",
        )
        orm.Project.objects.create(
            title="Coffeehous.es",
            summary="A place for conversation and ideas.  Coffeehouses was built to support intellectual discourse among people who know each other.",
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
            summary="An open-source robot that automatically scales your heroku apps. Built at Wieden+Kennedy",
            url="https://github.com/wieden-kennedy/autoscalebot",
            date_started=datetime.datetime(2012, 2, 1),
            status="success",
        )
        orm.Project.objects.create(
            title="Branch Leaf Idea",
            summary="A blog on sustainability, how-tech-works, and musings on a bright green future.",
            url=None,
            date_started=datetime.datetime(2005, 5, 1),
            status="lived",
        )
        orm.Project.objects.create(
            title="ebDB: The International Ethnobotany Database",
            summary="A web-accessible database, intended to securely house all the world's ethnobotanical research. v1 succeeded, but v2 became my Duke Nukem albatross, and ultimately failed.  v3 lives on Zoho.  With Drs. Rainer Bussman and Doug Sharon.",
            url="https://ebdb.org",
            date_started=datetime.datetime(2002, 6, 1),
            status="lived",
        )
        orm.Project.objects.create(
            title="Olorien",
            summary="An open-source framework for scientific journal creation, with Dr. Rainer Bussmann",
            url="https://www.quantumimagery.com/software-olorien.",
            date_started=datetime.datetime(2003, 2, 1),
            status="failed",
        )
        orm.Project.objects.create(
            title="Lyonia",
            summary="The first installation of olorien, with Dr. Rainer Bussmann",
            url="https://www.quantumimagery.com",
            date_started=datetime.datetime(2003, 1, 1),
            status="who_knows",
        )
        orm.Project.objects.create(
            title="Will",
            summary="The most friendly, easy-to-program chat bot you've ever used. Pure python, built at GreenKahuna",
            url="https://www.github.com/greenkahuna/will",
            date_started=datetime.datetime(2013, 12, 15),
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
            title="Django Ajax Uploader",
            summary="Solving the problem of ajax upload to django, once and for all.",
            url="https://www.github.com/goodcloud/django-ajax-uploader.git",
            date_started=datetime.datetime(2011, 3, 1),
            status="success",
        )
        orm.Project.objects.create(
            title="Django Longer Username",
            summary="Django had an annoying username problem.  This project fixed it, for many many people.  Eventually replaced by a forked project, django-longer-username-and-email.",
            url="https://www.github.com/goodcloud/django-longer-username.git",
            date_started=datetime.datetime(2011, 4, 1),
            status="success",
        )
        orm.Project.objects.create(
            title="Django Zebra",
            summary="A library for integrating the stripe billing service into django apps.",
            url="https://www.github.com/goodcloud/django-zebra.git",
            date_started=datetime.datetime(2011, 5, 1),
            status="success",
        )
        orm.Project.objects.create(
            title="Salad",
            summary="A python library for writing easy-to-read behavior-driven tests than run in web-browsers. Built at Wieden+Kennedy, and open-sourced.",
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
            summary="Built an accessible joint-pain reporter that worked for patients with advanced arthritis, and generated doctor-friendly output.  With Drs. Ann Sturley and Leslie Lenert, at UCSD.",
            url=None,
            date_started=datetime.datetime(2003, 10, 1),
            status="lived",
        )
        orm.Project.objects.create(
            title="Honda E-Learning framework",
            summary="Built an e-learning framework for Honda that beat out competing projects from 10 firms, and was used unchanged for 7 years.  With YPG.",
            url=None,
            date_started=datetime.datetime(2002, 6, 1),
            status="success",
        )
        orm.Project.objects.create(
            title="Home",
            summary="A photo book about the desert, development, and home.",
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
            summary="A sculptural piece, about touch",
            url=None,
            date_started=datetime.datetime(2013, 5, 1),
            status="success",
        )
        orm.Project.objects.create(
            title="Steven's Computer Solutions",
            summary="My first real company, mowing lawns aside.",
            url=None,
            date_started=datetime.datetime(1996, 6, 1),
            status="lived",
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