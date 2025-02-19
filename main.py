'''
AutoCompile 0.1
Author: Braden DeForest
Creation Date: 02/07/2025
Project: Final Project

Description: This will take input in a window and then compile the file on the
command line without the user ever having to interact with the command line.

Changelog available in "changelog.txt"
'''

#Imports
import os
import checks

#Variables
compilationFile = "" #File to compile
compiler = "" #Compiler to use
switches = [] #Command line switches (such as -x, /x, etc...)


#Functions
def openWindow():

    '''
    Create the main window
    '''
    return 0

def doCompilation(compiler, compilationFile, switches):
    '''
    This is in charge of the actual compilation.
    '''
    
    x = checks.compilerCheck(compiler)
    
    #Make sure the compiler exists...
    if x == 1:
        return "Compiler not found or unavailable."
    elif (x != 0 and x != 1):
        return "Unexpected error. Please try a different compiler."
    

    switchList = ""
    
    #Make sure switches are in place
    for switch in switches:
        switchList += switch
        switchList += " "
    #Finally, we can execute it!
    cmdLine = compiler + " " + switchList + " " + compilationFile

    hostOS = checks.osTypeCheck()
    if hostOS == "Windows": os.system(cmdLine + \
                                      " 2> %HOMEPATH%\\AutoCompileLog.txt")
    elif hostOS == "Linux" or hostOS == "Darwin": os.system("bash " + cmdLine + \
                                                    " 2> ~/AutoCompileLog.txt")

    return "Completed"