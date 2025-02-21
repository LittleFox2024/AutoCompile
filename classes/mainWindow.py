'''
Include the mainWindow() class
'''
#import
from tkinter import *
import tkinter.ttk as tk
import classes.compilation as compilation
import classes.checks as checks
import classes.mainWindow

class mainWindow():
    '''For main window'''

    #Set up Window
    window = Tk()
    window.title("AutoCompile")
    photo = PhotoImage(file = "assets/icon.png")
    window.iconphoto(True, photo)

    #Variables
    check = 1

    #Functions
    def createCompilerSuccessWindow():
        '''If compiler is found'''
        newWindow = Tk(mainWindow)
        newWindow.title("Success!")
        tk.Label(newWindow, text="Success!").grid(row=1, column=1)
        newWindow.mainloop()
    
    def createCompilerFailWindow():
        '''If compiler is not found'''
        newWindow = Tk(mainWindow)
        newWindow.title("Failure")
        tk.Label(newWindow, text="Fail").grid(row=1, column=1)
        newWindow.mainloop()

    def startCompilation():
        '''Start Compiling'''
        compiler = mainWindow.compilerInput.get()
        compilationFile = mainWindow.fileInput.get()
        compilation.doCompilation(compiler, compilationFile)
        import classes.successWindow
        classes.successWindow.successWindow.mainloop()

    def compilerTest():
        '''Test Compiler'''
        import classes.compilerSuccessWindow
        compiler = mainWindow.compilerInput.get()
        classes.mainWindow.mainWindow.check = checks.compilerCheck(compiler)
        if classes.mainWindow.mainWindow.check == 0:
            classes.mainWindow.mainWindow.check = 0
            #classes.mainWindow.mainWindow.createCompilerSuccessWindow()
        else:
            classes.mainWindow.mainWindow.check = 1
            #classes.mainWindow.mainWindow.createCompilerFailWindow()
        classes.compilerSuccessWindow.createWindow()


    #tk Window
    '''This section is just making and aligning everything right'''
    instructionText = tk.Label(text = "Please choose a compiler and a file" + \
                               " to compile.")
    instructionText.grid(row=1, column=1)
    compilerLabel = tk.Label(text = "Compiler:")
    compilerLabel.grid(row=2, column=1, padx=4, pady=4)
    compilerInput = tk.Entry()
    compilerInput.grid(row=2, column=2, padx=4, pady=4, columnspan=2)
    fileLabel = tk.Label(text = "Choose the file to compile:")
    fileLabel.grid(row=3, column=1, padx=4, pady=4)
    fileInput = tk.Entry()
    fileInput.grid(row=3, column=2, padx=4, pady=4)
    cwdLabel = tk.Label(text = "Choose the working directory")
    cwdLabel.grid(row=4, column=1, padx=4, pady=4)
    cwdInput = tk.Entry()
    cwdInput.grid(row=4, column=2, padx=4, pady=4)
    compileButton = tk.Button(text="Compile", command=startCompilation)
    compileButton.grid(row=6, column=1, padx=4, pady=4)
    testButton = tk.Button(text="Test Compiler", command=compilerTest)
    testButton.grid(row=6, column=2, padx=4, pady=4)