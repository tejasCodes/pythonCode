import tkinter as tk

root = tk.Tk()
logo = tk.PhotoImage(file="logo.png")

w1 = tk.Label(root, image=logo).pack(side="right")

explanation = """ Tejas Tejas Tejas Tejas Tejas Tejas Tejas Tejas Tejas 
Tejas Tejas Tejas Tejas Tejas Tejas Tejas Tejas Tejas Tejas Tejas Tejas 
Tejas Tejas Tejas Tejas Tejas Tejas Tejas Tejas Tejas """

w2 = tk.Label(root, 
			  justify = tk.LEFT,
			  padx=10,
			  text=explanation).pack(side="left")
root.mainloop()

