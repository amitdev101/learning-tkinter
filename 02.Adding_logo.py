import tkinter as tk

root = tk.Tk()
logo = tk.PhotoImage(file='python.gif')
w1 = tk.Label(root, image=logo).pack(side='right')

# The "justify" parameter can be used to justify a text on the LEFT, RIGHT or CENTER. 
# padx can be used to add additional horizontal padding around a text label. 
# The default padding is 1 pixel. pady is similar for vertical padding.

w2 = tk.Label(root, 
              justify=tk.LEFT,
              padx = 10, 
              text='explanation to left').pack(side="left")


# You want the text drawn on top of the image? 
# No problem! We need just one label and use the image and the text option at the same time. 
# By default, if an image is given, it is drawn instead of the text. 
# To get the text as well, you have to use the compound option. 
# If you set the compound option to CENTER the text will be drawn on top of the image:

w3 = tk.Label(root, 
             compound = tk.CENTER, # here we set compound to get both images and text at same time
             text='explanation at center', 
             image=logo).pack(side="right")

# If the compound option is set to BOTTOM, LEFT, RIGHT, or TOP, 
# the image is drawn correspondingly to the bottom, left, right or top of the text.

w4 = tk.Label(root, 
             compound = tk.LEFT, # here we set compound to get both images and text at same time
             text='explanation of compound set to left', 
             image=logo).pack(side="right")


root.mainloop()