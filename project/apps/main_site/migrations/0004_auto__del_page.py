# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Deleting model 'Page'
        db.delete_table('main_site_page')


    def backwards(self, orm):
        
        # Adding model 'Page'
        db.create_table('main_site_page', (
            ('bottom', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('active', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('middle_link', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('middle_html', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('top', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('year', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('order', self.gf('django.db.models.fields.IntegerField')(default=0)),
        ))
        db.send_create_signal('main_site', ['Page'])


    models = {
        
    }

    complete_apps = ['main_site']
