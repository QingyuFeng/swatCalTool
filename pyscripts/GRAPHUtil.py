# -*- coding: utf-8 -*-
"""
Created on Tue May 12 2020 

This class is designed to create watershed and find the contributing 
subareas.

@author: Qingyu.Feng
"""

##########################################################################
# Import modules #########################################################
##########################################################################
import pandas as pd

##########################################################################
# Define classes #########################################################
##########################################################################
def getGraph(field_names, subAttSWAT):

    """
    This function read in the attribute table of the shapefile and
    create a graph to represent the watershed.
    The graph will be a dictionary, with the reach no as key and upstream 
    reach no as values.
    For example, wsGraph = {reachNo: [upStrmNo1, upStrmNo2]}

    For the river generated by the SWAT model, the records are stored
    in the logic of downstream, not upstream.
    So, we need to find the reach no and all its up streams. 
    ['OBJECTID', 'ARCID', 'GRID_CODE', 'FROM_NODE', 'TO_NODE', 
    'Subbasin', 'SubbasinR', 'AreaC', 'Len2', 'Slo2', 'Wid2', 
    'Dep2', 'MinEl', 'MaxEl', 'Shape_Leng', 'HydroID', 'OutletID']
    """

    # Get all stream receiving streams, 
    rchAttDF = pd.DataFrame.from_dict(subAttSWAT, orient='index', columns=field_names)

    rcvRchNo = rchAttDF["GRID_CODE"].unique()
    
    wsGraph = {}

    for rchID in rcvRchNo:
        rchAttSubset = rchAttDF[rchAttDF["TO_NODE"] == rchID].dropna()["FROM_NODE"]
        if len(list(rchAttSubset)) > 0:
            wsGraph[rchID] = list(rchAttSubset)
        else:
            wsGraph[rchID] =[]

    return wsGraph




def dfs_iterative(graph, start):
    stack, path, pathminus = [start], [], []

    # Stack as the starting point
    while stack:
        # Signed vertex: for path routing
        signedvertex = stack.pop()
        # remove sign for looping
        vertex = str(abs(int(signedvertex)))
        # Mark vertex as visited.
        if vertex in path:
            continue
        # If not visited, append it.
        path.append(vertex)
        pathminus.append(signedvertex)
        for nbid in range(len(graph[vertex])):
            if nbid > 0:
                neighbor = '-%s' %(graph[vertex][nbid])
            else:
                neighbor = graph[vertex][nbid]
                
            stack.append(neighbor)

    return path, pathminus
