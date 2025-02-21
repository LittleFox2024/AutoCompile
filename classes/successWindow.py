'''
Class for success window.
'''

#import
import tkinter as tk
'''For main window'''
#Set up Window
successWindow = tk.Tk()
successWindow.title("AutoCompile Complete")
tk.Label(text="Compilation has been completed. You can find it in the same " + \
        "folder as this program." , master=successWindow).grid(row=1, column=1)