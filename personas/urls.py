from django.conf.urls.defaults import *
from ccm.settings import MEDIA_ROOT
import views

urlpatterns = patterns('',
    (r'^$', views.index),
    (r'^autocomplete/$', views.autocomplete),

)


urlpatterns += patterns('',
    # TODO: Use this just for development
    # Change this to use Apache directly to serve the static files
    (r'^media/(?P<path>.*)/$', 'django.views.static.serve',{'document_root': MEDIA_ROOT}),
)

