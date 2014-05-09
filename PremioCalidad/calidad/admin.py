# -*- coding: utf-8 -*- 
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from calidad.models import GrupoEvaluador, PostulacionesCalidad,EvaluacionIndividualCalidad,Evaluador,TipoInstitucion,Estudio,AreaExperiencia,TelefonosEvaluador,ExperienciaEvaluador,CriteriosCalidad,CriteriosEvaluacion,PuntajeEvaluacion,CriteriosMejoresPracticas,PostulacionesMejoresPracticas,GrupoEvaluadorMejoresPracticas
from calidad.models import EvaluacionIndividualMejoresPracticas,PuntajeEvaluacionMejoresPracticas,CriteriosEvaluacionMejoresPracticas
from calidad.models import CuadernosDeEvaluacion,EstadoPostulacion,EvaluacionConsensoCalidad,PuntajeConsensoCalidad
from calidad.models import FortalezasConsenso,AreaMejoraConsenso,PuntosVisitaConsenso,InformeConsolidadoCalidad
from calidad.models import AmbienteOrganizacionalConsenso,RelacionesOrganizacionalesConsenso,AmbienteCompetitivoConsenso,DesafiosEstrategicosConsenso,SistemaMejoraConsenso
from calidad.models import EstadoPostulacionMejoresPracticas, EvaluacionConsensoMejoresPracticas, PuntajeConsensoMejoresPracticas
from calidad.models import VinculoProyecto, Metodologia, AmbienteCompetitivo, Soporte, Resultados
from calidad.models import FortalezasConsensoMejoresPracticas, AreaMejoraConsensoMejoresPracticas, PuntosVisitaConsensoMejoresPracticas
from calidad.models import CuadernosDeEvaluacionMejoresPracticas,InformeConsolidadoMejoresPracticas

from calidad.models import EvaluacionVisitaCalidad,PuntajeVisitaCalidad
from calidad.models import FortalezasVisitaCalidad,AreasMejorarVisitaCalidad
from calidad.models import AmbienteOrganizacionalVisita,RelacionesOrganizacionalesVisita,AmbienteCompetitivoVisita,DesafiosEstrategicosVisita,SistemaMejoraVisita


from calidad.models import EvaluacionVisitaMejoresPracticas,PuntajeVisitaMejoresPracticas
from calidad.models import FortalezasVisitaMejoresPracticas,AreaMejoraVisitaMejoresPracticas
from calidad.models import VinculoProyectoVisita,MetodologiaVisita,AmbienteCompetitivoVisitaMP,SoporteVisita,ResultadosVisita
from calidad.models import InformeVisitaMejoresPracticas

from calidad.models import PanelDeAyuda,RespuestasDeAyuda

from calidad.models import DocumentosCompartidosCalidad,DocumentosCompartidosMp

from django.http import HttpResponse, Http404
#from calidad.models import CriteriosEvaluacionConsensoCalidad
#Inlines Ficha de Evaluador

class TelefonoEvaluadorInline(admin.StackedInline):
	extra = 0
	model = TelefonosEvaluador

class ExperienciaEvaluadorInline(admin.TabularInline):
	extra = 0
	model = ExperienciaEvaluador

class EvaluadorInline(admin.StackedInline):
	model = Evaluador 
	can_delete = False
	verbose_plural = "Evaluadore"

	
class EvaluadorAdmin(admin.ModelAdmin):
	model = Evaluador
	search_field = ['codigo','dui','nit','experiencia']
	list_filter = ['tipo_institucion','capacitacion_formacion','formacion_en_calidad','experiencia_en_calidad','estudios','experiencia_facilitador']
	inlines = (TelefonoEvaluadorInline,ExperienciaEvaluadorInline,)
	list_display = ['codigo','nombre','apellido']

#ENDInlines Ficha de Evaluador

#======================================= Evaluaciones Individuales ======================

class CuadernosDeEvaluacionInline(admin.TabularInline):
	extra = 0
	model = CuadernosDeEvaluacion

class CuadernosDeEvaluacionMejoresPracticasInline(admin.TabularInline):
	extra = 0
	model = CuadernosDeEvaluacionMejoresPracticas

class InformeConsolidadoCalidadInline(admin.TabularInline):
	extra = 0
	model = InformeConsolidadoCalidad

class InformeConsolidadoMejoresPracticasInline(admin.TabularInline):
	extra = 0
	model = InformeConsolidadoMejoresPracticas

class InformeVisitaMejoresPracticasInline(admin.TabularInline):
	extra = 0
	model = InformeVisitaMejoresPracticas

class EstadoPostulacionInline(admin.TabularInline):
	extra = 0
	model = EstadoPostulacion

class CriteriosEvaluacionInline(admin.StackedInline):
	extra = 0
	model = CriteriosEvaluacion
	readonly_fields = ['link_edicion',]
	fieldsets =  (('Puntuaciones',{'fields':('criterio','link_edicion',)})),
	#fieldsets =  (('Puntuaciones',{'fields':('criterio',('enfoque','despligue','aprendizaje','integracion'))})),
	#extra = 0
	#fieldsets = (('Puntuaciones',{'fields':('criterio',('enfoque','despligue','aprendizaje','integracion'))}),
	#	('Criterios',{'fields':('fortalezas','areas_mejorar','puntos_visita')}))
	#readonly_fields = ['criterio']

class GrupoEvaluadorInline(admin.TabularInline):
	extra = 0
	max_num = 8
	model = GrupoEvaluador

class PuntajeEvaluacionIndividualInline(admin.TabularInline):
	extra = 0
	model = PuntajeEvaluacion
	readonly_fields = ['link_edicion_puntaje',]

	def get_readonly_fields(self, request, obj=None):
		if request.user.groups.filter(name='individual_calidad_end').exists():
			return  ['criterio','puntaje_maximo','enfoque','despligue','aprendizaje','integracion','promedio','total','link_edicion_puntaje']
		return self.readonly_fields

class EvaluacionIndividualCalidadAdmin(admin.ModelAdmin):
	list_display = ('postulacion_evaluacion','evaluador_postulacion','guardar_cuaderno')
	search_fields = ('postulacion_evaluacion__codigo','evaluador_postulacion__codigo',)
	list_filter = ('postulacion_evaluacion__codigo',)
	readonly_fields = ['guardar_cuaderno',]
	fieldsets  = ((None,{'fields':('postulacion_evaluacion','evaluador_postulacion','nota','nota_global','guardar_cuaderno',)})
		,('Aspectos Claves',{'classes':('collapse','wide', 'extrapretty',),
			'fields':('ambiente_organizacional','relaciones_organizacionales','ambiente_competitivo','desafios_estrategicos',
				'sistema_mejora')}),)
	#inlines = (PuntajeEvaluacionIndividualInline,CriteriosEvaluacionInline,)
	inlines = (PuntajeEvaluacionIndividualInline,CuadernosDeEvaluacionInline,)
	#inlines = (CriteriosEvaluacionInline,)
	#list_filter = ['postulacion']

	def get_readonly_fields(self, request, obj=None):
		if request.user.groups.filter(name='individual_calidad_end').exists():
			return self.readonly_fields + ['postulacion_evaluacion','evaluador_postulacion']
		return self.readonly_fields

	def queryset(self, request):
		#return None
		#print "esta entrando aca de casualidad?"
		qs = super(EvaluacionIndividualCalidadAdmin, self).queryset(request)
		#print str(request.user.evaluador)
		if request.user.is_superuser or request.user.groups.filter(name__in=['responsables_proceso']):
			return qs
		return qs.filter(evaluador_postulacion=request.user.evaluador)


class PostulacionesCalidadAdmin(admin.ModelAdmin):
	list_display = ('codigo','nombre',)
	search_fields = ('codigo','nombre','ejecutivo','contacto_nombre','contacto_alterno','representante_oficial',)
	list_filter = ('clasificacion',)

	fieldsets = (('Organizacion',{'fields':('codigo','nombre','direccion','web','telefono','fax')}),
		('Ejecutivo de mas Alto Nivel de la Organizacion',{'fields':('ejecutivo','cargo_ejecutivo','telefono_ejecutivo','fax_ejecutivo','email_ejecutivo')}),
		('Contacto Designado para el Premio',{'fields':('contacto_nombre','contacto_cargo','telefono_contacto','email_contacto','fax_contacto')}),
		('Contacto Alterno para el Premio',{'fields':('contacto_alterno','cargo_alterno','telefono_alterno','fax_alterno','email_alterno')}),
		('Clasificacion de la Organizacion',{'fields':('clasificacion',)}),
		('Representante Oficial',{'fields':('representante_oficial','representante_cargo')}))

	inlines = (GrupoEvaluadorInline,EstadoPostulacionInline,)


class UserAdmin(UserAdmin):
    inlines = (EvaluadorInline,)

#Mejores Practicas

class EstadoPostulacionMejoresPracticasInline(admin.TabularInline):
	extra = 0
	model = EstadoPostulacionMejoresPracticas

class GrupoEvaluadorMejoresPracticasInline(admin.TabularInline):
	extra = 0
	max_num = 8
	model = GrupoEvaluadorMejoresPracticas

class PostulacionesMejoresPracticasAdmin(admin.ModelAdmin):
	list_display = ('codigo','nombre',)
	search_fields = ('codigo','nombre','ejecutivo','contacto_nombre','contacto_alterno','representante_oficial',)
	list_filter = ('clasificacion',)

	fieldsets = (('Organizacion',{'fields':('codigo','nombre','direccion','web','telefono','fax')}),
		('Ejecutivo de mas Alto Nivel de la Organizacion',{'fields':('ejecutivo','cargo_ejecutivo','telefono_ejecutivo','fax_ejecutivo','email_ejecutivo')}),
		('Contacto Designado para el Premio',{'fields':('contacto_nombre','contacto_cargo','telefono_contacto','email_contacto','fax_contacto')}),
		('Contacto Alterno para el Premio',{'fields':('contacto_alterno','cargo_alterno','telefono_alterno','fax_alterno','email_alterno')}),
		('Clasificacion de la Organizacion',{'fields':('clasificacion',)}),
		('Representante Oficial',{'fields':('representante_oficial','representante_cargo')}),
		('Informacion de Equipo',{'fields':('nombre_equipo','nombre_proyecto','objetivo_proyecto','fecha_inicio','fecha_fin')}))

	inlines = (GrupoEvaluadorMejoresPracticasInline,EstadoPostulacionMejoresPracticasInline,)

class PuntajeEvaluacionIndividualMejoresPracticasInline(admin.TabularInline):
	extra = 0
	model = PuntajeEvaluacionMejoresPracticas
	readonly_fields = ['link_edicion_mp_puntaje',]

	def get_readonly_fields(self, request, obj=None):
		if request.user.groups.filter(name='individual_mp_end').exists():
			return  self.readonly_fields + ['criterio','puntaje_maximo','porcentaje','total']
		return self.readonly_fields


class EvaluacionIndividualMejoresPracticasAdmin(admin.ModelAdmin):
	list_display = ('postulacion_evaluacion','evaluador_postulacion','guardar_cuaderno_mp',)
	fieldsets  = ((None,{'fields':('postulacion_evaluacion','evaluador_postulacion','guardar_cuaderno_mp',)})
		,('Aspectos Claves',{'classes':('collapse','wide', 'extrapretty',),
			'fields':('vinculo_proyecto','metodologia','ambiente_competitivo','soporte',
				'resultados')}),)
	inlines = (PuntajeEvaluacionIndividualMejoresPracticasInline,CuadernosDeEvaluacionMejoresPracticasInline,)
	readonly_fields = ['guardar_cuaderno_mp']

	def queryset(self, request):
		#return None
		#print "esta entrando aca de casualidad?"
		qs = super(EvaluacionIndividualMejoresPracticasAdmin, self).queryset(request)
		#print str(request.user.evaluador)
		if request.user.is_superuser or request.user.groups.filter(name__in=['responsables_proceso']):
			return qs
		return qs.filter(evaluador_postulacion=request.user.evaluador)

#Etapa de Consenso

class PuntajeConsensoCalidadInline(admin.StackedInline):
	extra = 0
	model = PuntajeConsensoCalidad
	#readonly_fields = ['link_edicion',]
	#fieldsets =  (('Puntuaciones',{'fields':('criterio','link_edicion',)})),
	#fieldsets =  (('Puntuaciones',{'fields':('criterio',('enfoque','despligue','aprendizaje','integracion'))})),
	#extra = 0
	fieldsets = (('Puntuaciones',{'fields':('criterio',('link_fortaleza_consenso_calidad','link_area_mejora_consenso_calidad','link_puntos_visita_consenso_calidad',),('puntaje_maximo','promedio','desviacion_estandar','mediana','maximo','minimo','rango','puntuacion','puntacion_consenso_porcentual','puntacion_consenso',))}),
		('Comentarios',{'classes':('collapse','wide', 'extrapretty',),'fields':('comentario',)}))
	readonly_fields = ['link_fortaleza_consenso_calidad','link_area_mejora_consenso_calidad','link_puntos_visita_consenso_calidad']

	def get_readonly_fields(self, request, obj=None):
		if request.user.groups.filter(name='consenso_calidad_end').exists():
			return self.readonly_fields + ['criterio','puntaje_maximo','promedio','desviacion_estandar','mediana','maximo','minimo','rango','puntuacion','puntacion_consenso_porcentual','puntacion_consenso','comentario']
		return self.readonly_fields

class PuntajeVisitaCalidadInline(admin.StackedInline):
	extra = 0
	model = PuntajeVisitaCalidad
	fieldsets = (('Puntuaciones',{'fields':('criterio',('link_fortaleza_visita_calidad','link_area_mejora_visita_calidad',),('puntaje_maximo','puntaje_consenso','puntaje_visita_porcentual','puntaje_visita',))}),
		('Comentarios',{'classes':('collapse','wide', 'extrapretty',),'fields':('comentario',)}))
	readonly_fields = ['link_fortaleza_visita_calidad','link_area_mejora_visita_calidad']

	def get_readonly_fields(self, request, obj=None):
		if request.user.groups.filter(name='visita_calidad_end').exists():
			return self.readonly_fields+['criterio','puntaje_maximo','puntaje_consenso','puntaje_visita_porcentual','puntaje_visita','comentario']
		return self.readonly_fields	

class EvaluacionConsensoCalidadAdmin(admin.ModelAdmin):
	list_display = ['postulacion_evaluacion','coordinador_postulacion','cuaderno_consolidado','informe_consenso_calidad']
	fieldsets = (('Datos Generales',{'fields':('postulacion_evaluacion','coordinador_postulacion')}),
		('Aspectos Claves',{'fields':(('ambiente_organizacional','relaciones_organizacionales','ambiente_competitivo','desafios_estrategicos'),('sistema_mejora'))}),
		('Informes',{'fields':(('cuaderno_consolidado','informe_consenso_calidad','hoja_puntuacion'),)}))
	readonly_fields =['cuaderno_consolidado','informe_consenso_calidad','ambiente_organizacional','relaciones_organizacionales','ambiente_competitivo','desafios_estrategicos','sistema_mejora','hoja_puntuacion']
	inlines = (PuntajeConsensoCalidadInline,InformeConsolidadoCalidadInline,)

	def queryset(self, request):
		#return None
		#print "esta entrando aca de casualidad?"
		qs = super(EvaluacionConsensoCalidadAdmin, self).queryset(request)
		#print str(request.user.evaluador)
		if request.user.is_superuser or request.user.groups.filter(name__in=['responsables_proceso']):
			return qs
		return qs.filter(coordinador_postulacion=request.user.evaluador)

class EvaluacionVisitaCalidadAdmin(admin.ModelAdmin):
	list_display = ['postulacion_evaluacion','coordinador_postulacion']
	fieldsets = (('Datos Generales',{'fields':('postulacion_evaluacion','coordinador_postulacion')}),
		('Aspectos Claves',{'fields':(('ambiente_organizacional','relaciones_organizacionales','ambiente_competitivo','desafios_estrategicos'),('sistema_mejora'))}),
		('Informes',{'fields':(('informe_visita_calidad','hoja_puntuacion',),)}))
	readonly_fields =['ambiente_organizacional','relaciones_organizacionales','ambiente_competitivo','desafios_estrategicos','sistema_mejora','informe_visita_calidad','hoja_puntuacion']#'hoja_puntuacion','cuaderno_consolidado','informe_consenso_calidad',]
	inlines = (PuntajeVisitaCalidadInline,)

	def queryset(self, request):
		#return None
		#print "esta entrando aca de casualidad?"
		qs = super(EvaluacionVisitaCalidadAdmin, self).queryset(request)
		#print str(request.user.evaluador)
		if request.user.is_superuser or request.user.groups.filter(name__in=['responsables_proceso']):
			return qs
		return qs.filter(coordinador_postulacion=request.user.evaluador)

class CriteriosVisitaCalidadAdmin(admin.ModelAdmin):
	
	def queryset(self, request):
		#return None
		#print "esta entrando aca de casualidad?"
		qs = super(CriteriosVisitaCalidadAdmin, self).queryset(request)
		#print str(request.user.evaluador)
		if request.user.is_superuser or request.user.groups.filter(name__in=['responsables_proceso']):
			return qs
		else:
			d = EvaluacionVisitaCalidad.objects.filter(coordinador_postulacion=request.user.evaluador)[0]
			return qs.filter(evaluacion_consenso=d)

	def get_readonly_fields(self, request, obj=None):
		if not request.user.groups.filter(name='responsables_proceso').exists():
			return self.readonly_fields + ('comentario_revision','aprobado',)
		return self.readonly_fields

	def response_add(self, request, obj, post_url_continue=None):
		return HttpResponse('<!DOCTYPE html><html><head><title></title></head><body>'+'<script type="text/javascript">window.close();</script></body></html>')

	def response_change(self, request, obj, post_url_continue=None):
		return HttpResponse('<!DOCTYPE html><html><head><title></title></head><body>'+'<script type="text/javascript">window.close();</script></body></html>')

class CriteriosVisitaCalidadAdmin2(admin.ModelAdmin):
	
	def queryset(self, request):
		#return None
		#print "esta entrando aca de casualidad?"
		qs = super(CriteriosVisitaCalidadAdmin2, self).queryset(request)
		#print str(request.user.evaluador)
		if request.user.is_superuser or request.user.groups.filter(name__in=['responsables_proceso']):
			return qs
		else:
			d = EvaluacionVisitaCalidad.objects.filter(coordinador_postulacion=request.user.evaluador)[0]
			return qs.filter(evaluacion_visita=d)


	def get_readonly_fields(self, request, obj=None):
		if not request.user.groups.filter(name='responsables_proceso').exists():
			return self.readonly_fields + ('comentario_revision','aprobado',)
		return self.readonly_fields

	def response_add(self, request, obj, post_url_continue=None):
		return HttpResponse('<!DOCTYPE html><html><head><title></title></head><body>'+'<script type="text/javascript">window.close();</script></body></html>')

	def response_change(self, request, obj, post_url_continue=None):
		return HttpResponse('<!DOCTYPE html><html><head><title></title></head><body>'+'<script type="text/javascript">window.close();</script></body></html>')


class CriteriosConsensoMejoresPracticasAdmin2(admin.ModelAdmin):
	
	def queryset(self, request):
		#return None
		#print "esta entrando aca de casualidad?"
		qs = super(CriteriosConsensoMejoresPracticasAdmin2, self).queryset(request)
		#print str(request.user.evaluador)
		if request.user.is_superuser or request.user.groups.filter(name__in=['responsables_proceso']):
			return qs
		else:
			d = EvaluacionConsensoMejoresPracticas.objects.filter(coordinador_postulacion=request.user.evaluador)[0]
			return qs.filter(evaluacion_consenso=d)

	def response_add(self, request, obj, post_url_continue=None):
		return HttpResponse('<!DOCTYPE html><html><head><title></title></head><body>'+'<script type="text/javascript">window.close();</script></body></html>')

	def response_change(self, request, obj, post_url_continue=None):
		return HttpResponse('<!DOCTYPE html><html><head><title></title></head><body>'+'<script type="text/javascript">window.close();</script></body></html>')

class CriteriosConsensoCalidadAdmin2(admin.ModelAdmin):
	
	def queryset(self, request):
		#return None
		#print "esta entrando aca de casualidad?"
		qs = super(CriteriosConsensoCalidadAdmin2, self).queryset(request)
		#print str(request.user.evaluador)
		if request.user.is_superuser or request.user.groups.filter(name__in=['responsables_proceso']):
			return qs
		else:
			d = EvaluacionConsensoCalidad.objects.filter(coordinador_postulacion=request.user.evaluador)[0]
			return qs.filter(evaluacion_consenso=d)

	def response_add(self, request, obj, post_url_continue=None):
		return HttpResponse('<!DOCTYPE html><html><head><title></title></head><body>'+'<script type="text/javascript">window.close();</script></body></html>')

	def response_change(self, request, obj, post_url_continue=None):
		return HttpResponse('<!DOCTYPE html><html><head><title></title></head><body>'+'<script type="text/javascript">window.close();</script></body></html>')

class CriteriosVisitaMPAdmin2(admin.ModelAdmin):
	
	def queryset(self, request):
		#return None
		#print "esta entrando aca de casualidad?"
		qs = super(CriteriosVisitaMPAdmin2, self).queryset(request)
		#print str(request.user.evaluador)
		if request.user.is_superuser or request.user.groups.filter(name__in=['responsables_proceso']):
			return qs
		else:
			d = EvaluacionVisitaMejoresPracticas.objects.filter(coordinador_postulacion=request.user.evaluador)[0]
			return qs.filter(evaluacion_consenso=d)


	def get_readonly_fields(self, request, obj=None):
		if not request.user.groups.filter(name='responsables_proceso').exists():
			return self.readonly_fields + ('comentario_revision','aprobado',)
		return self.readonly_fields

	def response_add(self, request, obj, post_url_continue=None):
		return HttpResponse('<!DOCTYPE html><html><head><title></title></head><body>'+'<script type="text/javascript">window.close();</script></body></html>')

	def response_change(self, request, obj, post_url_continue=None):
		return HttpResponse('<!DOCTYPE html><html><head><title></title></head><body>'+'<script type="text/javascript">window.close();</script></body></html>')

class CriteriosEvaCalidadAdmin(admin.ModelAdmin):
	
	def queryset(self, request):
		#return None
		#print "esta entrando aca de casualidad?"
		qs = super(CriteriosEvaCalidadAdmin, self).queryset(request)
		#print str(request.user.evaluador)
		if request.user.is_superuser or request.user.groups.filter(name__in=['responsables_proceso']):
			return qs
		else:
			d = EvaluacionIndividualCalidad.objects.filter(evaluador_postulacion=request.user.evaluador)[0]
			return qs.filter(evaluacion=d)

	def response_add(self, request, obj, post_url_continue=None):
		return HttpResponse('<!DOCTYPE html><html><head><title></title></head><body>'+'<script type="text/javascript">window.close();</script></body></html>')

	def response_change(self, request, obj, post_url_continue=None):
		return HttpResponse('<!DOCTYPE html><html><head><title></title></head><body>'+'<script type="text/javascript">window.close();</script></body></html>')

class CriteriosEvaMPAdmin(admin.ModelAdmin):
	
	def queryset(self, request):
		#return None
		#print "esta entrando aca de casualidad?"
		qs = super(CriteriosEvaMPAdmin, self).queryset(request)
		#print str(request.user.evaluador)
		if request.user.is_superuser or request.user.groups.filter(name__in=['responsables_proceso']):
			return qs
		else:
			d = EvaluacionIndividualMejoresPracticas.objects.filter(evaluador_postulacion=request.user.evaluador)[0]
			return qs.filter(evaluacion=d)

	def response_add(self, request, obj, post_url_continue=None):
		return HttpResponse('<!DOCTYPE html><html><head><title></title></head><body>'+'<script type="text/javascript">window.close();</script></body></html>')

	def response_change(self, request, obj, post_url_continue=None):
		return HttpResponse('<!DOCTYPE html><html><head><title></title></head><body>'+'<script type="text/javascript">window.close();</script></body></html>')


#Etapa Consenso Mejores Practicas

class PuntajeConsensoMejoresPracticasInline(admin.StackedInline):
	extra = 0
	model = PuntajeConsensoMejoresPracticas
	fieldsets = (('Puntuaciones',{'fields':('criterio',('link_fortaleza_consenso_mp','link_area_mejora_consenso_mp','link_puntos_visita_consenso_mp',),('puntaje_maximo','promedio','desviacion_estandar','mediana','maximo','minimo','rango','puntuacion','puntacion_consenso_porcentual','puntacion_consenso',))}),
		('Comentarios',{'classes':('collapse','wide', 'extrapretty',),'fields':('comentario',)}))
	#readonly_fields = ['link_edicion',]
	#fieldsets =  (('Puntuaciones',{'fields':('criterio','link_edicion',)})),
	#fieldsets =  (('Puntuaciones',{'fields':('criterio',('enfoque','despligue','aprendizaje','integracion'))})),
	#extra = 0
	#fieldsets = (('Puntuaciones',{'fields':('criterio',('link_fortaleza_consenso_calidad','link_area_mejora_consenso_calidad','link_puntos_visita_consenso_calidad',),('puntaje_maximo','promedio','desviacion_estandar','mediana','maximo','minimo','rango','puntuacion','puntacion_consenso',))}),
	#	('Comentarios',{'classes':('collapse','wide', 'extrapretty',),'fields':('comentario',)}))
	readonly_fields = ['link_fortaleza_consenso_mp','link_area_mejora_consenso_mp','link_puntos_visita_consenso_mp']

	def get_readonly_fields(self, request, obj=None):
		if request.user.groups.filter(name='consenso_mp_end').exists():
			return  self.readonly_fields + ['criterio','puntaje_maximo','promedio','desviacion_estandar','mediana','maximo','minimo','rango','puntuacion','puntacion_consenso_porcentual','puntacion_consenso','comentario']
		return self.readonly_fields

class EvaluacionConsensoMejoresPracticasAdmin(admin.ModelAdmin):
	list_display = ['postulacion_evaluacion','coordinador_postulacion','cuaderno_consolidado_mp','informe_consenso_mp']
	fieldsets = (('Datos Generales',{'fields':('postulacion_evaluacion','coordinador_postulacion')}),#,
		('Aspectos Claves',{'fields':(('vinculo_proyecto','metodologia','ambiente_competitivo','soporte'),('resultados'))}),
		('Informes',{'fields':(('cuaderno_consolidado_mp','informe_consenso_mp','hoja_puntuacion',),)}))
	inlines = (PuntajeConsensoMejoresPracticasInline,InformeConsolidadoMejoresPracticasInline,)
	readonly_fields = ['vinculo_proyecto','metodologia','ambiente_competitivo','soporte','resultados','cuaderno_consolidado_mp','informe_consenso_mp','hoja_puntuacion']

	def queryset(self, request):
		#return None
		#print "esta entrando aca de casualidad?"
		qs = super(EvaluacionConsensoMejoresPracticasAdmin, self).queryset(request)
		#print str(request.user.evaluador)
		if request.user.is_superuser or request.user.groups.filter(name__in=['responsables_proceso']):
			return qs
		return qs.filter(coordinador_postulacion=request.user.evaluador)

class PuntajeVisitaMejoresPracticasInline(admin.StackedInline):
	extra = 0
	model = PuntajeVisitaMejoresPracticas
	fieldsets = (('Puntuaciones',{'fields':('criterio',('link_fortaleza_consenso_mp','link_area_mejora_consenso_mp',),('puntaje_maximo','puntacion_consenso','puntacion_visita_porcentual','puntacion_visita',))}),
		('Comentarios',{'classes':('collapse','wide', 'extrapretty',),'fields':('comentario',)}))
	readonly_fields = ['link_fortaleza_consenso_mp','link_area_mejora_consenso_mp']

	def get_readonly_fields(self, request, obj=None):
		if request.user.groups.filter(name='visita_mp_end').exists():
			return  self.readonly_fields + ['criterio','puntaje_maximo','puntacion_consenso','puntacion_visita_porcentual','puntacion_visita','comentario']
		return self.readonly_fields

#Etapa Visita Mejores Practicas
class EvaluacionVisitaMejoresPracticasAdmin(admin.ModelAdmin):
	list_display = ['postulacion_evaluacion','coordinador_postulacion','informe_realimentacion_mp']
	fieldsets = (('Datos Generales',{'fields':('postulacion_evaluacion','coordinador_postulacion')}),#,
		('Aspectos Claves',{'fields':(('vinculo_proyecto','metodologia','ambiente_competitivo','soporte'),('resultados'))}),
		('Informes',{'fields':(('informe_realimentacion_mp','hoja_puntuacion',),)}))
	inlines = (PuntajeVisitaMejoresPracticasInline,InformeVisitaMejoresPracticasInline,)
	readonly_fields = ['vinculo_proyecto','metodologia','ambiente_competitivo','soporte','resultados','informe_realimentacion_mp','hoja_puntuacion']

	def queryset(self, request):
		#return None
		#print "esta entrando aca de casualidad?"
		qs = super(EvaluacionVisitaMejoresPracticasAdmin, self).queryset(request)
		#print str(request.user.evaluador)
		if request.user.is_superuser or request.user.groups.filter(name__in=['responsables_proceso']):
			return qs
		return qs.filter(coordinador_postulacion=request.user.evaluador)


class PopUpsAdmin(admin.ModelAdmin):

	def response_add(self, request, obj, post_url_continue=None):
		return HttpResponse('<!DOCTYPE html><html><head><title></title></head><body>'+'<script type="text/javascript">window.close();</script></body></html>')

	def response_change(self, request, obj, post_url_continue=None):
		return HttpResponse('<!DOCTYPE html><html><head><title></title></head><body>'+'<script type="text/javascript">window.close();</script></body></html>')

#===========================================REGISTRO DE APLICACIONES=========================

#Catalogos
admin.site.register(TipoInstitucion)
admin.site.register(Estudio)
admin.site.register(AreaExperiencia)
admin.site.register(CriteriosCalidad)
admin.site.register(CriteriosMejoresPracticas)

#Registro de Evaluadores
admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(Evaluador, EvaluadorAdmin)

#Registro de Evaluaciones Calidad
admin.site.register(PostulacionesCalidad,PostulacionesCalidadAdmin)
admin.site.register(EvaluacionIndividualCalidad,EvaluacionIndividualCalidadAdmin)
admin.site.register(CriteriosEvaluacion,CriteriosEvaCalidadAdmin)

admin.site.register(EvaluacionConsensoCalidad,EvaluacionConsensoCalidadAdmin)
admin.site.register(FortalezasConsenso,CriteriosConsensoCalidadAdmin2)
admin.site.register(AreaMejoraConsenso,CriteriosConsensoCalidadAdmin2)
admin.site.register(PuntosVisitaConsenso,CriteriosConsensoCalidadAdmin2)
admin.site.register(AmbienteOrganizacionalConsenso,CriteriosConsensoCalidadAdmin2)
admin.site.register(RelacionesOrganizacionalesConsenso,CriteriosConsensoCalidadAdmin2)
admin.site.register(AmbienteCompetitivoConsenso,CriteriosConsensoCalidadAdmin2)
admin.site.register(DesafiosEstrategicosConsenso,CriteriosConsensoCalidadAdmin2)
admin.site.register(SistemaMejoraConsenso,CriteriosConsensoCalidadAdmin2)

admin.site.register(EvaluacionVisitaCalidad,EvaluacionVisitaCalidadAdmin)
admin.site.register(FortalezasVisitaCalidad,CriteriosVisitaCalidadAdmin2)
admin.site.register(AreasMejorarVisitaCalidad,CriteriosVisitaCalidadAdmin2)
admin.site.register(AmbienteOrganizacionalVisita,CriteriosVisitaCalidadAdmin)
admin.site.register(RelacionesOrganizacionalesVisita,CriteriosVisitaCalidadAdmin)
admin.site.register(AmbienteCompetitivoVisita,CriteriosVisitaCalidadAdmin)
admin.site.register(DesafiosEstrategicosVisita,CriteriosVisitaCalidadAdmin)
admin.site.register(SistemaMejoraVisita,CriteriosVisitaCalidadAdmin)

#admin.site.register(CriteriosEvaluacionConsensoCalidad)

#Registro de Evaluaciones Mejores Practicas
admin.site.register(PostulacionesMejoresPracticas,PostulacionesMejoresPracticasAdmin)
admin.site.register(EvaluacionIndividualMejoresPracticas,EvaluacionIndividualMejoresPracticasAdmin)
admin.site.register(CriteriosEvaluacionMejoresPracticas,CriteriosEvaMPAdmin)
admin.site.register(EvaluacionConsensoMejoresPracticas,EvaluacionConsensoMejoresPracticasAdmin)
admin.site.register(VinculoProyecto,CriteriosConsensoMejoresPracticasAdmin2)
admin.site.register(Metodologia,CriteriosConsensoMejoresPracticasAdmin2)
admin.site.register(AmbienteCompetitivo,CriteriosConsensoMejoresPracticasAdmin2)
admin.site.register(Soporte,CriteriosConsensoMejoresPracticasAdmin2)
admin.site.register(Resultados,CriteriosConsensoMejoresPracticasAdmin2)
admin.site.register(FortalezasConsensoMejoresPracticas,CriteriosConsensoMejoresPracticasAdmin2)
admin.site.register(AreaMejoraConsensoMejoresPracticas,CriteriosConsensoMejoresPracticasAdmin2)
admin.site.register(PuntosVisitaConsensoMejoresPracticas,CriteriosConsensoMejoresPracticasAdmin2)

admin.site.register(EvaluacionVisitaMejoresPracticas,EvaluacionVisitaMejoresPracticasAdmin)
admin.site.register(VinculoProyectoVisita,CriteriosVisitaMPAdmin2)
admin.site.register(MetodologiaVisita,CriteriosVisitaMPAdmin2)
admin.site.register(AmbienteCompetitivoVisitaMP,CriteriosVisitaMPAdmin2)
admin.site.register(SoporteVisita,CriteriosVisitaMPAdmin2)
admin.site.register(ResultadosVisita,CriteriosVisitaMPAdmin2)
admin.site.register(FortalezasVisitaMejoresPracticas,CriteriosVisitaMPAdmin2)
admin.site.register(AreaMejoraVisitaMejoresPracticas,CriteriosVisitaMPAdmin2)

#Documentos Compartidos

class DocumentosCompartidosCalidadAdmin(admin.ModelAdmin):
	list_display = ['postulacion','evaluador','documento','comentario','fecha_subida']
	readonly_fields = ['postulacion','evaluador','comentario','fecha_subida']
	search_fields = ['postulacion','evaluador']

	def queryset(self, request):
		#return None
		#print "esta entrando aca de casualidad?"
		qs = super(DocumentosCompartidosCalidadAdmin, self).queryset(request)
		#print str(request.user.evaluador)
		if request.user.is_superuser or request.user.groups.filter(name__in=['responsables_proceso']):
			return qs
		return qs.filter(evaluador=request.user.evaluador).order_by('-fecha_subida')

class DocumentosCompartidosMpAdmin(admin.ModelAdmin):
	list_display = ['postulacion','evaluador','documento','comentario','fecha_subida']
	readonly_fields = ['postulacion','evaluador','comentario','fecha_subida']
	search_fields = ['postulacion__codigo','evaluador__codigo']

	def queryset(self, request):
		#return None
		#print "esta entrando aca de casualidad?"
		qs = super(DocumentosCompartidosMpAdmin, self).queryset(request)
		#print str(request.user.evaluador)
		if request.user.is_superuser or request.user.groups.filter(name__in=['responsables_proceso']):
			return qs
		return qs.filter(evaluador=request.user.evaluador).order_by('-fecha_subida')

admin.site.register(DocumentosCompartidosCalidad,DocumentosCompartidosCalidadAdmin)
admin.site.register(DocumentosCompartidosMp,DocumentosCompartidosMpAdmin)

#Panel de Ayuda

class RespuestasAyudaInline(admin.TabularInline):
	model = RespuestasDeAyuda
	extra = 0

class PanelAyudaAdmin(admin.ModelAdmin):
	list_display = ['evaluador','asunto','estado_caso','fecha']
	list_filter = ['evaluador','estado_caso']
	readonly_fields = ['evaluador']

	inlines = (RespuestasAyudaInline,)

	def queryset(self, request):
		#return None
		#print "esta entrando aca de casualidad?"
		qs = super(PanelAyudaAdmin, self).queryset(request)
		#print str(request.user.evaluador)
		if request.user.is_superuser or request.user.groups.filter(name__in=['responsables_proceso']):
			return qs
		return qs.filter(evaluador=request.user).order_by('-fecha')

	def save_model(self, request, obj, form, change):
		if obj.evaluador==None: 
			obj.evaluador = request.user
		obj.save()

admin.site.register(PanelDeAyuda,PanelAyudaAdmin)