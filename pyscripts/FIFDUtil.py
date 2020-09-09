# -*- coding: utf-8 -*-
"""
Created on Tue May 12 2020 

This class contains a collection of functions dealing with files, 
such as deleting File and folder.

@author: Qingyu.Feng
"""

##########################################################################
# Import modules #########################################################
##########################################################################
import os, sys, glob

##########################################################################
# Define classes #########################################################
##########################################################################


def createFdIfNotExist(fdname):

    if not os.path.isdir(fdname):
        os.mkdir(fdname)




def get_osplatform():

    platforms = {
        'linux1' : 'Linux',
        'linux2' : 'Linux',
        'darwin' : 'OS X',
        'win32' : 'Windows'
    }
    if sys.platform not in platforms:
        return sys.platform

    return platforms[sys.platform]


def removeFlifExists(fname):

    if os.path.isfile(fname):
        os.remove(fname)


def removeFDifExists(fdname):

    if os.path.isdir(fdname):
        os.remove(fdname)




def removeFiles(fileName):
    """
    Delete all files with same root as fileName, 
    i.e. regardless of suffix.
    """
    pattern = os.path.splitext(fileName)[0] + '.*'
    for f in glob.iglob(pattern):
        os.remove(f)
        

def getListOfFiles(fd, fileSuffix):

    "Get the list of files with specified suffix within a dir"
    pattern = os.path.join(fd, '*.{}'.format(fileSuffix))

    flst = glob.glob(pattern)
    for idx in range(len(flst)):
        flst[idx] = os.path.basename(flst[idx])
        flst[idx] = os.path.splitext(flst[idx])[0]

    return flst