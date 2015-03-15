from django.conf.urls import patterns, include, url
from django.contrib import admin

from django.views.generic.base import TemplateView  # ya this is not great

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'kegstarter.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', TemplateView.as_view(template_name="base.html"), name='home'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^kegmanager/', include('kegstarter.kegmanager.urls')),
)
