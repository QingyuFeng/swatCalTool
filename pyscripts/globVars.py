# -*- coding: utf-8 -*-
"""
Created on Wed, Sept 9, 2020

This is a module defining global values for the program

@author: Qingyu.Feng
"""

##########################################################################
# Import modules #########################################################
##########################################################################
import os


##########################################################################
# Define classes #########################################################
##########################################################################

# Folder structure
fdTxtInOut = "txtInOut"
fdCalCtrl = "calCtrlParm"
fdObs = "observed"
fdTemp = "tempRuns"


# Parameter set names
fnParmSetFlow = os.path.join(fdCalCtrl, "IPEAT_Para_Flow.set")
fnParmJsonFlow = os.path.join(fdCalCtrl, "ctlParmFlow.json")

fnParmSetSed = os.path.join(fdCalCtrl, "IPEAT_Para_Sed.set")
fnParmJsonSed = os.path.join(fdCalCtrl, "ctlParmSed.json")

fnParmSetN = os.path.join(fdCalCtrl, "IPEAT_Para_N.set")
fnParmJsonN = os.path.join(fdCalCtrl, "ctlParmN.json")

fnParmSetP = os.path.join(fdCalCtrl, "IPEAT_Para_P.set")
fnParmJsonP = os.path.join(fdCalCtrl, "ctlParmP.json")

# Intersted outlet nos
