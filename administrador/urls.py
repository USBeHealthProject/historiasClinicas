from django.conf.urls import url, patterns
from administrador.views import *

urlpatterns = patterns(
    '',
    url(
        r'^$',
        Index.as_view(),
        name='index'
    ),
)
