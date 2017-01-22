from django.conf.urls import url
from . import views


urlpatterns = [
	url(r'^$', views.index, name="index"),
	url(r'^mostra_imagem', views.mostra_imagem, name="mostra_imagem"),
]


