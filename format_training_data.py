from PIL import Image
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def data_extraction():

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
				pixels[j] = int.from_bytes(file_images.read(1), "big")

			images.append(pixels)

	#On a créé une liste des images qui contient des listes des pixels
	images = np.array(images)


	np.save("thd_training_labels", labels)
	np.save("thd_training_images", images)	


if __name__ == "__main__":
	data_extraction()