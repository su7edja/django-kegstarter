from django.conf.urls import patterns, url

from . import views


urlpatterns = patterns('',
    url(r'^beers/', views.BeerListView.as_view(), name='beer-list'),
    url(r'^beers/(?P<pk>\d+)/$', views.BeerView.as_view(), name='beer'),
    url(r'^brewers/', views.BrewerListView.as_view(), name='brewer-list'),
    url(r'^brewers/(?P<pk>\d+)/$', views.BrewerView.as_view(), name='brewer'),
    #taps?
    #kegs?
)
