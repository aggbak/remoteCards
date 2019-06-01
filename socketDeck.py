import socket
from Card import Card
import Tkinter as Tk

class Application(Tk.Frame):
	def __init__(self, master=None):
		Tk.Frame.__init__(self, master)
		

def main():
	root = Application()
	root.mainloop()

if __name__ == "__main__":
	main()
