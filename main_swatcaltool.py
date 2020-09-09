#!/usr/bin/python3

"""
This program was developed to calibrate the SWAT model for large watershed.
The general steps include:
1. Read in parameter set
2. Break the watershed into several groups based on interested outlets, e.g. monitoring sites.
3. Read in subarea and hru list.
4. modify parameter of each group based on specific method.
5. Run the SWAT model
6. Calculate statistics between simulated and observed values.
7. Judge whether the criteria meet required values.
8. Determine the parameter set of the next set
9. Loop again until the stitis

The framework will follow these steps
"""




##############################################################################################
# Module load
# Reference: https://stackoverflow.com/questions/12332975/installing-python-module-within-code
def install_and_import(package):
    import importlib,  pip
    try:
        importlib.import_module(package)
    except ImportError:
        import pip
        pip.main(['install', package])


# Check package installateion
requiredPkg = ['fortranformat', 'pandas']

for ipkg in requiredPkg:
    install_and_import('fortranformat')


# Import packages
import pandas as pd
import sys, os
import fortranformat as ff