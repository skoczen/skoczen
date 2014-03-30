# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Weight'
        db.create_table('manual_weight', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('updated_at', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('when', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2014, 3, 29, 0, 0))),
            ('weight', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('body_fat_percent', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
        ))
        db.send_create_signal('manual', ['Weight'])


    def backwards(self, orm):
        # Deleting model 'Weight'
        db.delete_table('manual_weight')


    models = {
        'manual.datasensitivity': {
            'Meta': {'object_name': 'DataSensitivity'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        'manual.emotion': {
            'Meta': {'ordering': "('name',)", 'object_name': 'Emotion'},
            'cause': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'helpful': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'one_liner': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'slug': ('django.db.models.fields.CharField', [], {'max_length': '210', 'null': 'True', 'blank': 'True'}),
            'symptoms': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        'manual.gutterbumper': {
            'Meta': {'ordering': "('date',)", 'object_name': 'GutterBumper'},
            'alone_hrs': ('django.db.models.fields.FloatField', [], {'default': '0', 'null': 'True', 'blank': 'True'}),
            'body_fat_percent': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'creativity': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'creativity_set': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'date': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime(2014, 3, 29, 0, 0)'}),
            'emotions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['manual.Emotion']", 'null': 'True', 'blank': 'True'}),
            'fell_asleep_at': ('django.db.models.fields.TimeField', [], {'default': 'datetime.time(0, 0)'}),
            'friend_hrs': ('django.db.models.fields.FloatField', [], {'default': '0', 'null': 'True', 'blank': 'True'}),
            'happiness': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'happiness_set': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'inbox_zero': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'interacted_with_art': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'left_the_house': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'meditated': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'morning_mood': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'morning_mood_set': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'nature_time': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'notes': ('django.db.models.fields.TextField', [], {'default': "'86400'", 'null': 'True', 'blank': 'True'}),
            'number_of_fun_beers': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'number_of_sleep_beers': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'off': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'presence': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'presence_set': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'public_hrs': ('django.db.models.fields.FloatField', [], {'default': '0', 'null': 'True', 'blank': 'True'}),
            'relationship_hrs': ('django.db.models.fields.FloatField', [], {'default': '0', 'null': 'True', 'blank': 'True'}),
            'sex': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'sleep_hrs': ('django.db.models.fields.FloatField', [], {'default': '0', 'null': 'True', 'blank': 'True'}),
            'travelling_or_out_of_routine': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'unbusy': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'unbusy_set': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'weight': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'woke_up_at': ('django.db.models.fields.TimeField', [], {'default': 'datetime.time(8, 30)'}),
            'work_hrs': ('django.db.models.fields.FloatField', [], {'default': '0', 'null': 'True', 'blank': 'True'}),
            'worked_out': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
        'manual.monthlycheckin': {
            'Meta': {'object_name': 'MonthlyCheckin'},
            'closer_to_two_year_plan_notes': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'closer_to_two_year_plan_rating': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'enough_time_alone_notes': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'enough_time_alone_rating': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'enough_time_in_nature_notes': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'enough_time_in_nature_rating': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'finances_on_track_notes': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'finances_on_track_rating': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'getting_out_enough_notes': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'getting_out_enough_rating': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'habit_success_notes': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'habit_success_rating': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'habits_for_next_month': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'habits_from_last_month': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'happiness_notes': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'happiness_rating': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'have_a_space_that_is_just_mine_notes': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'have_a_space_that_is_just_mine_rating': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'healthy_activity_notes': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'healthy_activity_rating': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'healthy_drinking_notes': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'healthy_drinking_rating': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'healthy_eating_notes': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'healthy_eating_rating': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'in_touch_with_spirtuality_notes': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'in_touch_with_spirtuality_rating': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'making_the_world_a_bit_better_notes': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'making_the_world_a_bit_better_rating': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'making_things_notes': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'making_things_rating': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'month_start_date': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime(2014, 3, 29, 0, 0)'}),
            'presence_notes': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'presence_rating': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'relationship_health_notes': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'relationship_health_rating': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'sex_life_is_good_notes': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'sex_life_is_good_rating': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'what_is_the_identity_story_i_am_telling': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'what_is_the_relationship_story_i_am_telling': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'what_is_the_work_story_i_am_telling': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'})
        },
        'manual.restaurant': {
            'Meta': {'object_name': 'Restaurant'},
            'date_went': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'have_gone': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'meal': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'notes': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'rating': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        'manual.value': {
            'Meta': {'object_name': 'Value'},
            'explanation': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'slug': ('django.db.models.fields.CharField', [], {'max_length': '210', 'null': 'True', 'blank': 'True'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        'manual.weeklymeal': {
            'Meta': {'object_name': 'WeeklyMeal'},
            'how_it_went': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ingredients': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'preparation': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'week_start_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'})
        },
        'manual.weight': {
            'Meta': {'object_name': 'Weight'},
            'body_fat_percent': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'weight': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'when': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2014, 3, 29, 0, 0)'})
        }
    }

    complete_apps = ['manual']