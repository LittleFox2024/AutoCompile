'''
This module contains functions needed to check that files exist, are useable,
the user has permission to use it, etc.
'''

#Imports
import os
import platform

#Functions
def osTypeCheck():
    '''Gets the user's OS'''
    hostOS = platform.system()
    return hostOS

def pathVarCheck(fileName):
    '''
    Last check in case the file is in the $PATH or %PATH% variable This is
    usually for if the given path doesn't work, or if only a file name is
    given without its path.
    '''
    
    #Get host from osTypeCheck()
    hostOS = osTypeCheck()

    #If it is Windows, use cmd.exe
    #If it is Linux or Mac, use bash
    #Darwin is for some reason what Mac is registered as.
    #Uses "where" for Windows and "which" for the others.
    if hostOS == "Windows":
        exist = os.system("where " + fileName)
    elif hostOS == "Linux" or hostOS == "Darwin":
        exist = os.system("which " + fileName)
    else:
        #Assuming this is probably UNIX
        exist = os.system("sh which " + fileName)
    
    #Return check
    if exist == 0: return 0
    else: return 1

def compilerCheck(compiler):
    '''
    Check for compiler
    '''
    #Check if the full path is valid
    if os.path.exists(compiler): return 0
    else: 
        #If not, see if it is in $PATH or %PATH%
        x = pathVarCheck(compiler)
        if x == 0: return 0
        else: return 1