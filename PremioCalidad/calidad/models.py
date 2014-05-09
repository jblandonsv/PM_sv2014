# -*- coding: utf-8 -*- 
from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from django.core.exceptions import ValidationError
from django.conf import settings
from math import sqrt

from django.contrib.auth.models import Group

from tinymce.models import HTMLField

#Validadores
def validate_fivemultiple(value):
    if value % 5 != 0:
        raise ValidationError(u'%s Por favor colocar un multiplo de 5' % value)

def validate_mymultiple(value,maximo=70):
	print "esta entrando??"
	if value==None:
		raise ValidationError(u'Este es el problema')
	if maximo==None:
		maximo = 90
	if value == 0:
		raise ValidationError(u'Por favor colocar un multiplo de 5')


#Ficha de Evaluadores
#==============================================

class TipoInstitucion(models.Model):
	nombre_tipo_institucion = models.CharField(max_length=150,blank=False,unique=True)

	def __unicode__(self):
		return self.nombre_tipo_institucion

class Estudio(models.Model):
	nombre_estudio = models.CharField(max_length=150,blank=False,unique=True)

	def __unicode__(self):
		return self.nombre_estudio

class AreaExperiencia(models.Model):
	nombre_area =  models.CharField(max_length=150,blank=False,unique=True)

	def __unicode__(self):
		return self.nombre_area

class Evaluador(models.Model):
	identificador = models.OneToOneField(User)
	codigo =  models.CharField(max_length=15,blank=False,unique=True,verbose_name="Codigo Evaluador")
	dui = models.CharField(max_length=15,blank=False,unique=True)
	nit = models.CharField(max_length=15,blank=False,unique=True)
	tipo_institucion = models.ForeignKey(TipoInstitucion)
	edad = models.IntegerField(blank=True)
	experiencia = models.CharField(max_length=85,blank=True)
	capacitacion_formacion = models.BooleanField(help_text="Capacitacion o Formacion")
	formacion_en_calidad = models.BooleanField(help_text="Formacion en Calidad")
	experiencia_en_calidad = models.BooleanField(help_text="Experiencia en Calidad")
	estudios = models.ForeignKey(Estudio)
	profesion = models.CharField(max_length=75,blank=True)
	empresa_actual = models.CharField(max_length=150,blank=True,help_text="Empresa donde labora actualmente")
	cargo = models.CharField(max_length=150,blank=True,help_text="Cargo que tiene en la empresa")
	experiencia_facilitador = models.BooleanField(help_text="Experiencia como facilitador")
	ingles = models.CharField(max_length=50,blank=True)

	def __unicode__(self):
		return self.codigo

	def nombre(self):
		return self.identificador.first_name

	def apellido(self):
		return self.identificador.last_name

class TelefonosEvaluador(models.Model):
	evaluador_tel = models.ForeignKey(Evaluador)
	telefono = models.CharField(max_length=25,blank=False)

	def __unicode__(self):
		return self.evaluador_tel.codigo

class ExperienciaEvaluador(models.Model):
	evaluador_experiencia = models.ForeignKey(Evaluador)
	area = models.ForeignKey(AreaExperiencia)
	tiempo_experiencia = models.CharField(max_length=75,blank=False,help_text="describa tiempo de experiencia")

#End Ficha Evaluadores
#===============================================================

#Ficha de Postulacion

class PostulacionesCalidad(models.Model): 
	codigo = models.CharField(max_length=15,blank=False,unique=True)
	nombre = models.CharField(max_length=150,blank=False,verbose_name="Razon Social")
	direccion = models.CharField(max_length=450,blank=True,verbose_name="Direccion")
	web = models.CharField(max_length=150,blank=True,verbose_name="Direccion Web")
	telefono = models.CharField(max_length=25,blank=True,verbose_name="Telefono")
	fax = models.CharField(max_length=25,blank=True,verbose_name="Fax")
	ejecutivo = models.CharField(max_length=75,blank=True,verbose_name="Nombre")
	cargo_ejecutivo = models.CharField(max_length=175,blank=True,verbose_name="Cargo")
	telefono_ejecutivo = models.CharField(max_length=25,blank=True,verbose_name="Telefono")
	fax_ejecutivo = models.CharField(max_length=25,blank=True,verbose_name="Fax")
	email_ejecutivo = models.CharField(max_length=100,blank=True,verbose_name="Email")
	contacto_nombre = models.CharField(max_length=125,blank=True,verbose_name="Nombre")
	contacto_cargo = models.CharField(max_length=175,blank=True,verbose_name="Cargo")
	telefono_contacto = models.CharField(max_length=25,blank=True,verbose_name="Telefono")
	fax_contacto = models.CharField(max_length=25,blank=True,verbose_name="Fax")
	email_contacto = models.CharField(max_length=100,blank=True,verbose_name="Email")
	contacto_alterno = models.CharField(max_length=125,blank=True,verbose_name="Nombre")
	cargo_alterno = models.CharField(max_length=175,blank=True,verbose_name="Cargo")
	telefono_alterno = models.CharField(max_length=25,blank=True,verbose_name="Telefono")
	fax_alterno = models.CharField(max_length=25,blank=True,verbose_name="Fax")
	email_alterno = models.CharField(max_length=100,blank=True,verbose_name="Email")
	clasificacion = models.ForeignKey(TipoInstitucion)	
	representante_oficial = models.CharField(max_length=125,blank=True,verbose_name="Nombre")
	representante_cargo = models.CharField(max_length=125,blank=True,verbose_name="Cargo")

	def __unicode__(self):
		return self.codigo

class EstadoPostulacion(models.Model):
	postulacion_calidad = models.OneToOneField(PostulacionesCalidad)
	consenso = models.BooleanField()
	visita = models.BooleanField()
	finalizado = models.BooleanField()

	def save(self, *args, **kwargs):
		#Sirve para controlar el movimiento de los datos a las distintas etapas

		#Primero se verifica si no estaba esa postulacion ya en una etapa determinada
		ep = EstadoPostulacion.objects.filter(postulacion_calidad=self.postulacion_calidad)
		if ep:
			#Ya existia un estado creado, ahora hay que proceder a ver de que se trataba
			if ep[0].consenso == False and self.consenso==True:
				#La postulacion no se encontraba en la etapa de consenso, y ahora se esta moviendo a esa etapa
				self.mover_datos_consenso()
			if ep[0].consenso == True and ep[0].visita==False and self.visita==True:
				#La postulacion Ya habia pasado la etapa de consenso y ahora se esta moviendo a la etapa de visita
				self.mover_datos_visita()
			if self.finalizado == True:
				g = Group.objects.get(name='visita_calidad_end') 
				ecc = EvaluacionConsensoCalidad.objects.filter(postulacion_evaluacion=self.postulacion_calidad)[0]
				g.user_set.add(ecc.coordinador_postulacion.identificador)
		else:
			#No habia un estado creado por lo que se debe ahora hacer el movimiento de datos respectivos
			#NOTA IMPORTANTE: No existe un movimiento a etapa de visita a partir de un estado nuevo
			#para mover una postulacion a la etapa de visita, primero hay que pasar por consenso y mover todo ahi
			if self.consenso:
				#TODO: MOVER DATOS ETAPA CONSENSO
				self.mover_datos_consenso()

		super(EstadoPostulacion, self).save(*args, **kwargs)

	def desviacion_estandar(self,valores):

		prom = (sum(valores)/len(valores))

		varianza=map(lambda x: (x - prom)**2, valores)
		prom_varianza=(sum(varianza))/len(varianza)

		return sqrt(prom_varianza)

	def mover_datos_visita(self):
		#Moviendo datos de etapa de consenso a etapa de visita
		#NOTA IMPORTANTE: para poder ejecutar esta accion, primero tiene que haber una postulacion en etapa de consenso

		#Primero hay que crear la evaluacion de visita colocando los mismos datos generales que en la etapa de consenso

		ev = EvaluacionVisitaCalidad()
		ecc = EvaluacionConsensoCalidad.objects.filter(postulacion_evaluacion=self.postulacion_calidad)[0]
		ev.postulacion_evaluacion = ecc.postulacion_evaluacion
		ev.coordinador_postulacion = ecc.coordinador_postulacion
		ev.save()

		#Agregando al coordinador al grupo respectivo
		g = Group.objects.get(name='coordinador_calidad_visita') 
		g.user_set.add(ev.coordinador_postulacion.identificador)
		gend = Group.objects.get(name='consenso_calidad_end') 
		gend.user_set.add(ev.coordinador_postulacion.identificador)

		#Luego hay que crear la hoja de Puntuacion Respectiva moviendo la puntuacion de consenso
		puntajes = PuntajeConsensoCalidad.objects.filter(evaluacion_consenso=ecc)

		for puntaje in puntajes:
			pv = PuntajeVisitaCalidad()
			pv.evaluacion = ev
			pv.criterio = puntaje.criterio
			pv.puntaje_maximo = puntaje.puntaje_maximo
			pv.puntaje_consenso = puntaje.puntacion_consenso

			pv.save()

		#Ahora hay que mover los datos de los Aspectos Claves de Calidad de la etapa de consenso a la etapa de visita
		aoc = AmbienteOrganizacionalConsenso.objects.filter(evaluacion_consenso=ecc)[0]
		roc = RelacionesOrganizacionalesConsenso.objects.filter(evaluacion_consenso=ecc)[0]
		acc = AmbienteCompetitivoConsenso.objects.filter(evaluacion_consenso=ecc)[0]
		dec = DesafiosEstrategicosConsenso.objects.filter(evaluacion_consenso=ecc)[0]
		smc = SistemaMejoraConsenso.objects.filter(evaluacion_consenso=ecc)[0]

		aov = AmbienteOrganizacionalVisita(evaluacion_consenso=ev,
			ambiente_organizacional=aoc.ambiente_organizacional)
		aov.save()

		rov = RelacionesOrganizacionalesVisita(evaluacion_consenso=ev,
			relaciones_organizacionales=roc.relaciones_organizacionales)
		rov.save()

		acv = AmbienteCompetitivoVisita(evaluacion_consenso=ev,
			ambiente_competitivo=acc.ambiente_competitivo)
		acv.save()

		dev = DesafiosEstrategicosVisita(evaluacion_consenso=ev,
			desafios_estrategicos=dec.desafios_estrategicos)
		dev.save()

		smv = SistemaMejoraVisita(evaluacion_consenso=ev,
			sistema_mejora=smc.sistema_mejora)
		smv.save()

		#Por ultimo se mueven unicamente las fortalezas y areas de mejora de los criterios de consenso a visita
		fortalezas_consenso = FortalezasConsenso.objects.filter(evaluacion_consenso = ecc)
		areas_mejorar_consenso = AreaMejoraConsenso.objects.filter(evaluacion_consenso = ecc)

		for fortaleza in fortalezas_consenso:
			fv = FortalezasVisitaCalidad(evaluacion_visita=ev,
				criterio=fortaleza.criterio,fortalezas = fortaleza.fortalezas)
			fv.save()

		for area_mejorar in areas_mejorar_consenso:
			am = AreasMejorarVisitaCalidad(evaluacion_visita=ev,
				criterio=area_mejorar.criterio,areas_mejorar = area_mejorar.areas_mejora)
			am.save()

	def mover_datos_consenso(self):
		#Primero hay que crear la evaluacion de consenso colocando como evaluador al coordinador
		ecc = EvaluacionConsensoCalidad()
		#Para tener el listado de evaluadores de la evaluacion individual y buscar coordinador
		ge = GrupoEvaluador.objects.filter(postulacion_calidad=self.postulacion_calidad)

		#Buscando el coordinador del equipo
		eva_coor = None
		li_ids = list()
		for ev in ge:
			gend = Group.objects.get(name='individual_calidad_end')
			eva = Evaluador.objects.filter(id=ev.codigo_evaluador.id)[0]
			gend.user_set.add(eva.identificador)
			print "lista = " + str(ev.codigo_evaluador.id)
			li_ids.append(ev.codigo_evaluador.id)
			if ev.coordinador:
				#Este evaluador es el coordinador y se le deberá agregar el rol respectivo
				eva_coor = Evaluador.objects.filter(id=ev.codigo_evaluador.id)[0]
				g = Group.objects.get(name='coordinador_calidad_consenso') 
				g.user_set.add(eva_coor.identificador)
		
		ecc.postulacion_evaluacion = self.postulacion_calidad
		ecc.coordinador_postulacion = eva_coor
		ecc.save()

		caux = CriteriosCalidad.objects.all()

		#for crit in caux:
		#	ceva = CriteriosEvaluacionConsensoCalidad(evaluacion=ecc,criterio=crit)
		#	ceva.save()

		#Se obtienen las evaluaciones individuales relacionadas a la postulacion y que estan dentro del grupo evaluador excluyendo la gente que paso a lista negra
		evas_indv = EvaluacionIndividualCalidad.objects.filter(postulacion_evaluacion=self.postulacion_calidad,
			evaluador_postulacion__id__in=li_ids)

		#Se registran los aspectos claves
		aoc = AmbienteOrganizacionalConsenso(evaluacion_consenso=ecc)
		roc = RelacionesOrganizacionalesConsenso(evaluacion_consenso=ecc)
		acc=AmbienteCompetitivoConsenso(evaluacion_consenso=ecc)
		dec = DesafiosEstrategicosConsenso(evaluacion_consenso=ecc)
		smc = SistemaMejoraConsenso(evaluacion_consenso=ecc)

		for eva_indv in evas_indv:
			aoc.ambiente_organizacional = aoc.ambiente_organizacional + eva_indv.ambiente_organizacional
			roc.relaciones_organizacionales = roc.relaciones_organizacionales + eva_indv.relaciones_organizacionales
			acc.ambiente_competitivo = acc.ambiente_competitivo+eva_indv.ambiente_competitivo
			dec.desafios_estrategicos = dec.desafios_estrategicos + eva_indv.desafios_estrategicos
			smc.sistema_mejora = smc.sistema_mejora+eva_indv.sistema_mejora

		aoc.save()
		roc.save()
		acc.save()
		dec.save()
		smc.save()

		#Ahora hay que registrar todos los criterios calculando sus datos
		criterios_calidad = CriteriosCalidad.objects.all()
		for criterio_calidad in criterios_calidad:
			#Se realizan los calculos para cada uno

			listado_puntajes = PuntajeEvaluacion.objects.filter(evaluacion__in=evas_indv,criterio = criterio_calidad)
			listado_criterios_eva = CriteriosEvaluacion.objects.filter(evaluacion__in=evas_indv,criterio = criterio_calidad)
			
			listado_puntajes_totales = list()
			listado_puntajes_promedio = list()
			listado_puntajes_totales_aux = list()

			#Listado de Puntajes Totales
			for punto in listado_puntajes:
				#listado_puntajes_totales.append(punto.total)
				#Cambio realizado en base a requerimiento 07/05/2014
				listado_puntajes_totales.append(punto.promedio)
				listado_puntajes_promedio.append(punto.promedio)

				listado_puntajes_totales_aux(punto.total)

			#Listado de criterios
			f = FortalezasConsenso(evaluacion_consenso = ecc,criterio=criterio_calidad)
			am = AreaMejoraConsenso(evaluacion_consenso = ecc,criterio=criterio_calidad)
			pv = PuntosVisitaConsenso(evaluacion_consenso = ecc,criterio=criterio_calidad)
			
			for comentario in listado_criterios_eva:
				f.fortalezas = f.fortalezas + comentario.fortalezas
				am.areas_mejora = am.areas_mejora + comentario.areas_mejorar
				pv.puntos_visita = pv.puntos_visita + comentario.puntos_visita

			f.save()
			am.save()
			pv.save()

			#criterios_existentes_consenso = CriteriosEvaluacionConsensoCalidad.objects.filter(evaluacion=self.postulacion_calidad)


			#HACIENDO CALCULOS

			#Desviacion Estandar
			desv_std = self.desviacion_estandar(listado_puntajes_totales)
			mediana = 0.00

			#Calculo Mediana
			listado_puntajes_totales.sort()
                                                                                         
			if len(listado_puntajes_totales) % 2 == 0:
				n = len(listado_puntajes_totales)
				mediana = (listado_puntajes_totales[n/2-1]+ listado_puntajes_totales[n/2] )/2
			else:
				mediana =listado_puntajes_totales[len(listado_puntajes_totales)/2]

			promedio = sum(listado_puntajes_promedio)/len(listado_puntajes_promedio)
			maximo = max(listado_puntajes_totales)
			minimo = min(listado_puntajes_totales)
			rango = maximo-minimo
			puntuacion = round((promedio * criterio_calidad.puntaje_maximo) / 100,2)

			pcc = PuntajeConsensoCalidad(evaluacion_consenso=ecc,criterio = criterio_calidad,
				puntaje_maximo=criterio_calidad.puntaje_maximo,promedio = promedio,maximo=maximo,minimo=minimo,
				puntuacion = puntuacion,mediana=mediana,desviacion_estandar=desv_std,rango=rango)

			pcc.save()

class GrupoEvaluador(models.Model):
	postulacion_calidad = models.ForeignKey(PostulacionesCalidad)
	codigo_evaluador = models.ForeignKey(Evaluador)
	coordinador = models.BooleanField(help_text = "Marcar si el usuario podra ver la hoja de consenso para esta postulacion")

	def save(self, *args, **kwargs):
		
		#Verificando si existe la evaluacion individual antes creada, en caso no existir, se creara una

		eva_inv_new = EvaluacionIndividualCalidad(postulacion_evaluacion=self.postulacion_calidad,
			evaluador_postulacion=self.codigo_evaluador)

		eva_inv_new.save()

		super(GrupoEvaluador, self).save(*args, **kwargs)
		#Aca se crean las evaluaciones individuales para cada postulacion
		

	def __unicode__(self):
		return self.codigo_evaluador.codigo+'-'+self.postulacion_calidad.codigo

#END Ficha de Postulacion

#Ficha de Evaluacion Individual

class EvaluacionIndividualCalidad(models.Model):
	postulacion_evaluacion = models.ForeignKey(PostulacionesCalidad) 
	evaluador_postulacion = models.ForeignKey(Evaluador)
	#models.IntegerField(default=0,blank=False)
	nota = models.IntegerField(default=0,blank=False,validators=[MinValueValidator(0),MaxValueValidator(20),validate_fivemultiple])
	nota_global = models.IntegerField(default=0,blank=False,)
	ambiente_organizacional = HTMLField(verbose_name="A. Ambiente Organizacional",blank=True)
	relaciones_organizacionales = HTMLField(verbose_name="B. Relaciones Organizacionales",blank=True)
	ambiente_competitivo = HTMLField(verbose_name="C. Ambiente Competitivo",blank=True)
	desafios_estrategicos = HTMLField(verbose_name="D. Desafios Estrategicos",blank=True)
	sistema_mejora = HTMLField(verbose_name="E. Sistema de Mejora del Desempeno",blank=True)



	def save(self, *args, **kwargs):
		#Se verifica si es una evaluacion individual nueva contando la cantidad de criterios
		# de evaluacion ya que una evaluacion nueva, por default tiene 0 criterios
		super(EvaluacionIndividualCalidad, self).save(*args, **kwargs)
		criterios_existentes = CriteriosEvaluacion.objects.filter(evaluacion=self)

		#print str(criterios_existentes)

		if len(criterios_existentes)<1:
			# No existen criterios, por lo tanto es una evaluacion nueva
			# se debe incorporar todos los criterios que existiran por default en la ficha de evaluacion
			# individual. De igual manera se arma el listado de puntajes a llenar

			caux = CriteriosCalidad.objects.all()

			for crit in caux:
				ceva = CriteriosEvaluacion(evaluacion=self,criterio=crit)
				puntajes = PuntajeEvaluacion(evaluacion=self,criterio=crit,puntaje_maximo=crit.puntaje_maximo)
				ceva.save()
				puntajes.save()

	def guardar_cuaderno(self):
		id_postulacion = self.postulacion_evaluacion.id
		id_eva = self.evaluador_postulacion.id
		args = (str(id_postulacion),str(id_eva),)
		btn_guardar = "<a href='/archivo_individual_calidad/%s/%s'>Descargar Cuaderno Evaluación</a>" % args
		#btn_guardar = "<a href='/archivo_individual_calidad/21/4'>Descargar Cuaderno</a>"
		return btn_guardar

	guardar_cuaderno.allow_tags=True
	#def __unicode__(self):
	#	return self.evaluador_postulacion.codigo


#Para la etapa de consenso, por tema de data management se debera poder los campos HTML en una tabla separada
class EvaluacionConsensoCalidad(models.Model):
	postulacion_evaluacion = models.OneToOneField(PostulacionesCalidad) 
	coordinador_postulacion = models.ForeignKey(Evaluador)

	def __unicode__(self):
		return self.postulacion_evaluacion.codigo

	def cuaderno_consolidado(self):
		return "<a href = '/archivo_consolidado_calidad/" + str(self.postulacion_evaluacion.id)+ "' >Descargar Cuaderno Consolidado</a>"

	def informe_consenso_calidad(self):
		return "<a href = '/informe_consenso_calidad/" + str(self.id)+ "' >Informe Consenso</a>"

	def ambiente_organizacional(self):
		#TODO
		ao = AmbienteOrganizacionalConsenso.objects.filter(evaluacion_consenso=self)[0]
		return "<a href = '/admin/calidad/ambienteorganizacionalconsenso/" + str(ao.id)+ "/' onclick='return showAddAnotherPopup(this);' >A. Ambiente Organizacional</a>"

	def relaciones_organizacionales(self):
		#TODO
		ro = RelacionesOrganizacionalesConsenso.objects.filter(evaluacion_consenso=self)[0]
		return "<a href = '/admin/calidad/relacionesorganizacionalesconsenso/" + str(ro.id)+ "/' onclick='return showAddAnotherPopup(this);'>B. Relaciones Organizacionales</a>"

	def ambiente_competitivo(self):
		#TODO
		ac = AmbienteCompetitivoConsenso.objects.filter(evaluacion_consenso=self)[0]
		return "<a href = '/admin/calidad/ambientecompetitivoconsenso/" + str(ac.id)+ "/' onclick='return showAddAnotherPopup(this);'>C. Ambiente Competitivo</a>"

	def desafios_estrategicos(self):
		#TODO
		de = DesafiosEstrategicosConsenso.objects.filter(evaluacion_consenso=self)[0]
		return "<a href = '/admin/calidad/desafiosestrategicosconsenso/" + str(de.id)+ "/' onclick='return showAddAnotherPopup(this);'>D. Desafíos Estratégicos</a>"

	def sistema_mejora(self):
		#TODO
		sm = SistemaMejoraConsenso.objects.filter(evaluacion_consenso=self)[0]
		return "<a href = '/admin/calidad/sistemamejoraconsenso/" + str(sm.id)+ "/' onclick='return showAddAnotherPopup(this);'>E. Sistema de Mejora</a>"

	def hoja_puntuacion(self):
		#TODO
		return "<a href = '/puntuaciones_consenso_calidad/" + str(self.id)+ "' onclick='return showAddAnotherPopup(this);' >Hoja de Puntuación</a>"

	ambiente_organizacional.allow_tags = True
	relaciones_organizacionales.allow_tags = True
	ambiente_competitivo.allow_tags = True
	desafios_estrategicos.allow_tags = True
	sistema_mejora.allow_tags = True
	cuaderno_consolidado.allow_tags = True
	informe_consenso_calidad.allow_tags = True
	hoja_puntuacion.allow_tags = True

class CriteriosCalidad(models.Model):
	nombre = models.CharField(max_length=100,blank=False,unique=True)
	literal = models.CharField(max_length=5,blank=True)
	agrupador = models.BooleanField()
	cod_agrupador = models.CharField(max_length=2,blank=True)
	puntaje_maximo = models.IntegerField(blank=True,default=0)

	def __unicode__(self):
		return self.nombre

class FortalezasConsenso(models.Model):
	evaluacion_consenso = models.ForeignKey(EvaluacionConsensoCalidad)
	criterio = models.ForeignKey(CriteriosCalidad)
	fortalezas = HTMLField(verbose_name="Fortalezas",blank=True)

class AreaMejoraConsenso(models.Model):
	evaluacion_consenso = models.ForeignKey(EvaluacionConsensoCalidad)
	criterio = models.ForeignKey(CriteriosCalidad)
	areas_mejora = HTMLField(verbose_name=u"Áreas de Mejora",blank=True)

class PuntosVisitaConsenso(models.Model):
	evaluacion_consenso = models.ForeignKey(EvaluacionConsensoCalidad)
	criterio = models.ForeignKey(CriteriosCalidad)
	puntos_visita = HTMLField(verbose_name=u"Puntos para la Visita",blank=True)

class AmbienteOrganizacionalConsenso(models.Model):
	evaluacion_consenso = models.ForeignKey(EvaluacionConsensoCalidad)
	ambiente_organizacional = HTMLField(verbose_name=u"A. Ambiente Organizacional",blank=True)

class RelacionesOrganizacionalesConsenso(models.Model):
	evaluacion_consenso = models.ForeignKey(EvaluacionConsensoCalidad)
	relaciones_organizacionales = HTMLField(verbose_name=u"B. Relaciones Organizacionales",blank=True)

class AmbienteCompetitivoConsenso(models.Model):
	evaluacion_consenso = models.ForeignKey(EvaluacionConsensoCalidad)
	ambiente_competitivo = HTMLField(verbose_name=u"C. Ambiente Competitivo",blank=True)

class DesafiosEstrategicosConsenso(models.Model):
	evaluacion_consenso = models.ForeignKey(EvaluacionConsensoCalidad)
	desafios_estrategicos = HTMLField(verbose_name=u"D. Desafíos Estratégico",blank=True)

class SistemaMejoraConsenso(models.Model):
	evaluacion_consenso = models.ForeignKey(EvaluacionConsensoCalidad)
	sistema_mejora = HTMLField(verbose_name=u"E. Sistema de Mejora",blank=True)

class PuntajeConsensoCalidad(models.Model):
	evaluacion_consenso = models.ForeignKey(EvaluacionConsensoCalidad)
	criterio = models.ForeignKey(CriteriosCalidad)
	puntaje_maximo = models.IntegerField(blank=True,verbose_name="Puntaje Maximo (A)")
	promedio = models.DecimalField(default=0.00,max_digits=7,decimal_places=2,blank=True,verbose_name="Promedio% (B)")
	desviacion_estandar = models.DecimalField(default=0.00,max_digits=7,decimal_places=2,blank=True,verbose_name="Desv. Std")
	mediana = models.DecimalField(default=0.00,max_digits=7,decimal_places=2,blank=True,verbose_name="Mediana")
	maximo = models.DecimalField(default=0.00,max_digits=7,decimal_places=2,blank=True,verbose_name="Max")
	minimo = models.DecimalField(default=0.00,max_digits=7,decimal_places=2,blank=True,verbose_name="Min")
	rango = models.DecimalField(default=0.00,max_digits=7,decimal_places=2,blank=True,verbose_name="Rango")
	puntuacion = models.DecimalField(default=0.00,max_digits=7,decimal_places=2,blank=True,verbose_name="Puntuación (AxB)/100")
	#puntacion_consenso = models.IntegerField(default=0,blank=True,validators=[validate_fivemultiple,MinValueValidator(0),MaxValueValidator(100)],verbose_name=u"Puntuación de Consenso")
	puntacion_consenso = models.DecimalField(default=0.00,max_digits=7,decimal_places=2,blank=True,verbose_name="Puntuación de Consenso")
	puntacion_consenso_porcentual = models.IntegerField(default=0,blank=True,validators=[validate_fivemultiple,MinValueValidator(0),MaxValueValidator(100)],verbose_name=u"Puntaje Consenso(%)")
	comentario = HTMLField(verbose_name="Comentario",blank=True)

	#def save(self, *args, **kwargs):
	#	if self.validate_mymultiple2():
	#		print "entro"
	#		self.clean_fields()
	#	else:
	#		super(PuntajeConsensoCalidad, self).save(*args, **kwargs)



	def validate_mymultiple2(self):
		if self.puntacion_consenso>self.puntaje_maximo:
			return True
		else:
			return False

	def validate_maxmin(self):
		if self.puntacion_consenso_porcentual>100:
			return True
		if self.puntacion_consenso_porcentual<0:
			return True
		return False

	def validate_fivemultiple(self):
		if self.puntacion_consenso_porcentual == 0:
			return False
		if self.puntacion_consenso_porcentual % 5 != 0:
			return True
		else:
			return False

	def clean_fields(self, exclude=None):
		if self.validate_maxmin():
			raise ValidationError({'puntacion_consenso_porcentual': [u"La calificación debe ser de 0 a 100"]})
		if self.validate_fivemultiple():
			raise ValidationError({'puntacion_consenso_porcentual': [u"Colocar una calificación que sea múltiplo de 5"]})
		if self.validate_mymultiple2():
			raise ValidationError({'puntacion_consenso': [u"La puntuación de consenso debe ser entre 0 y el puntaje máximo del subcriterio (%s)" % self.puntaje_maximo]})

	def link_fortaleza_consenso_calidad(self):
		ce = FortalezasConsenso.objects.filter(evaluacion_consenso__id = self.evaluacion_consenso.id,criterio__id = self.criterio.id)[0].id
		return "<a href='/admin/calidad/fortalezasconsenso/" + str(ce) + "/' onclick='return showAddAnotherPopup(this);'>Fortalezas</a>"

	def link_area_mejora_consenso_calidad(self):
		ce = AreaMejoraConsenso.objects.filter(evaluacion_consenso__id = self.evaluacion_consenso.id,criterio__id = self.criterio.id)[0].id
		return "<a href='/admin/calidad/areamejoraconsenso/" + str(ce) + "/' onclick='return showAddAnotherPopup(this);'>Áreas de Mejora</a>"

	def link_puntos_visita_consenso_calidad(self):
		ce = PuntosVisitaConsenso.objects.filter(evaluacion_consenso__id = self.evaluacion_consenso.id,criterio__id = self.criterio.id)[0].id
		return "<a href='/admin/calidad/puntosvisitaconsenso/" + str(ce) + "/' onclick='return showAddAnotherPopup(this);'>Puntos para la Visita</a>"

	link_fortaleza_consenso_calidad.allow_tags = True
	link_fortaleza_consenso_calidad.short_description=u"Ver"
	link_area_mejora_consenso_calidad.allow_tags = True
	link_area_mejora_consenso_calidad.short_description = u"Ver"
	link_puntos_visita_consenso_calidad.allow_tags = True
	link_puntos_visita_consenso_calidad.short_description = u"Ver"
	
	#link_edicion_puntaje_consenso_calidad.verbose_name = "Enlace"


class CriteriosEvaluacion(models.Model):
	evaluacion = models.ForeignKey(EvaluacionIndividualCalidad)
	criterio = models.ForeignKey(CriteriosCalidad)
	fortalezas = HTMLField(verbose_name="Fortalezas",blank=True)
	areas_mejorar = HTMLField(verbose_name="Areas a Mejorar",blank=True)
	puntos_visita = HTMLField(verbose_name="Puntos para la Visita",blank=True)
	#enfoque = models.IntegerField(default=0,blank=True,validators=[validate_fivemultiple,MinValueValidator(0)])
	#despligue = models.IntegerField(default=0,blank=True,validators=[validate_fivemultiple,MinValueValidator(0)])
	#aprendizaje = models.IntegerField(default=0,blank=True,validators=[validate_fivemultiple,MinValueValidator(0)])
	#integracion = models.IntegerField(default=0,blank=True,validators=[validate_fivemultiple,MinValueValidator(0)])
	#promedio = models.DecimalField(default=0,max_digits=3,decimal_places=2,blank=True,validators=[validate_fivemultiple,MinValueValidator(0)])
	#total = models.DecimalField(default=0,max_digits=3,decimal_places=2,blank=True,validators=[validate_fivemultiple,MinValueValidator(0)],verbose_name="Puntuacion")

	def __unicode__(self):
		return str(self.evaluacion.id) + ' - ' + self.criterio.nombre

	def link_edicion(self):
		return "<a href='/admin/calidad/criteriosevaluacion/" + str(self.id) + "/' onclick='return showAddAnotherPopup(this);'>Fortalezas, Areas de Mejora y Puntos para la Visita</a>"

	link_edicion.allow_tags = True

class PuntajeEvaluacion(models.Model):
	evaluacion = models.ForeignKey(EvaluacionIndividualCalidad)
	criterio = models.ForeignKey(CriteriosCalidad)
	puntaje_maximo = models.IntegerField(blank=True,verbose_name="Puntaje Maximo(A)")
	enfoque = models.IntegerField(default=0,blank=True,validators=[validate_fivemultiple,MinValueValidator(0),MaxValueValidator(100)])
	despligue = models.IntegerField(default=0,blank=True,validators=[validate_fivemultiple,MinValueValidator(0),MaxValueValidator(100)])
	aprendizaje = models.IntegerField(default=0,blank=True,validators=[validate_fivemultiple,MinValueValidator(0),MaxValueValidator(100)])
	integracion = models.IntegerField(default=0,blank=True,validators=[validate_fivemultiple,MinValueValidator(0),MaxValueValidator(100)])
	promedio = models.DecimalField(default=0.00,max_digits=7,decimal_places=2,blank=True,verbose_name="Promedio(B)")
	total = models.DecimalField(default=0.00,max_digits=7,decimal_places=2,blank=True,verbose_name="Puntuacion (AxB)/100")


	#Esto sirve para prevenir que desde el cliente se esten registrando calculos modificados de forma manual
	def save(self, *args, **kwargs):

		promedio = 0.00
		total = 0.00

		puntaje_maximo = CriteriosCalidad.objects.filter(id=self.criterio.id)[0].puntaje_maximo

		suma = self.enfoque + self.despligue + self.aprendizaje + self.integracion
		promedio = suma/4.00
		total = (promedio*puntaje_maximo)/100.00

		self.promedio = round(promedio,2)
		self.total = round(total,2)

		super(PuntajeEvaluacion, self).save(*args, **kwargs)

	def link_edicion_puntaje(self):
		ce = CriteriosEvaluacion.objects.filter(evaluacion_id = self.evaluacion.id,criterio_id = self.criterio.id)[0].id
		return "<a href='/admin/calidad/criteriosevaluacion/" + str(ce) + "/' onclick='return showAddAnotherPopup(this);'>Fortalezas<br>Areas de Mejora<br>Puntos para Visita</a>"

	link_edicion_puntaje.allow_tags = True
#End Ficha de Evaluacion Individual

class CuadernosDeEvaluacion(models.Model):
	evaluacion = models.ForeignKey(EvaluacionIndividualCalidad)
	cuaderno = models.FileField(upload_to="individual",blank=False)
	fecha_subida = models.DateTimeField(auto_now=True,auto_now_add=False)
	comentario = models.CharField(max_length=350,blank=True)


class InformeConsolidadoCalidad(models.Model):
	evaluacion = models.ForeignKey(EvaluacionConsensoCalidad)
	cuaderno = models.FileField(upload_to="consenso",blank=False,max_length=500)
	fecha_subida = models.DateTimeField(auto_now=True,auto_now_add=False)
	comentario = models.CharField(max_length=350,blank=True)

	def save(self, *args, **kwargs):
		super(InformeConsolidadoCalidad, self).save(*args, **kwargs)
		postulacion = self.evaluacion.postulacion_evaluacion
		grupo = GrupoEvaluador.objects.filter(postulacion_calidad=postulacion)
		for g in grupo:
			eva = Evaluador.objects.filter(id=g.codigo_evaluador.id)[0]
			share = DocumentosCompartidosCalidad(postulacion=postulacion,evaluador=eva,documento=self.cuaderno,comentario=self.comentario)
			share.save()

#class CriteriosEvaluacionConsensoCalidad(models.Model):
	##evaluacion = models.ForeignKey(EvaluacionConsensoCalidad)
	#criterio = models.ForeignKey(CriteriosCalidad)
	#fortalezas = HTMLField(verbose_name="Fortalezas",blank=True)
	#areas_mejorar = HTMLField(verbose_name="Areas a Mejorar",blank=True)
	#puntos_visita = HTMLField(verbose_name="Puntos para la Visita",blank=True)

	#def __unicode__(self):
		#return str(self.evaluacion.id) + '-' + str(self.criterio.id)


#-------------- MEJORES PRACTICAS -------------- #

class CriteriosMejoresPracticas(models.Model):
	nombre = models.CharField(max_length=100,blank=False,unique=True)
	literal = models.CharField(max_length=5,blank=True)
	agrupador = models.BooleanField()
	cod_agrupador = models.CharField(max_length=2,blank=True)
	puntaje_maximo = models.IntegerField(blank=True,default=0)

	def __unicode__(self):
		return self.nombre


class PostulacionesMejoresPracticas(models.Model): 
	codigo = models.CharField(max_length=15,blank=False,unique=True)
	nombre = models.CharField(max_length=150,blank=False,verbose_name="Razon Social")
	direccion = models.CharField(max_length=450,blank=True,verbose_name="Direccion")
	web = models.CharField(max_length=150,blank=True,verbose_name="Direccion Web")
	telefono = models.CharField(max_length=25,blank=True,verbose_name="Telefono")
	fax = models.CharField(max_length=25,blank=True,verbose_name="Fax")
	ejecutivo = models.CharField(max_length=75,blank=True,verbose_name="Nombre")
	cargo_ejecutivo = models.CharField(max_length=175,blank=True,verbose_name="Cargo")
	telefono_ejecutivo = models.CharField(max_length=25,blank=True,verbose_name="Telefono")
	fax_ejecutivo = models.CharField(max_length=25,blank=True,verbose_name="Fax")
	email_ejecutivo = models.CharField(max_length=100,blank=True,verbose_name="Email")
	contacto_nombre = models.CharField(max_length=125,blank=True,verbose_name="Nombre")
	contacto_cargo = models.CharField(max_length=175,blank=True,verbose_name="Cargo")
	telefono_contacto = models.CharField(max_length=25,blank=True,verbose_name="Telefono")
	fax_contacto = models.CharField(max_length=25,blank=True,verbose_name="Fax")
	email_contacto = models.CharField(max_length=100,blank=True,verbose_name="Email")
	contacto_alterno = models.CharField(max_length=125,blank=True,verbose_name="Nombre")
	cargo_alterno = models.CharField(max_length=175,blank=True,verbose_name="Cargo")
	telefono_alterno = models.CharField(max_length=25,blank=True,verbose_name="Telefono")
	fax_alterno = models.CharField(max_length=25,blank=True,verbose_name="Fax")
	email_alterno = models.CharField(max_length=100,blank=True,verbose_name="Email")
	clasificacion = models.ForeignKey(TipoInstitucion)	
	representante_oficial = models.CharField(max_length=125,blank=True,verbose_name="Nombre")
	representante_cargo = models.CharField(max_length=125,blank=True,verbose_name="Cargo")
	nombre_equipo = models.CharField(max_length=300,blank=True,verbose_name="Nombre del Equipo")
	nombre_proyecto = models.CharField(max_length=300,blank=True,verbose_name="Nombre del Proyecto")
	objetivo_proyecto = HTMLField(verbose_name="Objetivos del Proyecto",blank=True)
	fecha_inicio = models.DateField(blank = True)
	fecha_fin = models.DateField(blank = True)

	def __unicode__(self):
		return self.codigo

class EvaluacionIndividualMejoresPracticas(models.Model):
	postulacion_evaluacion = models.ForeignKey(PostulacionesMejoresPracticas) 
	evaluador_postulacion = models.ForeignKey(Evaluador)
	#models.IntegerField(default=0,blank=False)
	vinculo_proyecto = HTMLField(verbose_name="A. Vinculo del Proyecto con la Estrategia Organizacional",blank=True)
	metodologia = HTMLField(verbose_name="B. Metodolodia empleada para la solucion del problema",blank=True)
	ambiente_competitivo = HTMLField(verbose_name="C. Ambiente Competitivo",blank=True)
	soporte = HTMLField(verbose_name="D. Soporte de la Alta Direccion al Proyecto",blank=True)
	resultados = HTMLField(verbose_name="E. Resultados Obtenidos",blank=True)

	def guardar_cuaderno_mp(self):
		id_postulacion = self.postulacion_evaluacion.id
		id_eva = self.evaluador_postulacion.id
		args = (str(id_postulacion),str(id_eva),)
		btn_guardar = "<a href='/archivo_individual_mp/%s/%s'>Descargar Cuaderno Evaluación</a>" % args
		#btn_guardar = "<a href='/archivo_individual_calidad/21/4'>Descargar Cuaderno</a>"
		return btn_guardar

	guardar_cuaderno_mp.allow_tags=True

	def save(self, *args, **kwargs):
		#Se verifica si es una evaluacion individual nueva contando la cantidad de criterios
		# de evaluacion ya que una evaluacion nueva, por default tiene 0 criterios
		super(EvaluacionIndividualMejoresPracticas, self).save(*args, **kwargs)
		criterios_existentes = CriteriosEvaluacionMejoresPracticas.objects.filter(evaluacion=self)

		#print str(criterios_existentes)

		if len(criterios_existentes)<1:
			# No existen criterios, por lo tanto es una evaluacion nueva
			# se debe incorporar todos los criterios que existiran por default en la ficha de evaluacion
			# individual. De igual manera se arma el listado de puntajes a llenar

			caux = CriteriosMejoresPracticas.objects.all()

			for crit in caux:
				ceva = CriteriosEvaluacionMejoresPracticas(evaluacion=self,criterio=crit)
				puntajes = PuntajeEvaluacionMejoresPracticas(evaluacion=self,criterio=crit,puntaje_maximo=crit.puntaje_maximo)
				ceva.save()
				puntajes.save()


class CriteriosEvaluacionMejoresPracticas(models.Model):
	evaluacion = models.ForeignKey(EvaluacionIndividualMejoresPracticas)
	criterio = models.ForeignKey(CriteriosMejoresPracticas)
	fortalezas = HTMLField(verbose_name="Fortalezas",blank=True)
	areas_mejorar = HTMLField(verbose_name="Areas a Mejorar",blank=True)
	puntos_visita = HTMLField(verbose_name="Puntos para la Visita",blank=True)
	#enfoque = models.IntegerField(default=0,blank=True,validators=[validate_fivemultiple,MinValueValidator(0)])
	#despligue = models.IntegerField(default=0,blank=True,validators=[validate_fivemultiple,MinValueValidator(0)])
	#aprendizaje = models.IntegerField(default=0,blank=True,validators=[validate_fivemultiple,MinValueValidator(0)])
	#integracion = models.IntegerField(default=0,blank=True,validators=[validate_fivemultiple,MinValueValidator(0)])
	#promedio = models.DecimalField(default=0,max_digits=3,decimal_places=2,blank=True,validators=[validate_fivemultiple,MinValueValidator(0)])
	#total = models.DecimalField(default=0,max_digits=3,decimal_places=2,blank=True,validators=[validate_fivemultiple,MinValueValidator(0)],verbose_name="Puntuacion")

	def __unicode__(self):
		return str(self.evaluacion.id) + ' - ' + self.criterio.nombre

	def link_edicion_mp(self):
		return "<a href='/admin/calidad/criteriosevaluacionmejorespracticas/" + str(self.id) + "/' onclick='return showAddAnotherPopup(this);'>Fortalezas, Areas de Mejora y Puntos para la Visita</a>"

	link_edicion_mp.allow_tags = True


class PuntajeEvaluacionMejoresPracticas(models.Model):
	evaluacion = models.ForeignKey(EvaluacionIndividualMejoresPracticas)
	criterio = models.ForeignKey(CriteriosMejoresPracticas)
	puntaje_maximo = models.IntegerField(blank=True,verbose_name="Puntaje Maximo(A)")
	porcentaje = models.IntegerField(default=0,blank=True,validators=[validate_fivemultiple,MinValueValidator(0),MaxValueValidator(100)],verbose_name="Porcentaje 0 a 100(B)")
	total = models.DecimalField(default=0.00,max_digits=7,decimal_places=2,blank=True,verbose_name="Puntuacion (AxB)/100")

#Esto sirve para prevenir que desde el cliente se esten registrando calculos modificados de forma manual
	def save(self, *args, **kwargs):

		procentaje = 0.00
		total = 0.00

		puntaje_maximo = CriteriosMejoresPracticas.objects.filter(id=self.criterio.id)[0].puntaje_maximo

		procentaje = self.porcentaje
		total = (procentaje*puntaje_maximo)/100.00

		#self.promedio = round(promedio,2)
		self.total = round(total,2)

		super(PuntajeEvaluacionMejoresPracticas, self).save(*args, **kwargs)

	def link_edicion_mp_puntaje(self):
		ce = CriteriosEvaluacionMejoresPracticas.objects.filter(evaluacion_id = self.evaluacion.id,criterio_id = self.criterio.id)[0].id
		return "<a href='/admin/calidad/criteriosevaluacionmejorespracticas/" + str(ce) + "/' onclick='return showAddAnotherPopup(this);'>Fortalezas, Areas de Mejora y Puntos para la Visita</a>"

	link_edicion_mp_puntaje.allow_tags = True

class GrupoEvaluadorMejoresPracticas(models.Model):
	postulacion_calidad = models.ForeignKey(PostulacionesMejoresPracticas)
	codigo_evaluador = models.ForeignKey(Evaluador)
	coordinador = models.BooleanField(help_text = "Marcar si el usuario podra ver la hoja de consenso para esta postulacion")

	def save(self, *args, **kwargs):
		
		#Verificando si existe la evaluacion individual antes creada, en caso no existir, se creara una

		eva_inv_new = EvaluacionIndividualMejoresPracticas(postulacion_evaluacion=self.postulacion_calidad,
			evaluador_postulacion=self.codigo_evaluador)

		eva_inv_new.save()

		super(GrupoEvaluadorMejoresPracticas, self).save(*args, **kwargs)
		#Aca se crean las evaluaciones individuales para cada postulacion
		

	def __unicode__(self):
		return self.codigo_evaluador.codigo+'-'+self.postulacion_calidad.codigo

#Esto es para la etapa consolidada de mejores practicas

class EstadoPostulacionMejoresPracticas(models.Model):
	postulacion_mejor_practica = models.OneToOneField(PostulacionesMejoresPracticas)
	consenso = models.BooleanField()
	visita = models.BooleanField()
	finalizado = models.BooleanField()

	def save(self, *args, **kwargs):
		#Sirve para controlar el movimiento de los datos a las distintas etapas

		#Primero se verifica si no estaba esa postulacion ya en una etapa determinada
		ep = EstadoPostulacionMejoresPracticas.objects.filter(postulacion_mejor_practica=self.postulacion_mejor_practica)
		if ep:
			#Ya existia un estado creado, ahora hay que proceder a ver de que se trataba
			if ep[0].consenso == False and self.consenso==True:
				#La postulacion no se encontraba en la etapa de consenso, y ahora se esta moviendo a esa etapa
				self.mover_datos_consenso()
			if ep[0].consenso == True and self.visita==True:
				#La postulacion Ya habia pasado la etapa de consenso y ahora se esta moviendo a la etapa de visita
				self.mover_datos_visita()
			if self.finalizado == True:
				g = Group.objects.get(name='visita_mp_end') 
				ecc = EvaluacionConsensoMejoresPracticas.objects.filter(postulacion_evaluacion=self.postulacion_mejor_practica)[0]
				g.user_set.add(ecc.coordinador_postulacion.identificador)
		else:
			#No habia un estado creado por lo que se debe ahora hacer el movimiento de datos respectivos
			if self.consenso:
				#TODO: MOVER DATOS ETAPA CONSENSO
				self.mover_datos_consenso()

		super(EstadoPostulacionMejoresPracticas, self).save(*args, **kwargs)

	def desviacion_estandar(self,valores):

		prom = (sum(valores)/len(valores))

		varianza=map(lambda x: (x - prom)**2, valores)
		prom_varianza=(sum(varianza))/len(varianza)

		return sqrt(prom_varianza)

	def mover_datos_visita(self):
		#Moviendo datos de etapa de consenso a etapa de visita
		#NOTA IMPORTANTE: para poder ejecutar esta accion, primero tiene que haber una postulacion en etapa de consenso

		#Primero hay que crear la evaluacion de visita colocando los mismos datos generales que en la etapa de consenso
		ev = EvaluacionVisitaMejoresPracticas()
		ecc = EvaluacionConsensoMejoresPracticas.objects.filter(postulacion_evaluacion=self.postulacion_mejor_practica)[0]
		ev.postulacion_evaluacion = ecc.postulacion_evaluacion
		ev.coordinador_postulacion = ecc.coordinador_postulacion
		ev.save()
		g = Group.objects.get(name='coordinador_mp_visita') 
		g.user_set.add(ev.coordinador_postulacion.identificador)
		gend = Group.objects.get(name='consenso_mp_end') 
		gend.user_set.add(ev.coordinador_postulacion.identificador)

		#Luego hay que crear la hoja de Puntuacion Respectiva moviendo la puntuacion de consenso
		puntajes = PuntajeConsensoMejoresPracticas.objects.filter(evaluacion_consenso=ecc)

		for puntaje in puntajes:
			pv = PuntajeVisitaMejoresPracticas()
			pv.evaluacion_consenso = ev
			pv.criterio = puntaje.criterio
			pv.puntaje_maximo = puntaje.puntaje_maximo
			pv.puntacion_consenso = puntaje.puntacion_consenso

			pv.save()

		#Ahora hay que mover los datos de los Aspectos Claves de Calidad de la etapa de consenso a la etapa de visita
		aoc = VinculoProyecto.objects.filter(evaluacion_consenso=ecc)[0]
		roc = Metodologia.objects.filter(evaluacion_consenso=ecc)[0]
		acc = AmbienteCompetitivo.objects.filter(evaluacion_consenso=ecc)[0]
		dec = Soporte.objects.filter(evaluacion_consenso=ecc)[0]
		smc = Resultados.objects.filter(evaluacion_consenso=ecc)[0]

		aov = VinculoProyectoVisita(evaluacion_consenso=ev,
			vinculo_proyecto=aoc.vinculo_proyecto)
		aov.save()

		rov = MetodologiaVisita(evaluacion_consenso=ev,
			metologia_proyecto=roc.metologia_proyecto)
		rov.save()

		acv = AmbienteCompetitivoVisitaMP(evaluacion_consenso=ev,
			ambiente_competitivo=acc.ambiente_competitivo)
		acv.save()

		dev = SoporteVisita(evaluacion_consenso=ev,
			soporte_direccion=dec.soporte_direccion)
		dev.save()

		smv = ResultadosVisita(evaluacion_consenso=ev,
			resultados_obtenidos=smc.resultados_obtenidos)
		smv.save()

		#Por ultimo se mueven unicamente las fortalezas y areas de mejora de los criterios de consenso a visita
		fortalezas_consenso = FortalezasConsensoMejoresPracticas.objects.filter(evaluacion_consenso = ecc)
		areas_mejorar_consenso = AreaMejoraConsensoMejoresPracticas.objects.filter(evaluacion_consenso = ecc)

		for fortaleza in fortalezas_consenso:
			fv = FortalezasVisitaMejoresPracticas(evaluacion_consenso=ev,
				criterio=fortaleza.criterio,fortalezas = fortaleza.fortalezas)
			fv.save()

		for area_mejorar in areas_mejorar_consenso:
			am = AreaMejoraVisitaMejoresPracticas(evaluacion_consenso=ev,
				criterio=area_mejorar.criterio,areas_mejora = area_mejorar.areas_mejora)
			am.save()

	def mover_datos_consenso(self):
		#Primero hay que crear la evaluacion de consenso colocando como evaluador al coordinador
		ecc = EvaluacionConsensoMejoresPracticas()
		#Para tener el listado de evaluadores de la evaluacion individual y buscar coordinador
		ge = GrupoEvaluadorMejoresPracticas.objects.filter(postulacion_calidad=self.postulacion_mejor_practica)

		#Buscando el coordinador del equipo
		eva_coor = None
		li_ids = list()
		for ev in ge:
			gend = Group.objects.get(name='individual_mp_end')
			eva = Evaluador.objects.filter(id=ev.codigo_evaluador.id)[0]
			gend.user_set.add(eva.identificador)
			li_ids.append(ev.codigo_evaluador.id)
			if ev.coordinador:
				#Este evaluador es el coordinador
				eva_coor = Evaluador.objects.filter(id=ev.codigo_evaluador.id)[0]
				g = Group.objects.get(name='coordinador_mp_consenso') 
				g.user_set.add(eva_coor.identificador)
		
		ecc.postulacion_evaluacion = self.postulacion_mejor_practica
		ecc.coordinador_postulacion = eva_coor
		ecc.save()

		caux = CriteriosMejoresPracticas.objects.all()

		#for crit in caux:
		#	ceva = CriteriosEvaluacionConsensoCalidad(evaluacion=ecc,criterio=crit)
		#	ceva.save()

		#Se obtienen las evaluaciones individuales relacionadas a la postulacion y que estan dentro del grupo evaluador excluyendo la gente que paso a lista negra
		evas_indv = EvaluacionIndividualMejoresPracticas.objects.filter(postulacion_evaluacion=self.postulacion_mejor_practica,
			evaluador_postulacion__id__in=li_ids)

		#Se registran los aspectos claves
		vin = VinculoProyecto(evaluacion_consenso=ecc)
		met = Metodologia(evaluacion_consenso=ecc)
		ac = AmbienteCompetitivo(evaluacion_consenso=ecc)
		so = Soporte(evaluacion_consenso=ecc)
		res = Resultados(evaluacion_consenso=ecc)

		for eva_indv in evas_indv:
			vin.vinculo_proyecto = vin.vinculo_proyecto + eva_indv.vinculo_proyecto
			met.metologia_proyecto = met.metologia_proyecto + eva_indv.metodologia
			ac.ambiente_competitivo = ac.ambiente_competitivo+eva_indv.ambiente_competitivo
			so.soporte_direccion = so.soporte_direccion + eva_indv.soporte
			res.resultados_obtenidos = res.resultados_obtenidos+eva_indv.resultados

		vin.save()
		met.save()
		ac.save()
		so.save()
		res.save()

		#Ahora hay que registrar todos los criterios calculando sus datos
		criterios_calidad = CriteriosMejoresPracticas.objects.all()
		for criterio_calidad in criterios_calidad:
			#Se realizan los calculos para cada uno

			listado_puntajes = PuntajeEvaluacionMejoresPracticas.objects.filter(evaluacion__in=evas_indv,criterio = criterio_calidad)
			listado_criterios_eva = CriteriosEvaluacionMejoresPracticas.objects.filter(evaluacion__in=evas_indv,criterio = criterio_calidad)
			
			listado_puntajes_totales = list()
			listado_puntajes_promedio = list()

			#Listado de Puntajes Totales
			for punto in listado_puntajes:
				#Esta modificacion se realizo en base a requerimiento que se deben de presentar los datos en base a (%) 7/05/2014
				#listado_puntajes_totales.append(punto.total)

				listado_puntajes_totales.append(punto.porcentaje)
				listado_puntajes_promedio.append(punto.porcentaje)

			#Listado de criterios
			f = FortalezasConsensoMejoresPracticas(evaluacion_consenso = ecc,criterio=criterio_calidad)
			am = AreaMejoraConsensoMejoresPracticas(evaluacion_consenso = ecc,criterio=criterio_calidad)
			pv = PuntosVisitaConsensoMejoresPracticas(evaluacion_consenso = ecc,criterio=criterio_calidad)
			
			for comentario in listado_criterios_eva:
				f.fortalezas = f.fortalezas + comentario.fortalezas
				am.areas_mejora = am.areas_mejora + comentario.areas_mejorar
				pv.puntos_visita = pv.puntos_visita + comentario.puntos_visita

			f.save()
			am.save()
			pv.save()

			#criterios_existentes_consenso = CriteriosEvaluacionConsensoCalidad.objects.filter(evaluacion=self.postulacion_calidad)


			#HACIENDO CALCULOS

			#Desviacion Estandar
			desv_std = self.desviacion_estandar(listado_puntajes_totales)
			mediana = 0.00

			#Calculo Mediana
			listado_puntajes_totales.sort()
                                                                                         
			if len(listado_puntajes_totales) % 2 == 0:
				n = len(listado_puntajes_totales)
				mediana = (listado_puntajes_totales[n/2-1]+ listado_puntajes_totales[n/2] )/2
			else:
				mediana =listado_puntajes_totales[len(listado_puntajes_totales)/2]

			promedio = sum(listado_puntajes_promedio)/len(listado_puntajes_promedio)
			maximo = max(listado_puntajes_totales)
			minimo = min(listado_puntajes_totales)
			rango = maximo-minimo
			puntuacion = round((promedio * criterio_calidad.puntaje_maximo) / 100,2)

			pcc = PuntajeConsensoMejoresPracticas(evaluacion_consenso=ecc,criterio = criterio_calidad,
				puntaje_maximo=criterio_calidad.puntaje_maximo,promedio = promedio,maximo=maximo,minimo=minimo,
				puntuacion = puntuacion,mediana=mediana,desviacion_estandar=desv_std,rango=rango)

			pcc.save()

class EvaluacionConsensoMejoresPracticas(models.Model):
	postulacion_evaluacion = models.OneToOneField(PostulacionesMejoresPracticas) 
	coordinador_postulacion = models.ForeignKey(Evaluador)

	def cuaderno_consolidado_mp(self):
		return "<a href = '/archivo_consolidado_mp/" + str(self.postulacion_evaluacion.id)+ "' >Descargar Cuaderno Consolidado</a>"

	def informe_consenso_mp(self):
		return "<a href = '/informe_consenso_mp/" + str(self.id)+ "' >Informe Consenso</a>"

	def vinculo_proyecto(self):
		#TODO
		ao = VinculoProyecto.objects.filter(evaluacion_consenso=self)[0]
		return "<a href = '/admin/calidad/vinculoproyecto/" + str(ao.id)+ "/' onclick='return showAddAnotherPopup(this);' >A. Vinculo del Proyecto con la Estrategia Organizacional</a>"

	def metodologia(self):
		#TODO
		ro = Metodologia.objects.filter(evaluacion_consenso=self)[0]
		return "<a href = '/admin/calidad/metodologia/" + str(ro.id)+ "/' onclick='return showAddAnotherPopup(this);'>B. Metodologia empleada para la solucion del problema</a>"

	def ambiente_competitivo(self):
		#TODO
		ac = AmbienteCompetitivo.objects.filter(evaluacion_consenso=self)[0]
		return "<a href = '/admin/calidad/ambientecompetitivo/" + str(ac.id)+ "/' onclick='return showAddAnotherPopup(this);'>C. Ambiente Competitivo</a>"

	def soporte(self):
		#TODO
		de = Soporte.objects.filter(evaluacion_consenso=self)[0]
		return "<a href = '/admin/calidad/soporte/" + str(de.id)+ "/' onclick='return showAddAnotherPopup(this);'>D. Soporte de la Alta Direccion al Proyecto</a>"

	def resultados(self):
		#TODO
		sm = Resultados.objects.filter(evaluacion_consenso=self)[0]
		return "<a href = '/admin/calidad/resultados/" + str(sm.id)+ "/' onclick='return showAddAnotherPopup(this);'>E. Resultados Obtenidos</a>"

	def hoja_puntuacion(self):
		#TODO
		return "<a href = '/puntuaciones_consenso_mp/" + str(self.id)+ "' onclick='return showAddAnotherPopup(this);' >Hoja de Puntuación</a>"

	vinculo_proyecto.allow_tags = True
	metodologia.allow_tags = True
	ambiente_competitivo.allow_tags = True
	soporte.allow_tags = True
	resultados.allow_tags = True
	cuaderno_consolidado_mp.allow_tags = True
	informe_consenso_mp.allow_tags = True
	hoja_puntuacion.allow_tags = True

class PuntajeConsensoMejoresPracticas(models.Model):
	evaluacion_consenso = models.ForeignKey(EvaluacionConsensoMejoresPracticas)
	criterio = models.ForeignKey(CriteriosMejoresPracticas)
	puntaje_maximo = models.IntegerField(blank=True,verbose_name="Puntaje Maximo")
	promedio = models.DecimalField(default=0.00,max_digits=7,decimal_places=2,blank=True,verbose_name="Promedio(%)")
	desviacion_estandar = models.DecimalField(default=0.00,max_digits=7,decimal_places=2,blank=True,verbose_name="Desv. Std")
	mediana = models.DecimalField(default=0.00,max_digits=7,decimal_places=2,blank=True,verbose_name="Mediana")
	maximo = models.DecimalField(default=0.00,max_digits=7,decimal_places=2,blank=True,verbose_name="Max")
	minimo = models.DecimalField(default=0.00,max_digits=7,decimal_places=2,blank=True,verbose_name="Min")
	rango = models.DecimalField(default=0.00,max_digits=7,decimal_places=2,blank=True,verbose_name="Rango")
	puntuacion = models.DecimalField(default=0.00,max_digits=7,decimal_places=2,blank=True,verbose_name="Puntuacion Consolidada")
	#puntacion_consenso = models.IntegerField(default=0,blank=True,validators=[validate_fivemultiple,MinValueValidator(0),MaxValueValidator(100)])
	puntacion_consenso = models.DecimalField(default=0.00,max_digits=7,decimal_places=2,blank=True,verbose_name="Puntuación de Consenso")
	puntacion_consenso_porcentual = models.IntegerField(default=0,blank=True,validators=[validate_fivemultiple,MinValueValidator(0),MaxValueValidator(100)],verbose_name=u"Puntuación Consenso %")
	comentario = HTMLField(verbose_name="Comentario",blank=True)

	def validate_maxmin(self):
		if self.puntacion_consenso_porcentual>100:
			return True
		if self.puntacion_consenso_porcentual<0:
			return True
		return False

	def validate_fivemultiple(self):
		if self.puntacion_consenso_porcentual == 0:
			return False
		if self.puntacion_consenso_porcentual % 5 != 0:
			return True
		else:
			return False

	def validate_mymultiple2(self):
		if self.puntacion_consenso>self.puntaje_maximo:
			return True
		else:
			return False

	def clean_fields(self, exclude=None):
		if self.validate_maxmin():
			raise ValidationError({'puntacion_consenso_porcentual': [u"La calificación debe ser de 0 a 100"]})
		if self.validate_fivemultiple():
			raise ValidationError({'puntacion_consenso_porcentual': [u"Colocar una calificación que sea múltiplo de 5"]})
		if self.validate_mymultiple2():
			raise ValidationError({'puntacion_consenso': [u"Debe colocar una puntuación de consenso entre 0 y el puntaje máximo del subcriterio (%s)" % self.puntaje_maximo]})

	def link_fortaleza_consenso_mp(self):
		ce = FortalezasConsensoMejoresPracticas.objects.filter(evaluacion_consenso__id = self.evaluacion_consenso.id,criterio__id = self.criterio.id)[0].id
		return "<a href='/admin/calidad/fortalezasconsensomejorespracticas/" + str(ce) + "/' onclick='return showAddAnotherPopup(this);'>Fortalezas</a>"

	def link_area_mejora_consenso_mp(self):
		ce = AreaMejoraConsensoMejoresPracticas.objects.filter(evaluacion_consenso__id = self.evaluacion_consenso.id,criterio__id = self.criterio.id)[0].id
		return "<a href='/admin/calidad/areamejoraconsensomejorespracticas/" + str(ce) + "/' onclick='return showAddAnotherPopup(this);'>Áreas de Mejora</a>"

	def link_puntos_visita_consenso_mp(self):
		ce = PuntosVisitaConsensoMejoresPracticas.objects.filter(evaluacion_consenso__id = self.evaluacion_consenso.id,criterio__id = self.criterio.id)[0].id
		return "<a href='/admin/calidad/puntosvisitaconsensomejorespracticas/" + str(ce) + "/' onclick='return showAddAnotherPopup(this);'>Puntos para la Visita</a>"

	link_fortaleza_consenso_mp.allow_tags = True
	link_area_mejora_consenso_mp.allow_tags = True
	link_puntos_visita_consenso_mp.allow_tags = True

#Estos son los aspectos claves a ser evaluados en la etapa de consenso de mejores practicas
class VinculoProyecto(models.Model):
	evaluacion_consenso = models.ForeignKey(EvaluacionConsensoMejoresPracticas)
	vinculo_proyecto = HTMLField(verbose_name=u"A. Vinculo del Proyecto con la Estrategia Organizacional",blank=True)

class Metodologia(models.Model):
	evaluacion_consenso = models.ForeignKey(EvaluacionConsensoMejoresPracticas)
	metologia_proyecto = HTMLField(verbose_name=u"B. Metodologia empleada para la solucion del problema",blank=True)

class AmbienteCompetitivo(models.Model):
	evaluacion_consenso = models.ForeignKey(EvaluacionConsensoMejoresPracticas)
	ambiente_competitivo = HTMLField(verbose_name=u"C. Ambiente Competitivo",blank=True)

class Soporte(models.Model):
	evaluacion_consenso = models.ForeignKey(EvaluacionConsensoMejoresPracticas)
	soporte_direccion = HTMLField(verbose_name=u"D. Soporte de la Alta Direccion al Proyecto",blank=True)

class Resultados(models.Model):
	evaluacion_consenso = models.ForeignKey(EvaluacionConsensoMejoresPracticas)
	resultados_obtenidos = HTMLField(verbose_name=u"E. Resultados Obtenidos",blank=True)

#Estos son los criterios consolidados de Mejores Practicas:

class FortalezasConsensoMejoresPracticas(models.Model):
	evaluacion_consenso = models.ForeignKey(EvaluacionConsensoMejoresPracticas)
	criterio = models.ForeignKey(CriteriosMejoresPracticas)
	fortalezas = HTMLField(verbose_name="Fortalezas",blank=True)

class AreaMejoraConsensoMejoresPracticas(models.Model):
	evaluacion_consenso = models.ForeignKey(EvaluacionConsensoMejoresPracticas)
	criterio = models.ForeignKey(CriteriosMejoresPracticas)
	areas_mejora = HTMLField(verbose_name=u"Áreas de Mejora",blank=True)

class PuntosVisitaConsensoMejoresPracticas(models.Model):
	evaluacion_consenso = models.ForeignKey(EvaluacionConsensoMejoresPracticas)
	criterio = models.ForeignKey(CriteriosMejoresPracticas)
	puntos_visita = HTMLField(verbose_name=u"Puntos para la Visita",blank=True)

class CuadernosDeEvaluacionMejoresPracticas(models.Model):
	evaluacion = models.ForeignKey(EvaluacionIndividualMejoresPracticas)
	cuaderno = models.FileField(upload_to="individual_mp",blank=False)
	fecha_subida = models.DateTimeField(auto_now=True,auto_now_add=False)
	comentario = models.CharField(max_length=350,blank=True)

class InformeConsolidadoMejoresPracticas(models.Model):
	evaluacion = models.ForeignKey(EvaluacionConsensoMejoresPracticas)
	cuaderno = models.FileField(upload_to="consenso_mp",blank=False,max_length=500)
	fecha_subida = models.DateTimeField(auto_now=True,auto_now_add=False)
	comentario = models.CharField(max_length=350,blank=True)

	def save(self, *args, **kwargs):
		super(InformeConsolidadoMejoresPracticas, self).save(*args, **kwargs)
		postulacion = self.evaluacion.postulacion_evaluacion
		grupo = GrupoEvaluadorMejoresPracticas.objects.filter(postulacion_calidad=postulacion)
		for g in grupo:
			eva = Evaluador.objects.filter(id=g.codigo_evaluador.id)[0]
			share = DocumentosCompartidosMp(postulacion=postulacion,evaluador=eva,documento=self.cuaderno,comentario=self.comentario)
			share.save()

#Etapa Visita y comentarios de revision Calidad 

class EvaluacionVisitaCalidad(models.Model):
	postulacion_evaluacion = models.OneToOneField(PostulacionesCalidad) 
	coordinador_postulacion = models.ForeignKey(Evaluador)

	def informe_visita_calidad(self):
		return "<a href = '/informe_visita_calidad/" + str(self.id)+ "' >Informe Realimentación</a>"

	informe_visita_calidad.allow_tags = True

	def ambiente_organizacional(self):
		#TODO
		ao = AmbienteOrganizacionalVisita.objects.filter(evaluacion_consenso=self)[0]
		return "<a href = '/admin/calidad/ambienteorganizacionalvisita/" + str(ao.id)+ "/' onclick='return showAddAnotherPopup(this);' >A. Ambiente Organizacional</a>"

	def relaciones_organizacionales(self):
		#TODO
		ro = RelacionesOrganizacionalesVisita.objects.filter(evaluacion_consenso=self)[0]
		return "<a href = '/admin/calidad/relacionesorganizacionalesvisita/" + str(ro.id)+ "/' onclick='return showAddAnotherPopup(this);'>B. Relaciones Organizacionales</a>"

	def ambiente_competitivo(self):
		#TODO
		ac = AmbienteCompetitivoVisita.objects.filter(evaluacion_consenso=self)[0]
		return "<a href = '/admin/calidad/ambientecompetitivovisita/" + str(ac.id)+ "/' onclick='return showAddAnotherPopup(this);'>C. Ambiente Competitivo</a>"

	def desafios_estrategicos(self):
		#TODO
		de = DesafiosEstrategicosVisita.objects.filter(evaluacion_consenso=self)[0]
		return "<a href = '/admin/calidad/desafiosestrategicosvisita/" + str(de.id)+ "/' onclick='return showAddAnotherPopup(this);'>D. Desafíos Estratégicos</a>"

	def sistema_mejora(self):
		#TODO
		sm = SistemaMejoraVisita.objects.filter(evaluacion_consenso=self)[0]
		return "<a href = '/admin/calidad/sistemamejoravisita/" + str(sm.id)+ "/' onclick='return showAddAnotherPopup(this);'>E. Sistema de Mejora</a>"

	def hoja_puntuacion(self):
		#TODO
		return "<a href = '/puntuaciones_visita_calidad/" + str(self.id)+ "' onclick='return showAddAnotherPopup(this);' >Hoja de Puntuación</a>"

	ambiente_organizacional.allow_tags = True
	relaciones_organizacionales.allow_tags = True
	ambiente_competitivo.allow_tags = True
	desafios_estrategicos.allow_tags = True
	sistema_mejora.allow_tags = True
	hoja_puntuacion.allow_tags = True

class PuntajeVisitaCalidad(models.Model):
	evaluacion = models.ForeignKey(EvaluacionVisitaCalidad)
	criterio = models.ForeignKey(CriteriosCalidad)
	puntaje_maximo = models.IntegerField(blank=True,verbose_name="Puntaje")
	#puntaje_consenso = models.IntegerField(blank=True,verbose_name="Puntaje Consenso")
	puntaje_consenso = models.DecimalField(default=0.00,max_digits=7,decimal_places=2,blank=True,verbose_name="Puntuación de Consenso")
	#puntaje_visita = models.IntegerField(default=0,blank=True,verbose_name="Puntuación Post. Visita")
	puntaje_visita = models.DecimalField(default=0.00,max_digits=7,decimal_places=2,blank=True,verbose_name="Puntuación Visita")
	puntaje_visita_porcentual = models.IntegerField(default=0,blank=True,verbose_name="Puntuación Visita %")
	comentario = HTMLField(verbose_name=u"Comentarios",blank=True)

	def validate_maxmin(self):
		if self.puntaje_visita_porcentual>100:
			return True
		if self.puntaje_visita_porcentual<0:
			return True
		return False

	def validate_fivemultiple(self):
		if self.puntaje_visita_porcentual == 0:
			return False
		if self.puntaje_visita_porcentual % 5 != 0:
			return True
		else:
			return False

	def validate_mymultiple2(self):
		if self.puntaje_visita>self.puntaje_maximo:
			return True
		else:
			return False

	def clean_fields(self, exclude=None):
		if self.validate_maxmin():
			raise ValidationError({'puntaje_visita_porcentual': [u"La calificación debe ser de 0 a 100"]})
		if self.validate_fivemultiple():
			raise ValidationError({'puntaje_visita_porcentual': [u"Colocar una calificación que sea múltiplo de 5"]})
		if self.validate_mymultiple2():
			raise ValidationError({'puntaje_visita': [u"Debe colocar una puntuación de visita entre 0 y el puntaje máximo del subcriterio (%s)" % self.puntaje_maximo]})

	def link_fortaleza_visita_calidad(self):
		ce = FortalezasVisitaCalidad.objects.filter(evaluacion_visita__id = self.evaluacion.id,criterio__id = self.criterio.id)[0].id
		return "<a href='/admin/calidad/fortalezasvisitacalidad/" + str(ce) + "/' onclick='return showAddAnotherPopup(this);'>Fortalezas</a>"

	def link_area_mejora_visita_calidad(self):
		ce = AreasMejorarVisitaCalidad.objects.filter(evaluacion_visita__id = self.evaluacion.id,criterio__id = self.criterio.id)[0].id
		return "<a href='/admin/calidad/areasmejorarvisitacalidad/" + str(ce) + "/' onclick='return showAddAnotherPopup(this);'>Áreas de Mejora</a>"

	link_fortaleza_visita_calidad.allow_tags = True
	link_area_mejora_visita_calidad.allow_tags = True

class FortalezasVisitaCalidad(models.Model):
	evaluacion_visita = models.ForeignKey(EvaluacionVisitaCalidad)
	criterio = models.ForeignKey(CriteriosCalidad)
	fortalezas = HTMLField(verbose_name=u"Fortalezas",blank=True)
	comentario_revision = HTMLField(verbose_name=u"Comentarios para Revisión",blank=True)
	aprobado = models.BooleanField(verbose_name = u"Revisado sin Comentarios",default=False)

class AreasMejorarVisitaCalidad(models.Model):
	evaluacion_visita = models.ForeignKey(EvaluacionVisitaCalidad)
	criterio = models.ForeignKey(CriteriosCalidad)
	areas_mejorar = HTMLField(verbose_name=u"Áreas a Mejorar",blank=True)
	comentario_revision = HTMLField(verbose_name=u"Comentarios para Revisión",blank=True)
	aprobado = models.BooleanField(verbose_name = u"Revisado sin Comentarios",default=False)

class AmbienteOrganizacionalVisita(models.Model):
	evaluacion_consenso = models.ForeignKey(EvaluacionVisitaCalidad)
	ambiente_organizacional = HTMLField(verbose_name=u"A. Ambiente Organizacional",blank=True)
	comentario_revision = HTMLField(verbose_name=u"Comentarios para Revisión",blank=True)
	aprobado = models.BooleanField(verbose_name = u"Revisado sin Comentarios",default=False)

class RelacionesOrganizacionalesVisita(models.Model):
	evaluacion_consenso = models.ForeignKey(EvaluacionVisitaCalidad)
	relaciones_organizacionales = HTMLField(verbose_name=u"B. Relaciones Organizacionales",blank=True)
	comentario_revision = HTMLField(verbose_name=u"Comentarios para Revisión",blank=True)
	aprobado = models.BooleanField(verbose_name = u"Revisado sin Comentarios",default=False)

class AmbienteCompetitivoVisita(models.Model):
	evaluacion_consenso = models.ForeignKey(EvaluacionVisitaCalidad)
	ambiente_competitivo = HTMLField(verbose_name=u"C. Ambiente Competitivo",blank=True)
	comentario_revision = HTMLField(verbose_name=u"Comentarios para Revisión",blank=True)
	aprobado = models.BooleanField(verbose_name = u"Revisado sin Comentarios",default=False)

class DesafiosEstrategicosVisita(models.Model):
	evaluacion_consenso = models.ForeignKey(EvaluacionVisitaCalidad)
	desafios_estrategicos = HTMLField(verbose_name=u"D. Desafíos Estratégico",blank=True)
	comentario_revision = HTMLField(verbose_name=u"Comentarios para Revisión",blank=True)
	aprobado = models.BooleanField(verbose_name = u"Revisado sin Comentarios",default=False)

class SistemaMejoraVisita(models.Model):
	evaluacion_consenso = models.ForeignKey(EvaluacionVisitaCalidad)
	sistema_mejora = HTMLField(verbose_name=u"E. Sistema de Mejora",blank=True)
	comentario_revision = HTMLField(verbose_name=u"Comentarios para Revisión",blank=True)
	aprobado = models.BooleanField(verbose_name = u"Revisado sin Comentarios",default=False)

#Etapa Visita y comentarios de revision Mejores Prácticas

class EvaluacionVisitaMejoresPracticas(models.Model):
	postulacion_evaluacion = models.OneToOneField(PostulacionesMejoresPracticas) 
	coordinador_postulacion = models.ForeignKey(Evaluador)

	def informe_realimentacion_mp(self):
		return "<a href = '/informe_visita_mp/" + str(self.id)+ "' >Informe de Realimentación</a>"

	def vinculo_proyecto(self):
		#TODO
		ao = VinculoProyectoVisita.objects.filter(evaluacion_consenso=self)[0]
		return "<a href = '/admin/calidad/vinculoproyectovisita/" + str(ao.id)+ "/' onclick='return showAddAnotherPopup(this);' >A. Vinculo del Proyecto con la Estrategia Organizacional</a>"

	def metodologia(self):
		#TODO
		ro = MetodologiaVisita.objects.filter(evaluacion_consenso=self)[0]
		return "<a href = '/admin/calidad/metodologiavisita/" + str(ro.id)+ "/' onclick='return showAddAnotherPopup(this);'>B. Metodologia empleada para la solucion del problema</a>"

	def ambiente_competitivo(self):
		#TODO
		ac = AmbienteCompetitivoVisitaMP.objects.filter(evaluacion_consenso=self)[0]
		return "<a href = '/admin/calidad/ambientecompetitivovisitamp/" + str(ac.id)+ "/' onclick='return showAddAnotherPopup(this);'>C. Ambiente Competitivo</a>"

	def soporte(self):
		#TODO
		de = SoporteVisita.objects.filter(evaluacion_consenso=self)[0]
		return "<a href = '/admin/calidad/soportevisita/" + str(de.id)+ "/' onclick='return showAddAnotherPopup(this);'>D. Soporte de la Alta Direccion al Proyecto</a>"

	def resultados(self):
		#TODO
		sm = ResultadosVisita.objects.filter(evaluacion_consenso=self)[0]
		return "<a href = '/admin/calidad/resultadosvisita/" + str(sm.id)+ "/' onclick='return showAddAnotherPopup(this);'>E. Resultados Obtenidos</a>"
	def hoja_puntuacion(self):
		#TODO
		return "<a href = '/puntuaciones_visita_mp/" + str(self.id)+ "' onclick='return showAddAnotherPopup(this);' >Hoja de Puntuación</a>"

	vinculo_proyecto.allow_tags = True
	metodologia.allow_tags = True
	ambiente_competitivo.allow_tags = True
	soporte.allow_tags = True
	resultados.allow_tags = True
	informe_realimentacion_mp.allow_tags = True
	hoja_puntuacion.allow_tags = True

class PuntajeVisitaMejoresPracticas(models.Model):
	evaluacion_consenso = models.ForeignKey(EvaluacionVisitaMejoresPracticas)
	criterio = models.ForeignKey(CriteriosMejoresPracticas)
	puntaje_maximo = models.IntegerField(blank=True,verbose_name="Puntaje Maximo")	
	#puntacion_consenso = models.IntegerField(default=0,blank=True,)
	puntacion_consenso = models.DecimalField(default=0.00,max_digits=7,decimal_places=2,blank=True,verbose_name="Puntuación de Consenso")
	#puntacion_visita = models.IntegerField(default=0,blank=True,validators=[validate_fivemultiple,MinValueValidator(0)])
	puntacion_visita = models.DecimalField(default=0.00,max_digits=7,decimal_places=2,blank=True,verbose_name="Puntuación de Visita")
	puntacion_visita_porcentual = models.IntegerField(default=0,blank=True,validators=[validate_fivemultiple,MinValueValidator(0)])
	comentario = HTMLField(verbose_name="Comentario",blank=True)

	def validate_maxmin(self):
		if self.puntacion_visita_porcentual>100:
			return True
		if self.puntacion_visita_porcentual<0:
			return True
		return False

	def validate_fivemultiple(self):
		if self.puntacion_visita_porcentual == 0:
			return False
		if self.puntacion_visita_porcentual % 5 != 0:
			return True
		else:
			return False

	def validate_mymultiple2(self):
		if self.puntacion_visita>self.puntaje_maximo:
			return True
		else:
			return False

	def clean_fields(self, exclude=None):
		if self.validate_maxmin():
			raise ValidationError({'puntacion_visita_porcentual': [u"La calificación debe ser de 0 a 100"]})
		if self.validate_fivemultiple():
			raise ValidationError({'puntacion_visita_porcentual': [u"Colocar una calificación que sea múltiplo de 5"]})
		if self.validate_mymultiple2():
			raise ValidationError({'puntacion_visita': [u"Debe colocar una puntuación de visita entre 0 y el puntaje máximo del subcriterio (%s)" % self.puntaje_maximo]})

	def link_fortaleza_consenso_mp(self):
		ce = FortalezasVisitaMejoresPracticas.objects.filter(evaluacion_consenso__id = self.evaluacion_consenso.id,criterio__id = self.criterio.id)[0].id
		return "<a href='/admin/calidad/fortalezasvisitamejorespracticas/" + str(ce) + "/' onclick='return showAddAnotherPopup(this);'>Fortalezas</a>"

	def link_area_mejora_consenso_mp(self):
		ce = AreaMejoraVisitaMejoresPracticas.objects.filter(evaluacion_consenso__id = self.evaluacion_consenso.id,criterio__id = self.criterio.id)[0].id
		return "<a href='/admin/calidad/areamejoravisitamejorespracticas/" + str(ce) + "/' onclick='return showAddAnotherPopup(this);'>Áreas de Mejora</a>"

	link_fortaleza_consenso_mp.allow_tags = True
	link_area_mejora_consenso_mp.allow_tags = True

class FortalezasVisitaMejoresPracticas(models.Model):
	evaluacion_consenso = models.ForeignKey(EvaluacionVisitaMejoresPracticas)
	criterio = models.ForeignKey(CriteriosMejoresPracticas)
	fortalezas = HTMLField(verbose_name="Fortalezas",blank=True)
	comentario_revision = HTMLField(verbose_name=u"Comentarios para Revisión",blank=True)
	aprobado = models.BooleanField(verbose_name = u"Revisado sin Comentarios",default=False)

class AreaMejoraVisitaMejoresPracticas(models.Model):
	evaluacion_consenso = models.ForeignKey(EvaluacionVisitaMejoresPracticas)
	criterio = models.ForeignKey(CriteriosMejoresPracticas)
	areas_mejora = HTMLField(verbose_name=u"Áreas de Mejora",blank=True)
	comentario_revision = HTMLField(verbose_name=u"Comentarios para Revisión",blank=True)
	aprobado = models.BooleanField(verbose_name = u"Revisado sin Comentarios",default=False)

class VinculoProyectoVisita(models.Model):
	evaluacion_consenso = models.ForeignKey(EvaluacionVisitaMejoresPracticas)
	vinculo_proyecto = HTMLField(verbose_name=u"A. Vinculo del Proyecto con la Estrategia Organizacional",blank=True)
	comentario_revision = HTMLField(verbose_name=u"Comentarios para Revisión",blank=True)
	aprobado = models.BooleanField(verbose_name = u"Revisado sin Comentarios",default=False)

class MetodologiaVisita(models.Model):
	evaluacion_consenso = models.ForeignKey(EvaluacionVisitaMejoresPracticas)
	metologia_proyecto = HTMLField(verbose_name=u"B. Metodologia empleada para la solucion del problema",blank=True)
	comentario_revision = HTMLField(verbose_name=u"Comentarios para Revisión",blank=True)
	aprobado = models.BooleanField(verbose_name = u"Revisado sin Comentarios",default=False)

class AmbienteCompetitivoVisitaMP(models.Model):
	evaluacion_consenso = models.ForeignKey(EvaluacionVisitaMejoresPracticas)
	ambiente_competitivo = HTMLField(verbose_name=u"C. Ambiente Competitivo",blank=True)
	comentario_revision = HTMLField(verbose_name=u"Comentarios para Revisión",blank=True)
	aprobado = models.BooleanField(verbose_name = u"Revisado sin Comentarios",default=False)

class SoporteVisita(models.Model):
	evaluacion_consenso = models.ForeignKey(EvaluacionVisitaMejoresPracticas)
	soporte_direccion = HTMLField(verbose_name=u"D. Soporte de la Alta Direccion al Proyecto",blank=True)
	comentario_revision = HTMLField(verbose_name=u"Comentarios para Revisión",blank=True)
	aprobado = models.BooleanField(verbose_name = u"Revisado sin Comentarios",default=False)

class ResultadosVisita(models.Model):
	evaluacion_consenso = models.ForeignKey(EvaluacionVisitaMejoresPracticas)
	resultados_obtenidos = HTMLField(verbose_name=u"E. Resultados Obtenidos",blank=True)
	comentario_revision = HTMLField(verbose_name=u"Comentarios para Revisión",blank=True)
	aprobado = models.BooleanField(verbose_name = u"Revisado sin Comentarios",default=False)

class InformeVisitaMejoresPracticas(models.Model):
	evaluacion = models.ForeignKey(EvaluacionVisitaMejoresPracticas)
	cuaderno = models.FileField(upload_to="visita_mp",blank=False,max_length=500)
	fecha_subida = models.DateTimeField(auto_now=True,auto_now_add=False)
	comentario = models.CharField(max_length=350,blank=True)

	def save(self, *args, **kwargs):
		super(InformeVisitaMejoresPracticas, self).save(*args, **kwargs)
		postulacion = self.evaluacion.postulacion_evaluacion
		grupo = GrupoEvaluadorMejoresPracticas.objects.filter(postulacion_calidad=postulacion)
		for g in grupo:
			eva = Evaluador.objects.filter(id=g.codigo_evaluador.id)[0]
			share = DocumentosCompartidosMp(postulacion=postulacion,evaluador=eva,documento=self.cuaderno,comentario=self.comentario)
			share.save()

class TestVisitaMejoresPracticas(models.Model):
	evaluacion = models.ForeignKey(EvaluacionVisitaMejoresPracticas)
	cuaderno = models.FileField(upload_to="visita_mp",blank=False,max_length=500)
	fecha_subida = models.DateTimeField(auto_now=True,auto_now_add=False)
	comentario = models.CharField(max_length=350,blank=True)

#Compartir Documentos
class DocumentosCompartidosCalidad(models.Model):
	postulacion = models.ForeignKey(PostulacionesCalidad)
	evaluador = models.ForeignKey(Evaluador)
	documento = models.FileField(upload_to="shared_files",blank=True,max_length=500)
	comentario = models.CharField(max_length=350,blank=True)
	fecha_subida = models.DateTimeField(auto_now=True,auto_now_add=False)

	documento.allow_tags = True

class DocumentosCompartidosMp(models.Model):
	postulacion = models.ForeignKey(PostulacionesMejoresPracticas)
	evaluador = models.ForeignKey(Evaluador)
	documento = models.FileField(upload_to="shared_files",blank=True,max_length=500)
	comentario = models.CharField(max_length=350,blank=True)
	fecha_subida = models.DateTimeField(auto_now=True,auto_now_add=False)


class PanelDeAyuda(models.Model):
	evaluador = models.ForeignKey(User)
	asunto = models.CharField(max_length=350,verbose_name=u"Asunto",blank = False)
	caso = HTMLField(verbose_name=u"Resumen de la consulta o problema",blank=False)
	adjunto = models.FileField(upload_to="panel_ayuda",blank=True,max_length=500)
	fecha = models.DateTimeField(auto_now=True,auto_now_add=False)
	estado_caso = models.BooleanField(verbose_name=u"Caso Resuelto")

	def __unicode__(self):
		return self.asunto

class RespuestasDeAyuda(models.Model):
	caso = models.ForeignKey(PanelDeAyuda)
	respuesta = HTMLField(verbose_name=u"Resumen de la consulta o problema",blank=False)
	fecha = models.DateTimeField(auto_now=True,auto_now_add=False)