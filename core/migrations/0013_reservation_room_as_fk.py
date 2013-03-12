# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import DataMigration
from django.db import models

class Migration(DataMigration):

	def forwards(self, orm):
		"Write your forwards methods here."
		# Note: Remember to use orm['appname.ModelName'] rather than "from appname.models..."
		for r in orm.Reservation.objects.all():
			if r.accommodation_preference == 'private' or r.accommodation_preference == 'prefer private':
				penrose = orm.Room.objects.filter(name="Penrose")[0]
				r.room = penrose
			else:
				hostel = orm.Room.objects.filter(name="Ada Lovelace Hostel")[0]
				r.room = hostel
			r.save()

	def backwards(self, orm):
		"Write your backwards methods here."
		penrose = orm.Room.objects.filter(name="Penrose")[0]
		hostel = orm.Room.objects.filter(name="Ada Lovelace Hostel")[0]
		for r in orm.Reservation.objects.all():
			if r.room == penrose: 
				r.accommodation_preference = 'private'
			else:
				r.accommodation_preference = 'shared'
			r.save()
		

	models = {
		'auth.group': {
			'Meta': {'object_name': 'Group'},
			'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
			'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
			'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
		},
		'auth.permission': {
			'Meta': {'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
			'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
			'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
			'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
			'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
		},
		'auth.user': {
			'Meta': {'object_name': 'User'},
			'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
			'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
			'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
			'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
			'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
			'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
			'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
			'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
			'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
			'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
			'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
			'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
			'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
		},
		'contenttypes.contenttype': {
			'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
			'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
			'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
			'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
			'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
		},
		'core.reconcile': {
			'Meta': {'object_name': 'Reconcile'},
			'automatic_invoice': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
			'custom_rate': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
			'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
			'paid_amount': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
			'payment_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
			'payment_method': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
			'payment_service': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
			'reservation': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['core.Reservation']", 'unique': 'True'}),
			'room_name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
			'status': ('django.db.models.fields.CharField', [], {'default': "'unpaid'", 'max_length': '200'}),
			'transaction_id': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'})
		},
		'core.reservation': {
			'Meta': {'object_name': 'Reservation'},
			'accommodation_preference': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
			'arrival_time': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
			'arrive': ('django.db.models.fields.DateField', [], {}),
			'comments': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
			'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
			'depart': ('django.db.models.fields.DateField', [], {}),
			'guest_emails': ('django.db.models.fields.CharField', [], {'max_length': '400', 'null': 'True', 'blank': 'True'}),
			'guest_name': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
			'hosted': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
			'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
			'purpose': ('django.db.models.fields.TextField', [], {}),
			'room': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.Room']", 'null': 'True'}),
			'status': ('django.db.models.fields.CharField', [], {'default': "'pending'", 'max_length': '200', 'blank': 'True'}),
			'tags': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
			'updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
			'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"})
		},
		'core.room': {
			'Meta': {'object_name': 'Room'},
			'default_rate': ('django.db.models.fields.IntegerField', [], {}),
			'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
			'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
			'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
			'primary_use': ('django.db.models.fields.CharField', [], {'default': "'private'", 'max_length': '200'})
		},
		'core.userprofile': {
			'Meta': {'object_name': 'UserProfile'},
			'bio': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
			'discussion': ('django.db.models.fields.TextField', [], {}),
			'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
			'image': ('django.db.models.fields.files.ImageField', [], {'default': "'data/avatars/default.jpg'", 'max_length': '100'}),
			'image_thumb': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
			'links': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
			'projects': ('django.db.models.fields.TextField', [], {}),
			'referral': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
			'sharing': ('django.db.models.fields.TextField', [], {}),
			'updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
			'user': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['auth.User']", 'unique': 'True'})
		}
	}

	complete_apps = ['core']
	symmetrical = True
