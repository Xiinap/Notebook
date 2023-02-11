import tkinter
from tkinter import *
from tkinter.filedialog import asksaveasfile, askopenfile
from tkinter.messagebox import showerror
from tkinter import messagebox

FILE_NAME = tkinter.NONE

def new_file():
	global FILE_NAME
	FILE_NAME = "Noname"
	text.delete('1.0', tkinter.END)

def save_file():
	data = text.get('1.0', tkinter.END)
	out = open(FILE_NAME, 'w')
	out.write(data)
	out.close()

def save_as():
	out = asksaveasfile(mode='w', defaultextension='txt')
	data = text.get('1.0', tkinter.END)
	try:
		out.write(data.rstrip())
	except Exception:
		showerror(title="Error", message="Saving file error")

def open_file():
	global FILE_NAME
	inp = askopenfile(mode="r")
	if inp is None:
		return
	FILE_NAME = inp.name
	data = inp.read()
	text.delete('1.0', tkinter.END)
	text.insert('1.0', data)

def info():
	messagebox.showinfo("Information", "1\n2\n3")

def yellow_bg():
    color == 'yellow'

def blue_bg():
    color == 'blue'

def red_bg():
    color == 'red'

def green_bg():
    color == 'green'

def white_bg():
    color == 'white'

def black_bg():
    color == 'black'


root = tkinter.Tk()
root.title("github.com/Xiinap/")

root.minsize(width=500, height=500)
root.maxsize(width=500, height=500)

color = 'black'
text = tkinter.Text(root, width=400, height=400, wrap="word", fg=color)
scrollb = Scrollbar(root, orient=VERTICAL, command=text.yview)
scrollb.pack(side="right", fill="y")
text.configure(yscrollcommand=scrollb.set)

text.pack()
menuBar = tkinter.Menu(root)
fileMenu = tkinter.Menu(menuBar)
fileLight = tkinter.Menu(menuBar)
fileTheme = tkinter.Menu(menuBar)
fileBg = tkinter.Menu(menuBar)

fileMenu.add_command(label="New", command=new_file)
fileMenu.add_command(label="Open", command=open_file)
fileMenu.add_command(label="Save", command=save_file)
fileMenu.add_command(label="Save as", command=save_as)

fileLight.add_command(label="Yellow", command=yellow_bg)
fileLight.add_command(label="Blue", command=blue_bg)
fileLight.add_command(label="Green", command=green_bg)
fileLight.add_command(label="Red", command=red_bg)
fileLight.add_command(label="White", command=white_bg)
fileLight.add_command(label="Black", command=black_bg)

fileTheme.add_cascade(label="Text", menu=fileLight)
fileTheme.add_cascade(label="Back Ground", menu=fileBg)

menuBar.add_cascade(label="File", menu=fileMenu)
menuBar.add_cascade(label="Exit", command=root.quit)
menuBar.add_cascade(label="Theme", menu=fileTheme)
menuBar.add_cascade(label="Info", command=info)
root.config(menu=menuBar)
root.mainloop()
