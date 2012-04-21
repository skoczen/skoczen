# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Page'
        db.create_table('main_site_page', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('top', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('bottom', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('middle_html', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('year', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('order', self.gf('django.db.models.fields.IntegerField')(default=0)),
        ))
        db.send_create_signal('main_site', ['Page'])


    def backwards(self, orm):
        
        # Deleting model 'Page'
        db.delete_table('main_site_page')


    models = {
        'main_site.page': {
            'Meta': {'object_name': 'Page'},
            'bottom': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'middle_html': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'order': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'top': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'year': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['main_site']