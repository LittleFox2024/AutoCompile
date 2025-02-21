'''
Class for success window.
'''

#import
import tkinter as tk
import classes.mainWindow
'''For main window'''


#Set up Window
def createWindow():
    compSuccessWindow = tk.Tk()
    compSuccessWindow.title("Complete!")
    if classes.mainWindow.mainWindow.check == 0:
        tk.Label(text="Compiler was found. You can use it!", master=compSuccessWindow).\
                                                        grid(row=1, column=1)
    else:
        tk.Label(text="Compiler was not found. Please give the full path or add it to " +\
             "your path variable.", master=compSuccessWindow).grid(row=1, column=1)
    compSuccessWindow.mainloop()