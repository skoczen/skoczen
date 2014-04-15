# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import DataMigration
from django.db import models



class Migration(DataMigration):

    def forwards(self, orm):
        orm.Idea.objects.create(
            title="Idea Incubator",
            idea="Make a space on stevenskoczen.com that allows me put ideas to incubate, instead of having them disappear into scraps of paper!",
            status="living",
        )
        orm.Idea.objects.create(
            title="New StevenSkoczen.com with timeline",
            idea="Redo stevenskoczen.com to show a timeline of projects and work, as much for my benefit as anyone - allow me to see how much I've started, tried, accomplished, and failed, as a rebuttal to the 'you haven't done anything' blues.",
            status="incubating",
        )
        orm.Idea.objects.create(
            title="Poetr",
            idea="""Flickr for poetry.

Wide-open, free accounts. Features:
- Drafts and published
- Comments allowed on your work, or not.
- Pretty urls (premium?)
- Show draft revisions?
- Show published revisions?
- Monthly emailed backups (zip file of all your work, premium?)
- Choose font?
- Beautiful layout.  Poetry on page vs prose
- Formatting: bold/italic/underline/page break
- Use pileus engine
- Allow putting poems into collections
- Type: poem/prose/spoken word
- Audio (from soundcloud)
- Video (from vimeo/youtube)
- Post to fb? ("new poem at poetr "title...", link")
- Post to twitter? (same)
- Post to g+?
- Keep all revisions - every save is versioned.
- Names: Poetr, Poemshelf, Wordtable, Poettable, Poemtable, Wordr.
            """,
            status="incubating",
        )
        orm.Idea.objects.create(
            title="Coffeehouses",
            idea="""
Make a place for discussion, and intellectual discourse.

Post an article, title, summary.  See only things your friends posted, but don't see who posted it.
Have conversations with faces only.
Overheard
Conversations go away two weeks after nobody's replied - can only see the URL+title, and who you talked to.  Nobody else can see that there was a convo.
Limited avail/ only 3 articles to read per session? 
    "Welcome back, Steven.  Here's three things you should see:"  Resets once per day, shows progress when you've opened the link.
            """,
            status="started",
        )
        orm.Idea.objects.create(
            title="Science for Humans",
            idea="""Translate journal articles into fun, amusing cartoons.
Long-term, build a business offering this as a premium service to journals.
Move fast. Ship the videos, move on. Iterate in public.
""",
            status="started",
        )
        orm.Idea.objects.create(
            title="My poetry has a home",
            idea="""Really, this is the precursor to poetr, and I'm not sure if it'd be better to just build it there.
I want a place to see all my work, grouped by year, to edit and revise, and to see drafts and progress.  Less interested in comments, likes, etc - this is for me.

But - it'd be a great place to work out the kinks on formatting, UX, etc.
""",
            status="incubating",
        )

    def backwards(self, orm):
        "Write your backwards methods here."

    models = {
        'ideas.idea': {
            'Meta': {'ordering': "('thought_of_date',)", 'object_name': 'Idea'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'idea': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'started_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'status': ('django.db.models.fields.CharField', [], {'default': "'incubating'", 'max_length': '50'}),
            'thought_of_date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2014, 4, 15, 11, 15)'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['ideas']
    symmetrical = True
