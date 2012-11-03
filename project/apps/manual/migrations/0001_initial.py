# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'DataSensitivity'
        db.create_table('manual_datasensitivity', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('updated_at', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal('manual', ['DataSensitivity'])

        # Adding model 'Emotion'
        db.create_table('manual_emotion', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('updated_at', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('slug', self.gf('django.db.models.fields.CharField')(max_length=210, null=True, blank=True)),
            ('one_liner', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('cause', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('symptoms', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('helpful', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
        ))
        db.send_create_signal('manual', ['Emotion'])

        # Adding model 'Value'
        db.create_table('manual_value', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('updated_at', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('slug', self.gf('django.db.models.fields.CharField')(max_length=210, null=True, blank=True)),
            ('explanation', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
        ))
        db.send_create_signal('manual', ['Value'])

        # Adding model 'GutterBumper'
        db.create_table('manual_gutterbumper', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('updated_at', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('date', self.gf('django.db.models.fields.DateField')(default=datetime.date(2012, 11, 2))),
            ('woke_up_at', self.gf('django.db.models.fields.TimeField')(default=datetime.time(7, 45))),
            ('fell_asleep_at', self.gf('django.db.models.fields.TimeField')(default=datetime.time(23, 30))),
            ('sleep_hrs', self.gf('django.db.models.fields.FloatField')(default=0, null=True, blank=True)),
            ('work_hrs', self.gf('django.db.models.fields.FloatField')(default=0, null=True, blank=True)),
            ('alone_hrs', self.gf('django.db.models.fields.FloatField')(default=0, null=True, blank=True)),
            ('friend_hrs', self.gf('django.db.models.fields.FloatField')(default=0, null=True, blank=True)),
            ('public_hrs', self.gf('django.db.models.fields.FloatField')(default=0, null=True, blank=True)),
            ('relationship_hrs', self.gf('django.db.models.fields.FloatField')(default=0, null=True, blank=True)),
            ('off', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('worked_out', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('meditated', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('left_the_house', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('nature_time', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('inbox_zero', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('travelling_or_out_of_routine', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('number_of_sleep_beers', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('number_of_fun_beers', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('presence', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('happiness', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('creativity', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('morning_mood', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('notes', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('weight', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('body_fat_percent', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
        ))
        db.send_create_signal('manual', ['GutterBumper'])

        # Adding M2M table for field emotions on 'GutterBumper'
        db.create_table('manual_gutterbumper_emotions', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('gutterbumper', models.ForeignKey(orm['manual.gutterbumper'], null=False)),
            ('emotion', models.ForeignKey(orm['manual.emotion'], null=False))
        ))
        db.create_unique('manual_gutterbumper_emotions', ['gutterbumper_id', 'emotion_id'])

        # Adding model 'WeeklyMeal'
        db.create_table('manual_weeklymeal', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('updated_at', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('ingredients', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('preparation', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('how_it_went', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('week_start_date', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
        ))
        db.send_create_signal('manual', ['WeeklyMeal'])

        # Adding model 'MonthlyCheckin'
        db.create_table('manual_monthlycheckin', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('updated_at', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('month_start_date', self.gf('django.db.models.fields.DateField')(default=datetime.date(2012, 11, 2))),
            ('happiness_rating', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('happiness_notes', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('relationship_health_rating', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('relationship_health_notes', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('enough_time_in_nature_rating', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('enough_time_in_nature_notes', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('presence_rating', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('presence_notes', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('in_touch_with_spirtuality_rating', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('in_touch_with_spirtuality_notes', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('making_things_rating', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('making_things_notes', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('have_a_space_that_is_just_mine_rating', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('have_a_space_that_is_just_mine_notes', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('enough_time_alone_rating', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('enough_time_alone_notes', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('finances_on_track_rating', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('finances_on_track_notes', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('getting_out_enough_rating', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('getting_out_enough_notes', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('sex_life_is_good_rating', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('sex_life_is_good_notes', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('making_the_world_a_bit_better_rating', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('making_the_world_a_bit_better_notes', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('healthy_eating_rating', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('healthy_eating_notes', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('healthy_drinking_rating', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('healthy_drinking_notes', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('healthy_activity_rating', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('healthy_activity_notes', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('closer_to_two_year_plan_rating', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('closer_to_two_year_plan_notes', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('habits_from_last_month', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('habit_success_rating', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('habit_success_notes', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('habits_for_next_month', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('what_is_the_work_story_i_am_telling', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('what_is_the_relationship_story_i_am_telling', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('what_is_the_identity_story_i_am_telling', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
        ))
        db.send_create_signal('manual', ['MonthlyCheckin'])


    def backwards(self, orm):
        
        # Deleting model 'DataSensitivity'
        db.delete_table('manual_datasensitivity')

        # Deleting model 'Emotion'
        db.delete_table('manual_emotion')

        # Deleting model 'Value'
        db.delete_table('manual_value')

        # Deleting model 'GutterBumper'
        db.delete_table('manual_gutterbumper')

        # Removing M2M table for field emotions on 'GutterBumper'
        db.delete_table('manual_gutterbumper_emotions')

        # Deleting model 'WeeklyMeal'
        db.delete_table('manual_weeklymeal')

        # Deleting model 'MonthlyCheckin'
        db.delete_table('manual_monthlycheckin')


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
            'date': ('django.db.models.fields.DateField', [], {'default': 'datetime.date(2012, 11, 2)'}),
            'emotions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['manual.Emotion']", 'null': 'True', 'blank': 'True'}),
            'fell_asleep_at': ('django.db.models.fields.TimeField', [], {'default': 'datetime.time(23, 30)'}),
            'friend_hrs': ('django.db.models.fields.FloatField', [], {'default': '0', 'null': 'True', 'blank': 'True'}),
            'happiness': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'inbox_zero': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'left_the_house': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'meditated': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'morning_mood': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'nature_time': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'notes': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'number_of_fun_beers': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'number_of_sleep_beers': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'off': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'presence': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'public_hrs': ('django.db.models.fields.FloatField', [], {'default': '0', 'null': 'True', 'blank': 'True'}),
            'relationship_hrs': ('django.db.models.fields.FloatField', [], {'default': '0', 'null': 'True', 'blank': 'True'}),
            'sleep_hrs': ('django.db.models.fields.FloatField', [], {'default': '0', 'null': 'True', 'blank': 'True'}),
            'travelling_or_out_of_routine': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'weight': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'woke_up_at': ('django.db.models.fields.TimeField', [], {'default': 'datetime.time(7, 45)'}),
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
            'month_start_date': ('django.db.models.fields.DateField', [], {'default': 'datetime.date(2012, 11, 2)'}),
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
        }
    }

    complete_apps = ['manual']
