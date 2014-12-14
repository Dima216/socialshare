# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding unique constraint on 'Join', fields ['email', 'ref_id']
        db.create_unique(u'heroku_app_join', ['email', 'ref_id'])


    def backwards(self, orm):
        # Removing unique constraint on 'Join', fields ['email', 'ref_id']
        db.delete_unique(u'heroku_app_join', ['email', 'ref_id'])


    models = {
        u'heroku_app.join': {
            'Meta': {'unique_together': "(('email', 'ref_id'),)", 'object_name': 'Join'},
            'email': ('django.db.models.fields.EmailField', [], {'unique': 'True', 'max_length': '75'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ip_address': ('django.db.models.fields.CharField', [], {'default': "'0.0.0.0'", 'max_length': '100'}),
            'ref_id': ('django.db.models.fields.CharField', [], {'default': "'abcdefg'", 'max_length': '100'}),
            'timestamp': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        u'heroku_app.joinfriend': {
            'Meta': {'object_name': 'JoinFriend'},
            'all_emails': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'all_emails'", 'to': u"orm['heroku_app.Join']"}),
            'friend_email': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "'Sharer'", 'unique': 'True', 'to': u"orm['heroku_app.Join']"}),
            'friends': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'Friend'", 'null': 'True', 'symmetrical': 'False', 'to': u"orm['heroku_app.Join']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        }
    }

    complete_apps = ['heroku_app']