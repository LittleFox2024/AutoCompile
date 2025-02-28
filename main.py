'''
AutoCompile 0.1
Author: LittleFox2024
Creation Date: 02/07/2025
Project: Final Project

Description: This will take input in a window and then compile the file on the
command line without the user ever having to interact with the command line.

Changelog available in "changelog.txt"
'''

from classes.mainWindow import mainWindow

try:
    mainWindow.window.mainloop()
except:
    try:
        import classes.errorWindow
        classes.errorWindow.error.mainloop()
    finally:
        print("System Alert: Code 871")
        exit(871)