# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Deleting model 'SobreNos'
        db.delete_table('about_sobrenos')

        # Adding model 'Sobre'
        db.create_table('about_sobre', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('text', self.gf('django.db.models.fields.TextField')()),
            ('link', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('photo', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True)),
        ))
        db.send_create_signal('about', ['Sobre'])


    def backwards(self, orm):
        
        # Adding model 'SobreNos'
        db.create_table('about_sobrenos', (
            ('title', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('photo', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('link', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('text', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal('about', ['SobreNos'])

        # Deleting model 'Sobre'
        db.delete_table('about_sobre')


    models = {
        'about.sobre': {
            'Meta': {'object_name': 'Sobre'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'link': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'photo': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'text': ('django.db.models.fields.TextField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['about']
