import subprocess
from sys import stderr
from tkMessageBox import IGNORE

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
    
    # Swiss Coordinate System
    SwisscordSys = arcpy.SpatialReference(21781) # EPSG:21781 ,CH1903 / LV03
    
    print("Path WWTP Catchements: " + str(pathCatchement))
    print("--")
    
    # street_USU   
    pathStreetUSU = str(pathCatchement) + "/" + "street_simplified_split.shp"
    pathRailwayUSU = str(pathCatchement) + "/" + "railwayNetwork.shp"
    pathSettlementArea = str(pathCatchement) + "/" + "settlementArea.shp"
    
    #print("pathStreetUSU " + str(pathStreetUSU))
    #print("pathRailwayUSU " + str(pathRailwayUSU))
    #print("pathSettlementArea " + str(pathSettlementArea))
    
    # Define Projection
    '''arcpy.DefineProjection_management(pathStreetUSU, SwisscordSys)
    arcpy.DefineProjection_management(pathRailwayUSU, SwisscordSys)
    arcpy.DefineProjection_management(pathSettlementArea, SwisscordSys)
    '''
    
    # Merge Street Network & Railroads
    arcpy.env.workspace = pathCatchement
    #arcpy.Merge_management([pathStreetUSU, pathRailwayUSU], pathCatchement + "/" + "streetRailMerge.shp")
    
    pathstreetRailMerge = pathCatchement + "/" + "streetRailMerge.shp"
    pathUSU = pathCatchement + "/" + "USU.shp"
    print("Finishing merging Street and Railway Network" + str(pathstreetRailMerge))
    
    #Assign same coordinate system
    #print("pathstreetRailMergeFile: " + str(pathstreetRailMerge))
    #SwisscordSys = arcpy.SpatialReference(21781) # EPSG:21781 ,CH1903 / LV03
    #arcpy.DefineProjection_management(pathstreetRailMerge, SwisscordSys)
    #print(arcpy.GetMessages(0))
    
    # split polygon with lines from tools: 
    # http://www.spatialecology.com/gme/gmedownload.htm
    # http://www.spatialecology.com/gme/geomsplitpolysbylines.htm
    
    # With Split Tool
    #arcpy.ImportToolbox("//eawag/EA-Daten/Abteilungsprojekte/eng/SWWData/Eggimann_Sven/09-GIS-Python/63-SplitPolyonTool/SplitPolysWithLines/Split_Polygons_with_Lines.tbx")
    #arcpy.gp.toolbox = "//eawag/EA-Daten/Abteilungsprojekte/eng/SWWData/Eggimann_Sven/09-GIS-Python/63-SplitPolyonTool/SplitPolysWithLines/Split_Polygons_with_Lines.tbx";
    #arcpy.gp.SplitPolygons(pathSettlementArea, {}, pathstreetRailMerge, {}, pathUSU) 
    
    
    pathToSEGME = r'C:\Users\eggimasv\AppData\Local\Apps\2.0\BN23RV48.G12\9DDGL0P7.2AJ\segm..tion_c23e290fb11c064b_0001.0000_eb3ca996fc44ae0f\SEGME.exe'
    
    
    # With GME
    #import subprocess
    import subprocess as subp
    
    # Trial with .txt (klappt)
    #subp.call(r'C:/Users/eggimasv/AppData/Local/Apps/2.0/BN23RV48.G12/9DDGL0P7.2AJ/segm..tion_c23e290fb11c064b_0001.0000_eb3ca996fc44ae0f/SEGME.exe -c run(in=\"C:\_scraop\Script.txt\");');


    #Works
    inputCodeBackSlash = r'C:\Users\eggimasv\AppData\Local\Apps\2.0\BN23RV48.G12\9DDGL0P7.2AJ\segm..tion_c23e290fb11c064b_0001.0000_eb3ca996fc44ae0f\SEGME.exe -c geom.splitpolysbylines(in=\"Q:\Abteilungsprojekte\eng\SWWData\Eggimann_Sven\07-Fallbeispiele\02_GIS_BERN\304_Kallnach\304Kallnach\settlementArea.shp\", line=\"Q:\Abteilungsprojekte\eng\SWWData\Eggimann_Sven\07-Fallbeispiele\02_GIS_BERN\304_Kallnach\304Kallnach\streetRailMerge.shp\", out=\"Q:\Abteilungsprojekte\eng\SWWData\Eggimann_Sven\07-Fallbeispiele\02_GIS_BERN\304_Kallnach\304Kallnach\Z_THATSI.shp\");'                             
    #inputCodeBackSlash = r'C:/Users/eggimasv/AppData/Local/Apps/2.0/BN23RV48.G12/9DDGL0P7.2AJ/segm..tion_c23e290fb11c064b_0001.0000_eb3ca996fc44ae0f/SEGME.exe -c geom.splitpolysbylines(in=\"Q:/Abteilungsprojekte/eng/SWWData/Eggimann_Sven/07-Fallbeispiele/02_GIS_BERN/304_Kallnach/304Kallnach/settlementArea.shp\", line=\"Q:/Abteilungsprojekte/eng/SWWData/Eggimann_Sven/07-Fallbeispiele/02_GIS_BERN/304_Kallnach/304Kallnach/streetRailMerge.shp\", out=\"Q:/Abteilungsprojekte/eng/SWWData/Eggimann_Sven/07-Fallbeispiele/02_GIS_BERN/304_Kallnach/304Kallnach/Z_THATSddI.shp\");'                             
    #print("inputCodeBackSlash" + str(inputCodeBackSlash))
    subp.call(inputCodeBackSlash, shell=False)
    
    
    
    #working on
    #inputCodeBackSlash = r'C:\Users\eggimasv\AppData\Local\Apps\2.0\BN23RV48.G12\9DDGL0P7.2AJ\segm..tion_c23e290fb11c064b_0001.0000_eb3ca996fc44ae0f\SEGME.exe -c geom.splitpolysbylines(in=\"Q:\Abteilungsprojekte\eng\SWWData\Eggimann_Sven\07-Fallbeispiele\02_GIS_BERN\304_Kallnach\304Kallnach\settlementArea.shp\", line=\"Q:\Abteilungsprojekte\eng\SWWData\Eggimann_Sven\07-Fallbeispiele\02_GIS_BERN\304_Kallnach\304Kallnach\streetRailMerge.shp\", out=\"Q:\Abteilungsprojekte\eng\SWWData\Eggimann_Sven\07-Fallbeispiele\02_GIS_BERN\304_Kallnach\304Kallnach\ZULU_GMEA.shp\");'         
    #print(inputCodeBackSlash)
    #subprocess.call(inputCodeBackSlash, shell=False)
    #subprocess.CalledProcessError(inputCodeBackSlash)

    
    #print("-------------")
    
    #os.system(inputCode)
    
    
    
    #os.system(r'C:/Users/eggimasv/AppData/Local/Apps/2.0/BN23RV48.G12/9DDGL0P7.2AJ/segm..tion_c23e290fb11c064b_0001.0000_1825d02f9dff539a/SEGME.exe geom.splitpolysbylines(in=pathSettlementArea, line=pathstreetRailMerge, out=pathUSU')  
    
    #Does Something
    #subprocess.call(r'C:/Users/eggimasv/AppData/Local/Apps/2.0/BN23RV48.G12/9DDGL0P7.2AJ/segm..tion_c23e290fb11c064b_0001.0000_1825d02f9dff539a/SEGME.exe geom.splitpolysbylines(in=pathSettlementArea, line=pathstreetRailMerge, out=pathUSU')   #-c run(in=\\\"" + newFile + "\\\");');
    
    #subprocess.call(r'C:/Users/eggimasv/AppData/Local/Apps/2.0/BN23RV48.G12/9DDGL0P7.2AJ/segm..tion_c23e290fb11c064b_0001.0000_1825d02f9dff539a/SEGME.exe geom.splitpolysbylines(in="Q:/Abteilungsprojekte/eng/SWWData/Eggimann_Sven/07-Fallbeispiele/02_GIS_BERN/304_Kallnach/304Kallnach/settlementArea.shp", line="Q:/Abteilungsprojekte/eng/SWWData/Eggimann_Sven/07-Fallbeispiele/02_GIS_BERN/304_Kallnach/304Kallnach/street_simplified_split.shp", out="Q:/Abteilungsprojekte/eng/SWWData/Eggimann_Sven/07-Fallbeispiele/02_GIS_BERN/304_Kallnach/304Kallnach/UUUUUUUt.shp");')   #-c run(in=\\\"" + newFile + "\\\");');
    #subprocess.call(r'C:/Users/eggimasv/AppData/Local/Apps/2.0/BN23RV48.G12/9DDGL0P7.2AJ/segm..tion_c23e290fb11c064b_0001.0000_1825d02f9dff539a/SEGME.exe geom.splitpolysbylines(in=/"Q:/Abteilungsprojekte/eng/SWWData/Eggimann_Sven/07-Fallbeispiele/02_GIS_BERN/304_Kallnach/304Kallnach/settlementArea.shp/", line=/"Q:/Abteilungsprojekte/eng/SWWData/Eggimann_Sven/07-Fallbeispiele/02_GIS_BERN/304_Kallnach/304Kallnach/street_simplified_split.shp/", out=/"Q:/Abteilungsprojekte/eng/SWWData/Eggimann_Sven/07-Fallbeispiele/02_GIS_BERN/304_Kallnach/304Kallnach/UUUUUUUt.shp/");')   #-c run(in=\\\"" + newFile + "\\\");');

    
    
    #subprocess.call(r'C:/Users/eggimasv/AppData/Local/Apps/2.0/BN23RV48.G12/9DDGL0P7.2AJ/segm..tion_c23e290fb11c064b_0001.0000_1825d02f9dff539a/SEGME.exe -c ' r'geom.splitpolysbylines(in="Q:\Abteilungsprojekte\eng\SWWData\Eggimann_Sven\07-Fallbeispiele\02_GIS_BERN\304_Kallnach\304Kallnach\settlementArea.shp", line="Q:\Abteilungsprojekte\eng\SWWData\Eggimann_Sven\07-Fallbeispiele\02_GIS_BERN\304_Kallnach\304Kallnach\streetRailMerge.shp", out="Q:\Abteilungsprojekte\eng\SWWData\Eggimann_Sven\07-Fallbeispiele\02_GIS_BERN\304_Kallnach\304Kallnach\ZZZZZ.shp");')
    print("passed the intersecting")
    
            
        
        
    '''GME = r'"C:/Users/eggimasv/AppData/Local/Apps/2.0/BN23RV48.G12/9DDGL0P7.2AJ/segm..tion_c23e290fb11c064b_0001.0000_1825d02f9dff539a/SEGME.exe"'
    ARG = ' geom.splitpolysbylines(in=r'"Q:/Abteilungsprojekte/eng/SWWData/Eggimann_Sven/07-Fallbeispiele/02_GIS_BERN/304_Kallnach/304Kallnach/street_simplified_split.shp"', line=r'"Q:/Abteilungsprojekte/eng/SWWData/Eggimann_Sven/07-Fallbeispiele/02_GIS_BERN/304_Kallnach/304Kallnach/street_simplified_split.shp"', out=r'"Q:/Abteilungsprojekte/eng/SWWData/Eggimann_Sven/07-Fallbeispiele/02_GIS_BERN/304_Kallnach/304Kallnach/UUUU.shp"');'
    CMD = GME + ARG
    
    print("Input Argument")
    print(CMD)
    subprocess.call(CMD)
    '''
    # How it should look like: geom.splitpolysbylines(in="C:\data\plots.shp", line="C:\data\roads.shp", out="C:\data\splitplots.shp");
    # geom.splitpolysbylines(in="Q:\Abteilungsprojekte\eng\SWWData\Eggimann_Sven\07-Fallbeispiele\02_GIS_BERN\304_Kallnach\304Kallnach\settlementArea.shp", line="Q:\Abteilungsprojekte\eng\SWWData\Eggimann_Sven\07-Fallbeispiele\02_GIS_BERN
    
    # railway_USU
    # settlement
    
    # Merge street & Railways
    




# 

