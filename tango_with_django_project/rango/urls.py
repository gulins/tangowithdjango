from django.conf.urls import patterns, url
from rango import views
from django.contrib import admin

urlpatterns = patterns('',
        url(r'^$', views.index, name='index'),
        url(r'^about$', views.about, name='about'),
)
