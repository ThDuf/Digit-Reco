import numpy as np
import matplotlib.pyplot as plt


def plot_img(image1D):
	image2D = []
	for i in range(28):
		ligne = []
		for j in range(28):
			try:
				ligne.append(image1D[i*28+j])
			except Exception as e:
				ligne.append(0)
			

		image2D.append(ligne)

	image2D = np.array(image2D)


	plt.imshow(image2D, cmap = "gray")
	plt.show()


if __name__ == "__main__":

	
	training_labels = np.load("thd_training_labels.npy")
	training_images = np.load("thd_training_images.npy")


	'''
	plot_img(training_images[0])	
	plot_img(training_images[1])
	plot_img(training_images[2])
	plot_img(training_images[3])
	plot_img(training_images[4])
	plot_img(training_images[5])
	plot_img(training_images[6])
	plot_img(training_images[7])
	plot_img(training_images[8])'''
	print(training_images[9])
#	plot_img(training_images[10])
	plt.show()


