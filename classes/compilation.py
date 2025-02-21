'''
Module with compilation functions
'''

#Imports
import os
import classes.checks as checks

#Variables
compilationFile = "" #File to compile
compiler = "" #Compiler to use
switches = [] #Command line switches (such as -x, /x, etc...)

def doCompilation(compiler, compilationFile, switches=""):
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
    if hostOS == "Windows": os.system(cmdLine)
    elif hostOS == "Linux" or hostOS == "Darwin": os.system("bash " + cmdLine)

    return "Completed"