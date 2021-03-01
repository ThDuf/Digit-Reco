import tkinter as tk
from PIL import Image
import io
import os


radius = 10
x_prec = 0
y_prec = 0


def draw(event):
	'''
		When you push the mouse Button
	'''
	global x_prec
	global y_prec
	global radius
	x, y = event.x, event.y
	canv.create_oval(x-radius,y-radius,x+radius,y+radius, fill="white", outline="white")
	if x_prec == 0 and y_prec == 0 :
		x_prec = x
		y_prec = y
	else :
		canv.create_line(x_prec, y_prec, x, y, width = 2*radius, fill="white")
		x_prec = x
		y_prec = y


def release_button(event):
	global x_prec
	global y_prec
	x_prec = 0
	y_prec = 0


def erase_all():
	for element in canv.find_all():
		canv.delete(element)


def validation_dessin():
	canv.postscript(file="images/dernier_dessin.eps", colormode='mono', height=350, width=350)
#	im = Image.open('images/dernier_dessin.eps')
#	im.save('images/dernier_dessin.png')
	window.destroy()
		

if __name__ == "__main__":

	window = tk.Tk()
	#la racine de la fenetre

	titre = tk.Label(window, text="Dessinez un chiffre puis cliquez sur valider : ")
	titre.grid(column=0, row=0,columnspan=2)
	canv = tk.Canvas(window, width=350, height=350, background="black")
	canv.create_rectangle(0,0,350,350, fill='black')
	canv.bind("<Button-1>", draw)
	canv.bind("<B1-Motion>", draw)
	canv.bind("<B1-ButtonRelease>", release_button)

	canv.grid(column=0, row=1,columnspan=2)

	validate_button = tk.Button(window, text="Valider", command = validation_dessin)
	validate_button.grid(column=1, row=2)

	erase_button = tk.Button(window, text="Effacer", command=erase_all)
	erase_button.grid(column=0, row=2)



	window.mainloop()