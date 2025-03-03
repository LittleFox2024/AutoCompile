'''
Class for error window.
'''

#import
import tkinter as tkm
import tkinter.ttk as tk
from PIL import ImageTk, Image


'''For main window'''

#Set up Window
error = tkm.Tk() #Error window
error.title("AutoCompile Error") #Window title

#Labels
#The images won't work for whatever reason...
tk.Label(master=error, text="This was going to be an error image,\n" +\
         "but Pillow does not like me.\nImage would be in 'assets/error.png'.").grid(row=1, column=0, sticky='N')
tk.Label(master=error, text="\nSomething went wrong. \n\nIf you got to this point, you may " +\
    "need to remove \nthis program and redownload it from GitHub.").grid(row=1, column=1, sticky="N")