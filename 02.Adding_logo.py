import tkinter as tk

root = tk.Tk()
logo = tk.PhotoImage(file='python.gif')
w1 = tk.Label(root, image=logo).pack(side='right')
w2 = tk.Label(root, 
              justify=tk.LEFT,
              padx = 10, 
              text='explanation').pack(side="left")

w = tk.Label(root, 
             compound = tk.CENTER,
             text='explanation', 
             image=logo).pack(side="right")
root.mainloop()