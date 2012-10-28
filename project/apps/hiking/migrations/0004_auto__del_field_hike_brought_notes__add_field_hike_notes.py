# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Hike.brought_notes'
        db.delete_column('hiking_hike', 'brought_notes')

        # Adding field 'Hike.notes'
        db.add_column('hiking_hike', 'notes',
                      self.gf('django.db.models.fields.TextField')(null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Adding field 'Hike.brought_notes'
        db.add_column('hiking_hike', 'brought_notes',
                      self.gf('django.db.models.fields.TextField')(null=True, blank=True),
                      keep_default=False)

        # Deleting field 'Hike.notes'
        db.delete_column('hiking_hike', 'notes')


    models = {
        'hiking.hike': {
            'Meta': {'ordering': "('date',)", 'object_name': 'Hike'},
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
            'is_back': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'left_on': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2012, 10, 25, 0, 0)'}),
            'notes': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'where': ('django.db.models.fields.TextField', [], {})
        }
    }

    complete_apps = ['hiking']