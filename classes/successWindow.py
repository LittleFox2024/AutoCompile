'''
Class for success window.
'''

#import
import tkinter as tk
'''For main window'''

#Set up Window
successWindow = tk.Tk() #Success Window
successWindow.title("AutoCompile") #Window title
tk.Label(text="Success\nIcon\n(assets/success.png)", master=successWindow).grid(row=1, column=0)
tk.Label(text="Compilation is working. You can find it in the same " + \
        "folder as this program unless you chose a different path." , master=successWindow).grid(row=1, column=1)