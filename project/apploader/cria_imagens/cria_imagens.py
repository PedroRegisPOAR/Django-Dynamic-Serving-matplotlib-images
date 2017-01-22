import os
import random
import matplotlib 

# http://stackoverflow.com/questions/27147300/how-to-clean-images-in-python-django
matplotlib.use("Agg")
import matplotlib.pyplot as plt


def criaImagem(path, image_name):
	x = random.sample(range(1,9), 3)
	y = random.sample(range(1,9), 3)

	plt.axis([0, 10, 0, 10])
	plt.plot(x, y, 'o')
	# Truque para mudar o lugar onde a figura será criada.
	initial_path = os.getcwd()
	os.chdir(path)
	plt.savefig(image_name)
	plt.close()
	# Não sei se é realmente necessario voltar ao diretório atual.
	os.chdir(initial_path)    