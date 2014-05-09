# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'TestVisitaMejoresPracticas'
        db.create_table(u'calidad_testvisitamejorespracticas', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('evaluacion', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['calidad.EvaluacionVisitaMejoresPracticas'])),
            ('cuaderno', self.gf('django.db.models.fields.files.FileField')(max_length=500)),
            ('fecha_subida', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('comentario', self.gf('django.db.models.fields.CharField')(max_length=350, blank=True)),
        ))
        db.send_create_signal(u'calidad', ['TestVisitaMejoresPracticas'])


    def backwards(self, orm):
        # Deleting model 'TestVisitaMejoresPracticas'
        db.delete_table(u'calidad_testvisitamejorespracticas')


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
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Permission']"}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'calidad.ambientecompetitivo': {
            'Meta': {'object_name': 'AmbienteCompetitivo'},
            'ambiente_competitivo': ('tinymce.models.HTMLField', [], {'blank': 'True'}),
            'evaluacion_consenso': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['calidad.EvaluacionConsensoMejoresPracticas']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'calidad.ambientecompetitivoconsenso': {
            'Meta': {'object_name': 'AmbienteCompetitivoConsenso'},
            'ambiente_competitivo': ('tinymce.models.HTMLField', [], {'blank': 'True'}),
            'evaluacion_consenso': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['calidad.EvaluacionConsensoCalidad']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'calidad.ambientecompetitivovisita': {
            'Meta': {'object_name': 'AmbienteCompetitivoVisita'},
            'ambiente_competitivo': ('tinymce.models.HTMLField', [], {'blank': 'True'}),
            'aprobado': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'comentario_revision': ('tinymce.models.HTMLField', [], {'blank': 'True'}),
            'evaluacion_consenso': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['calidad.EvaluacionVisitaCalidad']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'calidad.ambientecompetitivovisitamp': {
            'Meta': {'object_name': 'AmbienteCompetitivoVisitaMP'},
            'ambiente_competitivo': ('tinymce.models.HTMLField', [], {'blank': 'True'}),
            'aprobado': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'comentario_revision': ('tinymce.models.HTMLField', [], {'blank': 'True'}),
            'evaluacion_consenso': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['calidad.EvaluacionVisitaMejoresPracticas']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'calidad.ambienteorganizacionalconsenso': {
            'Meta': {'object_name': 'AmbienteOrganizacionalConsenso'},
            'ambiente_organizacional': ('tinymce.models.HTMLField', [], {'blank': 'True'}),
            'evaluacion_consenso': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['calidad.EvaluacionConsensoCalidad']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'calidad.ambienteorganizacionalvisita': {
            'Meta': {'object_name': 'AmbienteOrganizacionalVisita'},
            'ambiente_organizacional': ('tinymce.models.HTMLField', [], {'blank': 'True'}),
            'aprobado': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'comentario_revision': ('tinymce.models.HTMLField', [], {'blank': 'True'}),
            'evaluacion_consenso': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['calidad.EvaluacionVisitaCalidad']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'calidad.areaexperiencia': {
            'Meta': {'object_name': 'AreaExperiencia'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre_area': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '150'})
        },
        u'calidad.areamejoraconsenso': {
            'Meta': {'object_name': 'AreaMejoraConsenso'},
            'areas_mejora': ('tinymce.models.HTMLField', [], {'blank': 'True'}),
            'criterio': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['calidad.CriteriosCalidad']"}),
            'evaluacion_consenso': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['calidad.EvaluacionConsensoCalidad']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'calidad.areamejoraconsensomejorespracticas': {
            'Meta': {'object_name': 'AreaMejoraConsensoMejoresPracticas'},
            'areas_mejora': ('tinymce.models.HTMLField', [], {'blank': 'True'}),
            'criterio': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['calidad.CriteriosMejoresPracticas']"}),
            'evaluacion_consenso': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['calidad.EvaluacionConsensoMejoresPracticas']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'calidad.areamejoravisitamejorespracticas': {
            'Meta': {'object_name': 'AreaMejoraVisitaMejoresPracticas'},
            'aprobado': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'areas_mejora': ('tinymce.models.HTMLField', [], {'blank': 'True'}),
            'comentario_revision': ('tinymce.models.HTMLField', [], {'blank': 'True'}),
            'criterio': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['calidad.CriteriosMejoresPracticas']"}),
            'evaluacion_consenso': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['calidad.EvaluacionVisitaMejoresPracticas']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'calidad.areasmejorarvisitacalidad': {
            'Meta': {'object_name': 'AreasMejorarVisitaCalidad'},
            'aprobado': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'areas_mejorar': ('tinymce.models.HTMLField', [], {'blank': 'True'}),
            'comentario_revision': ('tinymce.models.HTMLField', [], {'blank': 'True'}),
            'criterio': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['calidad.CriteriosCalidad']"}),
            'evaluacion_visita': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['calidad.EvaluacionVisitaCalidad']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'calidad.criterioscalidad': {
            'Meta': {'object_name': 'CriteriosCalidad'},
            'agrupador': ('django.db.models.fields.BooleanField', [], {}),
            'cod_agrupador': ('django.db.models.fields.CharField', [], {'max_length': '2', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'literal': ('django.db.models.fields.CharField', [], {'max_length': '5', 'blank': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'}),
            'puntaje_maximo': ('django.db.models.fields.IntegerField', [], {'default': '0', 'blank': 'True'})
        },
        u'calidad.criteriosevaluacion': {
            'Meta': {'object_name': 'CriteriosEvaluacion'},
            'areas_mejorar': ('tinymce.models.HTMLField', [], {'blank': 'True'}),
            'criterio': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['calidad.CriteriosCalidad']"}),
            'evaluacion': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['calidad.EvaluacionIndividualCalidad']"}),
            'fortalezas': ('tinymce.models.HTMLField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'puntos_visita': ('tinymce.models.HTMLField', [], {'blank': 'True'})
        },
        u'calidad.criteriosevaluacionmejorespracticas': {
            'Meta': {'object_name': 'CriteriosEvaluacionMejoresPracticas'},
            'areas_mejorar': ('tinymce.models.HTMLField', [], {'blank': 'True'}),
            'criterio': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['calidad.CriteriosMejoresPracticas']"}),
            'evaluacion': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['calidad.EvaluacionIndividualMejoresPracticas']"}),
            'fortalezas': ('tinymce.models.HTMLField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'puntos_visita': ('tinymce.models.HTMLField', [], {'blank': 'True'})
        },
        u'calidad.criteriosmejorespracticas': {
            'Meta': {'object_name': 'CriteriosMejoresPracticas'},
            'agrupador': ('django.db.models.fields.BooleanField', [], {}),
            'cod_agrupador': ('django.db.models.fields.CharField', [], {'max_length': '2', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'literal': ('django.db.models.fields.CharField', [], {'max_length': '5', 'blank': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'}),
            'puntaje_maximo': ('django.db.models.fields.IntegerField', [], {'default': '0', 'blank': 'True'})
        },
        u'calidad.cuadernosdeevaluacion': {
            'Meta': {'object_name': 'CuadernosDeEvaluacion'},
            'comentario': ('django.db.models.fields.CharField', [], {'max_length': '350', 'blank': 'True'}),
            'cuaderno': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            'evaluacion': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['calidad.EvaluacionIndividualCalidad']"}),
            'fecha_subida': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'calidad.cuadernosdeevaluacionmejorespracticas': {
            'Meta': {'object_name': 'CuadernosDeEvaluacionMejoresPracticas'},
            'comentario': ('django.db.models.fields.CharField', [], {'max_length': '350', 'blank': 'True'}),
            'cuaderno': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            'evaluacion': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['calidad.EvaluacionIndividualMejoresPracticas']"}),
            'fecha_subida': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'calidad.desafiosestrategicosconsenso': {
            'Meta': {'object_name': 'DesafiosEstrategicosConsenso'},
            'desafios_estrategicos': ('tinymce.models.HTMLField', [], {'blank': 'True'}),
            'evaluacion_consenso': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['calidad.EvaluacionConsensoCalidad']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'calidad.desafiosestrategicosvisita': {
            'Meta': {'object_name': 'DesafiosEstrategicosVisita'},
            'aprobado': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'comentario_revision': ('tinymce.models.HTMLField', [], {'blank': 'True'}),
            'desafios_estrategicos': ('tinymce.models.HTMLField', [], {'blank': 'True'}),
            'evaluacion_consenso': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['calidad.EvaluacionVisitaCalidad']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'calidad.estadopostulacion': {
            'Meta': {'object_name': 'EstadoPostulacion'},
            'consenso': ('django.db.models.fields.BooleanField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'postulacion_calidad': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['calidad.PostulacionesCalidad']", 'unique': 'True'}),
            'visita': ('django.db.models.fields.BooleanField', [], {})
        },
        u'calidad.estadopostulacionmejorespracticas': {
            'Meta': {'object_name': 'EstadoPostulacionMejoresPracticas'},
            'consenso': ('django.db.models.fields.BooleanField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'postulacion_mejor_practica': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['calidad.PostulacionesMejoresPracticas']", 'unique': 'True'}),
            'visita': ('django.db.models.fields.BooleanField', [], {})
        },
        u'calidad.estudio': {
            'Meta': {'object_name': 'Estudio'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre_estudio': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '150'})
        },
        u'calidad.evaluacionconsensocalidad': {
            'Meta': {'object_name': 'EvaluacionConsensoCalidad'},
            'coordinador_postulacion': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['calidad.Evaluador']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'postulacion_evaluacion': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['calidad.PostulacionesCalidad']", 'unique': 'True'})
        },
        u'calidad.evaluacionconsensomejorespracticas': {
            'Meta': {'object_name': 'EvaluacionConsensoMejoresPracticas'},
            'coordinador_postulacion': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['calidad.Evaluador']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'postulacion_evaluacion': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['calidad.PostulacionesMejoresPracticas']", 'unique': 'True'})
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
        u'calidad.evaluacionindividualmejorespracticas': {
            'Meta': {'object_name': 'EvaluacionIndividualMejoresPracticas'},
            'ambiente_competitivo': ('tinymce.models.HTMLField', [], {'blank': 'True'}),
            'evaluador_postulacion': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['calidad.Evaluador']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'metodologia': ('tinymce.models.HTMLField', [], {'blank': 'True'}),
            'postulacion_evaluacion': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['calidad.PostulacionesMejoresPracticas']"}),
            'resultados': ('tinymce.models.HTMLField', [], {'blank': 'True'}),
            'soporte': ('tinymce.models.HTMLField', [], {'blank': 'True'}),
            'vinculo_proyecto': ('tinymce.models.HTMLField', [], {'blank': 'True'})
        },
        u'calidad.evaluacionvisitacalidad': {
            'Meta': {'object_name': 'EvaluacionVisitaCalidad'},
            'coordinador_postulacion': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['calidad.Evaluador']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'postulacion_evaluacion': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['calidad.PostulacionesCalidad']", 'unique': 'True'})
        },
        u'calidad.evaluacionvisitamejorespracticas': {
            'Meta': {'object_name': 'EvaluacionVisitaMejoresPracticas'},
            'coordinador_postulacion': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['calidad.Evaluador']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'postulacion_evaluacion': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['calidad.PostulacionesMejoresPracticas']", 'unique': 'True'})
        },
        u'calidad.evaluador': {
            'Meta': {'object_name': 'Evaluador'},
            'capacitacion_formacion': ('django.db.models.fields.BooleanField', [], {}),
            'cargo': ('django.db.models.fields.CharField', [], {'max_length': '150', 'blank': 'True'}),
            'codigo': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '15'}),
            'dui': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '15'}),
            'edad': ('django.db.models.fields.IntegerField', [], {'blank': 'True'}),
            'empresa_actual': ('django.db.models.fields.CharField', [], {'max_length': '150', 'blank': 'True'}),
            'estudios': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['calidad.Estudio']"}),
            'experiencia': ('django.db.models.fields.CharField', [], {'max_length': '85', 'blank': 'True'}),
            'experiencia_en_calidad': ('django.db.models.fields.BooleanField', [], {}),
            'experiencia_facilitador': ('django.db.models.fields.BooleanField', [], {}),
            'formacion_en_calidad': ('django.db.models.fields.BooleanField', [], {}),
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
        u'calidad.fortalezasconsenso': {
            'Meta': {'object_name': 'FortalezasConsenso'},
            'criterio': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['calidad.CriteriosCalidad']"}),
            'evaluacion_consenso': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['calidad.EvaluacionConsensoCalidad']"}),
            'fortalezas': ('tinymce.models.HTMLField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'calidad.fortalezasconsensomejorespracticas': {
            'Meta': {'object_name': 'FortalezasConsensoMejoresPracticas'},
            'criterio': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['calidad.CriteriosMejoresPracticas']"}),
            'evaluacion_consenso': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['calidad.EvaluacionConsensoMejoresPracticas']"}),
            'fortalezas': ('tinymce.models.HTMLField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'calidad.fortalezasvisitacalidad': {
            'Meta': {'object_name': 'FortalezasVisitaCalidad'},
            'aprobado': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'comentario_revision': ('tinymce.models.HTMLField', [], {'blank': 'True'}),
            'criterio': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['calidad.CriteriosCalidad']"}),
            'evaluacion_visita': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['calidad.EvaluacionVisitaCalidad']"}),
            'fortalezas': ('tinymce.models.HTMLField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'calidad.fortalezasvisitamejorespracticas': {
            'Meta': {'object_name': 'FortalezasVisitaMejoresPracticas'},
            'aprobado': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'comentario_revision': ('tinymce.models.HTMLField', [], {'blank': 'True'}),
            'criterio': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['calidad.CriteriosMejoresPracticas']"}),
            'evaluacion_consenso': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['calidad.EvaluacionVisitaMejoresPracticas']"}),
            'fortalezas': ('tinymce.models.HTMLField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'calidad.grupoevaluador': {
            'Meta': {'object_name': 'GrupoEvaluador'},
            'codigo_evaluador': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['calidad.Evaluador']"}),
            'coordinador': ('django.db.models.fields.BooleanField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'postulacion_calidad': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['calidad.PostulacionesCalidad']"})
        },
        u'calidad.grupoevaluadormejorespracticas': {
            'Meta': {'object_name': 'GrupoEvaluadorMejoresPracticas'},
            'codigo_evaluador': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['calidad.Evaluador']"}),
            'coordinador': ('django.db.models.fields.BooleanField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'postulacion_calidad': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['calidad.PostulacionesMejoresPracticas']"})
        },
        u'calidad.informeconsolidadocalidad': {
            'Meta': {'object_name': 'InformeConsolidadoCalidad'},
            'comentario': ('django.db.models.fields.CharField', [], {'max_length': '350', 'blank': 'True'}),
            'cuaderno': ('django.db.models.fields.files.FileField', [], {'max_length': '500'}),
            'evaluacion': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['calidad.EvaluacionConsensoCalidad']"}),
            'fecha_subida': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'calidad.informeconsolidadomejorespracticas': {
            'Meta': {'object_name': 'InformeConsolidadoMejoresPracticas'},
            'comentario': ('django.db.models.fields.CharField', [], {'max_length': '350', 'blank': 'True'}),
            'cuaderno': ('django.db.models.fields.files.FileField', [], {'max_length': '500'}),
            'evaluacion': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['calidad.EvaluacionConsensoMejoresPracticas']"}),
            'fecha_subida': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'calidad.informevisitamejorespracticas': {
            'Meta': {'object_name': 'InformeVisitaMejoresPracticas'},
            'comentario': ('django.db.models.fields.CharField', [], {'max_length': '350', 'blank': 'True'}),
            'cuaderno': ('django.db.models.fields.files.FileField', [], {'max_length': '500'}),
            'evaluacion': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['calidad.EvaluacionVisitaMejoresPracticas']"}),
            'fecha_subida': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'calidad.metodologia': {
            'Meta': {'object_name': 'Metodologia'},
            'evaluacion_consenso': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['calidad.EvaluacionConsensoMejoresPracticas']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'metologia_proyecto': ('tinymce.models.HTMLField', [], {'blank': 'True'})
        },
        u'calidad.metodologiavisita': {
            'Meta': {'object_name': 'MetodologiaVisita'},
            'aprobado': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'comentario_revision': ('tinymce.models.HTMLField', [], {'blank': 'True'}),
            'evaluacion_consenso': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['calidad.EvaluacionVisitaMejoresPracticas']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'metologia_proyecto': ('tinymce.models.HTMLField', [], {'blank': 'True'})
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
        u'calidad.postulacionesmejorespracticas': {
            'Meta': {'object_name': 'PostulacionesMejoresPracticas'},
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
            'fecha_fin': ('django.db.models.fields.DateField', [], {'blank': 'True'}),
            'fecha_inicio': ('django.db.models.fields.DateField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'nombre_equipo': ('django.db.models.fields.CharField', [], {'max_length': '300', 'blank': 'True'}),
            'nombre_proyecto': ('django.db.models.fields.CharField', [], {'max_length': '300', 'blank': 'True'}),
            'objetivo_proyecto': ('tinymce.models.HTMLField', [], {'blank': 'True'}),
            'representante_cargo': ('django.db.models.fields.CharField', [], {'max_length': '125', 'blank': 'True'}),
            'representante_oficial': ('django.db.models.fields.CharField', [], {'max_length': '125', 'blank': 'True'}),
            'telefono': ('django.db.models.fields.CharField', [], {'max_length': '25', 'blank': 'True'}),
            'telefono_alterno': ('django.db.models.fields.CharField', [], {'max_length': '25', 'blank': 'True'}),
            'telefono_contacto': ('django.db.models.fields.CharField', [], {'max_length': '25', 'blank': 'True'}),
            'telefono_ejecutivo': ('django.db.models.fields.CharField', [], {'max_length': '25', 'blank': 'True'}),
            'web': ('django.db.models.fields.CharField', [], {'max_length': '150', 'blank': 'True'})
        },
        u'calidad.puntajeconsensocalidad': {
            'Meta': {'object_name': 'PuntajeConsensoCalidad'},
            'comentario': ('tinymce.models.HTMLField', [], {'blank': 'True'}),
            'criterio': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['calidad.CriteriosCalidad']"}),
            'desviacion_estandar': ('django.db.models.fields.DecimalField', [], {'default': '0.0', 'max_digits': '7', 'decimal_places': '2', 'blank': 'True'}),
            'evaluacion_consenso': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['calidad.EvaluacionConsensoCalidad']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'maximo': ('django.db.models.fields.DecimalField', [], {'default': '0.0', 'max_digits': '7', 'decimal_places': '2', 'blank': 'True'}),
            'mediana': ('django.db.models.fields.DecimalField', [], {'default': '0.0', 'max_digits': '7', 'decimal_places': '2', 'blank': 'True'}),
            'minimo': ('django.db.models.fields.DecimalField', [], {'default': '0.0', 'max_digits': '7', 'decimal_places': '2', 'blank': 'True'}),
            'promedio': ('django.db.models.fields.DecimalField', [], {'default': '0.0', 'max_digits': '7', 'decimal_places': '2', 'blank': 'True'}),
            'puntacion_consenso': ('django.db.models.fields.IntegerField', [], {'default': '0', 'blank': 'True'}),
            'puntaje_maximo': ('django.db.models.fields.IntegerField', [], {'blank': 'True'}),
            'puntuacion': ('django.db.models.fields.DecimalField', [], {'default': '0.0', 'max_digits': '7', 'decimal_places': '2', 'blank': 'True'}),
            'rango': ('django.db.models.fields.DecimalField', [], {'default': '0.0', 'max_digits': '7', 'decimal_places': '2', 'blank': 'True'})
        },
        u'calidad.puntajeconsensomejorespracticas': {
            'Meta': {'object_name': 'PuntajeConsensoMejoresPracticas'},
            'comentario': ('tinymce.models.HTMLField', [], {'blank': 'True'}),
            'criterio': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['calidad.CriteriosMejoresPracticas']"}),
            'desviacion_estandar': ('django.db.models.fields.DecimalField', [], {'default': '0.0', 'max_digits': '7', 'decimal_places': '2', 'blank': 'True'}),
            'evaluacion_consenso': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['calidad.EvaluacionConsensoMejoresPracticas']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'maximo': ('django.db.models.fields.DecimalField', [], {'default': '0.0', 'max_digits': '7', 'decimal_places': '2', 'blank': 'True'}),
            'mediana': ('django.db.models.fields.DecimalField', [], {'default': '0.0', 'max_digits': '7', 'decimal_places': '2', 'blank': 'True'}),
            'minimo': ('django.db.models.fields.DecimalField', [], {'default': '0.0', 'max_digits': '7', 'decimal_places': '2', 'blank': 'True'}),
            'promedio': ('django.db.models.fields.DecimalField', [], {'default': '0.0', 'max_digits': '7', 'decimal_places': '2', 'blank': 'True'}),
            'puntacion_consenso': ('django.db.models.fields.IntegerField', [], {'default': '0', 'blank': 'True'}),
            'puntaje_maximo': ('django.db.models.fields.IntegerField', [], {'blank': 'True'}),
            'puntuacion': ('django.db.models.fields.DecimalField', [], {'default': '0.0', 'max_digits': '7', 'decimal_places': '2', 'blank': 'True'}),
            'rango': ('django.db.models.fields.DecimalField', [], {'default': '0.0', 'max_digits': '7', 'decimal_places': '2', 'blank': 'True'})
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
        u'calidad.puntajeevaluacionmejorespracticas': {
            'Meta': {'object_name': 'PuntajeEvaluacionMejoresPracticas'},
            'criterio': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['calidad.CriteriosMejoresPracticas']"}),
            'evaluacion': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['calidad.EvaluacionIndividualMejoresPracticas']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'porcentaje': ('django.db.models.fields.IntegerField', [], {'default': '0', 'blank': 'True'}),
            'puntaje_maximo': ('django.db.models.fields.IntegerField', [], {'blank': 'True'}),
            'total': ('django.db.models.fields.DecimalField', [], {'default': '0.0', 'max_digits': '7', 'decimal_places': '2', 'blank': 'True'})
        },
        u'calidad.puntajevisitacalidad': {
            'Meta': {'object_name': 'PuntajeVisitaCalidad'},
            'comentario': ('tinymce.models.HTMLField', [], {'blank': 'True'}),
            'criterio': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['calidad.CriteriosCalidad']"}),
            'evaluacion': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['calidad.EvaluacionVisitaCalidad']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'puntaje_consenso': ('django.db.models.fields.IntegerField', [], {'blank': 'True'}),
            'puntaje_maximo': ('django.db.models.fields.IntegerField', [], {'blank': 'True'}),
            'puntaje_visita': ('django.db.models.fields.DecimalField', [], {'default': '0.0', 'max_digits': '7', 'decimal_places': '2', 'blank': 'True'})
        },
        u'calidad.puntajevisitamejorespracticas': {
            'Meta': {'object_name': 'PuntajeVisitaMejoresPracticas'},
            'comentario': ('tinymce.models.HTMLField', [], {'blank': 'True'}),
            'criterio': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['calidad.CriteriosMejoresPracticas']"}),
            'evaluacion_consenso': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['calidad.EvaluacionVisitaMejoresPracticas']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'puntacion_consenso': ('django.db.models.fields.IntegerField', [], {'default': '0', 'blank': 'True'}),
            'puntacion_visita': ('django.db.models.fields.IntegerField', [], {'default': '0', 'blank': 'True'}),
            'puntaje_maximo': ('django.db.models.fields.IntegerField', [], {'blank': 'True'})
        },
        u'calidad.puntosvisitaconsenso': {
            'Meta': {'object_name': 'PuntosVisitaConsenso'},
            'criterio': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['calidad.CriteriosCalidad']"}),
            'evaluacion_consenso': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['calidad.EvaluacionConsensoCalidad']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'puntos_visita': ('tinymce.models.HTMLField', [], {'blank': 'True'})
        },
        u'calidad.puntosvisitaconsensomejorespracticas': {
            'Meta': {'object_name': 'PuntosVisitaConsensoMejoresPracticas'},
            'criterio': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['calidad.CriteriosMejoresPracticas']"}),
            'evaluacion_consenso': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['calidad.EvaluacionConsensoMejoresPracticas']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'puntos_visita': ('tinymce.models.HTMLField', [], {'blank': 'True'})
        },
        u'calidad.relacionesorganizacionalesconsenso': {
            'Meta': {'object_name': 'RelacionesOrganizacionalesConsenso'},
            'evaluacion_consenso': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['calidad.EvaluacionConsensoCalidad']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'relaciones_organizacionales': ('tinymce.models.HTMLField', [], {'blank': 'True'})
        },
        u'calidad.relacionesorganizacionalesvisita': {
            'Meta': {'object_name': 'RelacionesOrganizacionalesVisita'},
            'aprobado': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'comentario_revision': ('tinymce.models.HTMLField', [], {'blank': 'True'}),
            'evaluacion_consenso': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['calidad.EvaluacionVisitaCalidad']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'relaciones_organizacionales': ('tinymce.models.HTMLField', [], {'blank': 'True'})
        },
        u'calidad.resultados': {
            'Meta': {'object_name': 'Resultados'},
            'evaluacion_consenso': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['calidad.EvaluacionConsensoMejoresPracticas']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'resultados_obtenidos': ('tinymce.models.HTMLField', [], {'blank': 'True'})
        },
        u'calidad.resultadosvisita': {
            'Meta': {'object_name': 'ResultadosVisita'},
            'aprobado': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'comentario_revision': ('tinymce.models.HTMLField', [], {'blank': 'True'}),
            'evaluacion_consenso': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['calidad.EvaluacionVisitaMejoresPracticas']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'resultados_obtenidos': ('tinymce.models.HTMLField', [], {'blank': 'True'})
        },
        u'calidad.sistemamejoraconsenso': {
            'Meta': {'object_name': 'SistemaMejoraConsenso'},
            'evaluacion_consenso': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['calidad.EvaluacionConsensoCalidad']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'sistema_mejora': ('tinymce.models.HTMLField', [], {'blank': 'True'})
        },
        u'calidad.sistemamejoravisita': {
            'Meta': {'object_name': 'SistemaMejoraVisita'},
            'aprobado': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'comentario_revision': ('tinymce.models.HTMLField', [], {'blank': 'True'}),
            'evaluacion_consenso': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['calidad.EvaluacionVisitaCalidad']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'sistema_mejora': ('tinymce.models.HTMLField', [], {'blank': 'True'})
        },
        u'calidad.soporte': {
            'Meta': {'object_name': 'Soporte'},
            'evaluacion_consenso': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['calidad.EvaluacionConsensoMejoresPracticas']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'soporte_direccion': ('tinymce.models.HTMLField', [], {'blank': 'True'})
        },
        u'calidad.soportevisita': {
            'Meta': {'object_name': 'SoporteVisita'},
            'aprobado': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'comentario_revision': ('tinymce.models.HTMLField', [], {'blank': 'True'}),
            'evaluacion_consenso': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['calidad.EvaluacionVisitaMejoresPracticas']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'soporte_direccion': ('tinymce.models.HTMLField', [], {'blank': 'True'})
        },
        u'calidad.telefonosevaluador': {
            'Meta': {'object_name': 'TelefonosEvaluador'},
            'evaluador_tel': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['calidad.Evaluador']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'telefono': ('django.db.models.fields.CharField', [], {'max_length': '25'})
        },
        u'calidad.testvisitamejorespracticas': {
            'Meta': {'object_name': 'TestVisitaMejoresPracticas'},
            'comentario': ('django.db.models.fields.CharField', [], {'max_length': '350', 'blank': 'True'}),
            'cuaderno': ('django.db.models.fields.files.FileField', [], {'max_length': '500'}),
            'evaluacion': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['calidad.EvaluacionVisitaMejoresPracticas']"}),
            'fecha_subida': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'calidad.tipoinstitucion': {
            'Meta': {'object_name': 'TipoInstitucion'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre_tipo_institucion': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '150'})
        },
        u'calidad.vinculoproyecto': {
            'Meta': {'object_name': 'VinculoProyecto'},
            'evaluacion_consenso': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['calidad.EvaluacionConsensoMejoresPracticas']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'vinculo_proyecto': ('tinymce.models.HTMLField', [], {'blank': 'True'})
        },
        u'calidad.vinculoproyectovisita': {
            'Meta': {'object_name': 'VinculoProyectoVisita'},
            'aprobado': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'comentario_revision': ('tinymce.models.HTMLField', [], {'blank': 'True'}),
            'evaluacion_consenso': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['calidad.EvaluacionVisitaMejoresPracticas']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'vinculo_proyecto': ('tinymce.models.HTMLField', [], {'blank': 'True'})
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