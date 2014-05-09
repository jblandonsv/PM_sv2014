# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'PostulacionesCalidad.email_ejecutivo'
        db.alter_column(u'calidad_postulacionescalidad', 'email_ejecutivo', self.gf('django.db.models.fields.CharField')(max_length=100))

        # Changing field 'PostulacionesCalidad.email_alterno'
        db.alter_column(u'calidad_postulacionescalidad', 'email_alterno', self.gf('django.db.models.fields.CharField')(max_length=100))

        # Changing field 'PostulacionesCalidad.email_contacto'
        db.alter_column(u'calidad_postulacionescalidad', 'email_contacto', self.gf('django.db.models.fields.CharField')(max_length=100))

    def backwards(self, orm):

        # Changing field 'PostulacionesCalidad.email_ejecutivo'
        db.alter_column(u'calidad_postulacionescalidad', 'email_ejecutivo', self.gf('django.db.models.fields.CharField')(max_length=25))

        # Changing field 'PostulacionesCalidad.email_alterno'
        db.alter_column(u'calidad_postulacionescalidad', 'email_alterno', self.gf('django.db.models.fields.CharField')(max_length=25))

        # Changing field 'PostulacionesCalidad.email_contacto'
        db.alter_column(u'calidad_postulacionescalidad', 'email_contacto', self.gf('django.db.models.fields.CharField')(max_length=25))

    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'calidad.areaexperiencia': {
            'Meta': {'object_name': 'AreaExperiencia'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre_area': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '150'})
        },
        u'calidad.criterioscalidad': {
            'Meta': {'object_name': 'CriteriosCalidad'},
            'agrupador': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'cod_agrupador': ('django.db.models.fields.CharField', [], {'max_length': '2', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'literal': ('django.db.models.fields.CharField', [], {'max_length': '5', 'blank': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'}),
            'puntaje_maximo': ('django.db.models.fields.IntegerField', [], {'default': '0', 'blank': 'True'})
        },
        u'calidad.criteriosevaluacion': {
            'Meta': {'object_name': 'CriteriosEvaluacion'},
            'aprendizaje': ('django.db.models.fields.IntegerField', [], {'default': '0', 'blank': 'True'}),
            'areas_mejorar': ('tinymce.models.HTMLField', [], {'blank': 'True'}),
            'criterio': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['calidad.CriteriosCalidad']"}),
            'despligue': ('django.db.models.fields.IntegerField', [], {'default': '0', 'blank': 'True'}),
            'enfoque': ('django.db.models.fields.IntegerField', [], {'default': '0', 'blank': 'True'}),
            'evaluacion': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['calidad.EvaluacionIndividualCalidad']"}),
            'fortalezas': ('tinymce.models.HTMLField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'integracion': ('django.db.models.fields.IntegerField', [], {'default': '0', 'blank': 'True'}),
            'promedio': ('django.db.models.fields.DecimalField', [], {'default': '0', 'max_digits': '3', 'decimal_places': '2', 'blank': 'True'}),
            'puntos_visita': ('tinymce.models.HTMLField', [], {'blank': 'True'}),
            'total': ('django.db.models.fields.DecimalField', [], {'default': '0', 'max_digits': '3', 'decimal_places': '2', 'blank': 'True'})
        },
        u'calidad.estudio': {
            'Meta': {'object_name': 'Estudio'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre_estudio': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '150'})
        },
        u'calidad.evaluacionindividualcalidad': {
            'Meta': {'object_name': 'EvaluacionIndividualCalidad'},
            'ambiente_competitivo': ('tinymce.models.HTMLField', [], {'blank': 'True'}),
            'ambiente_organizacional': ('tinymce.models.HTMLField', [], {'blank': 'True'}),
            'desafios_estrategicos': ('tinymce.models.HTMLField', [], {'blank': 'True'}),
            'evaluador_postulacion': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['calidad.Evaluador']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nota': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'nota_global': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'postulacion_evaluacion': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['calidad.PostulacionesCalidad']"}),
            'relaciones_organizacionales': ('tinymce.models.HTMLField', [], {'blank': 'True'}),
            'sistema_mejora': ('tinymce.models.HTMLField', [], {'blank': 'True'})
        },
        u'calidad.evaluador': {
            'Meta': {'object_name': 'Evaluador'},
            'capacitacion_formacion': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'cargo': ('django.db.models.fields.CharField', [], {'max_length': '150', 'blank': 'True'}),
            'codigo': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '15'}),
            'dui': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '15'}),
            'edad': ('django.db.models.fields.IntegerField', [], {'blank': 'True'}),
            'empresa_actual': ('django.db.models.fields.CharField', [], {'max_length': '150', 'blank': 'True'}),
            'estudios': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['calidad.Estudio']"}),
            'experiencia': ('django.db.models.fields.CharField', [], {'max_length': '85', 'blank': 'True'}),
            'experiencia_en_calidad': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'experiencia_facilitador': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'formacion_en_calidad': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'identificador': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['auth.User']", 'unique': 'True'}),
            'ingles': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'nit': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '15'}),
            'profesion': ('django.db.models.fields.CharField', [], {'max_length': '75', 'blank': 'True'}),
            'tipo_institucion': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['calidad.TipoInstitucion']"})
        },
        u'calidad.experienciaevaluador': {
            'Meta': {'object_name': 'ExperienciaEvaluador'},
            'area': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['calidad.AreaExperiencia']"}),
            'evaluador_experiencia': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['calidad.Evaluador']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'tiempo_experiencia': ('django.db.models.fields.CharField', [], {'max_length': '75'})
        },
        u'calidad.grupoevaluador': {
            'Meta': {'object_name': 'GrupoEvaluador'},
            'codigo_evaluador': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['calidad.Evaluador']"}),
            'coordinador': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'postulacion_calidad': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['calidad.PostulacionesCalidad']"})
        },
        u'calidad.postulacionescalidad': {
            'Meta': {'object_name': 'PostulacionesCalidad'},
            'cargo_alterno': ('django.db.models.fields.CharField', [], {'max_length': '175', 'blank': 'True'}),
            'cargo_ejecutivo': ('django.db.models.fields.CharField', [], {'max_length': '175', 'blank': 'True'}),
            'clasificacion': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['calidad.TipoInstitucion']"}),
            'codigo': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '15'}),
            'contacto_alterno': ('django.db.models.fields.CharField', [], {'max_length': '125', 'blank': 'True'}),
            'contacto_cargo': ('django.db.models.fields.CharField', [], {'max_length': '175', 'blank': 'True'}),
            'contacto_nombre': ('django.db.models.fields.CharField', [], {'max_length': '125', 'blank': 'True'}),
            'direccion': ('django.db.models.fields.CharField', [], {'max_length': '450', 'blank': 'True'}),
            'ejecutivo': ('django.db.models.fields.CharField', [], {'max_length': '75', 'blank': 'True'}),
            'email_alterno': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'email_contacto': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'email_ejecutivo': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'fax': ('django.db.models.fields.CharField', [], {'max_length': '25', 'blank': 'True'}),
            'fax_alterno': ('django.db.models.fields.CharField', [], {'max_length': '25', 'blank': 'True'}),
            'fax_contacto': ('django.db.models.fields.CharField', [], {'max_length': '25', 'blank': 'True'}),
            'fax_ejecutivo': ('django.db.models.fields.CharField', [], {'max_length': '25', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'representante_cargo': ('django.db.models.fields.CharField', [], {'max_length': '125', 'blank': 'True'}),
            'representante_oficial': ('django.db.models.fields.CharField', [], {'max_length': '125', 'blank': 'True'}),
            'telefono': ('django.db.models.fields.CharField', [], {'max_length': '25', 'blank': 'True'}),
            'telefono_alterno': ('django.db.models.fields.CharField', [], {'max_length': '25', 'blank': 'True'}),
            'telefono_contacto': ('django.db.models.fields.CharField', [], {'max_length': '25', 'blank': 'True'}),
            'telefono_ejecutivo': ('django.db.models.fields.CharField', [], {'max_length': '25', 'blank': 'True'}),
            'web': ('django.db.models.fields.CharField', [], {'max_length': '150', 'blank': 'True'})
        },
        u'calidad.puntajeevaluacion': {
            'Meta': {'object_name': 'PuntajeEvaluacion'},
            'aprendizaje': ('django.db.models.fields.IntegerField', [], {'default': '0', 'blank': 'True'}),
            'criterio': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['calidad.CriteriosCalidad']"}),
            'despligue': ('django.db.models.fields.IntegerField', [], {'default': '0', 'blank': 'True'}),
            'enfoque': ('django.db.models.fields.IntegerField', [], {'default': '0', 'blank': 'True'}),
            'evaluacion': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['calidad.EvaluacionIndividualCalidad']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'integracion': ('django.db.models.fields.IntegerField', [], {'default': '0', 'blank': 'True'}),
            'promedio': ('django.db.models.fields.DecimalField', [], {'default': '0.0', 'max_digits': '7', 'decimal_places': '2', 'blank': 'True'}),
            'puntaje_maximo': ('django.db.models.fields.IntegerField', [], {'blank': 'True'}),
            'total': ('django.db.models.fields.DecimalField', [], {'default': '0.0', 'max_digits': '7', 'decimal_places': '2', 'blank': 'True'})
        },
        u'calidad.telefonosevaluador': {
            'Meta': {'object_name': 'TelefonosEvaluador'},
            'evaluador_tel': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['calidad.Evaluador']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'telefono': ('django.db.models.fields.CharField', [], {'max_length': '25'})
        },
        u'calidad.tipoinstitucion': {
            'Meta': {'object_name': 'TipoInstitucion'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre_tipo_institucion': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '150'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['calidad']