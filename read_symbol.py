from PIL import Image
import numpy as np
import data_visualisation as dv 


size = (28, 28)


def resize_image():
	'''
	Resize l'image dernier_dessin.eps en 28*28 pixels
	'''

	try :
		with Image.open("images/dernier_dessin.eps") as file:

			new_img = file.convert('L')
			new_img = new_img.resize(size)
			new_img.save("images/dernier_dessin_reduit.eps")

	except Exception as e:
		raise e


def get_pxls(small_img):
	'''
	prend en entrée une image et la transforme en array numpy de 784 de long
	'''

	img_list = [0 for i in range(size[0]*size[1])]
	for x in range(size[0]):
		for y in range(size[1]):
			img_list[28*y+x] = small_img.getpixel((x, y))


	return np.array(img_list)



if __name__ == "__main__":


	with Image.open("images/dernier_dessin_reduit.eps") as f:
		small_img = f.convert('L')

	print(small_img)
	print(get_pxls(small_img))

	dv.plot_img(get_pxls(small_img))