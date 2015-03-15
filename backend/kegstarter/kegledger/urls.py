from django.conf.urls import patterns, url, include

from .api import API_ROUTER


urlpatterns = patterns('',
    url(r'^api/', include(API_ROUTER.urls)),
)

