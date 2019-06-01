import socket
from Card import Card
import Tkinter as Tk
from PIL import Image, ImageTk

IMAGE_DIR = "images/"

def load_image(card):
	image_string = card.imageString()
	filename = IMAGE_DIR + image_string
	load = Image.open(filename)
	load = load.resize( (173,264), Image.ANTIALIAS )
	return ImageTk.PhotoImage(load)

class Application(Tk.Frame):
	def __init__(self, master=None):
		Tk.Frame.__init__(self, master)
		self.deck = Card.standardDeck()
		self.master = master
		self.grid()
		render = load_image(self.deck[0])
		self.label1 = Tk.Label(self, image=render)
		self.label1.img = render
		self.label1.pack()
		
def main():
	root = Tk.Tk()
	app = Application(master=root)
	app.mainloop()

if __name__ == "__main__":
	main()
