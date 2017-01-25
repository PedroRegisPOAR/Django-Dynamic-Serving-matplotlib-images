from django.shortcuts import render

from apploader.cria_imagens.cria_imagens import criaImagem
from . models import Plot

# Create your views here.


def index(request):
    return render(request, "apploader/home.html")


def mostra_imagem(request):
	all_plots = Plot.objects.all()
	context = {'all_plots':all_plots}
	
#	criaImagem()

	return render(request, 'apploader/mytemplate.html', context)





















"""
    path_imagem = 'static/projeção_populacional/nome_figura.png'
    #image_data = open(path, "rb").read()
    #return HttpResponse(image_data, content_type="image/png")
    #d = {"imagem":image_data}
    path_page = 'project/projeção_populacional/results_projeção_populacional.html'
    return render(request, path_page, {"imagem":path_imagem})
"""



"""
def mostra_imagem(request):
	image_name = 'imagemTeste.png'
	path = 'apploader/templates/apploader/'
	
	##criaImagem(path, image_name)

	##return render(request, 'apploader/mytemplate.html')
	path_page = 'apploader/mytemplate.html'
	path_imagem = 'apploader/templates/apploader/' + 'imagemTeste.png'

    #image_data = open(path, "rb").read()
    #return HttpResponse(image_data, content_type="image/png")
    #d = {"imagem":image_data}
    
	return render(request, path_page, {"imagem":path_imagem})
"""



