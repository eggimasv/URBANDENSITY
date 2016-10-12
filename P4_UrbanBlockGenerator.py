
# This files creates urban blocksize
#
# -----------------------------------


def collectDataAllRuns(path):
    '''
    Collects 
    '''
    # List with all results from all the calculations
    resultFolder = []
    
    # Get the folders
    mainfolderPaths = []
    folderList = os.listdir(path) 
    folderList.sort()
    for folder in folderList: #[0:2]: #[1:4]: #[2:27]:
        mainfolderPaths.append(path + "\\" + folder + "\\" + "ResultSNIP" + "\\")
    
    print ("Anzahl Folder: " + str(len(mainfolderPaths)))
    
    # Reat our txt files
    for i in mainfolderPaths: 

        path = str(i) + "plot_MATRIX_RUNS.txt" #costMatrixWithSummedCostCurves.txt"
        #path = str(i) + "plot_MATRIX_RUNS.txt"
        
        txtFileList = readLines(path)
        z = txtFileList[0]
        result = list(eval(z))
        resultFolder.append(result)
        
    return resultFolder












#----------



import arcpy
import os, sys                      # General Imports
import gc; gc.disable()             # Don't allow garbage collection
from itertools import product

#Path to Scripts
pythonScriptPath = "C:/Users/eggimasv/URBANDENSITY/P4"  # Path where SNIP Python files are stored

def rewritePath(inPath):
    ''' Replace Characters in string path to get correct path.'''
    replaceList = [["\a","REPLACEA"], ["\t", "REPLACET"], ["\r","REPLACER" ], ["\f", "REPLACEF"], ["\b", "REPLACEB"], ["\n", "REPLACEN"], ["\\", "//"], ["REPLACEA", "/a"], ["REPLACET","/t" ], ["REPLACER", "/r"], ["REPLACEF", "/f"], ["REPLACEB", "/b"], ["REPLACEN", "/n"]]
    for c in replaceList:
        inPath = inPath.replace(c[0], c[1])
    return inPath

# Paths
pythonPath = os.getcwd()
sys.path.append(pythonPath)
sys.path.append(pythonScriptPath)                           # Path where python scripts are stored


print("---------------------------")
print("Start Urban Block Generator")
print("---------------------------")

# Read out a list with all catchements

ListWithWWTPCatchments = ["Q:/Abteilungsprojekte/eng/SWWData/Eggimann_Sven/07-Fallbeispiele/02_GIS_BERN/304_Kallnach/304Kallnach"]
# Read in street network

for pathCatchement in ListWithWWTPCatchments:
    print("WWTP Catchements: " + str(pathCatchement))
    print("--")
    
    # street_USU   
    pathStreetUSU = str(pathCatchement) + "/" + "street_simplified_split.shp"
    pathRailwayUSU = str(pathCatchement) + "/" + "railwayNetwork.shp"
    pathSettlementArea = str(pathCatchement) + "/" + "settlementArea.shp"
    
    print("pathStreetUSU " + str(pathStreetUSU))
    print("pathRailwayUSU " + str(pathRailwayUSU))
    print("pathSettlementArea " + str(pathSettlementArea))
    
    # Merge Street Network & Railroads
    '''arcpy.env.workspace = pathCatchement
    arcpy.Merge_management([pathStreetUSU, pathRailwayUSU], pathCatchement + "/" + "streetRailMerge.shp")

    pathstreetRailMerge = pathCatchement + "/" + "streetRailMerge.shp"
    pathUSU = pathCatchement + "/" + "USU.shp"
    print("Finishing merging Street and Railway Network" + str(pathstreetRailMerge))
    '''
    # split polygon with lines from tools: 
    # http://www.spatialecology.com/gme/gmedownload.htm
    # http://www.spatialecology.com/gme/geomsplitpolysbylines.htm
    
    # With Split Tool
    #(Input_Polygons__to_be_split_by_lines_, {Geometry_Type}, Input_Lines__to_split_Polygons_, {Extend_Lines_Limit}, {Extend_to_Extensions}, Output_Polygons__split_by_lines_) 
    
    
    # With GME
    os.system(r'C:/InstalledScriptsPaper4/64-GlobalModellingEnvironment/SEGME.exe')  
    
    '''import subprocess
    subprocess.call(r'C:/InstalledScriptsPaper4/64-GlobalModellingEnvironment/SEGME.exe geom.splitpolysbylines(in=pathSettlementArea, line=pathstreetRailMerge, out=pathUSU')   #-c run(in=\\\"" + newFile + "\\\");');
    
    GME = r'C:/InstalledScriptsPaper4/64-GlobalModellingEnvironment/SEGME.exe'
    #ARG = " export.csv(in=" + Input + ", out=" + OutputCSV + '");'
    ARG = " export.csv(in=" + Input + ", out=" + OutputCSV + '");'
    geom.splitpolysbylines(in=pathSettlementArea, line=pathstreetRailMerge, out=pathUSU
    CMD = GME + ARG
    '''
    
    print CMD
    subprocess.call(CMD)
    
    # railway_USU
    # settlement
    
    # Merge street & Railways
    




# 

