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


import subprocess as subp # Used for merging


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

#ListWithWWTPCatchments = ["Q:/Abteilungsprojekte/eng/SWWData/Eggimann_Sven/07-Fallbeispiele/02_GIS_BERN/304_Kallnach/304Kallnach"]
ListWithWWTPCatchments = ["Q:\\Abteilungsprojekte\\eng\\SWWData\\Eggimann_Sven\\07-Fallbeispiele\\02_GIS_BERN\\304_Kallnach\\304Kallnach"]
# Read in street network

for pathCatchement in ListWithWWTPCatchments:
    
    SwisscordSys = arcpy.SpatialReference(21781) # EPSG:21781 ,CH1903 / LV03 # Swiss Coordinate System
    
    print("Path WWTP Catchements: " + str(pathCatchement))
    
    # street_USU   
    pathStreetUSU = str(pathCatchement) + "\\" + "street_simplified_split.shp"
    pathRailwayUSU = str(pathCatchement) + "\\" + "railwayNetwork.shp"
    pathSettlementArea = str(pathCatchement) + "\\" + "settlementArea.shp"
    
    #print("pathStreetUSU " + str(pathStreetUSU))
    #print("pathRailwayUSU " + str(pathRailwayUSU))
    #print("pathSettlementArea " + str(pathSettlementArea))
    
    
    # -------------
    # 1. Define Projection
    # -------------
    '''arcpy.DefineProjection_management(pathStreetUSU, SwisscordSys)
    arcpy.DefineProjection_management(pathRailwayUSU, SwisscordSys)
    arcpy.DefineProjection_management(pathSettlementArea, SwisscordSys)
    '''
    
    # -------------
    # 2. Merge Street Network & Railroads
    # -------------
    arcpy.env.workspace = pathCatchement
    #arcpy.Merge_management([pathStreetUSU, pathRailwayUSU], pathCatchement + "/" + "streetRailMerge.shp")
    
    pathstreetRailMerge = pathCatchement + "\\" + "streetRailMerge.shp"
    pathUSU = pathCatchement + "\\" + "USU.shp"
    print("Finishing merging Street and Railway Network" + str(pathstreetRailMerge))
    
    #Assign same coordinate system
    #print("pathstreetRailMergeFile: " + str(pathstreetRailMerge))
    #SwisscordSys = arcpy.SpatialReference(21781) # EPSG:21781 ,CH1903 / LV03
    #arcpy.DefineProjection_management(pathstreetRailMerge, SwisscordSys)
    #print(arcpy.GetMessages(0))
       
    # -------------
    # 3. Intersect to create USU with TME
    # split polygon with lines from tools: 
    # http://www.spatialecology.com/gme/gmedownload.htm
    # http://www.spatialecology.com/gme/geomsplitpolysbylines.htm
    # -------------
    
    # With Split Tool
    #arcpy.ImportToolbox("//eawag/EA-Daten/Abteilungsprojekte/eng/SWWData/Eggimann_Sven/09-GIS-Python/63-SplitPolyonTool/SplitPolysWithLines/Split_Polygons_with_Lines.tbx")
    #arcpy.gp.toolbox = "//eawag/EA-Daten/Abteilungsprojekte/eng/SWWData/Eggimann_Sven/09-GIS-Python/63-SplitPolyonTool/SplitPolysWithLines/Split_Polygons_with_Lines.tbx";
    #arcpy.gp.SplitPolygons(pathSettlementArea, {}, pathstreetRailMerge, {}, pathUSU) 
    
    # Path to SEGME.exe
    pathToSEGME = r'C:\Users\eggimasv\AppData\Local\Apps\2.0\BN23RV48.G12\9DDGL0P7.2AJ\segm..tion_c23e290fb11c064b_0001.0000_143886b27f0a8c90\SEGME.exe'
    
    nameUSUfile = "USU_raw"   # Name of USU after first intersection
    
    # Files used to create USU
    areaGME = '"' + pathSettlementArea + "\\"  + '"'                            # r'\"Q:\Abteilungsprojekte\eng\SWWData\Eggimann_Sven\07-Fallbeispiele\02_GIS_BERN\304_Kallnach\304Kallnach\settlementArea.shp\"'
    lineGME = '"' + pathstreetRailMerge + "\\" + '"'                           # r'\"Q:\Abteilungsprojekte\eng\SWWData\Eggimann_Sven\07-Fallbeispiele\02_GIS_BERN\304_Kallnach\304Kallnach\streetRailMerge.shp\"'
    outGME = '"' + str(pathCatchement) + "\\" + nameUSUfile + ".shp" + "\\" + '"'        #"r'\"Q:\Abteilungsprojekte\eng\SWWData\Eggimann_Sven\07-Fallbeispiele\02_GIS_BERN\304_Kallnach\304Kallnach\Z_THATSI.shp\"'
    
    inputCodeBackSlash = pathToSEGME + ' -c ' + 'geom.splitpolysbylines(in=\\' + areaGME + ', line=\\' + lineGME + ', out=\\' + outGME + r');' # Create Path
    print("inputCodeBackSlash: " + str(inputCodeBackSlash))
        
    # Execute with .txt file
    #subp.call(r'C:/Users/eggimasv/AppData/Local/Apps/2.0/BN23RV48.G12/9DDGL0P7.2AJ/segm..tion_c23e290fb11c064b_0001.0000_eb3ca996fc44ae0f/SEGME.exe -c run(in=\"C:\_scraop\Script.txt\");');
 
    #Execute directly in script
    #inputCodeBackSlash = r'C:\Users\eggimasv\AppData\Local\Apps\2.0\BN23RV48.G12\9DDGL0P7.2AJ\segm..tion_c23e290fb11c064b_0001.0000_eb3ca996fc44ae0f\SEGME.exe -c geom.splitpolysbylines(in=\"Q:\Abteilungsprojekte\eng\SWWData\Eggimann_Sven\07-Fallbeispiele\02_GIS_BERN\304_Kallnach\304Kallnach\settlementArea.shp\", line=\"Q:\Abteilungsprojekte\eng\SWWData\Eggimann_Sven\07-Fallbeispiele\02_GIS_BERN\304_Kallnach\304Kallnach\streetRailMerge.shp\", out=\"Q:\Abteilungsprojekte\eng\SWWData\Eggimann_Sven\07-Fallbeispiele\02_GIS_BERN\304_Kallnach\304Kallnach\Z_THATSI.shp\");'                                 
    
    #secondTask= 'addarea(in=' + outGME +', area="USU_AREA"' + ', areaunits="m^2");'
    #inputCodeBackSlashSecondTask = pathToSEGME + ' -c ' + secondTask 
    #subp.call(inputCodeBackSlashSecondTask, shell=False)
    
    #subp.call(inputCodeBackSlash, shell=False)
    print("passed the intersecting")
    
    # -------------
    # 4. Add AREA field and calculate area
    # -------------
    in_table = str(pathCatchement) + "\\" + nameUSUfile + ".shp"
    field_name = "USU_AREA"
    field_type = "FLOAT"
    print("In-Table: " + str(in_table))
    
    #arcpy.AddField_management(in_table, field_name, field_type) #, {field_precision}, {field_scale}, {field_length}, {field_alias}, {field_is_nullable}, {field_is_required}, {field_domain})
    expression1 = "{0}".format("!SHAPE.area@SQUAREMETERS!")        
    arcpy.CalculateField_management(in_table, field_name, expression1, "PYTHON", )


    #arcpy.env.workspace = str(pathCatchement) + "\\" + nameUSUfile + ".gdb"
    #arcpy.AddField_management("USU_AREA", "ref_ID", "LONG")


    #------------------------------------------------------------------------------------------------------------------------
    #Delete by selection

    # Set environment settings
    arcpy.env.workspace = in_table
     
    # Set local variables
    inFeatures = in_table
    outFeatures =  str(pathCatchement) + "\\" + "USU_cleaned" + ".shp"
    tempLayer = "smallUSU"
    #expression = arcpy.AddFieldDelimiters(tempLayer, "USU_AREA") + " < '300'"
    expression = "USU_AREA" + " < 300" 

    # Execute CopyFeatures to make a new copy of the feature class
    arcpy.CopyFeatures_management(inFeatures, outFeatures)      #Make Copy
 
    # Execute MakeFeatureLayer
    arcpy.MakeFeatureLayer_management(outFeatures, tempLayer)
 
    # Execute SelectLayerByAttribute to determine which features to delete
    arcpy.SelectLayerByAttribute_management(tempLayer, "NEW_SELECTION",  expression)
 
    # Execute GetCount and if some features have been selected, then 
    #  execute DeleteFeatures to remove the selected features.
    if int(arcpy.GetCount_management(tempLayer).getOutput(0)) > 0:
        arcpy.DeleteFeatures_management(tempLayer)

    

