#------------------------------------------------------------------------------------------------
# Copyright 2014  Swiss Federal Institute of Aquatic Science and Technology, Eggimann Sven
#
# This file is part of SNIP (Sustainable Network Infrastructure Planning)
# SNIP is used for determining the optimal degree of centralization for waste
# water infrastructure.

# For detail information see:
#
# Eggimann Sven et al. (2015). BLBLABLABLA
#    
#
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>
    
# contact: sven.eggimann@eawag.ch
# Version 1.0
# Date: 20.10.2014

#===============================================================================
"""
    This script converts the results into ArcGIS format
    ---------------------------------------------------
    
    Change path in line 15
    Change path in line 20
"""
# ===================================================
# TODO Save arcpy file if arcGIS was not installed

# Parameters
#===========
print"-------------------------"
print("Execute writeResults.py")
print"-------------------------"

drawIntermediate = False        # Draw intermediate results
drawHouseConnections = 0        # Draw Houses or not
clusterCalculation = 0          # If calculations on cluster


# Imports
import sys, os
import arcpy

#inputArgument = sys.argv[1]     # Path of calculated results file from python SNIP file
inputArgument = "C:\\_SCRAP_FOLDERSTRUCTURE\\414100\\GIS_PYTHON\\"
inputArgument = "C:\\P4_CH\\10001\\GIS_PYTHON\\"

print"Input Argument from SNIP_python: " + str(inputArgument)
    
# Path with Folder, containing the .txt files with the results
# ====================================================
#folderContainingResults = "//eaw-homedirs//eggimasv$//Desktop//_results"_calculations//trubschachen_DEM/
#folderContainingResults = "Q://Abteilungsprojekte//Eng//SWWData//Eggimann_Sven//09-GIS-Python//01-Emmental//Trubschachen//GIS//__calculations//_txtResults_NEU4//"
folderContainingResults = str(inputArgument)

# Path with Folder, containing the python script
# ====================================================
#folderContainingScripts = "\\mnt\\storage\\eggimasv\\pythonScripts\\"
folderContainingScripts = "C://Users/eggimasv/URBANDENSITY/P4/" 

#folderContainingScripts = "Q:\\Abteilungsprojekte\\Eng\\SWWData\\Eggimann_Sven\\09-GIS-Python\\0-PythonFiles\\ModelPython\\"
#folderContainingScriptsII = "Q:\\Abteilungsprojekte\\Eng\\SWWData\\Eggimann_Sven\\09-GIS-Python\\0-PythonFiles\\"
sys.path.append(folderContainingResults)       # Append path to sys
sys.path.append(folderContainingScripts)       # Append path to sy

# path where output is stored
outFolder = folderContainingResults + "_GIS_FILES_FULLCOSTS_5"

print("outFolder: " + str(outFolder))
print("folderContainingResults: " + str(folderContainingResults))

from SNIP_functions import *
from txtFileReadingFunctions import *

# create new Folder
if not os.path.exists(outFolder):
    os.mkdir(outFolder)
    
allNames = []

# Iterate folder containing all results
for file in os.listdir(folderContainingResults):
    startCopy = 0
    # Get all statistics.txt files
    if file.endswith("VerticGraph.txt"):
        fullName = file
        singleCalcName = ""
        
        # Iterate file name and gest counter name
        for letter in fullName:
            if startCopy == 1:
                if letter == "_":
                    break
                else:
                    singleCalcName += letter
            
            if letter == "_":
                startCopy = 1
                
        allNames.append(singleCalcName)                    # Append to resultList
   
  
# Write out results of all files in a folder
for name in allNames:

    # Paths to .txt files
    result_VerticGraph = folderContainingResults  + "result_" + name + "_VerticGraph.txt"
    result_pointsPrim = folderContainingResults + "result_" + name + "_pointsPrim.txt"
    result_WWTPs = folderContainingResults + "result_" + name + "_WWTPs.txt"
    result_pumpList = folderContainingResults + "result_" + name + "_pumpList.txt"
    result_wtpstodraw = folderContainingResults  + "result_" + name + "_wtpstodraw.txt"
    result_intermediateResults = folderContainingResults  + "result_" + name + "_intermediateResults.txt"
    pathstreetVertices = folderContainingResults  + "result_" + name + "_streetVertices.txt"
    path_buildPoints = folderContainingResults + "result_" + name + "_buildPoints.txt"
    path_buildings = folderContainingResults + "result_" + name + "_buildings.txt"
    path_rasterPoints = folderContainingResults + "result_" + name + "_rasterPoints.txt"
    path_aggregatedNodes = folderContainingResults + "result_" + name + "_aggregatedNodes.txt"
    path_startnode = folderContainingResults + "result_" + name + "_startnode.txt"
    path_edgesID = folderContainingResults + "result_" + name + "_edgesID.txt" 
    
    print("A: " + str(folderContainingResults))
    print("T: " + str(result_WWTPs))
    
    # Read in .txt files
    streetVertices = readInstreetVertices(pathstreetVertices)                       
    VerticGRAPH = readResultsresult_VerticGraph(result_VerticGraph)
    pointsPrim = readResultspointsPrim(result_pointsPrim)
    listWTPs = readResultslistWTPs(result_WWTPs)
    pumpList = readResultslistPumps(result_pumpList)
    wtpstodraw = readResultswtpstodraw(result_wtpstodraw)
    buildPoints = readInbuildPoints(path_buildPoints)                       
    buildings = readInbuildings(path_buildings, clusterCalculation)                                 
    #intermediateResults = readResultsintermediateResults(result_intermediateResults)
    rasterPoints = readInRasterPoints(path_rasterPoints)
    aggregatetPoints = readInforPRIM(path_aggregatedNodes)
    edgeList = readInedgesID(path_edgesID)                                        
    #startnode = readInStartnode(path_startnode)                  

    outListStep_point = outFolder + "//" + str(name) + "_aggregated_nodes.shp"
    createPolyPoint(aggregatetPoints, outListStep_point)  # Draw the wtps in ArcGIS
    updateFieldAggregatedNodes(outListStep_point)
    writefieldsAggregatedNodes(outListStep_point, aggregatetPoints)
    
    print("START DRAWING....")
    print(pumpList)
    print("----------")

    # ArcGIS drawing
    # ==============
    
    '''# Aggregate nodes
    # ---------------------
    AggregateKritStreet = 20        # TODO: MAKE GLOBAL
    fromHouseToStreetCriteria = 10  # [m] Didd
    minTrenchDepth = 0.25           # MAKE GLOBAL
    buildingsPath = "Q:\\Abteilungsprojekte\\Eng\\SWWData\\Eggimann_Sven\\09-GIS-Python\\01-Emmental\\Trubschachen\\GIS\\geb25_pnt.shp"
    
    nearPoints = readClosestPointsAggregate(buildingsPath)
    outListStep_point = outFolder + "//" + str(name) + "_aggregated_nodes.shp"
    aggregatetPoints, buildings = aggregate(nearPoints, AggregateKritStreet, outListStep_point, fromHouseToStreetCriteria, minTrenchDepth)
    updateFieldStreetInlets(outListStep_point)
    writefieldsStreetInlets(outListStep_point, aggregatetPoints)
    # ---------------------
    '''
    list_GIS = primResultGISList(drawHouseConnections, VerticGRAPH, pointsPrim, streetVertices, buildings, buildPoints, rasterPoints, edgeList)   # list for drawing in arcGIS
    
    '''
    writeOutPipes(outListFolder, "info_pipes" + str(len(finalList)), list_GIS)
    
    # Pipe Distribution
    #==========================================
    print("Final - PipeSitriubiton")
    distributionList = pipeDistribution2d(list_GIS, 10, 10) #liste, interval, klassen
    writeToDoc(outListFolder, "pipeDistribution" + str(len(finalList)), distributionList)
    '''
    
    #Draw the pumps in ArcGIS
    #==========================================
    try:
        print("TESTER")
        print(pumpList)
        print(outFolder + "//" + str(name) + "_pumpes_original.shp")
        print("----")
        draw = createPolyPointPump(pumpList, outFolder + "//" + str(name) + "_pumpes_original.shp")
        print("DRAW: " + str(draw))
        
        if draw == True:
            writeFieldNodesPUMPS(outFolder + "//" + str(name) + "_pumpes_original.shp", pumpList)
            print("...The pumps are drawn in ArcGIS")
            print("Anzahl Pumpen: " + str(len(pumpList)))
    except:
        print("NO Pumps")
    
    
    # Create shapefile with pipes
    #==========================================
    createPolyLine(list_GIS, outFolder + "//" + str(name) + "_pipes_original.shp")      # Create pipes
    createPolyPointWWTP(wtpstodraw, outFolder + "//" + str(name) + "_WWTPs_original.shp")  # Draw the wtps in ArcGIS
    print("...Pipes are drawn")
    
    # Create shapefile with wwpts
    #==========================================
    #writeARAs(outFolder + "//" + str(name) + "_WWTPs_original.shp", wtpstodraw)
    writeWWTPs(outFolder + "//" + str(name) + "_WWTPs_original.shp", wtpstodraw)
    print("...wwtps are drawn in ArcGIS")
    
    
    
    # Create shapefile with nodes
    #==========================================
    createPolyPoint(pointsPrim, outFolder + "//" + str(name) + "_nodes_original.shp")
    writefieldsNodes(outFolder + "//" + str(name) + "_nodes_original.shp", pointsPrim)
    print("...nodes are drawn in ArcGIS")
    
    

    
    #writeLogFile(outListFolder, "logFile", logFileListe)    # Write out logfile
        
    # ========================
    # Draw intermediate results
    # ========================
    if drawIntermediate == True:
        name = 0
        for i in intermediateResults:
            name += 01           
                    
            print("length listWTPS")
            print(len(listWTPs))   
                    
            wwtpName = outFolder + "//" + "WWTPs_" + str(name) + ".shp"
            nodesName = outFolder + "//" + "nodes_" + str(name) + ".shp"
            pumpName = outFolder + "//" + "pumps_" + str(name) + ".shp"
            pipesName = outFolder + "//" + "pipes_" + str(name) + ".shp"
            try:
                pipeDistribution = "pipeDistribution_" + str(name)  + str(len(finalList))
            except:
                print("Konnte PIP DISTRIBUTION LIST NICHT ERSTELLEN")
                    
            list_GIS = primResultGISList(drawHouseConnections, i[0], i[1], streetVertices, buildings, buildPoints, rasterPoints, edgeList)     # Draw the graphs in ArcGIS, DrawHouse Connections
                   
            # TODO: CREATE FILES WITH NETWORK WHICH CAN BE easyil read into a GIS
            writeOutPipes(outFolder, "info_pipes" + str(name) + str(len(finalList)), list_GIS)
                    
            distributionList = pipeDistribution2d(list_GIS, 10, 10) #liste, interval, klassen
            writeToDoc(outFolder, pipeDistribution, distributionList)
                    
            createPolyLine(list_GIS, pipesName) 
            print("a. the pipes are drawn in ArcGIS")
                    
            #Draw the wtps in ArcGIS
            createPolyPoint(i[2], wwtpName)
            writeARAs(wwtpName, i[2])
            print("b. The wwtps are drawn in ArcGIS")
                    
            #Draw the points in ArcGIS
            createPolyPoint(i[1], nodesName)
            writefieldsNodes(nodesName, i[1])
            print("c. The nodes are drawn in ArcGIS")
            
            #Draw the pumps in ArcGIS
            draw = createPolyPointPump(i[3], pumpName)
                                               
            if draw == True:
                writeFieldNodesPUMPS(outFolder + "pumps" + str(name) + ".shp", i[3])
                print("d. The pumps are drawn in ArcGIS")
                print("Number of pumps: " + str(len(i[3])))

print("END OF SCRIPT")