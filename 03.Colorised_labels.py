import tkinter as tk
from tkinter import font

root = tk.Tk()
logo = tk.PhotoImage(file='python.gif')

# Colorized Labels in various fonts

# Some Tk widgets, like the label, text, and canvas widget, allow you to specify the fonts used to display text. 
# This can be achieved by setting the attribute "font". typically via a "font" configuration option. 
# You have to consider that fonts are one of several areas that are not platform-independent.

# The attribute fg can be used to have the text in another colour and the attribute bg can be used to change the background colour of the label.

w1 = tk.Label(root, text="I'll be in red", fg="red", font="Times").pack()

tk.Label(root, 
		 text="Green Text in Helvetica Font",
		 fg = "light green",
		 bg = "dark green",
		 font = "Helvetica 16 bold italic").pack()

# root.mainloop()

tk.Label(root, 
		 text="Blue Text in Verdana bold",
		 fg = "blue",
		 bg = "yellow",
		 font = "Verdana 10 bold").pack()

root.mainloop()