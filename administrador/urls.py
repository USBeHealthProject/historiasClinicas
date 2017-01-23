from django.conf.urls import url, patterns
from administrador.views import *

urlpatterns = patterns(
    '',
    url(
        r'^$',
        AfterLogin.as_view(),
        name='after_login'
    ),
)
