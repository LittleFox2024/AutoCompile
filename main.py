'''
AutoCompile 0.1
Author: LittleFox2024
Creation Date: 02/07/2025
Project: Final Project

Description: This will take input in a window and then compile the file on the
command line without the user ever having to interact with the command line.

Changelog available in "changelog.txt"
'''

#Imports
from classes.mainWindow import mainWindow

try:
    #Try main window first.
    mainWindow.window.mainloop()
except:
    try:
        #If the main window fails, try error window.
        import classes.errorWindow
        classes.errorWindow.error.mainloop()
    finally:
        #If all else fails, call Administrator.
        print("System Alert: Code 871")
        exit(871)