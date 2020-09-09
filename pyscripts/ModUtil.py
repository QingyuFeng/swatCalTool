# -*- coding: utf-8 -*-
"""
Created on Tue May 12 2020 

This class is designed to be a collection of GDAL function in python.

@author: Qingyu.Feng
"""

##########################################################################
# Import modules #########################################################
##########################################################################
import importlib,  pip


##########################################################################
# Define classes #########################################################
##########################################################################
# Module load
# Reference: https://stackoverflow.com/questions/12332975/installing-python-module-within-code
def install_and_import(package):
    
    try:
        importlib.import_module(package)
    except ImportError:
        import pip
        pip.main(['install', package])

