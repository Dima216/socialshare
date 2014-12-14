# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'JoinFriends'
        db.create_table(u'heroku_app_joinfriends', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('friend_email', self.gf('django.db.models.fields.related.OneToOneField')(related_name='Sharer', unique=True, to=orm['heroku_app.Join'])),
            ('all_emails', self.gf('django.db.models.fields.related.ForeignKey')(related_name='all_emails', to=orm['heroku_app.Join'])),
        ))
        db.send_create_signal(u'heroku_app', ['JoinFriends'])

        # Adding M2M table for field friends on 'JoinFriends'
        m2m_table_name = db.shorten_name(u'heroku_app_joinfriends_friends')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('joinfriends', models.ForeignKey(orm[u'heroku_app.joinfriends'], null=False)),
            ('join', models.ForeignKey(orm[u'heroku_app.join'], null=False))
        ))
        db.create_unique(m2m_table_name, ['joinfriends_id', 'join_id'])

        # Adding unique constraint on 'Join', fields ['email']
        db.create_unique(u'heroku_app_join', ['email'])


    def backwards(self, orm):
        # Removing unique constraint on 'Join', fields ['email']
        db.delete_unique(u'heroku_app_join', ['email'])

        # Deleting model 'JoinFriends'
        db.delete_table(u'heroku_app_joinfriends')

        # Removing M2M table for field friends on 'JoinFriends'
        db.delete_table(db.shorten_name(u'heroku_app_joinfriends_friends'))


    models = {
        u'heroku_app.join': {
            'Meta': {'object_name': 'Join'},
            'email': ('django.db.models.fields.EmailField', [], {'unique': 'True', 'max_length': '75'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ip_address': ('django.db.models.fields.CharField', [], {'default': "'0.0.0.0'", 'max_length': '100'}),
            'timestamp': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        u'heroku_app.joinfriends': {
            'Meta': {'object_name': 'JoinFriends'},
            'all_emails': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'all_emails'", 'to': u"orm['heroku_app.Join']"}),
            'friend_email': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "'Sharer'", 'unique': 'True', 'to': u"orm['heroku_app.Join']"}),
            'friends': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'Friend'", 'null': 'True', 'symmetrical': 'False', 'to': u"orm['heroku_app.Join']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        }
    }

    complete_apps = ['heroku_app']