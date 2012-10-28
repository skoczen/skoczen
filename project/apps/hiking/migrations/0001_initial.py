# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Hike'
        db.create_table('hiking_hike', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('updated_at', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('date', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2012, 10, 25, 0, 0))),
            ('expected_back', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2012, 10, 26, 0, 0))),
            ('where', self.gf('django.db.models.fields.TextField')()),
            ('have_left', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('am_back', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('brought_food', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('brought_water', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('brought_warm_layers', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('brought_water_purifier', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('brought_shelter', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('brought_flashlight', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('brought_spare_batteries', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('brought_rain_shell', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('brought_space_blankets', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('brought_leatherman', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('brought_hat', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('brought_gloves', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('brought_first_aid_kit', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('brought_gps', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('brought_phone', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('brought_spare_phone_battery', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('brought_hike_map', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('brought_compass', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('brought_paper_topo_map', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('brought_matches', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('brought_epipen', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('brought_notes', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
        ))
        db.send_create_signal('hiking', ['Hike'])


    def backwards(self, orm):
        # Deleting model 'Hike'
        db.delete_table('hiking_hike')


    models = {
        'hiking.hike': {
            'Meta': {'ordering': "('date',)", 'object_name': 'Hike'},
            'am_back': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'brought_compass': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'brought_epipen': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'brought_first_aid_kit': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'brought_flashlight': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'brought_food': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'brought_gloves': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'brought_gps': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'brought_hat': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'brought_hike_map': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'brought_leatherman': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'brought_matches': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'brought_notes': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'brought_paper_topo_map': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'brought_phone': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'brought_rain_shell': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'brought_shelter': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'brought_space_blankets': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'brought_spare_batteries': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'brought_spare_phone_battery': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'brought_warm_layers': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'brought_water': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'brought_water_purifier': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2012, 10, 25, 0, 0)'}),
            'expected_back': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2012, 10, 26, 0, 0)'}),
            'have_left': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'where': ('django.db.models.fields.TextField', [], {})
        }
    }

    complete_apps = ['hiking']