# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Project'
        db.create_table(u'po_projects_project', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=150)),
            ('slug', self.gf('django.db.models.fields.SlugField')(unique=True, max_length=75)),
            ('version', self.gf('django.db.models.fields.CharField')(max_length=15)),
            ('header_comment', self.gf('django.db.models.fields.TextField')()),
            ('mime_headers', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'po_projects', ['Project'])

        # Adding model 'TemplateMsg'
        db.create_table(u'po_projects_templatemsg', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('project', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['po_projects.Project'])),
            ('message', self.gf('django.db.models.fields.TextField')()),
            ('locations', self.gf('django.db.models.fields.TextField')()),
            ('flags', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'po_projects', ['TemplateMsg'])

        # Adding model 'Catalog'
        db.create_table(u'po_projects_catalog', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('project', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['po_projects.Project'])),
            ('locale', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('header_comment', self.gf('django.db.models.fields.TextField')()),
            ('mime_headers', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'po_projects', ['Catalog'])

        # Adding model 'TranslationMsg'
        db.create_table(u'po_projects_translationmsg', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('template', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['po_projects.TemplateMsg'])),
            ('catalog', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['po_projects.Catalog'])),
            ('message', self.gf('django.db.models.fields.TextField')(blank=True)),
        ))
        db.send_create_signal(u'po_projects', ['TranslationMsg'])


    def backwards(self, orm):
        # Deleting model 'Project'
        db.delete_table(u'po_projects_project')

        # Deleting model 'TemplateMsg'
        db.delete_table(u'po_projects_templatemsg')

        # Deleting model 'Catalog'
        db.delete_table(u'po_projects_catalog')

        # Deleting model 'TranslationMsg'
        db.delete_table(u'po_projects_translationmsg')


    models = {
        u'po_projects.catalog': {
            'Meta': {'object_name': 'Catalog'},
            'header_comment': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'locale': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'mime_headers': ('django.db.models.fields.TextField', [], {}),
            'project': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['po_projects.Project']"})
        },
        u'po_projects.project': {
            'Meta': {'object_name': 'Project'},
            'header_comment': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mime_headers': ('django.db.models.fields.TextField', [], {}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '75'}),
            'version': ('django.db.models.fields.CharField', [], {'max_length': '15'})
        },
        u'po_projects.templatemsg': {
            'Meta': {'object_name': 'TemplateMsg'},
            'flags': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'locations': ('django.db.models.fields.TextField', [], {}),
            'message': ('django.db.models.fields.TextField', [], {}),
            'project': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['po_projects.Project']"})
        },
        u'po_projects.translationmsg': {
            'Meta': {'object_name': 'TranslationMsg'},
            'catalog': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['po_projects.Catalog']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'message': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'template': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['po_projects.TemplateMsg']"})
        }
    }

    complete_apps = ['po_projects']