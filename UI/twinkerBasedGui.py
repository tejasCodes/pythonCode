import tkinter
import tkmessagebox

top = Tkinter.Tk()

def hello():
	tkMessageBox.showinfo("Hello Python", "Hello World")
	
B = Tkinter.Button(top, text = "Hello", command = hello)

#code to add widgets will go here
B.pack()
top.mainloop()