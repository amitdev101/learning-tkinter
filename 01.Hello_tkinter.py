import tkinter as tk
import os
print(tk)
print(dir(tk))
print(tk.TkVersion)
print(os.getcwd())

'''To initialize tkinter, we have to create a Tk root widget, which is a window with a title bar and 
other decoration provided by the window manager. The root widget has to be created before any other widgets and 
there can only be one root widget.'''
root = tk.Tk()

'''The next line of code contains the Label widget. 
The first parameter of the Label call is the name of the parent window, in our case "root". 
So our Label widget is a child of the root widget. The keyword parameter "text" specifies the text to be shown: '''
w = tk.Label(root,text='Hello world')

'''The pack method tells Tk to fit the size of the window to the given text. '''
w.pack()

'''The window won't appear until we enter the Tkinter event loop'''
root.mainloop()
