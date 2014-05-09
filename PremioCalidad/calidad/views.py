# -*- coding: utf-8 -*- 
from django.shortcuts import render
import json

from django.shortcuts import render_to_response
from django.http import HttpResponse, Http404
from django.template import RequestContext
from calidad.models import EvaluacionIndividualCalidad,CriteriosEvaluacion,PostulacionesCalidad,CriteriosCalidad,GrupoEvaluador
from calidad.models import EvaluacionConsensoCalidad,FortalezasConsenso,AreaMejoraConsenso,PuntosVisitaConsenso,AmbienteOrganizacionalConsenso
from calidad.models import RelacionesOrganizacionalesConsenso,AmbienteCompetitivoConsenso,DesafiosEstrategicosConsenso,SistemaMejoraConsenso
from calidad.models import PuntajeConsensoCalidad,PuntajeEvaluacion

from calidad.models import EstadoPostulacionMejoresPracticas, EvaluacionConsensoMejoresPracticas, PuntajeConsensoMejoresPracticas
from calidad.models import VinculoProyecto, Metodologia, AmbienteCompetitivo, Soporte, Resultados
from calidad.models import FortalezasConsensoMejoresPracticas, AreaMejoraConsensoMejoresPracticas, PuntosVisitaConsensoMejoresPracticas

from calidad.models import EvaluacionIndividualMejoresPracticas,PuntajeEvaluacionMejoresPracticas,CriteriosEvaluacionMejoresPracticas
from calidad.models import CriteriosMejoresPracticas,PostulacionesMejoresPracticas,GrupoEvaluadorMejoresPracticas

from calidad.models import EvaluacionVisitaCalidad,PuntajeVisitaCalidad
from calidad.models import FortalezasVisitaCalidad,AreasMejorarVisitaCalidad
from calidad.models import AmbienteOrganizacionalVisita,RelacionesOrganizacionalesVisita,AmbienteCompetitivoVisita,DesafiosEstrategicosVisita,SistemaMejoraVisita


from calidad.models import EvaluacionVisitaMejoresPracticas,PuntajeVisitaMejoresPracticas
from calidad.models import FortalezasVisitaMejoresPracticas,AreaMejoraVisitaMejoresPracticas
from calidad.models import VinculoProyectoVisita,MetodologiaVisita,AmbienteCompetitivoVisitaMP,SoporteVisita,ResultadosVisita

import time

def puntuaciones_consenso_calidad(request,id_eva_consenso):
	
	puntajes_totales_calidad = list()
	puntajes_totales_calidad_consenso = list()

	criterios_calidad = CriteriosCalidad.objects.all()
	eva_consenso = EvaluacionConsensoCalidad.objects.filter(id = id_eva_consenso)[0]

	#Protección de generación de esta página
	if request.user.username != eva_consenso.coordinador_postulacion.identificador.username:
		#El usuario NO es el evaluador designado para este proceso por lo que no debe poder generar el archivo
		# O tampoco tiene permisos de responsable de proceso
		if  not request.user.groups.filter(name='responsables_proceso').exists():
			response = HttpResponse(u"<html lang='es'><head><meta charset='utf-8'></head><body><h2>No tienes los permisos requeridos para generar el archivo, esto es debido a que no eres el coordinador designado para esta hoja de evaluación</h2></body></html>")
			return response

	ge = GrupoEvaluador.objects.filter(postulacion_calidad__id=eva_consenso.postulacion_evaluacion.id)

	documento = u"<html lang='es'><head><meta charset='utf-8' />"
	documento = documento +"<style>tr:nth-child(odd){background:#99FFCC;} tr:nth-child(even){background:#FFFFCC;}</style>"
	documento = documento + u"</head><body><center><header><h2>Detalle Puntuación Consolidada</h2>"
	documento = documento + u"<table style='border:1px solid black;text-align:center;'><tr><th>Criterio</th><th> Punt. Max (A)</th>"

	for eva in ge:
		documento = documento+u"<th>"+eva.codigo_evaluador.codigo+"</th>"

	documento = documento+u"<th>Promedio% (B)</th>"
	documento = documento+u"<th>Desv. Stand</th>"
	documento = documento+u"<th>Mediana</th>"
	documento = documento+u"<th>Max</th>"
	documento = documento+u"<th>Min</th>"
	documento = documento+u"<th>Rango</th>"
	documento = documento+u"<th>Puntuación (AXB)/100</th>"
	documento = documento+u"<th>Puntuación Consenso</th></tr>"

	for criterio in criterios_calidad:
		
		puntaje_consenso = PuntajeConsensoCalidad.objects.filter(evaluacion_consenso=eva_consenso,criterio=criterio)[0]
		#Obteniendo los puntajes individuales para los criterios
		documento = documento + "<tr><td>"+criterio.nombre+"</td><td>"+str(criterio.puntaje_maximo)+"</td>"
		for eva in ge:
			eva_individual = EvaluacionIndividualCalidad.objects.filter(evaluador_postulacion=eva.codigo_evaluador,
				postulacion_evaluacion__codigo=eva_consenso.postulacion_evaluacion.codigo)[0]
			puntaje_total_individual = PuntajeEvaluacion.objects.filter(criterio=criterio,evaluacion=eva_individual)[0]
			if not criterio.agrupador:
				#documento = documento + "<td>"+str(puntaje_total_individual.total)+" <br>(" + str(puntaje_total_individual.promedio) +"%)</td>"
				documento = documento + "<td>"+str(puntaje_total_individual.promedio) +"</td>"
			else:
				documento = documento + "<td>---</td>"

		if not criterio.agrupador:
			documento = documento + "<td>"+str(puntaje_consenso.promedio)+"</td>"
			documento = documento + "<td>"+str(puntaje_consenso.desviacion_estandar)+"</td>"
			documento = documento + "<td>"+str(puntaje_consenso.mediana)+"</td>"
			documento = documento + "<td>"+str(puntaje_consenso.maximo)+"</td>"
			documento = documento + "<td>"+str(puntaje_consenso.minimo)+"</td>"
			documento = documento + "<td>"+str(puntaje_consenso.rango)+"</td>"
			documento = documento + "<td>"+str(puntaje_consenso.puntuacion)+"</td>"
			documento = documento + "<td>"+str(puntaje_consenso.puntacion_consenso)+"</td>"
			documento = documento + "</tr>"
			puntajes_totales_calidad.append(puntaje_consenso.puntuacion)
			puntajes_totales_calidad_consenso.append(puntaje_consenso.puntacion_consenso)
		else:
			documento = documento + "<td><strong>---</strong></td>"
			documento = documento + "<td><strong>---</strong></td>"
			documento = documento + "<td><strong>---</strong></td>"
			documento = documento + "<td><strong>---</strong></td>"
			documento = documento + "<td><strong>---</strong></td>"
			documento = documento + "<td><strong>---</strong></td>"
			#Se debera de sumar el puntaje de los subcriterios
			criterios_agrupados = CriteriosCalidad.objects.filter(agrupador=False,cod_agrupador=criterio.cod_agrupador)
			caids = list()
			puntos = list()
			puntos_consenso = list()
			for cr in criterios_agrupados:
				caids.append(cr.id)
			
			puntajes_criterio_agrupado = PuntajeConsensoCalidad.objects.filter(evaluacion_consenso=eva_consenso,criterio__in=caids)
			for p in puntajes_criterio_agrupado:
				puntos.append(p.puntuacion)
				puntos_consenso.append(p.puntacion_consenso)

			documento = documento + "<td><strong>"+str(sum(puntos))+"</strong></td>"
			documento = documento + "<td><strong>"+str(sum(puntos_consenso))+"</strong></td>"
		
		documento = documento + "</tr>"

	
	columnas = 8 + len(ge)	
	documento = documento + "<tr><td colspan='"+str(columnas)+"'><strong><h3>TOTAL</h3></strong></td>"
	
	documento = documento + "<td><strong style='color:red;'><h3><u>"+str(sum(puntajes_totales_calidad)) + "</u></h3></strong></td>"
	documento = documento + "<td><strong style='color:red;'><h3><u>"+str(sum(puntajes_totales_calidad_consenso)) + "</u></h3></strong></td></tr>"
	documento = documento + "</table>"


	documento = documento+u"</center></html>"
	#response = HttpResponse(documento,content_type='text/html; charset=utf-8')
	response = HttpResponse(documento)
	#response['Content-Disposition'] = 'attachment; filename=%s.doc' % nombre_archivo
	return response

def puntuaciones_visita_calidad(request,id_eva_consenso):
	
	puntajes_totales_calidad = list()
	puntajes_totales_calidad_consenso = list()

	criterios_calidad = CriteriosCalidad.objects.all()
	eva_consenso = EvaluacionVisitaCalidad.objects.filter(id = id_eva_consenso)[0]

	#Protección de generación de esta página
	if request.user.username != eva_consenso.coordinador_postulacion.identificador.username:
		#El usuario NO es el evaluador designado para este proceso por lo que no debe poder generar el archivo
		# O tampoco tiene permisos de responsable de proceso
		if  not request.user.groups.filter(name='responsables_proceso').exists():
			response = HttpResponse(u"<html lang='es'><head><meta charset='utf-8'></head><body><h2>No tienes los permisos requeridos para generar el archivo, esto es debido a que no eres el coordinador designado para esta hoja de evaluación</h2></body></html>")
			return response

	documento = u"<html lang='es'><head><meta charset='utf-8' />"
	documento = documento +"<style>tr:nth-child(odd){background:#99FFCC;} tr:nth-child(even){background:#FFFFCC;}</style>"
	documento = documento + u"</head><body><center><header><h2>Detalle Puntuación Visita</h2>"
	documento = documento + u"<table style='border:1px solid black;text-align:center;'><tr><th>Criterio</th><th> Punt. Max (A)</th><th>Puntuación Consenso</th><th>Puntuación Visita % (B)</th><th>Puntuación de Visita (AxB)/100</th></tr>"


	for criterio in criterios_calidad:
		
		puntaje_consenso = PuntajeVisitaCalidad.objects.filter(evaluacion=eva_consenso,criterio=criterio)[0]
		#Obteniendo los puntajes individuales para los criterios
		documento = documento + "<tr><td>"+criterio.nombre+"</td><td>"+str(criterio.puntaje_maximo)+"</td>"

		if not criterio.agrupador:
			documento = documento + "<td>"+str(puntaje_consenso.puntaje_consenso)+"</td>"
			documento = documento + "<td>"+str(puntaje_consenso.puntaje_visita_porcentual)+"</td>"
			documento = documento + "<td>"+str(puntaje_consenso.puntaje_visita)+"</td>"
			documento = documento + "</tr>"
			#puntajes_totales_calidad.append(puntaje_consenso.puntuacion)
			#puntajes_totales_calidad_consenso.append(puntaje_consenso.puntacion_consenso)
		else:
			#documento = documento + "<td><strong>---</strong></td>"
			#documento = documento + "<td><strong>---</strong></td>"
			#Se debera de sumar el puntaje de los subcriterios
			criterios_agrupados = CriteriosCalidad.objects.filter(agrupador=False,cod_agrupador=criterio.cod_agrupador)
			caids = list()
			puntos = list()
			puntos_consenso = list()
			for cr in criterios_agrupados:
				caids.append(cr.id)
			
			puntajes_criterio_agrupado = PuntajeVisitaCalidad.objects.filter(evaluacion=eva_consenso,criterio__in=caids)
			for p in puntajes_criterio_agrupado:
				puntos.append(p.puntaje_visita)
				puntos_consenso.append(p.puntaje_consenso)
				puntajes_totales_calidad_consenso.append(p.puntaje_consenso)
				puntajes_totales_calidad.append(p.puntaje_visita)

			documento = documento + "<td><strong>"+str(sum(puntos_consenso))+"</strong></td>"
			documento = documento + "<td><strong>---</strong></td>"
			documento = documento + "<td><strong>"+str(sum(puntos))+"</strong></td>"
			
		
		documento = documento + "</tr>"

	
	columnas = 5
	documento = documento + "<tr><td colspan='2'><strong><h3>TOTALES</h3></strong></td>"
	
	documento = documento + "<td><strong style='color:red;'><h3><u>"+str(sum(puntajes_totales_calidad_consenso)) + "</u></h3></strong></td>"
	documento = documento + "<td><strong>---</strong></td>"
	documento = documento + "<td><strong style='color:red;'><h3><u>"+str(sum(puntajes_totales_calidad)) + "</u></h3></strong></td></tr>"
	
	documento = documento + "</table>"


	documento = documento+u"</center></html>"
	#response = HttpResponse(documento,content_type='text/html; charset=utf-8')
	response = HttpResponse(documento)
	#response['Content-Disposition'] = 'attachment; filename=%s.doc' % nombre_archivo
	return response

def informe_consenso_calidad(request,id_eva_consenso):
	#TODO, poner la proteccion a nivel de usuario que puede generar el documento
	documento = u"<html lang='es'><head><meta charset='utf-8' /></head><body><center><header><h2>INFORME DE CONSENSO</h2>"
	documento = documento + u"<p>&nbsp;</p>"
	documento = documento + u"<p>&nbsp;</p>"
	documento = documento + u"<p>&nbsp;</p>"
	documento = documento + u"<h2>2014</h2>"
	documento = documento + u"<p>&nbsp;</p>"
	documento = documento + u"<p>&nbsp;</p>"
	documento = documento + u"<p>&nbsp;</p>"
	documento = documento + u"<p>&nbsp;</p>"
	documento = documento + u'<h2>OFICINA ADMINISTRADORA DEL PREMIO <br>"ES Calidad"</h2>'
	documento = documento + u"<p>&nbsp;</p>"
	documento = documento + u"<p>&nbsp;</p>"
	documento = documento + u"<p>&nbsp;</p>"
	documento = documento + u"<p>&nbsp;</p>"
	documento = documento + u"<p>&nbsp;</p>"
	documento = documento + u"<p>&nbsp;</p>"
	documento = documento + u"<p>&nbsp;</p>"
	documento = documento + u'<h2>INFORME DE CONSENSO</h2>'
	documento = documento + u"<p>&nbsp;</p>"
	documento = documento + u"<p>&nbsp;</p>"
	documento = documento + u"<p>&nbsp;</p>"
	documento = documento + u'<h2>MODELO SALVADOREÑO PARA UNA GESTIÓN DE EXCELENCIA</h2></header></center>'
	
	#Datos Generales
	codigo_postulacion = EvaluacionConsensoCalidad.objects.filter(id=id_eva_consenso)[0].postulacion_evaluacion.codigo

	#Protección de Generación del archivo
	eva_consenso = EvaluacionConsensoCalidad.objects.filter(id = id_eva_consenso)[0]
	if request.user.username != eva_consenso.coordinador_postulacion.identificador.username:
		#El usuario NO es el evaluador designado para este proceso por lo que no debe poder generar el archivo
		# O tampoco tiene permisos de responsable de proceso
		if  not request.user.groups.filter(name='responsables_proceso').exists():
			response = HttpResponse(u"<html lang='es'><head><meta charset='utf-8'></head><body><h2>No tienes los permisos requeridos para generar el archivo, esto es debido a que no eres el coordinador designado para esta hoja de evaluación</h2></body></html>")
			return response

	nombre_archivo = "Informe_Consenso_"+codigo_postulacion+"_"+time.strftime("%x")
	grupo_evaluador = GrupoEvaluador.objects.filter(postulacion_calidad__codigo=codigo_postulacion)

	documento = documento + u"<center><table style='border-spacing:0;border-collapse: separate;'><tr><td><strong>Código de Postulación:</strong></td><td>"+codigo_postulacion+"</td></tr>"
	documento = documento + u"<tr><td><strong>Integrantes del Equipo:</strong></td><td>"

	for eva in grupo_evaluador:
		documento = documento + u""+eva.codigo_evaluador.codigo+u" " +eva.codigo_evaluador.identificador.first_name + " " + eva.codigo_evaluador.identificador.last_name + "<br>"

	documento = documento + u"" + "</td></tr></table></center>"

	documento = documento + u"<h3 style='width:80%;font-weight:bold;background:gray;'>Hoja de Factores Claves</h3><br>"
	documento = documento + u"<span style='width:80%;font-size:12px;'>Código de Postulación: "+codigo_postulacion+"</span><hr>"

	#Aspectos Claves
	ambiente_organizacional = AmbienteOrganizacionalConsenso.objects.filter(evaluacion_consenso__id = id_eva_consenso)[0].ambiente_organizacional
	relaciones_organizacionales = RelacionesOrganizacionalesConsenso.objects.filter(evaluacion_consenso__id = id_eva_consenso)[0].relaciones_organizacionales
	ambiente_competitivo = AmbienteCompetitivoConsenso.objects.filter(evaluacion_consenso__id = id_eva_consenso)[0].ambiente_competitivo
	desafios_estrategicos = DesafiosEstrategicosConsenso.objects.filter(evaluacion_consenso__id = id_eva_consenso)[0].desafios_estrategicos
	sistema_mejora = SistemaMejoraConsenso.objects.filter(evaluacion_consenso__id = id_eva_consenso)[0].sistema_mejora

	documento = documento + u"<h3>A. Ambiente Organizacional</h3>"
	documento = documento + u""+ambiente_organizacional
	documento = documento + u"<h3>B. Relaciones Organizacionales</h3>"
	documento = documento + u""+relaciones_organizacionales
	documento = documento + u"<h3>C. Ambiente Competitivo</h3>"
	documento = documento + u""+ambiente_competitivo
	documento = documento + u"<h3>D. Desafíos Estratégicos</h3>"
	documento = documento + u""+desafios_estrategicos
	documento = documento + u"<h3>E. Sistema de Mejora del Desempeño</h3>"
	documento = documento + u""+sistema_mejora

	documento = documento + u"<h3 style='width:80%;font-weight:bold;background:gray;'>Hoja de Temas Claves</h3>"
	documento = documento + u"<span style='width:80%;font-size:12px;'>Código de Postulación: "+codigo_postulacion+"</span>"
	documento = documento + u"<p style='font-size:12px;text-align:justify'>La Hoja de Temas Clave provee un resumen global de los aspectos claves de la evaluación de una postulación. También permite un análisis de los temas claves a ser examinados tanto en la Etapa de Consenso como en la Visita en Terreno. Estos temas deben ser presentados a nivel de Criterio, y deben cruzar todo el informe, o referirse a los Valores y Conceptos Fundamentales del Modelo de Excelencia."
	documento = documento + u" La Hoja de Temas Clave debe responder a las siguientes tres preguntas:"
	documento = documento + u" a. ¿Cuáles son las fortalezas o prácticas sobresalientes más importantes (de potencial valor para otras organizaciones) identificadas?"
	documento = documento + u" b. ¿Cuáles son las inquietudes, debilidades o vulnerabilidades más significantes identificadas?"
	documento = documento + u" c. ¿Considerando los factores claves de la organización postulante, cuáles son las fortalezas, vulnerabilidades y/o brechas más significativas (datos, comparaciones, vínculos) encontrados en sus resultados?</p><hr>"

	documento = documento + u"<span style='width:80%;font-weight:bold;background:gray;'>Hoja de Criterios</span><hr>"

	criterios = CriteriosCalidad.objects.all()

	for criterio in criterios:
		fortalezas_consenso = FortalezasConsenso.objects.filter(evaluacion_consenso__id=id_eva_consenso,criterio=criterio)[0].fortalezas
		areas_mejora_consenso = AreaMejoraConsenso.objects.filter(evaluacion_consenso__id=id_eva_consenso,criterio=criterio)[0].areas_mejora
		puntos_visita_consenso = PuntosVisitaConsenso.objects.filter(evaluacion_consenso__id=id_eva_consenso,criterio=criterio)[0].puntos_visita

		documento = documento + u"<h3 style='width:80%;font-weight:bold;background:gray;'>"+criterio.nombre+"</h3>"
		documento = documento + u"<h3'><i><u>Fortalezas</u></i></h3>"
		documento = documento + u""+fortalezas_consenso
		documento = documento + u"<h3'><i><u>Áreas a Mejorar</u></i></h3>"
		documento = documento + u""+areas_mejora_consenso
		documento = documento + u"<h3'><i><u>Puntos para la Visita</u></i></h3>"
		documento = documento + u""+puntos_visita_consenso

	documento = documento + '</body></html>'

	response = HttpResponse(documento,content_type='application/vnd.ms-word; charset=utf-8')
	response['Content-Disposition'] = 'attachment; filename=%s.doc' % nombre_archivo
	return response


def archivo_consolidado_calidad(request,id_postulacion):
	
	#Protección de Generación del archivo
	eva_consenso = EvaluacionConsensoCalidad.objects.filter(postulacion_evaluacion__id = id_postulacion)[0]
	if request.user.username != eva_consenso.coordinador_postulacion.identificador.username:
		#El usuario NO es el evaluador designado para este proceso por lo que no debe poder generar el archivo
		# O tampoco tiene permisos de responsable de proceso
		if  not request.user.groups.filter(name='responsables_proceso').exists():
			response = HttpResponse(u"<html lang='es'><head><meta charset='utf-8'></head><body><h2>No tienes los permisos requeridos para generar el archivo, esto es debido a que no eres el coordinador designado para esta hoja de evaluación</h2></body></html>")
			return response

	postulacion = PostulacionesCalidad.objects.filter(id = id_postulacion)

	ge = GrupoEvaluador.objects.filter(postulacion_calidad__id=id_postulacion)
	li_ids = list()

	for ev in ge:
		li_ids.append(ev.codigo_evaluador.id)

	coordinador = GrupoEvaluador.objects.filter(postulacion_calidad__id=id_postulacion,coordinador=True)

	datos = EvaluacionIndividualCalidad.objects.filter(postulacion_evaluacion__id = id_postulacion,evaluador_postulacion__id__in=li_ids)

	tabla_datos = u"<center><table style='border:1px solid black;border-spacing:0;border-collapse:collapse;width:70%;'><tr style='border:1px solid black;'><td style='border:1px solid black;'>Código de Postulación</td><td style='border:1px solid black;'>" + postulacion[0].codigo + "</td></tr>"
	tabla_datos = tabla_datos + u"<tr style='border:1px solid black;'><td style='border:1px solid black;'>Coordinador</td><td style='border:1px solid black;'>" +u""+ coordinador[0].codigo_evaluador.codigo + " " + u""+ coordinador[0].codigo_evaluador.identificador.first_name + " " +  coordinador[0].codigo_evaluador.identificador.last_name + "</td></tr>"
	tabla_datos = tabla_datos + "<tr style='border:1px solid black;'><td style='border:1px solid black;'>Evaluadores</td><td style='border:1px solid black;'>"

	for dato in datos:
		tabla_datos = tabla_datos + dato.evaluador_postulacion.codigo +u" "+dato.evaluador_postulacion.identificador.first_name+u" "+dato.evaluador_postulacion.identificador.last_name+"<br>"
	tabla_datos = tabla_datos + "</td></tr></table></center>"

	nombre_archivo = u"C_Eva_PSC_Consolidado_" +postulacion[0].codigo+"_"+time.strftime("%x")
	documento = u"<html><head><title>SayHey</title><meta charset='utf-8' /></head><body><center><h1 style='align:center;'>CUADERNO DE EVALUACIÓN CONSOLIDADO PREMIO SALVADOREÑO A LA CALIDAD</h1></center>"

	documento = documento + tabla_datos
	criterios_evaluacion = u""
	ambiente_organizacional = u""
	relaciones_organizacionales = u""
	ambiente_competitivo = u""
	desafios_estrategicos = u""
	sistema_mejora = u""

	for dato in datos:
		#criterios_evaluacion = criterios_evaluacion+CriteriosEvaluacion.objects.filter(evaluacion__id = dato.id)

		ambiente_organizacional = ambiente_organizacional+dato.ambiente_organizacional
		relaciones_organizacionales = relaciones_organizacionales+dato.relaciones_organizacionales
		ambiente_competitivo = ambiente_competitivo+dato.ambiente_competitivo
		desafios_estrategicos = desafios_estrategicos+dato.desafios_estrategicos
		sistema_mejora = sistema_mejora+dato.sistema_mejora

	documento = documento + u"<h2>ASPECTOS CLAVE</h2><hr />"
	documento = documento + u"<h3><i>A. Ambiente Organizacional</i></h3>"+u""+ambiente_organizacional
	documento = documento + u"<h3><i>B. Relaciones Organizacionales</i></h3>"+u""+ relaciones_organizacionales
	documento = documento + u"<h3><i>C. Ambiente Competitivo</i></h3>"+u""+ ambiente_competitivo
	documento = documento + u"<h3><i>D. Desafíos Estratégicos</i></h3>"+u""+ desafios_estrategicos
	documento = documento + u"<h3><i>E. Sistema de Mejora del Desempeño</i></h3>"+u""+ sistema_mejora

	documento = documento + u"<h2>CRITERIOS</h2><hr />"

	criterios_calidad = CriteriosCalidad.objects.all()

	for criterio_calidad in criterios_calidad:
		documento = documento + "<h3>"+u"" + criterio_calidad.nombre + "</h3>"

		fortalezas = u""
		areas_mejorar = u""
		puntos_visita = u""

		for dato in datos:	
			criterios_evaluacion = CriteriosEvaluacion.objects.filter(evaluacion__id=dato.id,criterio=criterio_calidad)

			for criterio_evaluacion in criterios_evaluacion:
				fortalezas = fortalezas + criterio_evaluacion.fortalezas
				areas_mejorar = areas_mejorar + criterio_evaluacion.areas_mejorar
				puntos_visita = puntos_visita + criterio_evaluacion.puntos_visita

		documento = documento + "<h3><i>Fortalezas</i></h3>"
		documento = documento +u""+ fortalezas
		documento = documento +u"<h3><i>Áreas a Mejorar</i></h3>"
		documento = documento +u""+ areas_mejorar
		documento = documento +u"<h3><i>Puntos para la Visita</i></h3>"
		documento = documento +u"" + puntos_visita

	documento = documento + '</body></html>'

	response = HttpResponse(documento,content_type='application/vnd.ms-word; charset=utf-8')
	response['Content-Disposition'] = 'attachment; filename=%s.doc' % nombre_archivo
	return response


def archivo_individual_calidad(request,id_postulacion,id_evaluador):
	
	
	#Seguridad de Usuario para la generación del cuaderno individual
	usuario_session = request.user.username
	datos = EvaluacionIndividualCalidad.objects.filter(postulacion_evaluacion__id = id_postulacion,evaluador_postulacion__id=id_evaluador)

	if request.user.username != datos[0].evaluador_postulacion.identificador.username:
		#El usuario NO es el evaluador designado para este proceso por lo que no debe poder generar el archivo
		# O tampoco tiene permisos de responsable de proceso
		if  not request.user.groups.filter(name='responsables_proceso').exists():
			response = HttpResponse(u"<html lang='es'><head><meta charset='utf-8'></head><body><h2>No tienes los permisos requeridos para generar el archivo, esto es debido a que no eres el evaluador designado para esta hoja de evaluación</h2></body></html>")
			return response


	criterios_evaluacion = CriteriosEvaluacion.objects.filter(evaluacion__id = datos[0].id)

	nombre_evaluador = request.user.first_name + request.user.last_name
	nombre_archivo = u"C_Eva_Individual_PSC_" + nombre_evaluador +"_"+  time.strftime("%x")

	ambiente_organizacional = datos[0].ambiente_organizacional
	relaciones_organizacionales = datos[0].relaciones_organizacionales
	ambiente_competitivo = datos[0].ambiente_competitivo
	desafios_estrategicos = datos[0].desafios_estrategicos
	sistema_mejora = datos[0].sistema_mejora

	documento = u"<html><head><title>PSC</title><meta charset='utf-8' /></head><body><center><h1>CUADERNO DE EVALUACIÓN INDIVIDUAL PREMIO SALVADOREÑO A LA CALIDAD</h1></center>"
	documento = documento + u"<h2>ASPECTOS CLAVE</h2><hr />"
	documento = documento + u"<h3><i>A. Ambiente Organizacional</i></h3>"+u""+ambiente_organizacional
	documento = documento + u"<h3><i>B. Relaciones Organizacionales</i></h3>"+u""+ relaciones_organizacionales
	documento = documento + u"<h3><i>C. Ambiente Competitivo</i></h3>"+u""+ ambiente_competitivo
	documento = documento + u"<h3><i>D. Desafíos Estratégicos</i></h3>"+u""+ desafios_estrategicos
	documento = documento + u"<h3><i>E. Sistema de Mejora del Desempeño</i></h3>"+u""+ sistema_mejora

	documento = documento + u"<h2>CRITERIOS</h2><hr />"

	for criterio in criterios_evaluacion:
		documento = documento + "<h3>"+u"" + criterio.criterio.nombre + "</h3>"
		documento = documento + "<h3><i>Fortalezas</i></h3>"
		documento = documento +u""+ criterio.fortalezas
		documento = documento +u"<h3><i>Áreas a Mejorar</i></h3>"
		documento = documento +u""+ criterio.areas_mejorar
		documento = documento +u"<h3><i>Puntos para la Visita</i></h3>"
		documento = documento +u"" + criterio.puntos_visita
	
	documento = documento + '</body></html>'

	response = HttpResponse(documento,content_type='application/vnd.ms-word; charset=utf-8')
	response['Content-Disposition'] = 'attachment; filename=%s.doc' % nombre_archivo
	return response

#Informes Mejores Prácticas: 

def archivo_individual_mp(request,id_postulacion,id_evaluador):
	
	#Protección para generación del archivo
	datos = EvaluacionIndividualMejoresPracticas.objects.filter(postulacion_evaluacion__id = id_postulacion,evaluador_postulacion__id=id_evaluador)	

	if request.user.username != datos[0].evaluador_postulacion.identificador.username:
		#El usuario NO es el evaluador designado para este proceso por lo que no debe poder generar el archivo
		# O tampoco tiene permisos de responsable de proceso
		if  not request.user.groups.filter(name='responsables_proceso').exists():
			response = HttpResponse(u"<html lang='es'><head><meta charset='utf-8'></head><body><h2>No tienes los permisos requeridos para generar el archivo, esto es debido a que no eres el evaluador designado para esta hoja de evaluación</h2></body></html>")
			return response

	criterios_evaluacion = CriteriosEvaluacionMejoresPracticas.objects.filter(evaluacion__id = datos[0].id)

	nombre_evaluador = request.user.first_name + request.user.last_name
	nombre_archivo = u"C_Eva_Individual_RMP_" + nombre_evaluador +"_"+  time.strftime("%x")

	vinculo_proyecto = datos[0].vinculo_proyecto
	metodologia = datos[0].metodologia
	ambiente_competitivo = datos[0].ambiente_competitivo
	soporte = datos[0].soporte
	resultados = datos[0].resultados

	documento = u"<html><head><title>RMP</title><meta charset='utf-8' /></head><body><center><h1>CUADERNO DE EVALUACIÓN INDIVIDUAL RECONOCIMIENTO A LAS MEJORES PRÁCTICAS</h1></center>"
	documento = documento + u"<h2>ASPECTOS CLAVE</h2><hr />"
	documento = documento + u"<h3><i>A. Vinculo del Proyecto con la Estrategia Organizacional</i></h3>"+u""+vinculo_proyecto
	documento = documento + u"<h3><i>B. Metodolodia empleada para la solucion del problema</i></h3>"+u""+ metodologia
	documento = documento + u"<h3><i>C. Ambiente Competitivo</i></h3>"+u""+ ambiente_competitivo
	documento = documento + u"<h3><i>D. Soporte de la Alta Direccion al Proyecto</i></h3>"+u""+ soporte
	documento = documento + u"<h3><i>E. Resultados Obtenidos</i></h3>"+u""+ resultados

	documento = documento + u"<h2>CRITERIOS</h2><hr />"

	for criterio in criterios_evaluacion:
		documento = documento + "<h3>"+u"" + criterio.criterio.nombre + "</h3>"
		documento = documento + "<h3><i>Fortalezas</i></h3>"
		documento = documento +u""+ criterio.fortalezas
		documento = documento +u"<h3><i>Áreas a Mejorar</i></h3>"
		documento = documento +u""+ criterio.areas_mejorar
		documento = documento +u"<h3><i>Puntos para la Visita</i></h3>"
		documento = documento +u"" + criterio.puntos_visita
	
	documento = documento + '</body></html>'

	response = HttpResponse(documento,content_type='application/vnd.ms-word; charset=utf-8')
	response['Content-Disposition'] = 'attachment; filename=%s.doc' % nombre_archivo
	return response


def archivo_consolidado_mp(request,id_postulacion):
	#Protección de Generación del archivo
	eva_consenso = EvaluacionConsensoMejoresPracticas.objects.filter(postulacion_evaluacion = id_postulacion)[0]
	if request.user.username != eva_consenso.coordinador_postulacion.identificador.username:
		#El usuario NO es el evaluador designado para este proceso por lo que no debe poder generar el archivo
		# O tampoco tiene permisos de responsable de proceso
		if  not request.user.groups.filter(name='responsables_proceso').exists():
			response = HttpResponse(u"<html lang='es'><head><meta charset='utf-8'></head><body><h2>No tienes los permisos requeridos para generar el archivo, esto es debido a que no eres el coordinador designado para esta hoja de evaluación</h2></body></html>")
			return response

	postulacion = PostulacionesMejoresPracticas.objects.filter(id = id_postulacion)

	ge = GrupoEvaluadorMejoresPracticas.objects.filter(postulacion_calidad__id=id_postulacion)
	li_ids = list()

	for ev in ge:
		li_ids.append(ev.codigo_evaluador.id)

	coordinador = GrupoEvaluadorMejoresPracticas.objects.filter(postulacion_calidad__id=id_postulacion,coordinador=True)

	datos = EvaluacionIndividualMejoresPracticas.objects.filter(postulacion_evaluacion__id = id_postulacion,evaluador_postulacion__id__in=li_ids)

	tabla_datos = u"<center><table style='border:1px solid black;border-spacing:0;border-collapse:collapse;width:70%;'><tr style='border:1px solid black;'><td style='border:1px solid black;'>Código de Postulación</td><td style='border:1px solid black;'>" + postulacion[0].codigo + "</td></tr>"
	tabla_datos = tabla_datos + u"<tr style='border:1px solid black;'><td style='border:1px solid black;'>Coordinador</td><td style='border:1px solid black;'>" +u""+ coordinador[0].codigo_evaluador.codigo + " " + u""+ coordinador[0].codigo_evaluador.identificador.first_name + " " +  coordinador[0].codigo_evaluador.identificador.last_name + "</td></tr>"
	tabla_datos = tabla_datos + "<tr style='border:1px solid black;'><td style='border:1px solid black;'>Evaluadores</td><td style='border:1px solid black;'>"

	for dato in datos:
		tabla_datos = tabla_datos + dato.evaluador_postulacion.codigo +u" "+dato.evaluador_postulacion.identificador.first_name+u" "+dato.evaluador_postulacion.identificador.last_name+"<br>"
	tabla_datos = tabla_datos + "</td></tr></table></center>"

	nombre_archivo = u"C_Eva_RMP_Consolidado_" +postulacion[0].codigo+"_"+time.strftime("%x")
	documento = u"<html><head><title>SayHey</title><meta charset='utf-8' /></head><body><center><h1 style='align:center;'>CUADERNO DE EVALUACIÓN CONSOLIDADO RECONOCIMIENTO A LAS MEJORES PRÁCTICAS</h1></center>"

	documento = documento + tabla_datos
	criterios_evaluacion = u""
	vinculo_proyecto = u""
	metodologia = u""
	ambiente_competitivo = u""
	soporte = u""
	resultados = u""

	for dato in datos:
		#criterios_evaluacion = criterios_evaluacion+CriteriosEvaluacion.objects.filter(evaluacion__id = dato.id)

		vinculo_proyecto = vinculo_proyecto+dato.vinculo_proyecto
		metodologia = metodologia+dato.metodologia
		ambiente_competitivo = ambiente_competitivo+dato.ambiente_competitivo
		soporte = soporte+dato.soporte
		resultados = resultados+dato.resultados

	documento = documento + u"<h2>ASPECTOS CLAVE</h2><hr />"
	documento = documento + u"<h3><i>A. Vinculo del Proyecto con la Estrategia Organizacional</i></h3>"+u""+vinculo_proyecto
	documento = documento + u"<h3><i>B. Metodolodia empleada para la solucion del problema</i></h3>"+u""+ metodologia
	documento = documento + u"<h3><i>C. Ambiente Competitivo</i></h3>"+u""+ ambiente_competitivo
	documento = documento + u"<h3><i>D. Soporte de la Alta Direccion al Proyecto</i></h3>"+u""+ soporte
	documento = documento + u"<h3><i>E. Resultados Obtenidos</i></h3>"+u""+ resultados

	documento = documento + u"<h2>CRITERIOS</h2><hr />"

	criterios_calidad = CriteriosMejoresPracticas.objects.all()

	for criterio_calidad in criterios_calidad:
		documento = documento + "<h3>"+u"" + criterio_calidad.nombre + "</h3>"

		fortalezas = u""
		areas_mejorar = u""
		puntos_visita = u""

		for dato in datos:	
			criterios_evaluacion = CriteriosEvaluacionMejoresPracticas.objects.filter(evaluacion__id=dato.id,criterio=criterio_calidad)

			for criterio_evaluacion in criterios_evaluacion:
				fortalezas = fortalezas + criterio_evaluacion.fortalezas
				areas_mejorar = areas_mejorar + criterio_evaluacion.areas_mejorar
				puntos_visita = puntos_visita + criterio_evaluacion.puntos_visita

		documento = documento + "<h3><i>Fortalezas</i></h3>"
		documento = documento +u""+ fortalezas
		documento = documento +u"<h3><i>Áreas a Mejorar</i></h3>"
		documento = documento +u""+ areas_mejorar
		documento = documento +u"<h3><i>Puntos para la Visita</i></h3>"
		documento = documento +u"" + puntos_visita

	documento = documento + '</body></html>'

	response = HttpResponse(documento,content_type='application/vnd.ms-word; charset=utf-8')
	response['Content-Disposition'] = 'attachment; filename=%s.doc' % nombre_archivo
	return response

def informe_consenso_mp(request,id_eva_consenso):
	eva_consenso = EvaluacionConsensoMejoresPracticas.objects.filter(id = id_eva_consenso)[0]

	#Protección de generación de esta página
	if request.user.username != eva_consenso.coordinador_postulacion.identificador.username:
		#El usuario NO es el evaluador designado para este proceso por lo que no debe poder generar el archivo
		# O tampoco tiene permisos de responsable de proceso
		if  not request.user.groups.filter(name='responsables_proceso').exists():
			response = HttpResponse(u"<html lang='es'><head><meta charset='utf-8'></head><body><h2>No tienes los permisos requeridos para generar el archivo, esto es debido a que no eres el coordinador designado para esta hoja de evaluación</h2></body></html>")
			return response

	documento = u"<html lang='es'><head><meta charset='utf-8' />"
	documento = documento + u"<style>"
	documento = documento + u"#columnas-personalizadas"
	documento = documento + u"{width:500px;margin:0 auto;}"
	documento = documento + u"#izquierda"
	documento = documento + u"{width:220px;}"
	documento = documento + u"#derecha"
	documento = documento + u"{width:220px;}"
	documento = documento + u"#izquierda,#derecha"
	documento = documento + u"{display:inline-block;}"
	documento = documento + u"</style>"
	documento = documento + u"</head><body><center><header><h2>INFORME DE CONSENSO</h2>"
	documento = documento + u"<p>&nbsp;</p>"
	documento = documento + u"<p>&nbsp;</p>"
	documento = documento + u"<p>&nbsp;</p>"
	documento = documento + u"<h2>2014</h2>"
	documento = documento + u"<p>&nbsp;</p>"
	documento = documento + u"<p>&nbsp;</p>"
	documento = documento + u"<p>&nbsp;</p>"
	documento = documento + u"<p>&nbsp;</p>"
	documento = documento + u'<h2>OFICINA ADMINISTRADORA DEL PREMIO <br>"ES Calidad"</h2>'
	documento = documento + u"<p>&nbsp;</p>"
	documento = documento + u"<p>&nbsp;</p>"
	documento = documento + u"<p>&nbsp;</p>"
	documento = documento + u"<p>&nbsp;</p>"
	documento = documento + u"<p>&nbsp;</p>"
	documento = documento + u"<p>&nbsp;</p>"
	documento = documento + u"<p>&nbsp;</p>"
	documento = documento + u'<h2>INFORME DE CONSENSO</h2>'
	documento = documento + u"<p>&nbsp;</p>"
	documento = documento + u"<p>&nbsp;</p>"
	documento = documento + u"<p>&nbsp;</p>"
	documento = documento + u'<h2>MODELO SALVADOREÑO PARA UNA GESTIÓN DE EXCELENCIA</h2></header></center>'
	
	#Datos Generales
	codigo_postulacion = EvaluacionConsensoMejoresPracticas.objects.filter(id=id_eva_consenso)[0].postulacion_evaluacion.codigo
	nombre_archivo = "Informe_Consenso_"+codigo_postulacion+"_"+time.strftime("%x")
	grupo_evaluador = GrupoEvaluadorMejoresPracticas.objects.filter(postulacion_calidad__codigo=codigo_postulacion)

	documento = documento + u"<center><table style='border-spacing:0;border-collapse: separate;'><tr><td><strong>Código de Postulación:</strong></td><td>"+codigo_postulacion+"</td></tr>"
	documento = documento + u"<tr><td><strong>Integrantes del Equipo:</strong></td><td>"

	for eva in grupo_evaluador:
		documento = documento + u""+eva.codigo_evaluador.codigo+u" " +eva.codigo_evaluador.identificador.first_name + " " + eva.codigo_evaluador.identificador.last_name + "<br>"


	documento = documento + u"" + "</td></tr></table></center>"

	documento = documento + u"<h3 style='width:80%;font-weight:bold;background:gray;'>Introducción e Instrucciones Generales</h3><br>"
	documento = documento + u"<section id='columnas-personalizadas' style='border:1px solid black;'>"

	documento = documento + u"<article id='izquierda'>"
	documento = documento + u"<p><h3>Introducción</h3> El presente Cuaderno de Evaluación proporciona a los evaluadores un conciso, organizado y estandarizado método para registrar sus comentarios y puntuación en el proceso de evaluación de las organizaciones postulantes al Reconocimiento a las Mejores Prácticas.</p>"
	documento = documento + u"<p>En la primera etapa de evaluación, este Cuaderno es usado para registrar los hallazgos de los evaluadores en forma individual. En la evaluación en consenso y en la visita en terreno, el Cuaderno de Evaluación es usado para registrar los hallazgos del equipo de evaluación. Un proceso sugerido para completar el Cuaderno de Evaluación ilustra un método sistemático para evaluar postulaciones.</p>"
	documento = documento + u"<p><h3>Puntualidad</h3> La cooperación de los evaluadores en ceñirse a las fechas previstas en el proceso de evaluación, en cada una de sus etapas, es crítica para el éxito del Reconocimiento.</p>"
	documento = documento + u"<p><h3>Confidencialidad</h3> El Informe de Postulación, el Cuaderno de Evaluación, todas las notas, los archivos en computadoras, y cualquier otra información relacionada con la postulación constituyen información altamente confidencial. <strong>Los evaluadores deben cuidar de no llevar a cabo su evaluación en presencia de otras personas ni dejar algún documento relacionado con la organización postulante en lugares en los que otras personas pueden tener acceso.</strong> </p>"
	documento = documento + u"<p><h3>Llenado y Devolución del Informe de Evaluación – Evaluación Individual </h3>Los evaluadores deben utilizar el procesador de textos MS Word para completar sus Cuadernos de Evaluación. Es importante además que los evaluadores: </p>"
	documento = documento + u"</article>"

	documento = documento + u"<article id='derecha'>"
	documento = documento + u"<ol>"
	documento = documento + u"<li>Usen el formato de Cuaderno de Evaluación proporcionado por la Oficina Administradora del Premio “ES Calidad” y no otro que pudiera ser creado. Ello incluye la utilización de la Hoja de Aspectos Clave, todas las Hojas para la evaluación de Subcriterios, la Hoja Resumen de Puntuación, la Lista de Verificación y la Declaración de Conflictos de Interés.</li>"
	documento = documento + u"<li>Preparen todas las Hojas del Cuaderno de Evaluación en MS Word utilizando el tipo de letra Arial, 10 pts.</li>"
	documento = documento + u"<li>Verifiquen que todas las Hojas de Subcriterios estén completas y se encuentren correctamente compaginadas.</li>"
	documento = documento + u"<li>Registren correctamente las puntuaciones en el Cuaderno de Evaluación.</li>"
	documento = documento + u"<li>Lean la Lista de Verificación.</li>"
	documento = documento + u"<li>Lean y firmen la Declaración de Conflictos de Interés.</li>"
	documento = documento + u"<li>Complete y devuelva por vía electrónica el Cuaderno de Evaluación debidamente llenado a la Oficina Administradora del Premio “ES Calidad”. Dicho Cuaderno debe incluir lo siguiente:"
	documento = documento + u"<ul><li>Carátula</li><li>Hoja de Aspectos Clave</li><li> Una Hoja de Subcriterio por cada Subcriterio</li><li> Hoja Resumen de Evaluación</li><li> Lista de Verificación y Declaración de Conflictos de Interés firmados</li><li> Clave del postulante</li></ul></li>"
	documento = documento + u"</ol>"
	documento = documento + u"</article>"

	documento = documento + u"</section>"

	documento = documento + u"<h3 style='width:80%;font-weight:bold;background:gray;'>Aspectos Claves</h3><br>"
	documento = documento + u"<span style='width:80%;font-size:12px;'>Código de Postulación: "+codigo_postulacion+"</span><hr>"		
	documento = documento + u"<p style='font-size:12px;text-align:justify'>Para iniciar un proceso de evaluación, revise el Perfil del Proyecto del postulante. Liste los Aspectos Clave "
	documento = documento + u"de la organización usando los encabezados en el orden que se presentan a continuación"

	#Aspectos Claves
	vinculo_proyecto = VinculoProyecto.objects.filter(evaluacion_consenso__id = id_eva_consenso)[0].vinculo_proyecto
	metodologia = Metodologia.objects.filter(evaluacion_consenso__id = id_eva_consenso)[0].metologia_proyecto
	ambiente_competitivo = AmbienteCompetitivo.objects.filter(evaluacion_consenso__id = id_eva_consenso)[0].ambiente_competitivo
	soporte = Soporte.objects.filter(evaluacion_consenso__id = id_eva_consenso)[0].soporte_direccion
	resultados = Resultados.objects.filter(evaluacion_consenso__id = id_eva_consenso)[0].resultados_obtenidos

	documento = documento + u"<h3>A. Vinculo del Proyecto con la Estrategia Organizacional</h3>"
	documento = documento + u""+vinculo_proyecto
	documento = documento + u"<h3>B. Metodologia empleada para la solucion del problema</h3>"
	documento = documento + u""+metodologia
	documento = documento + u"<h3>C. Ambiente Competitivo</h3>"
	documento = documento + u""+ambiente_competitivo
	documento = documento + u"<h3>D. Soporte de la Alta Dirección al Proyecto</h3>"
	documento = documento + u""+soporte
	documento = documento + u"<h3>E. Resultados Obtenidos</h3>"
	documento = documento + u""+resultados

	documento = documento + u"<h3 style='width:80%;font-weight:bold;background:gray;'>Criterios</h3>"

	documento = documento + u"<hr>"

	criterios = CriteriosMejoresPracticas.objects.all()

	for criterio in criterios:
		fortalezas_consenso = FortalezasConsensoMejoresPracticas.objects.filter(evaluacion_consenso__id=id_eva_consenso,criterio=criterio)[0].fortalezas
		areas_mejora_consenso = AreaMejoraConsensoMejoresPracticas.objects.filter(evaluacion_consenso__id=id_eva_consenso,criterio=criterio)[0].areas_mejora
		puntos_visita_consenso = PuntosVisitaConsensoMejoresPracticas.objects.filter(evaluacion_consenso__id=id_eva_consenso,criterio=criterio)[0].puntos_visita

		documento = documento + u"<h3 style='width:80%;font-weight:bold;background:gray;'>"+criterio.nombre+"</h3>"
		documento = documento + u"<h3'><i><u>Fortalezas</u></i></h3>"
		documento = documento + u""+fortalezas_consenso
		documento = documento + u"<h3'><i><u>Áreas a Mejorar</u></i></h3>"
		documento = documento + u""+areas_mejora_consenso
		documento = documento + u"<h3'><i><u>Puntos para la Visita</u></i></h3>"
		documento = documento + u""+puntos_visita_consenso

	documento = documento + '</body></html>'

	response = HttpResponse(documento,content_type='application/vnd.ms-word; charset=utf-8')
	#response = HttpResponse(documento,content_type='application/html; charset=utf-8')
	#response = HttpResponse(documento)
	response['Content-Disposition'] = 'attachment; filename=%s.doc' % nombre_archivo
	return response


def puntuaciones_consenso_mp(request,id_eva_consenso):
	
	eva_consenso = EvaluacionConsensoMejoresPracticas.objects.filter(id = id_eva_consenso)[0]

	#Protección de generación de esta página
	if request.user.username != eva_consenso.coordinador_postulacion.identificador.username:
		#El usuario NO es el evaluador designado para este proceso por lo que no debe poder generar el archivo
		# O tampoco tiene permisos de responsable de proceso
		if  not request.user.groups.filter(name='responsables_proceso').exists():
			response = HttpResponse(u"<html lang='es'><head><meta charset='utf-8'></head><body><h2>No tienes los permisos requeridos para generar el archivo, esto es debido a que no eres el coordinador designado para esta hoja de evaluación</h2></body></html>")
			return response

	puntajes_totales_calidad = list()
	puntajes_totales_calidad_consenso = list()

	criterios_calidad = CriteriosMejoresPracticas.objects.all()
	eva_consenso = EvaluacionConsensoMejoresPracticas.objects.filter(id = id_eva_consenso)[0]
	ge = GrupoEvaluadorMejoresPracticas.objects.filter(postulacion_calidad__id=eva_consenso.postulacion_evaluacion.id)

	documento = u"<html lang='es'><head><meta charset='utf-8' />"
	documento = documento +"<style>tr:nth-child(odd){background:#99FFCC;} tr:nth-child(even){background:#FFFFCC;}</style>"
	documento = documento + u"</head><body><center><header><h2>Detalle Puntuación Consolidada</h2>"
	documento = documento + u"<table style='border:1px solid black;text-align:center;'><tr><th>Criterio</th><th> Punt. Max (A)</th>"

	for eva in ge:
		documento = documento+u"<th>"+eva.codigo_evaluador.codigo+"</th>"

	documento = documento+u"<th>Promedio% (B)</th>"
	documento = documento+u"<th>Desv. Stand</th>"
	documento = documento+u"<th>Mediana</th>"
	documento = documento+u"<th>Max</th>"
	documento = documento+u"<th>Min</th>"
	documento = documento+u"<th>Rango</th>"
	documento = documento+u"<th>Puntuación (AxB)/100</th>"
	documento = documento+u"<th>Puntuación Consenso</th></tr>"

	for criterio in criterios_calidad:
		
		puntaje_consenso = PuntajeConsensoMejoresPracticas.objects.filter(evaluacion_consenso=eva_consenso,criterio=criterio)[0]
		#Obteniendo los puntajes individuales para los criterios
		documento = documento + "<tr><td>"+criterio.nombre+"</td><td>"+str(criterio.puntaje_maximo)+"</td>"
		for eva in ge:
			eva_individual = EvaluacionIndividualMejoresPracticas.objects.filter(evaluador_postulacion=eva.codigo_evaluador,
				postulacion_evaluacion__codigo=eva_consenso.postulacion_evaluacion.codigo)[0]
			puntaje_total_individual = PuntajeEvaluacionMejoresPracticas.objects.filter(criterio=criterio,evaluacion=eva_individual)[0]
			if not criterio.agrupador:
				#Cambio realizado en base a requerimiento 7/05/2014, se pidio manejar los valores de los evaluadores con % 07/05/2014
				#documento = documento + "<td>"+str(puntaje_total_individual.total)+" <br>(" + str(puntaje_total_individual.porcentaje) +"%)</td>"
				documento = documento + "<td>"+str(puntaje_total_individual.porcentaje) +"</td>"
			else:
				documento = documento + "<td>---</td>"

		if not criterio.agrupador:
			documento = documento + "<td>"+str(puntaje_consenso.promedio)+"</td>"
			documento = documento + "<td>"+str(puntaje_consenso.desviacion_estandar)+"</td>"
			documento = documento + "<td>"+str(puntaje_consenso.mediana)+"</td>"
			documento = documento + "<td>"+str(puntaje_consenso.maximo)+"</td>"
			documento = documento + "<td>"+str(puntaje_consenso.minimo)+"</td>"
			documento = documento + "<td>"+str(puntaje_consenso.rango)+"</td>"
			documento = documento + "<td>"+str(puntaje_consenso.puntuacion)+"</td>"
			documento = documento + "<td>"+str(puntaje_consenso.puntacion_consenso)+"</td>"
			documento = documento + "</tr>"
			puntajes_totales_calidad.append(puntaje_consenso.puntuacion)
			puntajes_totales_calidad_consenso.append(puntaje_consenso.puntacion_consenso)
		else:
			documento = documento + "<td><strong>---</strong></td>"
			documento = documento + "<td><strong>---</strong></td>"
			documento = documento + "<td><strong>---</strong></td>"
			documento = documento + "<td><strong>---</strong></td>"
			documento = documento + "<td><strong>---</strong></td>"
			documento = documento + "<td><strong>---</strong></td>"
			#Se debera de sumar el puntaje de los subcriterios
			criterios_agrupados = CriteriosMejoresPracticas.objects.filter(agrupador=False,cod_agrupador=criterio.cod_agrupador)
			caids = list()
			puntos = list()
			for cr in criterios_agrupados:
				caids.append(cr.id)
			
			puntajes_criterio_agrupado = PuntajeConsensoMejoresPracticas.objects.filter(evaluacion_consenso=eva_consenso,criterio__in=caids)
			for p in puntajes_criterio_agrupado:
				puntos.append(p.puntuacion)

			documento = documento + "<td><strong>"+str(sum(puntos))+"</strong></td>"
			documento = documento + "<td><strong>---</strong></td>"
		
		documento = documento + "</tr>"

	
	columnas = 8 + len(ge)	
	documento = documento + "<tr><td colspan='"+str(columnas)+"'><strong><h3>TOTAL</h3></strong></td>"
	
	documento = documento + "<td><strong style='color:red;'><h3><u>"+str(sum(puntajes_totales_calidad)) + "</u></h3></strong></td>"
	documento = documento + "<td><strong style='color:red;'><h3><u>"+str(sum(puntajes_totales_calidad_consenso)) + "</u></h3></strong></td></tr>"
	documento = documento + "</table>"


	documento = documento+u"</center></html>"
	#response = HttpResponse(documento,content_type='text/html; charset=utf-8')
	response = HttpResponse(documento)
	#response['Content-Disposition'] = 'attachment; filename=%s.doc' % nombre_archivo
	return response

def puntuaciones_visita_mp(request,id_eva_consenso):
	
	puntajes_totales_calidad = list()
	puntajes_totales_calidad_consenso = list()

	criterios_calidad = CriteriosMejoresPracticas.objects.all()
	eva_consenso = EvaluacionVisitaMejoresPracticas.objects.filter(id = id_eva_consenso)[0]

	#Protección de generación de esta página
	if request.user.username != eva_consenso.coordinador_postulacion.identificador.username:
		#El usuario NO es el evaluador designado para este proceso por lo que no debe poder generar el archivo
		# O tampoco tiene permisos de responsable de proceso
		if  not request.user.groups.filter(name='responsables_proceso').exists():
			response = HttpResponse(u"<html lang='es'><head><meta charset='utf-8'></head><body><h2>No tienes los permisos requeridos para generar el archivo, esto es debido a que no eres el coordinador designado para esta hoja de evaluación</h2></body></html>")
			return response

	documento = u"<html lang='es'><head><meta charset='utf-8' />"
	documento = documento +"<style>tr:nth-child(odd){background:#99FFCC;} tr:nth-child(even){background:#FFFFCC;}</style>"
	documento = documento + u"</head><body><center><header><h2>Detalle Puntuación Visita</h2>"
	documento = documento + u"<table style='border:1px solid black;text-align:center;'><tr><th>Criterio</th><th> Punt. Max (A)</th><th>Puntuación Consenso</th><th>Puntuación Visita % (B)</th><th>Puntuación de Visita (AxB)/100</th></tr>"


	for criterio in criterios_calidad:
		
		puntaje_consenso = PuntajeVisitaMejoresPracticas.objects.filter(evaluacion_consenso=eva_consenso,criterio=criterio)[0]
		#Obteniendo los puntajes individuales para los criterios
		documento = documento + "<tr><td>"+criterio.nombre+"</td><td>"+str(criterio.puntaje_maximo)+"</td>"

		if not criterio.agrupador:
			documento = documento + "<td>"+str(puntaje_consenso.puntacion_consenso)+"</td>"
			documento = documento + "<td>"+str(puntaje_consenso.puntacion_visita_porcentual)+"</td>"
			documento = documento + "<td>"+str(puntaje_consenso.puntacion_visita)+"</td>"
			documento = documento + "</tr>"
			#puntajes_totales_calidad.append(puntaje_consenso.puntuacion)
			#puntajes_totales_calidad_consenso.append(puntaje_consenso.puntacion_consenso)
		else:
			#documento = documento + "<td><strong>---</strong></td>"
			#documento = documento + "<td><strong>---</strong></td>"
			#Se debera de sumar el puntaje de los subcriterios
			criterios_agrupados = CriteriosMejoresPracticas.objects.filter(agrupador=False,cod_agrupador=criterio.cod_agrupador)
			caids = list()
			puntos = list()
			puntos_consenso = list()
			for cr in criterios_agrupados:
				caids.append(cr.id)
			
			puntajes_criterio_agrupado = PuntajeVisitaMejoresPracticas.objects.filter(evaluacion_consenso=eva_consenso,criterio__in=caids)
			for p in puntajes_criterio_agrupado:
				puntos.append(p.puntacion_visita)
				puntos_consenso.append(p.puntacion_consenso)
				puntajes_totales_calidad_consenso.append(p.puntacion_consenso)
				puntajes_totales_calidad.append(p.puntacion_visita)

			documento = documento + "<td><strong>"+str(sum(puntos_consenso))+"</strong></td>"
			documento = documento + "<td><strong>---</strong></td>"
			documento = documento + "<td><strong>"+str(sum(puntos))+"</strong></td>"
			
		
		documento = documento + "</tr>"

	
	columnas = 5
	documento = documento + "<tr><td colspan='2'><strong><h3>TOTALES</h3></strong></td>"
	
	documento = documento + "<td><strong style='color:red;'><h3><u>"+str(sum(puntajes_totales_calidad_consenso)) + "</u></h3></strong></td>"
	documento = documento + "<td><strong>---</strong></td>"
	documento = documento + "<td><strong style='color:red;'><h3><u>"+str(sum(puntajes_totales_calidad)) + "</u></h3></strong></td></tr>"
	
	documento = documento + "</table>"


	documento = documento+u"</center></html>"
	#response = HttpResponse(documento,content_type='text/html; charset=utf-8')
	response = HttpResponse(documento)
	#response['Content-Disposition'] = 'attachment; filename=%s.doc' % nombre_archivo
	return response

#Informes Visita Calidad
def informe_visita_calidad(request,id_eva_consenso):
	
	#Protección de Generación del archivo
	eva_consenso = EvaluacionVisitaCalidad.objects.filter(id = id_eva_consenso)[0]
	if request.user.username != eva_consenso.coordinador_postulacion.identificador.username:
		#El usuario NO es el evaluador designado para este proceso por lo que no debe poder generar el archivo
		# O tampoco tiene permisos de responsable de proceso
		if  not request.user.groups.filter(name='responsables_proceso').exists():
			response = HttpResponse(u"<html lang='es'><head><meta charset='utf-8'></head><body><h2>No tienes los permisos requeridos para generar el archivo, esto es debido a que no eres el coordinador designado para esta hoja de evaluación</h2></body></html>")
			return response

	codigo_postulacion = EvaluacionVisitaCalidad.objects.filter(id=id_eva_consenso)[0].postulacion_evaluacion.codigo
	razon_social_postulacion = EvaluacionVisitaCalidad.objects.filter(id=id_eva_consenso)[0].postulacion_evaluacion.nombre

	nombre_archivo = "Informe_Realimentacion_"+codigo_postulacion+"_"+time.strftime("%x")

	documento = u"<html lang='es'><head><meta charset='utf-8' /></head><body><center><header><h2>EDICIÓN 2014</h2>"
	documento = documento + u"<h2><u>INFORME DE REALIMENTACIÓN</u></h2>"
	documento = documento + u"<p>&nbsp;</p>"
	documento = documento + u"<p>&nbsp;</p>"
	documento = documento + u"<p>&nbsp;</p>"
	documento = documento + u"<p>&nbsp;</p>"
	documento = documento + u"<h2>"+razon_social_postulacion+"</h2>"
	documento = documento + u"<p>&nbsp;</p>"
	documento = documento + u"<p>&nbsp;</p>"
	documento = documento + u"<p>&nbsp;</p>"
	documento = documento + u"<p>&nbsp;</p>"
	documento = documento + u'<h2>OFICINA ADMINISTRADORA DEL PREMIO <br>"ES Calidad"</h2>'
	documento = documento + u"<p>&nbsp;</p>"
	documento = documento + u"<p>&nbsp;</p>"
	documento = documento + u"<p>&nbsp;</p>"
	documento = documento + u"<p>&nbsp;</p>"
	documento = documento + u"<p>&nbsp;</p>"
	documento = documento + u"<p>&nbsp;</p>"
	documento = documento + u"<p>&nbsp;</p>"
	documento = documento + u"<p>&nbsp;</p>"
	
	documento = documento + u"<p>&nbsp;</p>"
	documento = documento + u"<p>&nbsp;</p>"
	documento = documento + u"<p>&nbsp;</p>"
	documento = documento + u'</center>'
	
	#Datos Generales
	codigo_postulacion = EvaluacionVisitaCalidad.objects.filter(id=id_eva_consenso)[0].postulacion_evaluacion.codigo
	nombre_archivo = "Informe_Realimentacion_"+codigo_postulacion+"_"+time.strftime("%x")
	
	documento = documento + u"<h3>PRESENTACIÓN</h3>"
	documento = documento + u"<p style='text-align:justify;'>El Premio Salvadoreño a la Calidad constituye uno de los esfuerzos más importantes que se realizan para difundir y promover en las organizaciones la Excelencia en la Gestión con base a la Calidad. Al igual que los Premios Nacionales de Calidad de otros países, está orientado hacia la mejora de la competitividad y la economía en el país</p>"
	documento = documento + u"<p style='text-align:justify;'>En este sentido el Premio, a través de los criterios que lo conforman, comprende un conjunto de aspectos claves, determinantes en el éxito de cualquier organizacion, que deben ser comprendidos y gestionados al más alto nivel, renovando constantemente su compromiso con la calidad y mejorando permanentemente sus organizaciones y procesos para la satisfacción de sus clientes.</p>"
	documento = documento + u"<p style='text-align:justify;'>Por otro lado, adicionalmente al resultado positivo que se logra en las organizaciones comprometidas con el Premio, también se busca generar un efecto indirecto para involucrar a una mayor cantidad de empresas en procesos de mejora, gracias a los efectos demostrativos que sirven como estímulo a quienes aún no estuvieran fuertemente identificados con la Excelencia en la Gestión.</p>"
	documento = documento + u"<p style='text-align:justify;'>El presente Informe de Realimentación es el mecanismo que utiliza ES Calidad-Oficina Administradora del Premio para dar a conocer en forma individual y reservada a cada participante, información que puede ser usada por la organización postulante como una base para la elaboración de planes de acción tendientes a la mejora. Esta información, presentada a través de comentarios de fortalezas y oportunidades de mejora, no constituye una evaluación exhaustiva, ni tiene carácter definitivo, ya que se sustenta únicamente en el Informe de Postulación presentado y en los resultados de la evaluación efectuada en el proceso del Premio y no en un estudio detallado de los procesos y documentación existente.</p>"
	documento = documento + u"<p style='text-align:justify;'>Este trabajo es posible gracias a la participación desinteresada de los evaluadores y a los representantes de su organización, quienes con su aporte permitieron aplicar los criterios de evaluación de una manera objetiva</p>"
	documento = documento + u"<p style='text-align:right;'>ES Calidad - Oficina Administradora del Premio</p>"

	documento = documento + u"<p>&nbsp;</p>"
	documento = documento + u"<p>&nbsp;</p>"
	documento = documento + u"<p>&nbsp;</p>"
	documento = documento + u"<p>&nbsp;</p>"
	
	documento = documento + u"<p>&nbsp;</p>"
	documento = documento + u"<p>&nbsp;</p>"
	documento = documento + u"<p>&nbsp;</p>"
	documento = documento + u"<p>&nbsp;</p>"
	documento = documento + u"<p>&nbsp;</p>"

	documento = documento + u"<h3>1. ANTECEDENTES DEL INFORME DE REALIMENTACIÓN</h3>"
	documento = documento + u"<p style='text-align:justify;'>El Informe de Realimentación se generó a través de todas las etapas del proceso de evaluación de las postulaciones al Premio Salvadoreño a la Calidad.</p>"
	documento = documento + u"<p style='text-align:justify;'>Los trabajos presentados son sometidos a una revisión documental por ES Calidad – Oficina Administradora del Premio, con el objeto de verificar el cumplimiento de los requisitos establecidos en las bases de la presente edición del Premio, por parte de la organización postulante.</p>"
	documento = documento + u"<p style='text-align:justify;'>Todos los evaluadores han sido formados y calificados para realizar el proceso de evaluación de las postulaciones al Premio Salvadoreño para la Calidad. Los equipos de evaluación son conformados atendiendo varios criterios, entre ellos, los conocimientos, experiencias y habilidades pertinentes al proyecto de postulación, así como a la inexistencia de conflictos de interés de los miembros del equipo.</p>"
	documento = documento + u"<p style='text-align:justify;'>La evaluación se realiza individualmente y de manera integral por cada miembro del Equipo de Evaluadores. Posteriormente se unifican los diversos criterios y se obtiene un informe de consenso, que incluye las principales fortalezas y áreas de mejora identificados para cada criterio y subcriterio, producto de la revisión del informe de postulación. Se identifican de la misma forma aquellos aspectos que se consideren necesarios de validar en una visita de campo, siempre y cuando se considere que la organización se encuentra en condiciones adecuadas para ameritar el avance a esta etapa del proceso.</p>"
	documento = documento + u"<p style='text-align:justify;'>El Jurado está conformado por un selecto grupo de profesionales, que aportan una amplia gama de conocimientos y experiencias, gerenciales y empresariales, públicas y privadas, sumado a sus notorias cualidades personales que son necesarias para realizar los estudios, valoraciones, comparaciones y deliberaciones con base en la revisión y análisis de los informes de postulación presentados por las organizaciones y los informes de evaluación desarrollados por los Equipos de Evaluadores, al interior del Jurado.</p>"
	documento = documento + u"<p style='text-align:justify;'>Todos los miembros del Jurado se desempeñan bajo un Código de Ética claramente definido, firmando también una política de conflicto de intereses y confidencialidad de la información, como parte del asegurar la calidad para este proceso.</p>"

	documento = documento + u"<h3>2. RESUMEN EJECUTIVO DE DESEMPEÑO DEL POSTULANTE</h3>"

	#Aspectos Claves
	ambiente_organizacional = AmbienteOrganizacionalVisita.objects.filter(evaluacion_consenso__id = id_eva_consenso)[0].ambiente_organizacional
	relaciones_organizacionales = RelacionesOrganizacionalesVisita.objects.filter(evaluacion_consenso__id = id_eva_consenso)[0].relaciones_organizacionales
	ambiente_competitivo = AmbienteCompetitivoVisita.objects.filter(evaluacion_consenso__id = id_eva_consenso)[0].ambiente_competitivo
	desafios_estrategicos = DesafiosEstrategicosVisita.objects.filter(evaluacion_consenso__id = id_eva_consenso)[0].desafios_estrategicos
	sistema_mejora = SistemaMejoraVisita.objects.filter(evaluacion_consenso__id = id_eva_consenso)[0].sistema_mejora

	documento = documento + u"<h3>A. Ambiente Organizacional</h3>"
	documento = documento + u""+ambiente_organizacional
	documento = documento + u"<h3>B. Relaciones Organizacionales</h3>"
	documento = documento + u""+relaciones_organizacionales
	documento = documento + u"<h3>C. Ambiente Competitivo</h3>"
	documento = documento + u""+ambiente_competitivo
	documento = documento + u"<h3>D. Desafíos Estratégicos</h3>"
	documento = documento + u""+desafios_estrategicos
	documento = documento + u"<h3>E. Sistema de Mejora del Desempeño</h3>"
	documento = documento + u""+sistema_mejora

	documento = documento + u"<span style='width:80%;font-weight:bold;background:gray;'>3. COMENTARIOS SOBRE FORTALEZAS Y OPORTUNIDADES DE MEJORAPOR CRITERIO</span><hr>"

	criterios = CriteriosCalidad.objects.all()

	for criterio in criterios:
		fortalezas_consenso = FortalezasVisitaCalidad.objects.filter(evaluacion_visita__id=id_eva_consenso,criterio=criterio)[0].fortalezas
		areas_mejora_consenso = AreasMejorarVisitaCalidad.objects.filter(evaluacion_visita__id=id_eva_consenso,criterio=criterio)[0].areas_mejorar

		documento = documento + u"<h3 style='width:80%;font-weight:bold;background:gray;'>"+criterio.nombre+"</h3>"
		documento = documento + u"<h3'><i><u>Fortalezas</u></i></h3>"
		documento = documento + u""+fortalezas_consenso
		documento = documento + u"<h3'><i><u>Áreas a Mejorar</u></i></h3>"
		documento = documento + u""+areas_mejora_consenso

	documento = documento + '</body></html>'

	response = HttpResponse(documento,content_type='application/vnd.ms-word; charset=utf-8')
	response['Content-Disposition'] = 'attachment; filename=%s.doc' % nombre_archivo
	return response

#Informe Visita Mejores Prácticas
def informe_visita_mp(request,id_eva_consenso):
	
	#Protección de generación de esta página
	eva_consenso = EvaluacionVisitaMejoresPracticas.objects.filter(id = id_eva_consenso)[0]
	
	if request.user.username != eva_consenso.coordinador_postulacion.identificador.username:
		#El usuario NO es el evaluador designado para este proceso por lo que no debe poder generar el archivo
		# O tampoco tiene permisos de responsable de proceso
		if  not request.user.groups.filter(name='responsables_proceso').exists():
			response = HttpResponse(u"<html lang='es'><head><meta charset='utf-8'></head><body><h2>No tienes los permisos requeridos para generar el archivo, esto es debido a que no eres el coordinador designado para esta hoja de evaluación</h2></body></html>")
			return response

	codigo_postulacion = EvaluacionVisitaMejoresPracticas.objects.filter(id=id_eva_consenso)[0].postulacion_evaluacion.codigo
	razon_social_postulacion = EvaluacionVisitaMejoresPracticas.objects.filter(id=id_eva_consenso)[0].postulacion_evaluacion.nombre

	nombre_archivo = "Informe_Realimentacion_"+codigo_postulacion+"_"+time.strftime("%x")

	documento = u"<html lang='es'><head><meta charset='utf-8' /></head><body><center><header><h2>EDICIÓN 2014</h2>"
	documento = documento + u"<h2><u>INFORME DE REALIMENTACIÓN</u></h2>"
	documento = documento + u"<p>&nbsp;</p>"
	documento = documento + u"<p>&nbsp;</p>"
	documento = documento + u"<p>&nbsp;</p>"
	documento = documento + u"<p>&nbsp;</p>"
	documento = documento + u"<h2>Nombre del Proyecto: "+razon_social_postulacion+"</h2>"
	documento = documento + u"<p>&nbsp;</p>"
	documento = documento + u"<p>&nbsp;</p>"
	documento = documento + u"<p>&nbsp;</p>"
	documento = documento + u"<p>&nbsp;</p>"
	documento = documento + u'<h2>OFICINA ADMINISTRADORA DEL PREMIO <br>"ES Calidad"</h2>'
	documento = documento + u"<p>&nbsp;</p>"
	documento = documento + u"<p>&nbsp;</p>"
	documento = documento + u"<p>&nbsp;</p>"
	documento = documento + u"<p>&nbsp;</p>"
	documento = documento + u"<p>&nbsp;</p>"
	documento = documento + u"<p>&nbsp;</p>"
	documento = documento + u"<p>&nbsp;</p>"
	documento = documento + u"<p>&nbsp;</p>"
	
	documento = documento + u"<p>&nbsp;</p>"
	documento = documento + u"<p>&nbsp;</p>"
	documento = documento + u"<p>&nbsp;</p>"
	documento = documento + u'</center>'
	
	#Datos Generales
	codigo_postulacion = EvaluacionVisitaMejoresPracticas.objects.filter(id=id_eva_consenso)[0].postulacion_evaluacion.codigo
	nombre_archivo = "Informe_Realimentacion_"+codigo_postulacion+"_"+time.strftime("%x")
	
	documento = documento + u"<h3>PRESENTACIÓN</h3>"
	documento = documento + u"<p style='text-align:justify;'>Un elemento clave de la cultura de la calidad es la gente: cuando los trabajadores adecuadamente capacitados están involucrados en los problemas y retos de una organización participan en la toma de decisiones, trabajan en equipo, abordan sistemáticamente proyectos claves, logrando éxitos y crecimiento personal y organizacional.</p>"
	documento = documento + u"<p style='text-align:justify;'>La importancia y trascendencia que tienen para el país los logros de los equipos de mejora y la necesidad de divulgarlos y estimular el incremento y aprovechamiento de su potencial llevó a ES Calidad - Oficina Administradora del Premio a establecer el Reconocimiento a las Mejores Prácticas.</p>"
	documento = documento + u"<p style='text-align:justify;'>El presente Informe de Realimentación es el mecanismo que utiliza ES Calidad para dar a conocer a los participantes, información que puede ser usada por la organización postulante como una base para la elaboración de planes de acción tendientes a la mejora. Esta información, presentada a través de comentarios de fortalezas y oportunidades de mejora, no constituye una evaluación exhaustiva, ni tiene carácter definitivo, ya que se sustenta únicamente en los resultados de la evaluación efectuada en el proceso del Reconocimiento y no en un estudio detallado de los procesos y documentación existente.</p>"
	documento = documento + u"<p style='text-align:justify;'>Este trabajo es posible gracias a la participación desinteresada de los Evaluadores del Reconocimiento y a los representantes de su organización, quienes con su aporte permitieron aplicar los criterios de evaluación de manera objetiva.</p>"
	
	documento = documento + u"<p style='text-align:right;'>ES Calidad - Oficina Administradora del Premio</p>"

	documento = documento + u"<p>&nbsp;</p>"
	documento = documento + u"<p>&nbsp;</p>"
	documento = documento + u"<p>&nbsp;</p>"
	documento = documento + u"<p>&nbsp;</p>"
	
	documento = documento + u"<p>&nbsp;</p>"
	documento = documento + u"<p>&nbsp;</p>"
	documento = documento + u"<p>&nbsp;</p>"
	documento = documento + u"<p>&nbsp;</p>"
	documento = documento + u"<p>&nbsp;</p>"
	documento = documento + u"<p>&nbsp;</p>"
	documento = documento + u"<p>&nbsp;</p>"
	documento = documento + u"<p>&nbsp;</p>"
	

	documento = documento + u"<h3>1. PROCESO DE GENERACIÓN DEL INFORME DE REALIMENTACIÓN</h3>"
	documento = documento + u"<p style='text-align:justify;'>El Informe de Realimentación se generó a través de todas las etapas del proceso de evaluación de las postulaciones al Reconocimiento a las Mejores Prácticas.</p>"
	documento = documento + u"<p style='text-align:justify;'>Los trabajos presentados son sometidos a una revisión documental por ES Calidad, con el objeto de verificar el cumplimiento de los requisitos establecidos en las bases de la presente edición del Reconocimiento, por parte de la organización postulante.</p>"
	documento = documento + u"<p style='text-align:justify;'>Todos los evaluadores han sido formados y calificados para realizar el proceso de evaluación de las postulaciones al Reconocimiento a las Mejores Prácticas. Los equipos de evaluación son conformados atendiendo varios criterios, entre ellos, los conocimientos, experiencias y habilidades pertinentes al proyecto de postulación, así como a la inexistencia de conflictos de interés de los miembros del equipo.</p>"
	documento = documento + u"<p style='text-align:justify;'>La evaluación se realiza individualmente y de manera integral por cada miembro del Equipo de Evaluación. Posteriormente se unifican los diversos criterios y se obtiene un informe de consenso, que incluye las principales fortalezas y áreas de mejora identificados para cada criterio y subcriterio, producto de la revisión del informe de postulación. Se identifican de la misma forma aquellos aspectos que se consideren necesarios de validar en una visita de campo, siempre y cuando se considere que la organización se encuentra en condiciones adecuadas para ameritar el avance a esta etapa del proceso.</p>"
	documento = documento + u"<p style='text-align:justify;'>El Jurado está conformado por un selecto grupo de profesionales, que aportan una amplia gama de conocimientos y experiencias, gerenciales y empresariales, públicas y privadas, sumado sus notorias cualidades personales que son necesarias para realizar los estudios, valoraciones, comparaciones y deliberaciones con base en la revisión y análisis de los informes de postulación presentados por las organizaciones y los informes de evaluación desarrollados por los Equipos de Evaluadores.</p>"
	documento = documento + u"<p style='text-align:justify;'>Todos los miembros del Jurado se desempeñan bajo un Código de Ética claramente definido, firmando también una política de conflicto de intereses y confidencialidad de la información para asegurar la confiabilidad de este proceso.</p>"

	documento = documento + u"<h3>2. RESUMEN EJECUTIVO DE DESEMPEÑO DEL POSTULANTE</h3>"

	#Aspectos Claves
	vinculo_proyecto = VinculoProyectoVisita.objects.filter(evaluacion_consenso__id = id_eva_consenso)[0].vinculo_proyecto
	metodologia = MetodologiaVisita.objects.filter(evaluacion_consenso__id = id_eva_consenso)[0].metologia_proyecto
	ambiente_competitivo = AmbienteCompetitivoVisitaMP.objects.filter(evaluacion_consenso__id = id_eva_consenso)[0].ambiente_competitivo
	soporte = SoporteVisita.objects.filter(evaluacion_consenso__id = id_eva_consenso)[0].soporte_direccion
	resultados = ResultadosVisita.objects.filter(evaluacion_consenso__id = id_eva_consenso)[0].resultados_obtenidos

	documento = documento + u"<h3>A. Vinculo del Proyecto con la Estrategia Organizacional</h3>"
	documento = documento + u""+vinculo_proyecto
	documento = documento + u"<h3>B. Metodologia empleada para la solución del problema</h3>"
	documento = documento + u""+metodologia
	documento = documento + u"<h3>C. Ambiente Competitivo</h3>"
	documento = documento + u""+ambiente_competitivo
	documento = documento + u"<h3>D. Soporte de la Alta Dirección al Proyecto</h3>"
	documento = documento + u""+soporte
	documento = documento + u"<h3>E. Resultados Obtenidos</h3>"
	documento = documento + u""+resultados

	documento = documento + u"<span style='width:80%;font-weight:bold;background:gray;'>3. COMENTARIOS SOBRE FORTALEZAS Y OPORTUNIDADES DE MEJORA POR CRITERIO</span><hr>"

	criterios = CriteriosMejoresPracticas.objects.all()

	for criterio in criterios:
		fortalezas_consenso = FortalezasVisitaMejoresPracticas.objects.filter(evaluacion_consenso__id=id_eva_consenso,criterio=criterio)[0].fortalezas
		areas_mejora_consenso = AreaMejoraVisitaMejoresPracticas.objects.filter(evaluacion_consenso__id=id_eva_consenso,criterio=criterio)[0].areas_mejora

		documento = documento + u"<h3 style='width:80%;font-weight:bold;background:gray;'>"+criterio.nombre+"</h3>"
		documento = documento + u"<h3'><i><u>Fortalezas</u></i></h3>"
		documento = documento + u""+fortalezas_consenso
		documento = documento + u"<h3'><i><u>Áreas a Mejorar</u></i></h3>"
		documento = documento + u""+areas_mejora_consenso

	documento = documento + '</body></html>'

	response = HttpResponse(documento,content_type='application/vnd.ms-word; charset=utf-8')
	response['Content-Disposition'] = 'attachment; filename=%s.doc' % nombre_archivo
	return response