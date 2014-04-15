# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Idea'
        db.create_table('ideas_idea', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('updated_at', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('thought_of_date', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2014, 4, 15, 0, 0))),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=500)),
            ('idea', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('status', self.gf('django.db.models.fields.CharField')(default='incubating', max_length=50)),
            ('started_date', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
        ))
        db.send_create_signal('ideas', ['Idea'])


    def backwards(self, orm):
        # Deleting model 'Idea'
        db.delete_table('ideas_idea')


    models = {
        'ideas.idea': {
            'Meta': {'ordering': "('thought_of_date',)", 'object_name': 'Idea'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'idea': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'started_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'status': ('django.db.models.fields.CharField', [], {'default': "'incubating'", 'max_length': '50'}),
            'thought_of_date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2014, 4, 15, 0, 0)'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['ideas']