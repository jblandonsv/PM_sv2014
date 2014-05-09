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
            ('direccion', self.gf('django.db.models.fields.CharField')(max_length=450, blank=True)),
            ('web', self.gf('django.db.models.fields.CharField')(max_length=150, blank=True)),
            ('telefono', self.gf('django.db.models.fields.CharField')(max_length=25, blank=True)),
            ('fax', self.gf('django.db.models.fields.CharField')(max_length=25, blank=True)),
            ('ejecutivo', self.gf('django.db.models.fields.CharField')(max_length=75, blank=True)),
            ('cargo_ejecutivo', self.gf('django.db.models.fields.CharField')(max_length=175, blank=True)),
            ('telefono_ejecutivo', self.gf('django.db.models.fields.CharField')(max_length=25, blank=True)),
            ('fax_ejecutivo', self.gf('django.db.models.fields.CharField')(max_length=25, blank=True)),
            ('email_ejecutivo', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('contacto_nombre', self.gf('django.db.models.fields.CharField')(max_length=125, blank=True)),
            ('contacto_cargo', self.gf('django.db.models.fields.CharField')(max_length=175, blank=True)),
            ('telefono_contacto', self.gf('django.db.models.fields.CharField')(max_length=25, blank=True)),
            ('fax_contacto', self.gf('django.db.models.fields.CharField')(max_length=25, blank=True)),
            ('email_contacto', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('contacto_alterno', self.gf('django.db.models.fields.CharField')(max_length=125, blank=True)),
            ('cargo_alterno', self.gf('django.db.models.fields.CharField')(max_length=175, blank=True)),
            ('telefono_alterno', self.gf('django.db.models.fields.CharField')(max_length=25, blank=True)),
            ('fax_alterno', self.gf('django.db.models.fields.CharField')(max_length=25, blank=True)),
            ('email_alterno', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('clasificacion', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['calidad.TipoInstitucion'])),
            ('representante_oficial', self.gf('django.db.models.fields.CharField')(max_length=125, blank=True)),
            ('representante_cargo', self.gf('django.db.models.fields.CharField')(max_length=125, blank=True)),
        ))
        db.send_create_signal(u'calidad', ['PostulacionesCalidad'])

        # Adding model 'EstadoPostulacion'
        db.create_table(u'calidad_estadopostulacion', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('postulacion_calidad', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['calidad.PostulacionesCalidad'], unique=True)),
            ('consenso', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('visita', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(u'calidad', ['EstadoPostulacion'])

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

        # Adding model 'EvaluacionConsensoCalidad'
        db.create_table(u'calidad_evaluacionconsensocalidad', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('postulacion_evaluacion', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['calidad.PostulacionesCalidad'], unique=True)),
            ('coordinador_postulacion', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['calidad.Evaluador'])),
        ))
        db.send_create_signal(u'calidad', ['EvaluacionConsensoCalidad'])

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

        # Adding model 'FortalezasConsenso'
        db.create_table(u'calidad_fortalezasconsenso', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('evaluacion_consenso', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['calidad.EvaluacionConsensoCalidad'])),
            ('criterio', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['calidad.CriteriosCalidad'])),
            ('fortalezas', self.gf('tinymce.models.HTMLField')(blank=True)),
        ))
        db.send_create_signal(u'calidad', ['FortalezasConsenso'])

        # Adding model 'AreaMejoraConsenso'
        db.create_table(u'calidad_areamejoraconsenso', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('evaluacion_consenso', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['calidad.EvaluacionConsensoCalidad'])),
            ('criterio', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['calidad.CriteriosCalidad'])),
            ('areas_mejora', self.gf('tinymce.models.HTMLField')(blank=True)),
        ))
        db.send_create_signal(u'calidad', ['AreaMejoraConsenso'])

        # Adding model 'PuntosVisitaConsenso'
        db.create_table(u'calidad_puntosvisitaconsenso', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('evaluacion_consenso', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['calidad.EvaluacionConsensoCalidad'])),
            ('criterio', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['calidad.CriteriosCalidad'])),
            ('puntos_visita', self.gf('tinymce.models.HTMLField')(blank=True)),
        ))
        db.send_create_signal(u'calidad', ['PuntosVisitaConsenso'])

        # Adding model 'AmbienteOrganizacionalConsenso'
        db.create_table(u'calidad_ambienteorganizacionalconsenso', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('evaluacion_consenso', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['calidad.EvaluacionConsensoCalidad'])),
            ('ambiente_organizacional', self.gf('tinymce.models.HTMLField')(blank=True)),
        ))
        db.send_create_signal(u'calidad', ['AmbienteOrganizacionalConsenso'])

        # Adding model 'RelacionesOrganizacionalesConsenso'
        db.create_table(u'calidad_relacionesorganizacionalesconsenso', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('evaluacion_consenso', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['calidad.EvaluacionConsensoCalidad'])),
            ('relaciones_organizacionales', self.gf('tinymce.models.HTMLField')(blank=True)),
        ))
        db.send_create_signal(u'calidad', ['RelacionesOrganizacionalesConsenso'])

        # Adding model 'AmbienteCompetitivoConsenso'
        db.create_table(u'calidad_ambientecompetitivoconsenso', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('evaluacion_consenso', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['calidad.EvaluacionConsensoCalidad'])),
            ('ambiente_competitivo', self.gf('tinymce.models.HTMLField')(blank=True)),
        ))
        db.send_create_signal(u'calidad', ['AmbienteCompetitivoConsenso'])

        # Adding model 'DesafiosEstrategicosConsenso'
        db.create_table(u'calidad_desafiosestrategicosconsenso', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('evaluacion_consenso', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['calidad.EvaluacionConsensoCalidad'])),
            ('desafios_estrategicos', self.gf('tinymce.models.HTMLField')(blank=True)),
        ))
        db.send_create_signal(u'calidad', ['DesafiosEstrategicosConsenso'])

        # Adding model 'SistemaMejoraConsenso'
        db.create_table(u'calidad_sistemamejoraconsenso', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('evaluacion_consenso', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['calidad.EvaluacionConsensoCalidad'])),
            ('sistema_mejora', self.gf('tinymce.models.HTMLField')(blank=True)),
        ))
        db.send_create_signal(u'calidad', ['SistemaMejoraConsenso'])

        # Adding model 'PuntajeConsensoCalidad'
        db.create_table(u'calidad_puntajeconsensocalidad', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('evaluacion_consenso', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['calidad.EvaluacionConsensoCalidad'])),
            ('criterio', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['calidad.CriteriosCalidad'])),
            ('puntaje_maximo', self.gf('django.db.models.fields.IntegerField')(blank=True)),
            ('promedio', self.gf('django.db.models.fields.DecimalField')(default=0.0, max_digits=7, decimal_places=2, blank=True)),
            ('desviacion_estandar', self.gf('django.db.models.fields.DecimalField')(default=0.0, max_digits=7, decimal_places=2, blank=True)),
            ('mediana', self.gf('django.db.models.fields.DecimalField')(default=0.0, max_digits=7, decimal_places=2, blank=True)),
            ('maximo', self.gf('django.db.models.fields.DecimalField')(default=0.0, max_digits=7, decimal_places=2, blank=True)),
            ('minimo', self.gf('django.db.models.fields.DecimalField')(default=0.0, max_digits=7, decimal_places=2, blank=True)),
            ('rango', self.gf('django.db.models.fields.DecimalField')(default=0.0, max_digits=7, decimal_places=2, blank=True)),
            ('puntuacion', self.gf('django.db.models.fields.DecimalField')(default=0.0, max_digits=7, decimal_places=2, blank=True)),
            ('puntacion_consenso', self.gf('django.db.models.fields.IntegerField')(default=0, blank=True)),
            ('comentario', self.gf('tinymce.models.HTMLField')(blank=True)),
        ))
        db.send_create_signal(u'calidad', ['PuntajeConsensoCalidad'])

        # Adding model 'CriteriosEvaluacion'
        db.create_table(u'calidad_criteriosevaluacion', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('evaluacion', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['calidad.EvaluacionIndividualCalidad'])),
            ('criterio', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['calidad.CriteriosCalidad'])),
            ('fortalezas', self.gf('tinymce.models.HTMLField')(blank=True)),
            ('areas_mejorar', self.gf('tinymce.models.HTMLField')(blank=True)),
            ('puntos_visita', self.gf('tinymce.models.HTMLField')(blank=True)),
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

        # Adding model 'CuadernosDeEvaluacion'
        db.create_table(u'calidad_cuadernosdeevaluacion', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('evaluacion', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['calidad.EvaluacionIndividualCalidad'])),
            ('cuaderno', self.gf('django.db.models.fields.files.FileField')(max_length=100)),
            ('fecha_subida', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('comentario', self.gf('django.db.models.fields.CharField')(max_length=350, blank=True)),
        ))
        db.send_create_signal(u'calidad', ['CuadernosDeEvaluacion'])

        # Adding model 'InformeConsolidadoCalidad'
        db.create_table(u'calidad_informeconsolidadocalidad', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('evaluacion', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['calidad.EvaluacionConsensoCalidad'])),
            ('cuaderno', self.gf('django.db.models.fields.files.FileField')(max_length=500)),
            ('fecha_subida', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('comentario', self.gf('django.db.models.fields.CharField')(max_length=350, blank=True)),
        ))
        db.send_create_signal(u'calidad', ['InformeConsolidadoCalidad'])

        # Adding model 'CriteriosMejoresPracticas'
        db.create_table(u'calidad_criteriosmejorespracticas', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(unique=True, max_length=100)),
            ('literal', self.gf('django.db.models.fields.CharField')(max_length=5, blank=True)),
            ('agrupador', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('cod_agrupador', self.gf('django.db.models.fields.CharField')(max_length=2, blank=True)),
            ('puntaje_maximo', self.gf('django.db.models.fields.IntegerField')(default=0, blank=True)),
        ))
        db.send_create_signal(u'calidad', ['CriteriosMejoresPracticas'])

        # Adding model 'PostulacionesMejoresPracticas'
        db.create_table(u'calidad_postulacionesmejorespracticas', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('codigo', self.gf('django.db.models.fields.CharField')(unique=True, max_length=15)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=150)),
            ('direccion', self.gf('django.db.models.fields.CharField')(max_length=450, blank=True)),
            ('web', self.gf('django.db.models.fields.CharField')(max_length=150, blank=True)),
            ('telefono', self.gf('django.db.models.fields.CharField')(max_length=25, blank=True)),
            ('fax', self.gf('django.db.models.fields.CharField')(max_length=25, blank=True)),
            ('ejecutivo', self.gf('django.db.models.fields.CharField')(max_length=75, blank=True)),
            ('cargo_ejecutivo', self.gf('django.db.models.fields.CharField')(max_length=175, blank=True)),
            ('telefono_ejecutivo', self.gf('django.db.models.fields.CharField')(max_length=25, blank=True)),
            ('fax_ejecutivo', self.gf('django.db.models.fields.CharField')(max_length=25, blank=True)),
            ('email_ejecutivo', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('contacto_nombre', self.gf('django.db.models.fields.CharField')(max_length=125, blank=True)),
            ('contacto_cargo', self.gf('django.db.models.fields.CharField')(max_length=175, blank=True)),
            ('telefono_contacto', self.gf('django.db.models.fields.CharField')(max_length=25, blank=True)),
            ('fax_contacto', self.gf('django.db.models.fields.CharField')(max_length=25, blank=True)),
            ('email_contacto', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('contacto_alterno', self.gf('django.db.models.fields.CharField')(max_length=125, blank=True)),
            ('cargo_alterno', self.gf('django.db.models.fields.CharField')(max_length=175, blank=True)),
            ('telefono_alterno', self.gf('django.db.models.fields.CharField')(max_length=25, blank=True)),
            ('fax_alterno', self.gf('django.db.models.fields.CharField')(max_length=25, blank=True)),
            ('email_alterno', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('clasificacion', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['calidad.TipoInstitucion'])),
            ('representante_oficial', self.gf('django.db.models.fields.CharField')(max_length=125, blank=True)),
            ('representante_cargo', self.gf('django.db.models.fields.CharField')(max_length=125, blank=True)),
            ('nombre_equipo', self.gf('django.db.models.fields.CharField')(max_length=300, blank=True)),
            ('nombre_proyecto', self.gf('django.db.models.fields.CharField')(max_length=300, blank=True)),
            ('objetivo_proyecto', self.gf('tinymce.models.HTMLField')(blank=True)),
            ('fecha_inicio', self.gf('django.db.models.fields.DateField')(blank=True)),
            ('fecha_fin', self.gf('django.db.models.fields.DateField')(blank=True)),
        ))
        db.send_create_signal(u'calidad', ['PostulacionesMejoresPracticas'])

        # Adding model 'EvaluacionIndividualMejoresPracticas'
        db.create_table(u'calidad_evaluacionindividualmejorespracticas', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('postulacion_evaluacion', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['calidad.PostulacionesMejoresPracticas'])),
            ('evaluador_postulacion', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['calidad.Evaluador'])),
            ('vinculo_proyecto', self.gf('tinymce.models.HTMLField')(blank=True)),
            ('metodologia', self.gf('tinymce.models.HTMLField')(blank=True)),
            ('ambiente_competitivo', self.gf('tinymce.models.HTMLField')(blank=True)),
            ('soporte', self.gf('tinymce.models.HTMLField')(blank=True)),
            ('resultados', self.gf('tinymce.models.HTMLField')(blank=True)),
        ))
        db.send_create_signal(u'calidad', ['EvaluacionIndividualMejoresPracticas'])

        # Adding model 'CriteriosEvaluacionMejoresPracticas'
        db.create_table(u'calidad_criteriosevaluacionmejorespracticas', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('evaluacion', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['calidad.EvaluacionIndividualMejoresPracticas'])),
            ('criterio', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['calidad.CriteriosMejoresPracticas'])),
            ('fortalezas', self.gf('tinymce.models.HTMLField')(blank=True)),
            ('areas_mejorar', self.gf('tinymce.models.HTMLField')(blank=True)),
            ('puntos_visita', self.gf('tinymce.models.HTMLField')(blank=True)),
        ))
        db.send_create_signal(u'calidad', ['CriteriosEvaluacionMejoresPracticas'])

        # Adding model 'PuntajeEvaluacionMejoresPracticas'
        db.create_table(u'calidad_puntajeevaluacionmejorespracticas', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('evaluacion', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['calidad.EvaluacionIndividualMejoresPracticas'])),
            ('criterio', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['calidad.CriteriosMejoresPracticas'])),
            ('puntaje_maximo', self.gf('django.db.models.fields.IntegerField')(blank=True)),
            ('porcentaje', self.gf('django.db.models.fields.IntegerField')(default=0, blank=True)),
            ('total', self.gf('django.db.models.fields.DecimalField')(default=0.0, max_digits=7, decimal_places=2, blank=True)),
        ))
        db.send_create_signal(u'calidad', ['PuntajeEvaluacionMejoresPracticas'])

        # Adding model 'GrupoEvaluadorMejoresPracticas'
        db.create_table(u'calidad_grupoevaluadormejorespracticas', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('postulacion_calidad', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['calidad.PostulacionesMejoresPracticas'])),
            ('codigo_evaluador', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['calidad.Evaluador'])),
            ('coordinador', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(u'calidad', ['GrupoEvaluadorMejoresPracticas'])

        # Adding model 'EstadoPostulacionMejoresPracticas'
        db.create_table(u'calidad_estadopostulacionmejorespracticas', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('postulacion_mejor_practica', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['calidad.PostulacionesMejoresPracticas'], unique=True)),
            ('consenso', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('visita', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(u'calidad', ['EstadoPostulacionMejoresPracticas'])

        # Adding model 'EvaluacionConsensoMejoresPracticas'
        db.create_table(u'calidad_evaluacionconsensomejorespracticas', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('postulacion_evaluacion', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['calidad.PostulacionesMejoresPracticas'], unique=True)),
            ('coordinador_postulacion', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['calidad.Evaluador'])),
        ))
        db.send_create_signal(u'calidad', ['EvaluacionConsensoMejoresPracticas'])

        # Adding model 'PuntajeConsensoMejoresPracticas'
        db.create_table(u'calidad_puntajeconsensomejorespracticas', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('evaluacion_consenso', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['calidad.EvaluacionConsensoMejoresPracticas'])),
            ('criterio', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['calidad.CriteriosMejoresPracticas'])),
            ('puntaje_maximo', self.gf('django.db.models.fields.IntegerField')(blank=True)),
            ('promedio', self.gf('django.db.models.fields.DecimalField')(default=0.0, max_digits=7, decimal_places=2, blank=True)),
            ('desviacion_estandar', self.gf('django.db.models.fields.DecimalField')(default=0.0, max_digits=7, decimal_places=2, blank=True)),
            ('mediana', self.gf('django.db.models.fields.DecimalField')(default=0.0, max_digits=7, decimal_places=2, blank=True)),
            ('maximo', self.gf('django.db.models.fields.DecimalField')(default=0.0, max_digits=7, decimal_places=2, blank=True)),
            ('minimo', self.gf('django.db.models.fields.DecimalField')(default=0.0, max_digits=7, decimal_places=2, blank=True)),
            ('rango', self.gf('django.db.models.fields.DecimalField')(default=0.0, max_digits=7, decimal_places=2, blank=True)),
            ('puntuacion', self.gf('django.db.models.fields.DecimalField')(default=0.0, max_digits=7, decimal_places=2, blank=True)),
            ('puntacion_consenso', self.gf('django.db.models.fields.IntegerField')(default=0, blank=True)),
            ('comentario', self.gf('tinymce.models.HTMLField')(blank=True)),
        ))
        db.send_create_signal(u'calidad', ['PuntajeConsensoMejoresPracticas'])

        # Adding model 'VinculoProyecto'
        db.create_table(u'calidad_vinculoproyecto', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('evaluacion_consenso', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['calidad.EvaluacionConsensoMejoresPracticas'])),
            ('vinculo_proyecto', self.gf('tinymce.models.HTMLField')(blank=True)),
        ))
        db.send_create_signal(u'calidad', ['VinculoProyecto'])

        # Adding model 'Metodologia'
        db.create_table(u'calidad_metodologia', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('evaluacion_consenso', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['calidad.EvaluacionConsensoMejoresPracticas'])),
            ('metologia_proyecto', self.gf('tinymce.models.HTMLField')(blank=True)),
        ))
        db.send_create_signal(u'calidad', ['Metodologia'])

        # Adding model 'AmbienteCompetitivo'
        db.create_table(u'calidad_ambientecompetitivo', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('evaluacion_consenso', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['calidad.EvaluacionConsensoMejoresPracticas'])),
            ('ambiente_competitivo', self.gf('tinymce.models.HTMLField')(blank=True)),
        ))
        db.send_create_signal(u'calidad', ['AmbienteCompetitivo'])

        # Adding model 'Soporte'
        db.create_table(u'calidad_soporte', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('evaluacion_consenso', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['calidad.EvaluacionConsensoMejoresPracticas'])),
            ('soporte_direccion', self.gf('tinymce.models.HTMLField')(blank=True)),
        ))
        db.send_create_signal(u'calidad', ['Soporte'])

        # Adding model 'Resultados'
        db.create_table(u'calidad_resultados', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('evaluacion_consenso', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['calidad.EvaluacionConsensoMejoresPracticas'])),
            ('resultados_obtenidos', self.gf('tinymce.models.HTMLField')(blank=True)),
        ))
        db.send_create_signal(u'calidad', ['Resultados'])

        # Adding model 'FortalezasConsensoMejoresPracticas'
        db.create_table(u'calidad_fortalezasconsensomejorespracticas', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('evaluacion_consenso', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['calidad.EvaluacionConsensoMejoresPracticas'])),
            ('criterio', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['calidad.CriteriosMejoresPracticas'])),
            ('fortalezas', self.gf('tinymce.models.HTMLField')(blank=True)),
        ))
        db.send_create_signal(u'calidad', ['FortalezasConsensoMejoresPracticas'])

        # Adding model 'AreaMejoraConsensoMejoresPracticas'
        db.create_table(u'calidad_areamejoraconsensomejorespracticas', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('evaluacion_consenso', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['calidad.EvaluacionConsensoMejoresPracticas'])),
            ('criterio', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['calidad.CriteriosMejoresPracticas'])),
            ('areas_mejora', self.gf('tinymce.models.HTMLField')(blank=True)),
        ))
        db.send_create_signal(u'calidad', ['AreaMejoraConsensoMejoresPracticas'])

        # Adding model 'PuntosVisitaConsensoMejoresPracticas'
        db.create_table(u'calidad_puntosvisitaconsensomejorespracticas', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('evaluacion_consenso', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['calidad.EvaluacionConsensoMejoresPracticas'])),
            ('criterio', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['calidad.CriteriosMejoresPracticas'])),
            ('puntos_visita', self.gf('tinymce.models.HTMLField')(blank=True)),
        ))
        db.send_create_signal(u'calidad', ['PuntosVisitaConsensoMejoresPracticas'])

        # Adding model 'CuadernosDeEvaluacionMejoresPracticas'
        db.create_table(u'calidad_cuadernosdeevaluacionmejorespracticas', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('evaluacion', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['calidad.EvaluacionIndividualMejoresPracticas'])),
            ('cuaderno', self.gf('django.db.models.fields.files.FileField')(max_length=100)),
            ('fecha_subida', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('comentario', self.gf('django.db.models.fields.CharField')(max_length=350, blank=True)),
        ))
        db.send_create_signal(u'calidad', ['CuadernosDeEvaluacionMejoresPracticas'])

        # Adding model 'InformeConsolidadoMejoresPracticas'
        db.create_table(u'calidad_informeconsolidadomejorespracticas', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('evaluacion', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['calidad.EvaluacionConsensoMejoresPracticas'])),
            ('cuaderno', self.gf('django.db.models.fields.files.FileField')(max_length=500)),
            ('fecha_subida', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('comentario', self.gf('django.db.models.fields.CharField')(max_length=350, blank=True)),
        ))
        db.send_create_signal(u'calidad', ['InformeConsolidadoMejoresPracticas'])

        # Adding model 'EvaluacionVisitaCalidad'
        db.create_table(u'calidad_evaluacionvisitacalidad', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('postulacion_evaluacion', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['calidad.PostulacionesCalidad'], unique=True)),
            ('coordinador_postulacion', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['calidad.Evaluador'])),
        ))
        db.send_create_signal(u'calidad', ['EvaluacionVisitaCalidad'])

        # Adding model 'PuntajeVisitaCalidad'
        db.create_table(u'calidad_puntajevisitacalidad', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('evaluacion', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['calidad.EvaluacionVisitaCalidad'])),
            ('criterio', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['calidad.CriteriosCalidad'])),
            ('puntaje_maximo', self.gf('django.db.models.fields.IntegerField')(blank=True)),
            ('puntaje_consenso', self.gf('django.db.models.fields.IntegerField')(blank=True)),
            ('puntaje_visita', self.gf('django.db.models.fields.DecimalField')(default=0.0, max_digits=7, decimal_places=2, blank=True)),
            ('comentario', self.gf('tinymce.models.HTMLField')(blank=True)),
        ))
        db.send_create_signal(u'calidad', ['PuntajeVisitaCalidad'])

        # Adding model 'FortalezasVisitaCalidad'
        db.create_table(u'calidad_fortalezasvisitacalidad', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('evaluacion_visita', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['calidad.EvaluacionVisitaCalidad'])),
            ('criterio', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['calidad.CriteriosCalidad'])),
            ('fortalezas', self.gf('tinymce.models.HTMLField')(blank=True)),
            ('comentario_revision', self.gf('tinymce.models.HTMLField')(blank=True)),
            ('aprobado', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(u'calidad', ['FortalezasVisitaCalidad'])

        # Adding model 'AreasMejorarVisitaCalidad'
        db.create_table(u'calidad_areasmejorarvisitacalidad', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('evaluacion_visita', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['calidad.EvaluacionVisitaCalidad'])),
            ('criterio', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['calidad.CriteriosCalidad'])),
            ('areas_mejorar', self.gf('tinymce.models.HTMLField')(blank=True)),
            ('comentario_revision', self.gf('tinymce.models.HTMLField')(blank=True)),
            ('aprobado', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(u'calidad', ['AreasMejorarVisitaCalidad'])

        # Adding model 'AmbienteOrganizacionalVisita'
        db.create_table(u'calidad_ambienteorganizacionalvisita', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('evaluacion_consenso', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['calidad.EvaluacionVisitaCalidad'])),
            ('ambiente_organizacional', self.gf('tinymce.models.HTMLField')(blank=True)),
            ('comentario_revision', self.gf('tinymce.models.HTMLField')(blank=True)),
            ('aprobado', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(u'calidad', ['AmbienteOrganizacionalVisita'])

        # Adding model 'RelacionesOrganizacionalesVisita'
        db.create_table(u'calidad_relacionesorganizacionalesvisita', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('evaluacion_consenso', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['calidad.EvaluacionVisitaCalidad'])),
            ('relaciones_organizacionales', self.gf('tinymce.models.HTMLField')(blank=True)),
            ('comentario_revision', self.gf('tinymce.models.HTMLField')(blank=True)),
            ('aprobado', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(u'calidad', ['RelacionesOrganizacionalesVisita'])

        # Adding model 'AmbienteCompetitivoVisita'
        db.create_table(u'calidad_ambientecompetitivovisita', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('evaluacion_consenso', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['calidad.EvaluacionVisitaCalidad'])),
            ('ambiente_competitivo', self.gf('tinymce.models.HTMLField')(blank=True)),
            ('comentario_revision', self.gf('tinymce.models.HTMLField')(blank=True)),
            ('aprobado', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(u'calidad', ['AmbienteCompetitivoVisita'])

        # Adding model 'DesafiosEstrategicosVisita'
        db.create_table(u'calidad_desafiosestrategicosvisita', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('evaluacion_consenso', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['calidad.EvaluacionVisitaCalidad'])),
            ('desafios_estrategicos', self.gf('tinymce.models.HTMLField')(blank=True)),
            ('comentario_revision', self.gf('tinymce.models.HTMLField')(blank=True)),
            ('aprobado', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(u'calidad', ['DesafiosEstrategicosVisita'])

        # Adding model 'SistemaMejoraVisita'
        db.create_table(u'calidad_sistemamejoravisita', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('evaluacion_consenso', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['calidad.EvaluacionVisitaCalidad'])),
            ('sistema_mejora', self.gf('tinymce.models.HTMLField')(blank=True)),
            ('comentario_revision', self.gf('tinymce.models.HTMLField')(blank=True)),
            ('aprobado', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(u'calidad', ['SistemaMejoraVisita'])

        # Adding model 'EvaluacionVisitaMejoresPracticas'
        db.create_table(u'calidad_evaluacionvisitamejorespracticas', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('postulacion_evaluacion', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['calidad.PostulacionesMejoresPracticas'], unique=True)),
            ('coordinador_postulacion', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['calidad.Evaluador'])),
        ))
        db.send_create_signal(u'calidad', ['EvaluacionVisitaMejoresPracticas'])

        # Adding model 'PuntajeVisitaMejoresPracticas'
        db.create_table(u'calidad_puntajevisitamejorespracticas', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('evaluacion_consenso', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['calidad.EvaluacionVisitaMejoresPracticas'])),
            ('criterio', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['calidad.CriteriosMejoresPracticas'])),
            ('puntaje_maximo', self.gf('django.db.models.fields.IntegerField')(blank=True)),
            ('puntacion_consenso', self.gf('django.db.models.fields.IntegerField')(default=0, blank=True)),
            ('puntacion_visita', self.gf('django.db.models.fields.IntegerField')(default=0, blank=True)),
            ('comentario', self.gf('tinymce.models.HTMLField')(blank=True)),
        ))
        db.send_create_signal(u'calidad', ['PuntajeVisitaMejoresPracticas'])

        # Adding model 'FortalezasVisitaMejoresPracticas'
        db.create_table(u'calidad_fortalezasvisitamejorespracticas', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('evaluacion_consenso', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['calidad.EvaluacionVisitaMejoresPracticas'])),
            ('criterio', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['calidad.CriteriosMejoresPracticas'])),
            ('fortalezas', self.gf('tinymce.models.HTMLField')(blank=True)),
            ('comentario_revision', self.gf('tinymce.models.HTMLField')(blank=True)),
            ('aprobado', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(u'calidad', ['FortalezasVisitaMejoresPracticas'])

        # Adding model 'AreaMejoraVisitaMejoresPracticas'
        db.create_table(u'calidad_areamejoravisitamejorespracticas', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('evaluacion_consenso', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['calidad.EvaluacionVisitaMejoresPracticas'])),
            ('criterio', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['calidad.CriteriosMejoresPracticas'])),
            ('areas_mejora', self.gf('tinymce.models.HTMLField')(blank=True)),
            ('comentario_revision', self.gf('tinymce.models.HTMLField')(blank=True)),
            ('aprobado', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(u'calidad', ['AreaMejoraVisitaMejoresPracticas'])

        # Adding model 'VinculoProyectoVisita'
        db.create_table(u'calidad_vinculoproyectovisita', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('evaluacion_consenso', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['calidad.EvaluacionVisitaMejoresPracticas'])),
            ('vinculo_proyecto', self.gf('tinymce.models.HTMLField')(blank=True)),
            ('comentario_revision', self.gf('tinymce.models.HTMLField')(blank=True)),
            ('aprobado', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(u'calidad', ['VinculoProyectoVisita'])

        # Adding model 'MetodologiaVisita'
        db.create_table(u'calidad_metodologiavisita', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('evaluacion_consenso', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['calidad.EvaluacionVisitaMejoresPracticas'])),
            ('metologia_proyecto', self.gf('tinymce.models.HTMLField')(blank=True)),
            ('comentario_revision', self.gf('tinymce.models.HTMLField')(blank=True)),
            ('aprobado', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(u'calidad', ['MetodologiaVisita'])

        # Adding model 'AmbienteCompetitivoVisitaMP'
        db.create_table(u'calidad_ambientecompetitivovisitamp', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('evaluacion_consenso', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['calidad.EvaluacionVisitaMejoresPracticas'])),
            ('ambiente_competitivo', self.gf('tinymce.models.HTMLField')(blank=True)),
            ('comentario_revision', self.gf('tinymce.models.HTMLField')(blank=True)),
            ('aprobado', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(u'calidad', ['AmbienteCompetitivoVisitaMP'])

        # Adding model 'SoporteVisita'
        db.create_table(u'calidad_soportevisita', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('evaluacion_consenso', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['calidad.EvaluacionVisitaMejoresPracticas'])),
            ('soporte_direccion', self.gf('tinymce.models.HTMLField')(blank=True)),
            ('comentario_revision', self.gf('tinymce.models.HTMLField')(blank=True)),
            ('aprobado', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(u'calidad', ['SoporteVisita'])

        # Adding model 'ResultadosVisita'
        db.create_table(u'calidad_resultadosvisita', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('evaluacion_consenso', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['calidad.EvaluacionVisitaMejoresPracticas'])),
            ('resultados_obtenidos', self.gf('tinymce.models.HTMLField')(blank=True)),
            ('comentario_revision', self.gf('tinymce.models.HTMLField')(blank=True)),
            ('aprobado', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(u'calidad', ['ResultadosVisita'])

        # Adding model 'InformeVisitaMejoresPracticas'
        db.create_table(u'calidad_informevisitamejorespracticas', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('evaluacion', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['calidad.EvaluacionVisitaMejoresPracticas'])),
            ('cuaderno', self.gf('django.db.models.fields.files.FileField')(max_length=500)),
            ('fecha_subida', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('comentario', self.gf('django.db.models.fields.CharField')(max_length=350, blank=True)),
        ))
        db.send_create_signal(u'calidad', ['InformeVisitaMejoresPracticas'])

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

        # Deleting model 'EstadoPostulacion'
        db.delete_table(u'calidad_estadopostulacion')

        # Deleting model 'GrupoEvaluador'
        db.delete_table(u'calidad_grupoevaluador')

        # Deleting model 'EvaluacionIndividualCalidad'
        db.delete_table(u'calidad_evaluacionindividualcalidad')

        # Deleting model 'EvaluacionConsensoCalidad'
        db.delete_table(u'calidad_evaluacionconsensocalidad')

        # Deleting model 'CriteriosCalidad'
        db.delete_table(u'calidad_criterioscalidad')

        # Deleting model 'FortalezasConsenso'
        db.delete_table(u'calidad_fortalezasconsenso')

        # Deleting model 'AreaMejoraConsenso'
        db.delete_table(u'calidad_areamejoraconsenso')

        # Deleting model 'PuntosVisitaConsenso'
        db.delete_table(u'calidad_puntosvisitaconsenso')

        # Deleting model 'AmbienteOrganizacionalConsenso'
        db.delete_table(u'calidad_ambienteorganizacionalconsenso')

        # Deleting model 'RelacionesOrganizacionalesConsenso'
        db.delete_table(u'calidad_relacionesorganizacionalesconsenso')

        # Deleting model 'AmbienteCompetitivoConsenso'
        db.delete_table(u'calidad_ambientecompetitivoconsenso')

        # Deleting model 'DesafiosEstrategicosConsenso'
        db.delete_table(u'calidad_desafiosestrategicosconsenso')

        # Deleting model 'SistemaMejoraConsenso'
        db.delete_table(u'calidad_sistemamejoraconsenso')

        # Deleting model 'PuntajeConsensoCalidad'
        db.delete_table(u'calidad_puntajeconsensocalidad')

        # Deleting model 'CriteriosEvaluacion'
        db.delete_table(u'calidad_criteriosevaluacion')

        # Deleting model 'PuntajeEvaluacion'
        db.delete_table(u'calidad_puntajeevaluacion')

        # Deleting model 'CuadernosDeEvaluacion'
        db.delete_table(u'calidad_cuadernosdeevaluacion')

        # Deleting model 'InformeConsolidadoCalidad'
        db.delete_table(u'calidad_informeconsolidadocalidad')

        # Deleting model 'CriteriosMejoresPracticas'
        db.delete_table(u'calidad_criteriosmejorespracticas')

        # Deleting model 'PostulacionesMejoresPracticas'
        db.delete_table(u'calidad_postulacionesmejorespracticas')

        # Deleting model 'EvaluacionIndividualMejoresPracticas'
        db.delete_table(u'calidad_evaluacionindividualmejorespracticas')

        # Deleting model 'CriteriosEvaluacionMejoresPracticas'
        db.delete_table(u'calidad_criteriosevaluacionmejorespracticas')

        # Deleting model 'PuntajeEvaluacionMejoresPracticas'
        db.delete_table(u'calidad_puntajeevaluacionmejorespracticas')

        # Deleting model 'GrupoEvaluadorMejoresPracticas'
        db.delete_table(u'calidad_grupoevaluadormejorespracticas')

        # Deleting model 'EstadoPostulacionMejoresPracticas'
        db.delete_table(u'calidad_estadopostulacionmejorespracticas')

        # Deleting model 'EvaluacionConsensoMejoresPracticas'
        db.delete_table(u'calidad_evaluacionconsensomejorespracticas')

        # Deleting model 'PuntajeConsensoMejoresPracticas'
        db.delete_table(u'calidad_puntajeconsensomejorespracticas')

        # Deleting model 'VinculoProyecto'
        db.delete_table(u'calidad_vinculoproyecto')

        # Deleting model 'Metodologia'
        db.delete_table(u'calidad_metodologia')

        # Deleting model 'AmbienteCompetitivo'
        db.delete_table(u'calidad_ambientecompetitivo')

        # Deleting model 'Soporte'
        db.delete_table(u'calidad_soporte')

        # Deleting model 'Resultados'
        db.delete_table(u'calidad_resultados')

        # Deleting model 'FortalezasConsensoMejoresPracticas'
        db.delete_table(u'calidad_fortalezasconsensomejorespracticas')

        # Deleting model 'AreaMejoraConsensoMejoresPracticas'
        db.delete_table(u'calidad_areamejoraconsensomejorespracticas')

        # Deleting model 'PuntosVisitaConsensoMejoresPracticas'
        db.delete_table(u'calidad_puntosvisitaconsensomejorespracticas')

        # Deleting model 'CuadernosDeEvaluacionMejoresPracticas'
        db.delete_table(u'calidad_cuadernosdeevaluacionmejorespracticas')

        # Deleting model 'InformeConsolidadoMejoresPracticas'
        db.delete_table(u'calidad_informeconsolidadomejorespracticas')

        # Deleting model 'EvaluacionVisitaCalidad'
        db.delete_table(u'calidad_evaluacionvisitacalidad')

        # Deleting model 'PuntajeVisitaCalidad'
        db.delete_table(u'calidad_puntajevisitacalidad')

        # Deleting model 'FortalezasVisitaCalidad'
        db.delete_table(u'calidad_fortalezasvisitacalidad')

        # Deleting model 'AreasMejorarVisitaCalidad'
        db.delete_table(u'calidad_areasmejorarvisitacalidad')

        # Deleting model 'AmbienteOrganizacionalVisita'
        db.delete_table(u'calidad_ambienteorganizacionalvisita')

        # Deleting model 'RelacionesOrganizacionalesVisita'
        db.delete_table(u'calidad_relacionesorganizacionalesvisita')

        # Deleting model 'AmbienteCompetitivoVisita'
        db.delete_table(u'calidad_ambientecompetitivovisita')

        # Deleting model 'DesafiosEstrategicosVisita'
        db.delete_table(u'calidad_desafiosestrategicosvisita')

        # Deleting model 'SistemaMejoraVisita'
        db.delete_table(u'calidad_sistemamejoravisita')

        # Deleting model 'EvaluacionVisitaMejoresPracticas'
        db.delete_table(u'calidad_evaluacionvisitamejorespracticas')

        # Deleting model 'PuntajeVisitaMejoresPracticas'
        db.delete_table(u'calidad_puntajevisitamejorespracticas')

        # Deleting model 'FortalezasVisitaMejoresPracticas'
        db.delete_table(u'calidad_fortalezasvisitamejorespracticas')

        # Deleting model 'AreaMejoraVisitaMejoresPracticas'
        db.delete_table(u'calidad_areamejoravisitamejorespracticas')

        # Deleting model 'VinculoProyectoVisita'
        db.delete_table(u'calidad_vinculoproyectovisita')

        # Deleting model 'MetodologiaVisita'
        db.delete_table(u'calidad_metodologiavisita')

        # Deleting model 'AmbienteCompetitivoVisitaMP'
        db.delete_table(u'calidad_ambientecompetitivovisitamp')

        # Deleting model 'SoporteVisita'
        db.delete_table(u'calidad_soportevisita')

        # Deleting model 'ResultadosVisita'
        db.delete_table(u'calidad_resultadosvisita')

        # Deleting model 'InformeVisitaMejoresPracticas'
        db.delete_table(u'calidad_informevisitamejorespracticas')

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
            'agrupador': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
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
            'agrupador': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
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
            'consenso': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'postulacion_calidad': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['calidad.PostulacionesCalidad']", 'unique': 'True'}),
            'visita': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
        u'calidad.estadopostulacionmejorespracticas': {
            'Meta': {'object_name': 'EstadoPostulacionMejoresPracticas'},
            'consenso': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'postulacion_mejor_practica': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['calidad.PostulacionesMejoresPracticas']", 'unique': 'True'}),
            'visita': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
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
            'coordinador': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'postulacion_calidad': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['calidad.PostulacionesCalidad']"})
        },
        u'calidad.grupoevaluadormejorespracticas': {
            'Meta': {'object_name': 'GrupoEvaluadorMejoresPracticas'},
            'codigo_evaluador': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['calidad.Evaluador']"}),
            'coordinador': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
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