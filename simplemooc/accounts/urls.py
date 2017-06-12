from django.conf.urls import include, url
from django.contrib.auth.views import login, logout

from simplemooc.accounts.views import dashboard, register, password_reset, password_reset_confirm, edit, edit_password

#sessão 4 aula 33 e 34

urlpatterns = [
	url(r'^$', dashboard, name='dashboard'),
	#importados do django.contrib.auth.views
	url(r'^entrar/$', login, {'template_name': 'accounts/login.html'}, name='login'),
	#importados do django.contrib.auth.views
	url(r'^sair/$', logout, {'next_page': 'core:home'}, name='logout'),
	url(r'^cadastre-se/$', register, name='register'),
	url(r'^nova-senha/$', password_reset, name='password_reset'),
	# url(r'^nova-senha/$', password_reset, name='password_reset'),
	url(r'^confirmar-nova-senha/(?P<key>\w+)/$', password_reset_confirm, name='password_reset_confirm'),
	url(r'^editar/$', edit, name='edit'),
	url(r'^editar-senha/$', edit_password, name='edit_password'),
]