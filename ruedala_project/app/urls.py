from django.conf.urls import url, patterns
from app.views import *

urlpatterns = patterns(
    '',
    url(r'^$',
        Index.as_view(),
        name='index'),
)
