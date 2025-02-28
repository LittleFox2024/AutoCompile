'''
Class for error window.
'''

#import
import tkinter as tkm
import tkinter.ttk as tk
from PIL import ImageTk, Image


'''For main window'''

#Set up Window
error = tkm.Tk()
error.title("AutoCompile Error")

tk.Label(master=error, text="\nSomething went wrong. \n\nIf you got to this point, you may " +\
    "need to remove \nthis program and redownload it from GitHub.").grid(row=1, column=0, sticky="N")
tk.Label(master=error, text="This was going to be a silly image,\n" +\
         "but Pillow does not like me.\nImage would be in 'assets/sadnagisa.png'.").grid(row=1, column=2, sticky='N')