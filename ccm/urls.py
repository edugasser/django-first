from django.conf.urls import patterns, include, url
#dajax
from dajaxice.core import dajaxice_autodiscover, dajaxice_config
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
dajaxice_autodiscover()

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()
from ccm.settings import MEDIA_ROOT
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'ccm.views.home', name='home'),
    # url(r'^ccm/', include('ccm.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    (r'^persona_edit/(?P<id>\d+)/$', 'personas.views.persona_edit'),
    (r'^persona_add/$', 'personas.views.persona_add'),
    (r'^tablas/$', 'personas.views.tablas'),
    (dajaxice_config.dajaxice_url, include('dajaxice.urls')),
    (r'^web/', include('personas.urls')),

)

