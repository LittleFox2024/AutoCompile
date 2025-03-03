'''
Module with compilation functions
'''

#Imports
import os
import classes.checks as checks

#Variables
compilationFile = "" #File to compile
compiler = "" #Compiler to use
switches = "" #Command line switches (such as -x, /x, etc...)
wd = "" #Working directory

def doCompilation(compiler, compilationFile, switches="", wd=""):
    '''
    This is in charge of the actual compilation.
    '''
    
    x = checks.compilerCheck(compiler)
    
    #Make sure the compiler exists...
    if x == 1:
        return "Compiler not found or unavailable."
    elif (x != 0 and x != 1):
        return "Unexpected error. Please try a different compiler."
    
    #Make sure switches are in place
    #I think I changed how this works
    # for switch in switches:
    #     switchList += switch
    #     switchList += " "
    
    # #Finally, we can execute it!
    cmdLine = compiler + " " + switches + " " + compilationFile

    #Make sure to use the right one. Windows used cmd.exe, UNIX is /bin/bash
    hostOS = checks.osTypeCheck()
    #Execute
    if hostOS == "Windows": os.system("cd " + wd + " &" +  cmdLine)
    elif hostOS == "Linux" or hostOS == "Darwin": os.system("bash cd" \
                                                + wd + " ; " + cmdLine)
        
    #Finished!
    return "Completed"