from django.conf.urls import include, url
from django.contrib import admin

from simplemooc.core.views import home, contact

urlpatterns = [
	url(r'^$', home, name='home'),
	url(r'^contato/$', contact, name='contact'),
]