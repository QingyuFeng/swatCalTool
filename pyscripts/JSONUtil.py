# -*- coding: utf-8 -*-
"""
Created on Tue May 12 2020 

This class is designed to be a collection of GDAL function in python.

@author: Qingyu.Feng
"""

##########################################################################
# Import modules #########################################################
##########################################################################
import json

from pyscripts.FIFDUtil import *
##########################################################################
# Define classes #########################################################
##########################################################################

def parmToJSON(fnParmSet, fnParmJSON):
    
    """
    This function read in the para_set file and convert it into a json file,
    which is used later for grouping.
    """

    # First step: define parameter set
    fid = open(fnParmSet, "r")
    lif = fid.readlines()
    fid.close()

    del(lif[0])

    outdict = {}

    for idx in range(len(lif)):
        lif[idx] = lif[idx].split("\t")
        lif[idx][-1] = lif[idx][-1][:-1]

        outdict[lif[idx][1]] = {}
        outdict[lif[idx][1]]["orderNo"] = lif[idx][0]
        outdict[lif[idx][1]]["inFile"] = lif[idx][2]
        outdict[lif[idx][1]]["unit"] = lif[idx][3]
        outdict[lif[idx][1]]["initVal"] = lif[idx][4]
        outdict[lif[idx][1]]["select"] = lif[idx][5]
        outdict[lif[idx][1]]["lowerBd"] = lif[idx][6]
        outdict[lif[idx][1]]["upperBd"] = lif[idx][7]




    removeFlifExists(fnParmJSON)

    with open(fnParmJSON, 'w') as outfile:
        json.dump(outdict, outfile)


    

