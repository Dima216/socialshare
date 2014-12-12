# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'JoinFriend'
        db.delete_table(u'heroku_app_joinfriend')

        # Removing M2M table for field friends on 'JoinFriend'
        db.delete_table(db.shorten_name(u'heroku_app_joinfriend_friends'))

        # Adding field 'Join.friend'
        db.add_column(u'heroku_app_join', 'friend',
                      self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='referral', null=True, to=orm['heroku_app.Join']),
                      keep_default=False)


    def backwards(self, orm):
        # Adding model 'JoinFriend'
        db.create_table(u'heroku_app_joinfriend', (
            ('friend_email', self.gf('django.db.models.fields.related.OneToOneField')(related_name='Sharer', unique=True, to=orm['heroku_app.Join'])),
            ('all_emails', self.gf('django.db.models.fields.related.ForeignKey')(related_name='all_emails', to=orm['heroku_app.Join'])),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal(u'heroku_app', ['JoinFriend'])

        # Adding M2M table for field friends on 'JoinFriend'
        m2m_table_name = db.shorten_name(u'heroku_app_joinfriend_friends')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('joinfriend', models.ForeignKey(orm[u'heroku_app.joinfriend'], null=False)),
            ('join', models.ForeignKey(orm[u'heroku_app.join'], null=False))
        ))
        db.create_unique(m2m_table_name, ['joinfriend_id', 'join_id'])

        # Deleting field 'Join.friend'
        db.delete_column(u'heroku_app_join', 'friend_id')


    models = {
        u'heroku_app.join': {
            'Meta': {'unique_together': "(('email', 'ref_id'),)", 'object_name': 'Join'},
            'email': ('django.db.models.fields.EmailField', [], {'unique': 'True', 'max_length': '75'}),
            'friend': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'referral'", 'null': 'True', 'to': u"orm['heroku_app.Join']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ip_address': ('django.db.models.fields.CharField', [], {'default': "'0.0.0.0'", 'max_length': '100'}),
            'ref_id': ('django.db.models.fields.CharField', [], {'default': "'abcdefg'", 'max_length': '100'}),
            'timestamp': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['heroku_app']