from django.shortcuts import render, HttpResponse

from apploader.cria_imagens.cria_imagens import criaImagem

# Create your views here.


def index(request):
    return render(request, "apploader/home.html")


def mostra_imagem(request):
	image_name = 'imagemTeste.png'
	path = 'apploader/static/cria_imagens/'
	
	criaImagem(path, image_name)

#	return render(request, 'apploader/mytemplate.html')
	path_page = 'apploader/mytemplate.html'
	path_imagem = path + image_name
	return render(request, path_page)#, {"imagem":path_imagem})




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



