"""koodikoulu URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),

    url(r'^$', 'web.views.index', name='index'),
    url(r'^organize/$', 'web.views.organize', name='organize'),
    url(r'^story/$', 'web.views.story', name='story'),
    url(r'^own-events/$', 'web.views.own_events', name='own-events'),

    url(r'^register/$', 'web.views.register', name='register'),
    url(r'^login/$', 'web.views.login_view', name='login'),
    url(r'^logout/$', 'web.views.logout_view', name='logout'),
    url(r'^signup/(?P<pk>[0-9]+)/$', 'web.views.handle_signup', name='signup'),
    url(r'^participant/(?P<pk>[0-9]+)/$', 'web.views.remove_participant', name='remove-participant'),
    url(r'^export-signup/(?P<event_id>[0-9]+)/$', 'web.views.export_signup_list', name='export-signup'),
]
