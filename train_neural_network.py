from PIL import Image
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt



def plot_img(image1D):
	image2D = []
	for i in range(27):
		ligne = []
		for j in range(27):
			ligne.append(int.from_bytes(image1D[i*28+j], "big"))

		image2D.append(ligne)

	image2D = np.array(image2D)


	plt.imshow(image2D, cmap = "gray")
	plt.show()




#On créé d'abord une liste pour les labels
with open("data_set/train-labels-idx1-ubyte", "rb") as file_labels:
	labels = []
	for i in range(0, 0xea68):
		labels.append(file_labels.read(1))

#on supprime les 8 premières valeurs qui ne sont pas des labels
del labels[0:8] 

#la liste labels donne maintenant les labels en hexadecimal
labels = np.array(labels)



#On créé maintenant une liste de tuples pour les images
with open("data_set/train-images-idx3-ubyte", "rb") as file_images:
	images = [] #list des images

	file_images.read(15)   #il faut ignorer les 16 premières valeurs

	for i in range(60000): # Il y a 60000 images

		file_images.read(1)
		pixels = [0 for k in range(783)]
		for j in range(783):
			pixels[j] = file_images.read(1)
		images.append(pixels)

#On a créé une liste des images qui contient des listes des pixels
images = np.array(images)
#print(images[0])


plot_img(images[0])
print(labels[0])
plot_img(images[1])
print(labels[1])
plot_img(images[2])
print(labels[2])
plot_img(images[3])
print(labels[3])
plot_img(images[4])
print(labels[4])
plot_img(images[5])
print(labels[5])
plot_img(images[6])
print(labels[6])
plot_img(images[7])
print(labels[7])
plot_img(images[8])
print(labels[8])
plot_img(images[9])
print(labels[9])
