'''
Include the mainWindow() class
'''
#Imports
from tkinter import *
import tkinter.ttk as tk
import classes.compilation as compilation
import classes.checks as checks
import classes.mainWindow
import classes.mainWindow

class mainWindow():
    '''For main window'''
    #from PIL import ImageTk, Image

    #Set up Window
    window = Tk() #Main window
    window.title("AutoCompile") #Window title
    photo = PhotoImage(file = "assets/icon.png") #Window icon
    window.iconphoto(True, photo)

    #Variables
    check = 1 #This is for the compiler check.

    #Functions
    def createCompilerSuccessWindow():
        '''If compiler is found'''
        #Create success window
        newWindow = Tk(mainWindow) #Success window
        newWindow.title("Success!") #New window title
        tk.Label(newWindow, text="Success!").grid(row=1, column=1)
        newWindow.mainloop()
    
    def createCompilerFailWindow():
        '''If compiler is not found'''
        #Create failure window
        #I don't think I used this... :)
        newWindow = Tk(mainWindow) #Fail window
        newWindow.title("Failure") #New window title
        tk.Label(newWindow, text="Fail").grid(row=1, column=1)
        newWindow.mainloop()

    def startCompilation():
        '''Start Compiling'''
        #Variables for this
        compiler = mainWindow.compilerInput.get() #Compiler to use
        compilationFile = mainWindow.fileInput.get() #File to compile
        switches = mainWindow.switchInput.get() #Switches to apply
        wd = mainWindow.cwdInput.get() #Working directory
        
        #Send the varibles to doCompilation()
        compilation.doCompilation(compiler, compilationFile, switches, wd)

        #Create success window
        import classes.successWindow
        classes.successWindow.successWindow.mainloop()

    def compilerTest():
        '''Test Compiler'''
        #Import success window
        import classes.compilerSuccessWindow
        compiler = mainWindow.compilerInput.get() #Compiler to test

        #Check for compiler
        classes.mainWindow.mainWindow.check = checks.compilerCheck(compiler)
                #Compiler check

        #Make sure everything is right... ignore commented out options
        #That is a test.
        if classes.mainWindow.mainWindow.check == 0:
            classes.mainWindow.mainWindow.check = 0
            #classes.mainWindow.mainWindow.createCompilerSuccessWindow()
        else:
            classes.mainWindow.mainWindow.check = 1
            #classes.mainWindow.mainWindow.createCompilerFailWindow()
        classes.compilerSuccessWindow.createWindow()

    def sysExit():
        '''Exit the program'''
        mainWindow.window.destroy()


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
    cwdLabel = tk.Label(text = "Choose the working directory:")
    cwdLabel.grid(row=4, column=1, padx=4, pady=4)
    cwdInput = tk.Entry()
    cwdInput.grid(row=4, column=2, padx=4, pady=4)
    switchLabel = tk.Label(text = "Switches:")
    switchLabel.grid(row=5, column=1, padx=4, pady=4)
    switchInput = tk.Entry()
    switchInput.grid(row=5, column=2, padx=4, pady=4)
    compileButton = tk.Button(text="Compile", command=startCompilation)
    compileButton.grid(row=6, column=1, padx=4, pady=4)
    testButton = tk.Button(text="Test Compiler", command=compilerTest)
    testButton.grid(row=6, column=2, padx=4, pady=4)
    exitButton = tk.Button(text="Exit", command=sysExit)
    exitButton.grid(row=7, column=2, padx=4, pady=4)
    helpLabel=tk.Label(text="\nNeed help? Manual is at https://github.com/LittleFox2024/AutoCompile/wiki.")
    helpLabel.grid(row=8, column=1, padx=4, pady=4, columnspan=2)


    def forceError():
        '''Force and error message. For testing purposes only.'''
        import classes.errorWindow
        classes.mainWindow.mainWindow.window.destroy()
        classes.errorWindow.error.mainloop()
        exit(871)

    
    #Test button
    forceError = tk.Button(text="Force Error", command=forceError)
    forceError.grid(row=7, column = 1)