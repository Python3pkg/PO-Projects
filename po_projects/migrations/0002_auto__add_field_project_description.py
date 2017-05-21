# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Project.description'
        db.add_column('po_projects_project', 'description',
                      self.gf('django.db.models.fields.TextField')(default='', blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Project.description'
        db.delete_column('po_projects_project', 'description')


    models = {
        'po_projects.catalog': {
            'Meta': {'object_name': 'Catalog'},
            'header_comment': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'locale': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'mime_headers': ('django.db.models.fields.TextField', [], {}),
            'project_version': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['po_projects.ProjectVersion']"})
        },
        'po_projects.project': {
            'Meta': {'object_name': 'Project'},
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '75'})
        },
        'po_projects.projectversion': {
            'Meta': {'object_name': 'ProjectVersion'},
            'header_comment': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mime_headers': ('django.db.models.fields.TextField', [], {}),
            'project': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['po_projects.Project']"}),
            'version': ('django.db.models.fields.SmallIntegerField', [], {})
        },
        'po_projects.templatemsg': {
            'Meta': {'object_name': 'TemplateMsg'},
            'flags': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'locations': ('django.db.models.fields.TextField', [], {}),
            'message': ('django.db.models.fields.TextField', [], {}),
            'project_version': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['po_projects.ProjectVersion']"})
        },
        'po_projects.translationmsg': {
            'Meta': {'object_name': 'TranslationMsg'},
            'catalog': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['po_projects.Catalog']"}),
            'fuzzy': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'message': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'pluralizable': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'python_format': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'template': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['po_projects.TemplateMsg']"})
        }
    }

    complete_apps = ['po_projects']