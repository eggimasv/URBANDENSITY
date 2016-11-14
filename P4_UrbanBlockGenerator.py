import subprocess
import subprocess as subp # Used for merging
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
    folderList = os.listdir(path) 
    for folder in folderList[:-1]:
        resultFolder.append(path[:-1] + folder)

    return resultFolder

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
    os.remove(path[:-3] + "prj")
    os.remove(path[:-3] + "sbn")
    os.remove(path[:-3] + "cpg")
    os.remove(path[:-3] + "sbx")
    os.remove(path[:-3] + "shp.xml")
    os.remove(path[:-3] + "shx")
    return

def writeToTxtGMEcommand(outPath, GMECommand):
    """
    This functions writes to a .txt file.

    """
    outfile = outPath + "GMEcommands.txt"
    myDocument = open(outfile, 'a')
    myDocument.write(str(GMECommand) + "\n")
    myDocument.close()
    return


#----------
import arcpy
import os, sys                                              # General Imports
import gc; gc.disable()                                     # Don't allow garbage collection

#Path to Scripts
pythonScriptPath = "C:/Users/eggimasv/URBANDENSITY/P4"      # Path where SNIP Python files are stored

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

# Path to SEGME.exe of GME
pathToSEGME = r'C:\Users\eggimasv\AppData\Local\Apps\2.0\BN23RV48.G12\9DDGL0P7.2AJ\segm..tion_c23e290fb11c064b_0001.0000_143886b27f0a8c90\SEGME.exe'

pathForGMECommands = r'Q:\\Abteilungsprojekte\\eng\\SWWData\\Eggimann_Sven\\07-Fallbeispiele\\02_GIS_BERN\\'
pathForGMECommands = r'C:\\P4_CH\\'


# Global Variables
EW_Q = 0.162                                # [m3 / day] 1 EW is equal to 162 liter. This factor must be the same as for the GIS-Files
minimumUSUArea = 300                        # [m2] Minimum radius to merge USU
search_radius = 100                         # [m] Search radius for Near Analysis (otherwiese near-points become the points iself)


afterGME = True                            # False: Before GME Ececution to write out GME commands.
BetweenSteps = False

# ----------------------------------------------------------------------
# ----------------------------------------------------------------------
# Line to exectute command file with GME (full patz to .txt is necssary)
# PROVIDe LINK TO FOLDER!
# ----------------------------------------------------------------------
# ----------------------------------------------------------------------
if BetweenSteps == True:
    #subp.call(str(pathToSEGME) + r' -c run(in=\"C:\_SCRAP_FOLDERSTRUCTURE\GMEcommands.txt\");');
    subp.call(str(pathToSEGME) + r' -c run(in=\"C:\P4_CH\GMEcommands.txt\");');

# ------------------------------------------------------------------------------------------

#ListWithWWTPCatchments = ["Q:\\Abteilungsprojekte\\eng\\SWWData\\Eggimann_Sven\\07-Fallbeispiele\\02_GIS_BERN\\304_Kallnach\\304Kallnach", "Q:\\Abteilungsprojekte\\eng\\SWWData\\Eggimann_Sven\\07-Fallbeispiele\\02_GIS_BERN\\304_Kallnach\\304Kallnach1"]
#ListWithWWTPCatchments = ["C:\\_SCRAP_FOLDERSTRUCTURE\\430900"]

if afterGME == False:
    ListWithWWTPCatchments = collectDataAllRunsBefore(pathForGMECommands)
else:
    ListWithWWTPCatchments = collectDataAllRuns(pathForGMECommands)
    
    '''
    cnt = 0
    for i in ListWithWWTPCatchments:
        if i == "C:\\\\P4_CH\\359501" #300501":
            print("POSITION IN LSIt: " + str(cnt)) #179  , [179:180]
        
        cnt += 1
    '''

# SCRAP
ListWithWWTPCatchments = ListWithWWTPCatchments #[514:] #[252:] #[181:] #[179:180]
print(ListWithWWTPCatchments)
    

print("PAths: " + str(ListWithWWTPCatchments))

nameUSUfile = "USU_raw"   # Name of USU after first intersection

# Read in street network
for pathCatchement in ListWithWWTPCatchments:
    print("Iteration, pathCatchement : " + str(pathCatchement))
    
    pathStreetUSU = str(pathCatchement) + "\\" + "street_simplified_split.shp"
    pathRailwayUSU = str(pathCatchement) + "\\" + "railwayNetwork.shp"
    pathSettlementArea = str(pathCatchement) + "\\" + "settlementArea.shp"
    pathBuildings = str(pathCatchement) + "\\" + "buildings_inhabited.shp"
    
    pathstreetRailMerge = pathCatchement + "\\" + "streetRailMerge.shp"
      
    if afterGME == False:
        print("------------------------------------------------")
        print("Path WWTP Catchements: " + str(pathCatchement))
        

        # -------------
        # 1. Define Projection
        # -------------
        SwisscordSys = arcpy.SpatialReference(21781) # EPSG:21781 ,CH1903 / LV03 # Swiss Coordinate System
        #arcpy.DefineProjection_management(pathStreetUSU, SwisscordSys)
        #arcpy.DefineProjection_management(pathRailwayUSU, SwisscordSys)
        #arcpy.DefineProjection_management(pathSettlementArea, SwisscordSys)
    
        # -------------
        # 2. Merge Street Network & Railroads
        # -------------
        arcpy.env.workspace = pathCatchement
        arcpy.Merge_management([pathStreetUSU, pathRailwayUSU], pathCatchement + "/" + "streetRailMerge.shp")
    
        
        #pathUSU = pathCatchement + "\\" + "USU.shp"
        print("Finishing merging Street and Railway Network" + str(pathstreetRailMerge))
        
        #Assign same coordinate system
        #print("pathstreetRailMergeFile: " + str(pathstreetRailMerge))
        SwisscordSys = arcpy.SpatialReference(21781) # EPSG:21781 ,CH1903 / LV03
        arcpy.DefineProjection_management(pathstreetRailMerge, SwisscordSys)
        #print(arcpy.GetMessages(0))
           
        # -------------
        # 3. Intersect to create USU with TME
        # http://www.spatialecology.com/gme/gmedownload.htm
        # http://www.spatialecology.com/gme/geomsplitpolysbylines.htm
        # -------------
        
        # With Split Tool
        #arcpy.ImportToolbox("//eawag/EA-Daten/Abteilungsprojekte/eng/SWWData/Eggimann_Sven/09-GIS-Python/63-SplitPolyonTool/SplitPolysWithLines/Split_Polygons_with_Lines.tbx")
        #arcpy.gp.toolbox = "//eawag/EA-Daten/Abteilungsprojekte/eng/SWWData/Eggimann_Sven/09-GIS-Python/63-SplitPolyonTool/SplitPolysWithLines/Split_Polygons_with_Lines.tbx";
        #arcpy.gp.SplitPolygons(pathSettlementArea, {}, pathstreetRailMerge, {}, pathUSU) 
        
        
        
        # Files used to create USU
        #areaGME = '"' + pathSettlementArea + "\\"  + '"'                  
        #lineGME = '"' + pathstreetRailMerge + "\\" + '"'          
        #outGME = '"' + str(pathCatchement) + "\\" + nameUSUfile + ".shp" + "\\" + '"'
        
        areaGME = '"' + pathSettlementArea + '"'                  
        lineGME = '"' + pathstreetRailMerge + '"'          
        outGME = '"' + str(pathCatchement) + "\\" + nameUSUfile + ".shp" + '"'
        
        inputCodeBackSlash = pathToSEGME + ' -c ' + 'geom.splitpolysbylines(in=\\' + areaGME + ', line=\\' + lineGME + ', out=\\' + outGME + r');' # Create Path
        #OLD: inputCodeBackSlashForTxt = 'geom.splitpolysbylines(in=\\' + areaGME + ', line=\\' + lineGME + ', out=\\' + outGME + r');' # Create Path
        inputCodeBackSlashForTxt = 'geom.splitpolysbylines(in=' + areaGME + ', line=' + lineGME + ', out=' + outGME + r');' # Create Path
        print("inputCodeBackSlash: " + str(inputCodeBackSlashForTxt))
                
        # Write command for GME into textfile in order that it can be executed in a later step
        writeToTxtGMEcommand(pathForGMECommands, inputCodeBackSlashForTxt) 
        
    if afterGME == True:
        print("Only Execute after GME Was executed seperately")
        # ------------------
        # Execute with .txt file
        # ------------------
        # Write command for MSE into .txt file and execute from there  
        #GMEcommandFileOutPath = str(pathCatchement) + "\\" + "commandGME"
        #writeToTxtGMEcommand(GMEcommandFileOutPath, inputCodeBackSlashForTxt)
        #subp.call(r'C:\Users\eggimasv\AppData\Local\Apps\2.0\BN23RV48.G12\9DDGL0P7.2AJ\segm..tion_c23e290fb11c064b_0001.0000_143886b27f0a8c90\SEGME.exe -c run(in=\"' + str(GMEcommandFileOutPath) + '.txt\");');
        
    
        # SCRPA # Execute with .txt file
        # SCRPA #subp.call(r'C:\Users\eggimasv\AppData\Local\Apps\2.0\BN23RV48.G12\9DDGL0P7.2AJ\segm..tion_c23e290fb11c064b_0001.0000_143886b27f0a8c90\SEGME.exe -c run(in=\"C:\_scraop\Script.txt\");');
        # SCRPA #subp.call(r'C:\Users\eggimasv\AppData\Local\Apps\2.0\BN23RV48.G12\9DDGL0P7.2AJ\segm..tion_c23e290fb11c064b_0001.0000_143886b27f0a8c90\SEGME.exe run(in=\"Q:\Abteilungsprojekte\eng\SWWData\Eggimann_Sven\07-Fallbeispiele\02_GIS_BERN\304_Kallnach\304Kallnach\Script.txt\");');
        
        
        #Execute directly in script
        #inputCodeBackSlash = r'C:\Users\eggimasv\AppData\Local\Apps\2.0\BN23RV48.G12\9DDGL0P7.2AJ\segm..tion_c23e290fb11c064b_0001.0000_eb3ca996fc44ae0f\SEGME.exe -c geom.splitpolysbylines(in=\"Q:\Abteilungsprojekte\eng\SWWData\Eggimann_Sven\07-Fallbeispiele\02_GIS_BERN\304_Kallnach\304Kallnach\settlementArea.shp\", line=\"Q:\Abteilungsprojekte\eng\SWWData\Eggimann_Sven\07-Fallbeispiele\02_GIS_BERN\304_Kallnach\304Kallnach\streetRailMerge.shp\", out=\"Q:\Abteilungsprojekte\eng\SWWData\Eggimann_Sven\07-Fallbeispiele\02_GIS_BERN\304_Kallnach\304Kallnach\Z_THATSI.shp\");'                                 
        #secondTask= 'addarea(in=' + outGME +', area="USU_AREA"' + ', areaunits="m^2");'
        #inputCodeBackSlashSecondTask = pathToSEGME + ' -c ' + secondTask 
        #subp.call(inputCodeBackSlashSecondTask, shell=False)

        #subp.call(inputCodeBackSlash, shell=False) #ADD OR REMOVE THIS
        #print("passed the intersecting")
        
        # ECECUTE GME IN Seperate Step
        # ----------------------------
        #subp.call(r'C:\Users\eggimasv\AppData\Local\Apps\2.0\BN23RV48.G12\9DDGL0P7.2AJ\segm..tion_c23e290fb11c064b_0001.0000_143886b27f0a8c90\SEGME.exe -c run(in=\"' + str(pathForGMECommands) + "GMEcommands.txt" + '\");');
        
        # ----------------------
        # 3 Convert Multipart to Singlepart
        # ----------------------
        nameUSUfileSinglePart = "USU_rawSinglePart"   # Name of USU after first intersection
        in_table = str(pathCatchement) + "\\" + nameUSUfile + ".shp"
        outTableSingleFeatureUSU =  str(pathCatchement) + "\\" + nameUSUfileSinglePart + ".shp"
            
        arcpy.MultipartToSinglepart_management(in_table, outTableSingleFeatureUSU)  # Convert Multi to Singlepart

        # -------------
        # 4. Add AREA field and calculate area
        # -------------
        field_name = "USU_AREA"
        field_type = "FLOAT"
    
        arcpy.AddField_management(outTableSingleFeatureUSU, field_name, "FLOAT")
        expression1 = "{0}".format("!SHAPE.area@SQUAREMETERS!")        
        arcpy.CalculateField_management(outTableSingleFeatureUSU, field_name, expression1, "PYTHON", )
    
    
        # -------------
        # 4a. Remove dublicates
        # -------------
        arcpy.DeleteIdentical_management(outTableSingleFeatureUSU, ["Shape"]) #, "PERIMETER"])

        #------------------------------------------------------------------------------------------------------------------------
        # 5. Delete all which are smaller than minimumUSUArea
        #------------------------------------------------------------------------------------------------------------------------
        arcpy.env.workspace = outTableSingleFeatureUSU  # Set environment settings
         
        # Set local variables
        inFeatures = outTableSingleFeatureUSU
        outFeatures =  str(pathCatchement) + "\\" + "USU_cleaned" + ".shp"
        tempLayer = "smallUSU"
        expression = "USU_AREA" + " < " + str(minimumUSUArea)
    
        # Execute CopyFeatures to make a new copy of the feature class
        arcpy.CopyFeatures_management(inFeatures, outFeatures) 
     
        # Execute MakeFeatureLayer
        arcpy.MakeFeatureLayer_management(outFeatures, tempLayer)
    
        # Execute SelectLayerByAttribute to determine which features to delete
        arcpy.SelectLayerByAttribute_management(tempLayer, "NEW_SELECTION",  expression)
     
        # Execute GetCount and if some features have been selected, then execute DeleteFeatures to remove the selected features.
        if int(arcpy.GetCount_management(tempLayer).getOutput(0)) > 0:
            arcpy.DeleteFeatures_management(tempLayer)
        
        # Delete Layer
        arcpy.Delete_management(tempLayer)
        
        #------------------------------------------------------------------------------------------------------------------------
        # 6. Export only those USU with buildings on it and also export all single buildings outside settlement area
        #------------------------------------------------------------------------------------------------------------------------
        tempLayer2 = "smallUSU_inhabited"
        outFeatures3 = str(pathCatchement) + "\\" + "USU_cleaned_inhabited_NEW" + ".shp"
        
        arcpy.MakeFeatureLayer_management(outFeatures, tempLayer2)   # Execute MakeFeatureLayer
        arcpy.SelectLayerByLocation_management(tempLayer2, 'intersect', pathBuildings)
        
        # If features matched criteria write them to a new feature class
        matchcountUSU = int(arcpy.GetCount_management(tempLayer2)[0]) 
        if matchcountUSU == 0:
            print('no features matched spatial and attribute criteria')
        else:
            arcpy.CopyFeatures_management(tempLayer2, outFeatures3)
                
        # Select all single buildings outside settlement area
        tempLayerSinglebuildings = "singleBuildingsnoUSU"
        outFeaturesSingleBuildings = str(pathCatchement) + "\\" + "USU_SingleBuildings" + ".shp"
        
        arcpy.MakeFeatureLayer_management(pathBuildings, tempLayerSinglebuildings)   # Execute MakeFeatureLayer
        arcpy.SelectLayerByLocation_management(tempLayerSinglebuildings, 'intersect', outFeatures)
        arcpy.SelectLayerByLocation_management(tempLayerSinglebuildings, None, None, "", "SWITCH_SELECTION")
        
        matchcountBUILD = int(arcpy.GetCount_management(tempLayerSinglebuildings)[0]) 
            
        if matchcountBUILD == 0:
            print('There are no single buildlings')
        else:
            arcpy.CopyFeatures_management(tempLayerSinglebuildings, outFeaturesSingleBuildings)
            
        # Delete Layer
        #arcpy.Delete_management(tempLayer2)
        #arcpy.Delete_management(tempLayerSinglebuildings)
        
        # ----------
        # 7. Creat Temporary ID of USU
        # ------------
        if matchcountUSU > 0: # IF there are USUs
            print("There are USU")
            field_name_USU_ID_tp = "JOINID"
            field_type = "FLOAT"   
            arcpy.AddField_management(outFeatures3, field_name_USU_ID_tp, "FLOAT") 
        
            # Loop through the rows in the attribute table
            uniqueID = 0
            cur = arcpy.UpdateCursor(outFeatures3)
            for row in cur:
                uniqueID += 1
                row.setValue(field_name_USU_ID_tp, uniqueID)      # Assign value
                cur.updateRow(row)                             # Apply the change
        
            #------------------------------------------------------------------------------------------------------------------------
            # 8. Spatial Intersect to add USU_ID on buildings
            #------------------------------------------------------------------------------------------------------------------------
            outFeatures4 = str(pathCatchement) + "\\" + "USU_buildings_sj_ID" + ".shp"
            arcpy.Intersect_analysis([outFeatures3, pathBuildings], outFeatures4)
            
            #------------------------------------------------------------------------------------------------------------------------
            # 9. Spatial Statistics of USU with tempory ID
            #------------------------------------------------------------------------------------------------------------------------    
            summaryTable = str(pathCatchement) + "\\" + "usu_summary_table"
            statistics_fields = [["Einw_GEB", "SUM"]]
            arcpy.Statistics_analysis(outFeatures4, summaryTable, statistics_fields, field_name_USU_ID_tp)
        
            #------------------------------------------------------------------------------------------------------------------------
            # 10. Create Centroid File of USU with ID
            #------------------------------------------------------------------------------------------------------------------------
            USU_Centroids = str(pathCatchement) + "\\" + "USU_centroids" + ".shp"
            arcpy.FeatureToPoint_management(outFeatures3, USU_Centroids, "CENTROID")  
        else: # If there are not USU
            print("There are no USU")
            USU_Centroids = str(pathCatchement) + "\\" + "USU_centroids" + ".shp"
            arcpy.FeatureToPoint_management(tempLayerSinglebuildings, USU_Centroids, "CENTROID")  #13.11.2016
            
        # Delete Layer
        arcpy.Delete_management(tempLayer2)
        arcpy.Delete_management(tempLayerSinglebuildings)
        
        #------------------------------------------------------------------------------------------------------------------------
        # 11. Table joint of Centroid and Table statistics
        #-----------------------------------------------------------)-------------------------------------------------------------
        if matchcountUSU > 0: # IF there are USUs
            print("USU yeas 2")
            layerName1 = "layerForTableJoin"
            joinField = field_name_USU_ID_tp
            joinTable = summaryTable + ".dbf"
            outFeatureJoinCentroids = str(pathCatchement) + "\\" + "USU_centroids_join" + ".shp"
            
            arcpy.MakeFeatureLayer_management(USU_Centroids, layerName1)
            arcpy.AddJoin_management(layerName1, joinField, joinTable, joinField, "KEEP_ALL")
        
            # Copy the layer to a new permanent feature class
            arcpy.env.qualifiedFieldNames = False
            arcpy.CopyFeatures_management(layerName1, outFeatureJoinCentroids)
            
            arcpy.DeleteField_management(outFeatureJoinCentroids, field_name_USU_ID_tp + "_1") #Delte old USU_ID
            
            # Transfer SUM_EINWO_GEB into EINW_GEB
            field_name = "EINW_GEB"
            field_type = "FLOAT"
            arcpy.AddField_management(outFeatureJoinCentroids, field_name, "FLOAT")
            expression1 = "{0}".format("!SUM_EINW_G!")        
            arcpy.CalculateField_management(outFeatureJoinCentroids, field_name, expression1, "PYTHON", )
            arcpy.DeleteField_management(outFeatureJoinCentroids, "SUM_EINW_G") #Delte old USU_ID
            
            
            # Calculate USU Population Density by adding field
            field_name = "USU_PD" # USU Population Density
            field_type = "FLOAT"
        
            arcpy.AddField_management(outFeatureJoinCentroids, field_name, "FLOAT")
            expression1 = "{0}".format("!EINW_GEB!/ (!USU_AREA!/1000000)") # 1km2 has 1'000 000 m2
            arcpy.CalculateField_management(outFeatureJoinCentroids, field_name, expression1, "PYTHON", )
            
            # Delete Layer
            arcpy.Delete_management(layerName1)
            #------------------------------------------------------------------------------------------------------------------------
            # 12. Merge Single Buildings and USU
            #------------------------------------------------------------------------------------------------------------------------
            outFeatureSingleBuildingsAndUSU = str(pathCatchement) + "\\" + "USU_USUandSingleBuildings" + ".shp"
            if matchcountBUILD > 0:
                print("there are buildlings")
                arcpy.Merge_management([outFeatureJoinCentroids, outFeaturesSingleBuildings], outFeatureSingleBuildingsAndUSU)
            else:
                print("there reno single builldings")
                arcpy.Merge_management([outFeatureJoinCentroids], outFeatureSingleBuildingsAndUSU) # not merge as only USUS
                
                arcpy.AddField_management(outFeatureSingleBuildingsAndUSU, "POINT_X", "FLOAT") 
                arcpy.AddField_management(outFeatureSingleBuildingsAndUSU, "POINT_Y", "FLOAT")
                arcpy.AddField_management(outFeatureSingleBuildingsAndUSU, "Q", "FLOAT") 
                
        else:
            outFeatureSingleBuildingsAndUSU = str(pathCatchement) + "\\" + "USU_USUandSingleBuildings" + ".shp"
            arcpy.Merge_management([outFeaturesSingleBuildings], outFeatureSingleBuildingsAndUSU)
        #------------------------------------------------------------------------------------------------------------------------
        # 13. Generate definitiv USU_ID Field and assign USU_ID
        #------------------------------------------------------------------------------------------------------------------------
        #Genere USU_ID FIELD
        field_name_USU_ID = "USU_ID"
        field_type = "FLOAT"   
        arcpy.AddField_management(outFeatureSingleBuildingsAndUSU, field_name_USU_ID, "FLOAT") 
    
        # Loop through the rows in the attribute table
        uniqueID = 0
        cur = arcpy.UpdateCursor(outFeatureSingleBuildingsAndUSU)
        for row in cur:
            uniqueID += 1
            row.setValue(field_name_USU_ID, uniqueID)      # Assign value
            cur.updateRow(row)                             # Apply the change
    
        #------------------------------------------------------------------------------------------------------------------------
        # 14. Update Fields & Near Analysis of all USU with street
        # Update Near X, Near Y
        # Update Q (TODO:
        #------------------------------------------------------------------------------------------------------------------------   
        # Update X and Y Coordinate (X_Point, Y_Point)
        xExpression = 'float(!shape.firstpoint!.split() [0])'
        yExpression = 'float(!shape.firstpoint!.split() [1])'
        arcpy.CalculateField_management(outFeatureSingleBuildingsAndUSU, "POINT_X", xExpression, "PYTHON")
        arcpy.CalculateField_management(outFeatureSingleBuildingsAndUSU, "POINT_Y", yExpression, "PYTHON")
        
        #Near analysis to connect buildings to street
        arcpy.Near_analysis(outFeatureSingleBuildingsAndUSU, pathstreetRailMerge, search_radius, "LOCATION", "NO_ANGLE")
        
        #If no street is found within a certain distance (=para_radius), the near coordinates will be set to those of the building itself
        rows = arcpy.da.UpdateCursor(outFeatureSingleBuildingsAndUSU, ['NEAR_X', 'NEAR_Y', 'Shape@X', 'Shape@Y'],'"NEAR_FID" = -1 ')
        for row in rows:
            row[0], row[1] = row[2], row[3]
            rows.updateRow(row)        
        del row, rows
        
        
        #------------------------------------------------------------------------------------------------------------------------
        # 15. Flow, Q
        #------------------------------------------------------------------------------------------------------------------------  
        
        # Update Q (convert pop-data in flow)  
        field_name = "Q" # USU Population Density
        field_type = "FLOAT"
        
        expression1 = "{0}".format("!EINW_GEB! * " + str(EW_Q)) # 1km2 has 1'000 000 m2
        arcpy.CalculateField_management(outFeatureSingleBuildingsAndUSU, field_name, expression1, "PYTHON", )
    
        
        # Delete fields
        arcpy.DeleteField_management(outFeatureSingleBuildingsAndUSU, ["Id", "ORIG_FID", "JOINID", "Rowid_", "FID_1", "V25OBJECTO", "V25OBJECTV", "MINDTM", "HEIGHT", "Z_Min", "Z_Max", "Inhabited", "Area_Foot", "Volume", "OBJECTART", "BFS_NUMMER", "BEZIRKSNUM", "KANTONSNUM", "NAME", "GEM_TEIL", "SHN", "ARA_Nr", "ARA_Name", "POPGem_06", "VolSumInha", "Pop_Build", "P4_DATA"])
    
        #------------------------------------------------------------------------------------------------------------------------
        # 12. Remove shapefiles which are not needed
        #------------------------------------------------------------------------------------------------------------------------
        
        removeShapeFile(USU_Centroids)
        
        try:
            removeShapeFile(outFeaturesSingleBuildings)
        except:
            print("no Singel buildlings to deltete")
        removeShapeFile(outFeatures)
        
        try:
            removeShapeFile(outFeatures3)
        except:
            print "no USU File to Delete"
        try:
            removeShapeFile(outFeatures4)
        except:
            print"no outFeatures4            "
        try:
            removeShapeFile(outFeatureJoinCentroids)
        except:
            print"not outFeatureJoinCentroids"
        #os.remove(summaryTable)
        
    