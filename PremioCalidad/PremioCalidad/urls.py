from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.conf import settings
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()
from calidad import views
urlpatterns = patterns('',
    # Examples:
    url(r'^archivo_individual_calidad/(?P<id_postulacion>\d+)/(?P<id_evaluador>\d+)$', 
    	views.archivo_individual_calidad, name='archivo_individual_calidad'),

    url(r'^archivo_consolidado_calidad/(?P<id_postulacion>\d+)$', 
    	views.archivo_consolidado_calidad, name='archivo_consolidado_calidad'),

    url(r'^informe_consenso_calidad/(?P<id_eva_consenso>\d+)$', 
        views.informe_consenso_calidad, name='informe_consenso_calidad'),
    
    url(r'^puntuaciones_consenso_calidad/(?P<id_eva_consenso>\d+)$', 
        views.puntuaciones_consenso_calidad, name='puntuaciones_consenso_calidad'),

    url(r'^puntuaciones_visita_calidad/(?P<id_eva_consenso>\d+)$', 
        views.puntuaciones_visita_calidad, name='puntuaciones_visita_calidad'),

    url(r'^informe_visita_calidad/(?P<id_eva_consenso>\d+)$', 
        views.informe_visita_calidad, name='informe_visita_calidad'),

    #URL Mejores Practicas

    url(r'^archivo_individual_mp/(?P<id_postulacion>\d+)/(?P<id_evaluador>\d+)$', 
        views.archivo_individual_mp, name='archivo_individual_mp'),

    url(r'^archivo_consolidado_mp/(?P<id_postulacion>\d+)$', 
        views.archivo_consolidado_mp, name='archivo_consolidado_mp'),

    url(r'^informe_consenso_mp/(?P<id_eva_consenso>\d+)$', 
        views.informe_consenso_mp, name='informe_consenso_mp'),

    url(r'^puntuaciones_consenso_mp/(?P<id_eva_consenso>\d+)$', 
        views.puntuaciones_consenso_mp, name='puntuaciones_consenso_mp'),
    
    url(r'^puntuaciones_visita_mp/(?P<id_eva_consenso>\d+)$', 
        views.puntuaciones_visita_mp, name='puntuaciones_visita_mp'),

    url(r'^informe_visita_mp/(?P<id_eva_consenso>\d+)$', 
        views.informe_visita_mp, name='informe_visita_mp'),

    # url(r'^PremioCalidad/', include('PremioCalidad.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^tinymce/', include('tinymce.urls')),
    url(r'^admin/', include(admin.site.urls)),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)