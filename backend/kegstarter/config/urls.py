from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'kegstarter.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^kegledger/', include('kegstarter.kegledger.urls')),
    url(r'^kegmanager/', include('kegstarter.kegmanager.urls')),
    url(r'^votingbooth/', include('kegstarter.votingbooth.urls')),
)
