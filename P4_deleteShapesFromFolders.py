# Thsi file is used to delete shapesfiles to have only .txt files for Calculations

import os
import shutil
    
pathFoldersWithCatchements = r'C:\\P4_CH_NEU\\'

def collectDataAllRunsBefore(path):
    '''
    Collects 
    '''
    # List with all results from all the calculations
    resultFolder = []
    
    # Get the folders
    folderList = os.listdir(path) 
    for folder in folderList:
        resultFolder.append(path[:-1] + folder)

    return resultFolder


def removeShapeFile(path):
    os.remove(path)
    os.remove(path[:-3] + "dbf")
    
    try:
        os.remove(path[:-3] + "prj")
    except:
        #no file
        print"not prj file"       
    
    try:
        os.remove(path[:-3] + "sbn")
    except:
        #no file
        print"not sbn file"
    
    os.remove(path[:-3] + "cpg")
    
    try:
        os.remove(path[:-3] + "sbx")
    except:
        #no file
        print"not sbx file"    
    
    try:
        os.remove(path[:-3] + "shp.xml")
    except:
        #no file
        print"not shp.xml file" 
    
    try:    
        os.remove(path[:-3] + "shx")
    except:
        #no file
        print"not shx file" 
        
    return


import shutil



ListWithWWTPCatchments = collectDataAllRunsBefore(pathFoldersWithCatchements)   # Iterate Folders to get patsh

for path in ListWithWWTPCatchments:    
   
    # Remove Info folder
    pathInfo = path + "\\" + "info"
    try:
        shutil.rmtree(pathInfo)
        print(pathInfo)
    except:
        print"no found"

    
    
    path_aggregated_nodes = path + "\\" + "aggregated_nodes.shp"
    path_allNodes = path + "\\" + "allNodes.shp"
    path_streetGraph = path + "\\" + "streetGraph.shp"
    path_buildings_inabhited = path + "\\" + "buildings_inhabited.shp"
    path_dem_point = path + "\\" + "dem_point.shp"
    path_extent_gem = path + "\\" + "extent_gem.shp"
    path_extentPoly = path + "\\" + "extentPoly.shp"
    path_railwayNetwork = path + "\\" + "railwayNetwork.shp"
    path_settlementArea = path + "\\" + "settlementArea.shp"
    path_street_simplified_split = path + "\\" + "street_simplified_split.shp"
    path_street_RailMerge = path + "\\" + "streetRailMerge.shp"
    path_USU_raw = path + "\\" + "USU_raw.shp"
    path_USU_USUandSingleBuildings = path + "\\" + "USU_USUandSingleBuildings.shp"
    
    #
    try:
        removeShapeFile(path_aggregated_nodes)
    except:
        "file not found"
    
    try:
        removeShapeFile(path_allNodes)
    except:
        "file not found"
        
    try:
        removeShapeFile(path_streetGraph)
    #removeShapeFile(path_buildings_inabhited)
    except:
        "file not found"
            
    try:
        removeShapeFile(path_dem_point)
    #removeShapeFile(path_extent_gem)
    except:
        "file not found"
            
    try:
        removeShapeFile(path_extentPoly)
    except:
        "file not found"
            
    try: 
        removeShapeFile(path_railwayNetwork)
    except:
        "file not found"
           
    #removeShapeFile(path_settlementArea)
    
    try:
        removeShapeFile(path_street_simplified_split)
    except:
        "file not found"
            
    try:
        removeShapeFile(path_street_RailMerge)
    except:
        "file not found"
            
    try:
        removeShapeFile(path_USU_raw)
    except:
        "file not found"
            
    try:
        removeShapeFile(path_USU_USUandSingleBuildings)
    except:
        "file not found"    
    