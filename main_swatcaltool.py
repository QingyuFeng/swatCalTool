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

The framework will follow these steps.


Usage instruction:
1. Parameter determination:
# Users are expected to determine which parameter to be included for
# the calibration. 
# This is done by setting the value of yes/no into 1 in the calPara.
# set file. This is a json file, containing all commonly used files
# for calibrating corresponding variables.

"""

##########################################################################
# Import modules #########################################################
##########################################################################
from pyscripts.ModUtil import install_and_import

from pyscripts.globVars import *
from pyscripts.JSONUtil import parmToJSON
from pyscripts.FIFDUtil import *

# Check package installateion
requiredPkg = ['pandas']


for ipkg in requiredPkg:
    install_and_import(ipkg)

# Import local modules


##########################################################################
# Main function  #########################################################
##########################################################################

def main():

    # Process parameter from set format into json
    parmToJSON(fnParmSetFlow, fnParmJsonFlow)
    parmToJSON(fnParmSetSed, fnParmJsonSed)
    parmToJSON(fnParmSetN, fnParmJsonN)
    parmToJSON(fnParmSetP, fnParmJsonP)


    # Get subarea lists and hru lists from the TxtInOut
    subLst = getListOfFiles(fdTxtInOut, "sub")
    hruLst = getListOfFiles(fdTxtInOut, "hru")
    
    # Get groups of subareas













main()