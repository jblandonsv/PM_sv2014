# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'TipoInstitucion'
        db.create_table(u'calidad_tipoinstitucion', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre_tipo_institucion', self.gf('django.db.models.fields.CharField')(unique=True, max_length=150)),
        ))
        db.send_create_signal(u'calidad', ['TipoInstitucion'])

        # Adding model 'Estudio'
        db.create_table(u'calidad_estudio', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre_estudio', self.gf('django.db.models.fields.CharField')(unique=True, max_length=150)),
        ))
        db.send_create_signal(u'calidad', ['Estudio'])

        # Adding model 'AreaExperiencia'
        db.create_table(u'calidad_areaexperiencia', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre_area', self.gf('django.db.models.fields.CharField')(unique=True, max_length=150)),
        ))
        db.send_create_signal(u'calidad', ['AreaExperiencia'])

        # Adding model 'Evaluador'
        db.create_table(u'calidad_evaluador', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('identificador', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['auth.User'], unique=True)),
            ('codigo', self.gf('django.db.models.fields.CharField')(unique=True, max_length=15)),
            ('dui', self.gf('django.db.models.fields.CharField')(unique=True, max_length=15)),
            ('nit', self.gf('django.db.models.fields.CharField')(unique=True, max_length=15)),
            ('tipo_institucion', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['calidad.TipoInstitucion'])),
            ('edad', self.gf('django.db.models.fields.IntegerField')(blank=True)),
            ('experiencia', self.gf('django.db.models.fields.CharField')(max_length=85, blank=True)),
            ('capacitacion_formacion', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('formacion_en_calidad', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('experiencia_en_calidad', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('estudios', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['calidad.Estudio'])),
            ('profesion', self.gf('django.db.models.fields.CharField')(max_length=75, blank=True)),
            ('empresa_actual', self.gf('django.db.models.fields.CharField')(max_length=150, blank=True)),
            ('cargo', self.gf('django.db.models.fields.CharField')(max_length=150, blank=True)),
            ('experiencia_facilitador', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('ingles', self.gf('django.db.models.fields.CharField')(max_length=50, blank=True)),
        ))
        db.send_create_signal(u'calidad', ['Evaluador'])

        # Adding model 'TelefonosEvaluador'
        db.create_table(u'calidad_telefonosevaluador', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('evaluador_tel', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['calidad.Evaluador'])),
            ('telefono', self.gf('django.db.models.fields.CharField')(max_length=25)),
        ))
        db.send_create_signal(u'calidad', ['TelefonosEvaluador'])

        # Adding model 'ExperienciaEvaluador'
        db.create_table(u'calidad_experienciaevaluador', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('evaluador_experiencia', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['calidad.Evaluador'])),
            ('area', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['calidad.AreaExperiencia'])),
            ('tiempo_experiencia', self.gf('django.db.models.fields.CharField')(max_length=75)),
        ))
        db.send_create_signal(u'calidad', ['ExperienciaEvaluador'])

        # Adding model 'PostulacionesCalidad'
        db.create_table(u'calidad_postulacionescalidad', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('codigo', self.gf('django.db.models.fields.CharField')(unique=True, max_length=15)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=150)),
        ))
        db.send_create_signal(u'calidad', ['PostulacionesCalidad'])

        # Adding model 'GrupoEvaluador'
        db.create_table(u'calidad_grupoevaluador', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('postulacion_calidad', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['calidad.PostulacionesCalidad'])),
            ('codigo_evaluador', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['calidad.Evaluador'])),
            ('coordinador', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(u'calidad', ['GrupoEvaluador'])

        # Adding model 'EvaluacionIndividualCalidad'
        db.create_table(u'calidad_evaluacionindividualcalidad', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('postulacion_evaluacion', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['calidad.PostulacionesCalidad'])),
            ('evaluador_postulacion', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['calidad.Evaluador'])),
            ('nota', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('nota_global', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('ambiente_organizacional', self.gf('tinymce.models.HTMLField')(blank=True)),
            ('relaciones_organizacionales', self.gf('tinymce.models.HTMLField')(blank=True)),
            ('ambiente_competitivo', self.gf('tinymce.models.HTMLField')(blank=True)),
            ('desafios_estrategicos', self.gf('tinymce.models.HTMLField')(blank=True)),
            ('sistema_mejora', self.gf('tinymce.models.HTMLField')(blank=True)),
        ))
        db.send_create_signal(u'calidad', ['EvaluacionIndividualCalidad'])

        # Adding model 'CriteriosCalidad'
        db.create_table(u'calidad_criterioscalidad', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(unique=True, max_length=100)),
            ('literal', self.gf('django.db.models.fields.CharField')(max_length=5, blank=True)),
            ('agrupador', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('cod_agrupador', self.gf('django.db.models.fields.CharField')(max_length=2, blank=True)),
            ('puntaje_maximo', self.gf('django.db.models.fields.IntegerField')(default=0, blank=True)),
        ))
        db.send_create_signal(u'calidad', ['CriteriosCalidad'])

        # Adding model 'CriteriosEvaluacion'
        db.create_table(u'calidad_criteriosevaluacion', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('evaluacion', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['calidad.EvaluacionIndividualCalidad'])),
            ('criterio', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['calidad.CriteriosCalidad'])),
            ('fortalezas', self.gf('tinymce.models.HTMLField')(blank=True)),
            ('areas_mejorar', self.gf('tinymce.models.HTMLField')(blank=True)),
            ('puntos_visita', self.gf('tinymce.models.HTMLField')(blank=True)),
            ('enfoque', self.gf('django.db.models.fields.IntegerField')(default=0, blank=True)),
            ('despligue', self.gf('django.db.models.fields.IntegerField')(default=0, blank=True)),
            ('aprendizaje', self.gf('django.db.models.fields.IntegerField')(default=0, blank=True)),
            ('integracion', self.gf('django.db.models.fields.IntegerField')(default=0, blank=True)),
            ('promedio', self.gf('django.db.models.fields.DecimalField')(default=0, max_digits=3, decimal_places=2, blank=True)),
            ('total', self.gf('django.db.models.fields.DecimalField')(default=0, max_digits=3, decimal_places=2, blank=True)),
        ))
        db.send_create_signal(u'calidad', ['CriteriosEvaluacion'])

        # Adding model 'PuntajeEvaluacion'
        db.create_table(u'calidad_puntajeevaluacion', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('evaluacion', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['calidad.EvaluacionIndividualCalidad'])),
            ('criterio', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['calidad.CriteriosCalidad'])),
            ('puntaje_maximo', self.gf('django.db.models.fields.IntegerField')(blank=True)),
            ('enfoque', self.gf('django.db.models.fields.IntegerField')(default=0, blank=True)),
            ('despligue', self.gf('django.db.models.fields.IntegerField')(default=0, blank=True)),
            ('aprendizaje', self.gf('django.db.models.fields.IntegerField')(default=0, blank=True)),
            ('integracion', self.gf('django.db.models.fields.IntegerField')(default=0, blank=True)),
            ('promedio', self.gf('django.db.models.fields.DecimalField')(default=0.0, max_digits=7, decimal_places=2, blank=True)),
            ('total', self.gf('django.db.models.fields.DecimalField')(default=0.0, max_digits=7, decimal_places=2, blank=True)),
        ))
        db.send_create_signal(u'calidad', ['PuntajeEvaluacion'])


    def backwards(self, orm):
        # Deleting model 'TipoInstitucion'
        db.delete_table(u'calidad_tipoinstitucion')

        # Deleting model 'Estudio'
        db.delete_table(u'calidad_estudio')

        # Deleting model 'AreaExperiencia'
        db.delete_table(u'calidad_areaexperiencia')

        # Deleting model 'Evaluador'
        db.delete_table(u'calidad_evaluador')

        # Deleting model 'TelefonosEvaluador'
        db.delete_table(u'calidad_telefonosevaluador')

        # Deleting model 'ExperienciaEvaluador'
        db.delete_table(u'calidad_experienciaevaluador')

        # Deleting model 'PostulacionesCalidad'
        db.delete_table(u'calidad_postulacionescalidad')

        # Deleting model 'GrupoEvaluador'
        db.delete_table(u'calidad_grupoevaluador')

        # Deleting model 'EvaluacionIndividualCalidad'
        db.delete_table(u'calidad_evaluacionindividualcalidad')

        # Deleting model 'CriteriosCalidad'
        db.delete_table(u'calidad_criterioscalidad')

        # Deleting model 'CriteriosEvaluacion'
        db.delete_table(u'calidad_criteriosevaluacion')

        # Deleting model 'PuntajeEvaluacion'
        db.delete_table(u'calidad_puntajeevaluacion')


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
            'codigo': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '15'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '150'})
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