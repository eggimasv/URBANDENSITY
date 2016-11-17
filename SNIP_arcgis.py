# ======================================================================================
# Copyright 2014  Swiss Federal Institute of Aquatic Science and Technology
#
# This file is part of SNIP (Sustainable Network Infrastructure Planning)
# SNIP is used for determining the optimal degree of centralization for waste
# water infrastructures. You find detailed information about SNIP in Eggimann et al. (2014).
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.

## You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>
#    
# The Djikstra and a* algorithm are adapted from Hetland (2010).
# The algorithm is developed for Python 2.7 and ArcGIS 10.2
#
# Literature
# ==========
# Eggimann Sven, Truffer Bernhard, Maurer Max (2015): To connect or not to connect? 
# Modelling the optimal degree of centralisation for wastewater infrastructures.   
# Water Research, XY, .....
#
# Hetland M.L. (2010): Python Algorithms. Mastering Basic Algorithms in the Python Language. apress.
#
# Contact:   sven.eggimann@eawag.ch
# Version    1.0
# Date:      1.1.2015
# Autor:     Eggimann Sven
# ======================================================================================
import arcpy, os, sys               # General Imports
import gc; gc.disable()             # Don't allow garbage collection

# Change after the insallation of the ArcToolBox
pythonScriptPath = "Q://Abteilungsprojekte/Eng/SWWData/Eggimann_Sven/09-GIS-Python/0-PythonFiles/"  # Path where SNIP Python files are stored

# Parameters
inputViaGUI = 1                 # 1: Input via ArcGIS GUI
onlyTxtReadOut = 0              # 1: Only .txt files are read out, 1: .txt files are read out and SNIP executed
OnlyExecuteMerge = 0            # 0: Default, 1: Restart MM module with subcatchements which are already calculated in a previous step. Set correct path in MM


calculateSeveralFolders = 0     # Iterate folders and calculate Z

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

# SNIP Imports    
from SNIP_functions import *                                # Import Functions
from SNIP_astar import *                                    # Import a* functions
from SNIP_costs import *                                    # Import cost functions

toolboxes = ["Data Management Tools.tbx"]
arcpy.env.overwriteOutput = True

# ArcGIS System Arguments
if inputViaGUI == 1:                                        # Script is executed with ArcGIS GUI
    in_street = sys.argv[1]                                 # Street shape file
    buildings = sys.argv[3]                                 # Building shape file
    inDHM = sys.argv[4]                                     # DEM point shape file (DEM needs to be converted to points)
    DEMExists = str(sys.argv[5])                            # "YES" (Default) --> DEM Exists, "NO" --> A virtual flat DEM is created. 
    outListFolder = sys.argv[2].replace("\\","/") + "/"     # Output Folder
    demAlreadyReadOut = 0                                   # 1: Dem is already read out
else:                                                       # Script is not executed with ArcGIS GUI (e.g. for random case study generation)

    # Python System Arguments
    in_street = sys.argv[5]                                 # Street shape file
    buildings = sys.argv[4]                                 # Building shape file
    
    arcpy.AddMessage("buildings: " + str(buildings))
    arcpy.AddMessage("in_street: " + str(in_street))
    
    inDHM = sys.argv[6]                                     # DEM point shape file (DEM needs to be converted to points)
    DEMExists = str("YES")                                  # "YES" (Default): DEM Exists, "NO": A virtual flat DEM is created. 
    outListFolder = sys.argv[7]                             # Output Folder
    pathRasterPoints = sys.argv[8]                          # Path to raster points
    demAlreadyReadOut = 0                                   # Raster is already read out
    rasterPoints = readInRasterPoints(pathRasterPoints)     # Read in rasterPoints
    rasterSize = 50                                         # Size of already read out raster
    rasterSizeList = [rasterSize]                                       
 

# Model parameters (based parameters as in Eggimann et al. 2015)
# ========================================================================
  
# Sewer related
maxTD = 8                                   # [m] Maximum trench depth
minTD = 0.25                                # [m] Min trench depth
minSlope = 1                                # [%] Criteria of minimum slope without pumps needed
stricklerC = 85                             # [m^1/3 s^-1] Stricker Coefficient
EW_Q = 0.162                                # [m3 / day] 1 EW is equal to 162 liter. This factor must be the same as for the GIS-Files
    
# Cost related
resonableCostsPerEW = 7540                  # [currency] Reasonable Costs
pricekWh = 0.20                             # [currency / kWh] price per kWh of electricity 
pumpingYears = 30                           # [years] Pump lifespan
discountYearsSewers = 80                    # [years] Pipe lifespan
wwtpLifespan = 33                           # [years] WWTP lifespan
interestRate = 2                            # [%] Real interest rate
operationCosts = 5                          # [currency / meter] operation costs per meter pipe per year
pumpInvestmentCosts = 500                   # [currency] Fix costs of pumps
fc_SewerCost = 0                            # [-20% - 20%] Used for Sensitivity Analysis to shift cost curve  (e.g. 10 % = 0.1)
fc_wwtpOpex = 0                             # [-20% - 20%] Used for Sensitivity Analysis to shift cost curve  (e.g. 10 % = 0.1)
fc_wwtpCapex = 0                            # [-20% - 20%] Used for Sensitivity Analysis to shift cost curve 
        
# Algorithm related
f_street = 1.7                              # [-] Factor to set How close the sewer follow the road network
f_merge = 1.4                               # [-] Factor do determine how the WWTPS are merged.
f_topo = 1.2                                # [-] Factor weighting the dem graph creation for the a* algorithm
    
neighborhood = 100                          # [m] Defines how large the neighbourhood for the a-Star Algorithm (Needs to be at least twice the raster size)     
AggregateKritStreet = 100                     # [m] How long the distances on the roads can be in maximum be before they get aggregated on the street network (must not be 0)
border = 3000                               # [m] How large the virtual dem borders are around topleft and bottom
tileSize = 50                               # [m] for selection of density based starting node
    
pipeDiameterPrivateSewer = 0.25             # Cost Assumptions private sewers: Pipe Diameter
avgTDprivateSewer = 0.25                    # Cost Assumptions private sewers: AVerage Trench Depth
    
# ArcGIS Representation related
drawHouseConnections = 1                    # 1: House connections are drawn in ArcGIS, 0: House Connections are not drawn in ArcGIS
interestRate = float(interestRate) / 100.0  # Reformulate real interest rate

# Add parameters into List for SNIP Algorithm
InputParameter = [minTD, maxTD, minSlope, f_merge, resonableCostsPerEW, neighborhood, f_street, pricekWh, pumpingYears, discountYearsSewers, interestRate, stricklerC, EW_Q,  wwtpLifespan, operationCosts, pumpInvestmentCosts,  f_topo, fc_SewerCost, fc_wwtpOpex, fc_wwtpCapex]

if calculateSeveralFolders == 1:
    #mainFolder = "Q:\\Abteilungsprojekte\\eng\\SWWData\\Eggimann_Sven\\07-Fallbeispiele\\02_GIS_BERN\\__TEST MULTIPLE\\"
    #mainFolder = "Q:\\Abteilungsprojekte\\eng\\SWWData\\Eggimann_Sven\\07-Fallbeispiele\\02_GIS_BERN\\11_mittleresEmmental\\"
    mainFolder = "Q:\\Abteilungsprojekte\\eng\\SWWData\\Eggimann_Sven\\07-Fallbeispiele\\02_GIS_BERN\\43_Thunersee\\"

    # Iterate Folders
    def getAllFolders(mainFolder):
        folderPaths = []
        folderList = os.listdir(mainFolder) # Get the folders
        folderList.sort()
        for folder in folderList:
            folderPaths.append(mainFolder + folder + "\\")
        return folderPaths

    folders = getAllFolders(mainFolder)     # Get folder paths  
    
    # Iterate folders and execute SNIP
    for calculation in folders:
        arcpy.AddMessage("FOLDER: " + str(calculation))
        # Create folder to store results 
        outListFolder = calculation + "_SNIP_slope05_cost0" + "/"     
        if not os.path.exists(outListFolder):
            os.mkdir(outListFolder)
        
        # Python System Arguments
        in_street = calculation + "streetNetwork.shp"         # Street shape file
        buildings = calculation + "buildings_inhabited.shp"   # Building shape file
        inDHM = calculation + "dem_point.shp"                 # DEM point shape file (DEM needs to be converted to points)
        DEMExists = str("YES")                                # "YES" (Default) --> DEM Exists, "NO" --> A virtual flat DEM is created. 

        outListStep_point = outListFolder + "aggregated_nodes.shp"
        outPathPipes = outListFolder + "sewers.shp"
        outList_nodes = outListFolder + "nodes.shp"
        outList_pumpes = outListFolder + "pumpes.shp"
        outList_WWTPs = outListFolder + "WWTPs.shp"
        aggregatetStreetFile = outListFolder  + "streetGraph.shp"
        allNodesPath = outListFolder + "allNodes.shp"
        outPath_StartNode = outListFolder + "startnode.shp"
    
        # Create .txt files for SNIP Calculation
        if OnlyExecuteMerge == 0:
            buildPoints = readBuildingPoints(buildings)                                         # Read out buildings. read ID from Field
            arcpy.AddMessage("Building List was read out...")
        
            # If no DEM is given, create  virtual flat DEM
            if DEMExists == "No":
                rasterSize = 25                                                                 # Raster properties for virtual DEM
                rasterPoints = createVirtualDEM(rasterSize, border, buildPoints)                # Create virtual DEM with no heights
                rasterSizeList = [rasterSize]
            else:
                anzNumberOfConnections = len(buildPoints)                                       # used for setting new IDs
                if demAlreadyReadOut == 1:    
                    arcpy.AddMessage("start reading in DEM from already read out file")                                                  # In case DEM was read out elsewhere
                    
                    # SACHSEN
                    #pathRasterPoints = "Q:\Abteilungsprojekte\eng\SWWData\Eggimann_Sven\07-Fallbeispiele\00-Sachsen\01-Daten\01-Borna\_SNIP250\rasterPoints.txt"
                    pathRasterPoints = "Q:\Abteilungsprojekte\eng\SWWData\Eggimann_Sven\07-Fallbeispiele\00-Sachsen\01-Daten\02-Espenhain\_SNIP3\rasterPoints.txt"
                    rasterPoints, rasterSize = readInRasterPoints(pathRasterPoints)
                    rasterSizeList = [rasterSize] 
                else:
                    arcpy.AddMessage("start reading out DEM")
                    rasterPoints, rasterSize = readRasterPoints(inDHM, anzNumberOfConnections)  # Read out DEM
                    rasterSizeList = [rasterSize]                                               # Store raster size
                    arcpy.AddMessage("DEM was read out: " + str(len(rasterPoints)))
                    arcpy.AddMessage("Raster Resolution: " + str(rasterSize))
                
            nearPoints = readClosestPointsAggregate(buildings)                                  # Read the near_X, near_Y -points of the buildings into a list 
        
            # Aggregate houses on the street and create point file (sewer inlets).
            aggregatetPoints, buildings = aggregate(nearPoints, AggregateKritStreet, outListStep_point, minTD)
            arcpy.AddMessage("Nodes are aggregated..." + str(len(aggregatetPoints)))
            
            # Update field for the sewer inlets
            updateFieldStreetInlets(outListStep_point)
            writefieldsStreetInlets(outListStep_point, aggregatetPoints)
            
            # Split street network with the sewer inlets
            arcpy.AddMessage("the street network gets splitted at the sewer inlets...")
            splitStreetwithInlets(in_street, outListStep_point, aggregatetStreetFile)           # Split with aggregatetPoints
            
            
            # Update fields in splitted street and add StreetID, the height to each points is assigned from closest DEM-Point
            arcpy.AddMessage("fields are updated...")
            updatefieldsPoints(aggregatetStreetFile)
            
            arcpy.AddMessage("streetVertices are read in and height assigned from aggregatetPoints..." + str(len(aggregatetStreetFile)))
            streetVertices = readOutAllStreetVerticesAfterAggregation(aggregatetStreetFile, rasterPoints, rasterSize)
                           
            # Because after ArcGIS Clipping slightly different coordinate endings, change them in aggregatetPoints (different near-analysis)
            aggregatetPoints =  correctCoordinatesAfterClip(aggregatetPoints, streetVertices)
        
            # Build dictionary with vertexes and save which buildings are connected to which streetInlet
            forSNIP, aggregatetPoints = assignStreetVertAggregationMode(aggregatetPoints, streetVertices, minTD)
        
            # Write out all relevant nodes
            drawAllNodes(streetVertices, allNodesPath)
            updateFieldNode(allNodesPath)
            writefieldsAllNodes(allNodesPath, streetVertices)
            
            # Create list with edges from street network
            edges = createStreetGraph(aggregatetStreetFile)
            arcpy.AddMessage("edges were read in...")
            
            # Assign id and distance to edges
            arcpy.AddMessage("assign Id and distance to edges")
            edgeList = addedgesID(edges, streetVertices)
            
            # Create graph
            streetGraph = appendStreetIDandCreateGraph(edgeList) 
            arcpy.AddMessage("graph from street network is created...")
        
            aggregatetPoints = assignHighAggregatedNodes(aggregatetPoints, rasterPoints, rasterSize, minTD)  # Assign High to Aggregated Nodes

            # Add all buildings far from the road network 
            forSNIP = addBuildingsFarFromRoadTo(aggregatetPoints, forSNIP)  
            
            # ======================================================================================================================================================================================
            # SNIP Calculation
            # ======================================================================================================================================================================================            
            _, startnode, startX, startY = densityBasedSelection(aggregatetPoints, tileSize)        # Select start node with highest density
            arcpy.AddMessage("Startnode: " + str(startnode))
                    
            #randEntry = choice(aggregatetPoints)                                    # Select random start node
            #startnode, startX, startY = randEntry[0], randEntry[1], randEntry[2]
            #startnode = selectLowestNode(aggregatetPoints)                          # Select lowest start node
            
            # Write to .txt files
            writeTotxt(outListFolder, "inputParameters", InputParameter)
            writeTotxt(outListFolder, "rasterPoints", rasterPoints)
            writeTotxt(outListFolder, "rastersize", rasterSizeList)
            writeTotxt(outListFolder, "buildPoints", buildPoints)
            writeTotxt(outListFolder, "forSNIP", forSNIP)
            writeTotxt(outListFolder, "aggregatetPoints", aggregatetPoints)
            writeTotxt(outListFolder, "forSNIP", forSNIP)
            writeTotxt(outListFolder, "streetVertices", streetVertices)
            writeTotxt(outListFolder, "edgeList", edgeList)
            writeToDoc(outListFolder, "streetGraph", streetGraph)
            writeTotxt(outListFolder, "buildings", buildings)
        else:
            forSNIP, streetGraph, startnode, edgeList, streetVertices, rasterSize, buildPoints, rasterPoints, aggregatetPoints = None, None, None, None, None, None, None, None, None
         
        if onlyTxtReadOut == 1:                         # If only .txt files are read out
            print("Finished reading out .txt files")
        else:   
            
            ExpansionTime, MergeTime, sewers, pointsPrim, WWTPs, wtpstodraw, pumpList, edgeList, completePumpCosts, completeWWTPCosts, completePublicPipeCosts, totalSystemCosts, buildings, buildPoints, aggregatetPoints = SNIP(OnlyExecuteMerge, outListFolder, 1, forSNIP, 1, streetGraph, startnode, edgeList, streetVertices, rasterSize, buildPoints, buildings, rasterPoints, InputParameter, aggregatetPoints)

            # Calculate Costs of private sewers
            totCostPrivateSewer = costsPrivateSewers(buildings, buildPoints, pipeDiameterPrivateSewer, avgTDprivateSewer, discountYearsSewers, interestRate, operationCosts, fc_SewerCost) # Calculate costs of Private Sewers
            print("Costs are calculated...")
        
            # Draw optimal infrastructure layout in ArcGIS
            if OnlyExecuteMerge == 0:    
                    inputStartNod = [[startnode, startX, startY]]           
                    startNodeToDraw = createPolyPoint(inputStartNod, outPath_StartNode)     # Draw the wtps in ArcGIS
                    writeStartnode(outPath_StartNode, startNodeToDraw)                      # Write out startnode
                    arcpy.AddMessage("startnode is drawn--")
                
            # Draw the graphs in ArcGIS, DrawHouse Connections
            list_GIS = primResultGISList(drawHouseConnections, sewers, pointsPrim, streetVertices, buildings, buildPoints, rasterPoints, edgeList)
            writeOutPipes(outListFolder, "info_pipes", list_GIS)
            
            createPolyLine(list_GIS, outPathPipes)                              # Draw Pipes in ArcGIS
            arcpy.AddMessage("The sewers are drawn")
            
            wwtoArDrawn = createPolyPointWWTP(wtpstodraw, outList_WWTPs)        # Draw the wtps in ArcGIS
                
            if wwtoArDrawn == 1:
                writeWWTPs(outList_WWTPs, wtpstodraw)
                arcpy.AddMessage("The wwtps are drawn...")
            else:
                arcpy.AddMessage("Error: No WWTPs to draw")
                        
            #Draw the nodes in ArcGIS
            createPolyPoint(pointsPrim, outList_nodes)
            writefieldsNodes(outList_nodes, pointsPrim)
            arcpy.AddMessage("The nodes are drawn...")
                
            #Draw Pumps
            draw = createPolyPointPump(pumpList, outList_pumpes)
            if draw == True:
                writeFieldNodesPUMPS(outList_pumpes, pumpList)
                arcpy.AddMessage("The pumps are drawn...")
        
            # Statistics
            totCostPrivateSewer = costsPrivateSewers(buildings, buildPoints, pipeDiameterPrivateSewer, avgTDprivateSewer, discountYearsSewers, interestRate, operationCosts, fc_SewerCost) # Calculate costs of Private Sewers
            print("Costs are calculated...")
            
            # Sum whole System Costs
            totSystemCostsNoPrivate = completePumpCosts  + completeWWTPCosts + completePublicPipeCosts
            totSystemCostsWithPrivate = completePumpCosts  + completeWWTPCosts + completePublicPipeCosts + totCostPrivateSewer
            
            # Calculate number of neighbours (density)
            densityRaster, startnode, startX, startY = densityBasedSelection(aggregatetPoints, tileSize)        # Select startnode with highest density
            for entry in densityRaster:
                if startX >= densityRaster[entry][0] and startX < (densityRaster[entry][0] + tileSize) and startY > (densityRaster[entry][1] - tileSize) and startY <= densityRaster[entry][1]:
                    nrOfNeighboursDensity = densityRaster[entry][2]
                    break
        
        # Write out statistics
        statistics = getStatistics(startnode, sewers, pointsPrim, aggregatetPoints, WWTPs, edgeList, nrOfNeighboursDensity, EW_Q, buildings, buildPoints)     # Calculate statistics
        statistics.append(completePumpCosts)                    # Append costs
        statistics.append(completeWWTPCosts)                    # Append costs
        statistics.append(completePublicPipeCosts)              # Append costs
        statistics.append(totCostPrivateSewer)                  # Append costs
        statistics.append(totSystemCostsNoPrivate)              # Append costs
        statistics.append(totSystemCostsWithPrivate)            # Append costs
        writeTotxt(outListFolder, "statistics", statistics)     # Append costs
else:    
    outListStep_point = outListFolder + "aggregated_nodes.shp"
    outPathPipes = outListFolder + "sewers.shp"
    outList_nodes = outListFolder + "nodes.shp"
    outList_pumpes = outListFolder + "pumpes.shp"
    outList_WWTPs = outListFolder + "WWTPs.shp"
    aggregatetStreetFile = outListFolder  + "streetGraph.shp"
    allNodesPath = outListFolder + "allNodes.shp"
    outPath_StartNode = outListFolder + "startnode.shp"
    
    '''# Create folder to store results 
    outListFolder = outListFolder + "_SNIP" + "/"     
    if not os.path.exists(outListFolder):
        os.mkdir(outListFolder)
    '''

    # Create .txt files for SNIP Calculation
    if OnlyExecuteMerge == 0:                                                               # If Expansion and Merging Module are executed
        print("GEB: " + str(buildings))
        buildPoints = readBuildingPoints(buildings)                                         # Read out buildings. read ID from Field
        print("Building List was read out...")
        print("len: " + str(len(buildPoints)))
        
        # If no DEM is given, create  virtual flat DEM
        if DEMExists == "No":
            rasterSize = 25                                                                 # Raster properties for virtual DEM
            rasterPoints = createVirtualDEM(rasterSize, border, buildPoints)                # Create virtual DEM with no heights
            rasterSizeList = [rasterSize]
        else:
            anzNumberOfConnections = len(buildPoints)                                       # used for setting new IDs
            if demAlreadyReadOut == 1:                                                      # In case DEM was read out elsewhere
                
                #pathRasterPoints = "Q://Abteilungsprojekte//eng//SWWData//Eggimann_Sven//07-Fallbeispiele//00-Sachsen//01-Daten//01-Borna//_SNIP250//rasterPoints.txt"
                #pathRasterPoints = "Q://Abteilungsprojekte//eng//SWWData//Eggimann_Sven//07-Fallbeispiele//00-Sachsen//01-Daten//02-Espenhain//_SNIP3//rasterPoints.txt"
                print("pathRasterPoints: " + str(pathRasterPoints))
                
                rasterPoints, rasterSize = readInRasterPoints(pathRasterPoints)
                rasterSizeList = [rasterSize] 
                arcpy.AddMessage("rasterPoints: " + str(rasterPoints[:10]))
            else:
                arcpy.AddMessage("start reading out DEM")
                rasterPoints, rasterSize = readRasterPoints(inDHM, anzNumberOfConnections)  # Read out DEM
                rasterSizeList = [rasterSize]                                               # Store raster size
                arcpy.AddMessage("DEM was read out: " + str(len(rasterPoints)))
                arcpy.AddMessage("Raster Resolution: " + str(rasterSize))
            
        print("buildings: " + str(len(buildPoints)))
        nearPoints = readClosestPointsAggregate(buildings)                                  # Read the near_X, near_Y -points of the buildings into a list 
        
        print("nearPoints: " + str(len(nearPoints)))
        print("outListStep_point: " + str(outListStep_point))
        
        # Aggregate houses on the street and create point file (sewer inlets).
        aggregatetPoints, buildings = aggregate(nearPoints, AggregateKritStreet, outListStep_point, minTD)
        arcpy.AddMessage("Nodes are aggregated..." + str(len(aggregatetPoints)))
        
        # Update field for the sewer inlets
        updateFieldStreetInlets(outListStep_point)
        writefieldsStreetInlets(outListStep_point, aggregatetPoints)
        
        # Split street network with the sewer inlets
        arcpy.AddMessage("the street network gets splitted at the sewer inlets...")
        splitStreetwithInlets(in_street, outListStep_point, aggregatetStreetFile)           # Split with aggregatetPoints
        
        # Update fields in splitted street and add StreetID, the height to each points is assigned from closest DEM-Point
        arcpy.AddMessage("fields are updated...")
        updatefieldsPoints(aggregatetStreetFile)
        
        arcpy.AddMessage("streetVertices are read in and height assigned from aggregatetPoints..." + str(len(aggregatetStreetFile)))
        streetVertices = readOutAllStreetVerticesAfterAggregation(aggregatetStreetFile, rasterPoints, rasterSize)
                       
        # Because after ArcGIS Clipping slightly different coordinate endings, change them in aggregatetPoints (different near-analysis)
        aggregatetPoints =  correctCoordinatesAfterClip(aggregatetPoints, streetVertices)
    
        # Build dictionary with vertexes and save which buildings are connected to which streetInlet
        forSNIP, aggregatetPoints = assignStreetVertAggregationMode(aggregatetPoints, streetVertices, minTD)
    
        # Write out all relevant nodes
        drawAllNodes(streetVertices, allNodesPath)
        updateFieldNode(allNodesPath)
        writefieldsAllNodes(allNodesPath, streetVertices)
        
        # Create list with edges from street network
        edges = createStreetGraph(aggregatetStreetFile)
        arcpy.AddMessage("edges were read in...")
        
        # Assign id and distance to edges
        arcpy.AddMessage("assign Id and distance to edges")
        edgeList = addedgesID(edges, streetVertices)
        
        # Create graph
        streetGraph = appendStreetIDandCreateGraph(edgeList) 
        arcpy.AddMessage("graph from street network is created...")
    
        aggregatetPoints = assignHighAggregatedNodes(aggregatetPoints, rasterPoints, rasterSize, minTD)  # Assign High to Aggregated Nodes
        arcpy.AddMessage("Points are aggregated...")
        
        # Add all buildings far from the road network 
        forSNIP = addBuildingsFarFromRoadTo(aggregatetPoints, forSNIP)  
        arcpy.AddMessage("ready for SNIP Calculation...")
        
        # SNIP Calculation
        _, startnode, startX, startY = densityBasedSelection(aggregatetPoints, tileSize)                # Select start node with highest density  
        #randEntry = choice(aggregatetPoints)                                                           # Select random start node
        #startnode, startX, startY = randEntry[0], randEntry[1], randEntry[2]
        #startnode = selectLowestNode(aggregatetPoints)                                                 # Select lowest start node
        arcpy.AddMessage("Startnode: " + str(startnode))
        
        # Write to .txt files
        writeTotxt(outListFolder, "inputParameters", InputParameter)
        writeTotxt(outListFolder, "rasterPoints", rasterPoints)
        writeTotxt(outListFolder, "rastersize", rasterSizeList)
        writeTotxt(outListFolder, "buildPoints", buildPoints)
        writeTotxt(outListFolder, "forSNIP", forSNIP)
        writeTotxt(outListFolder, "aggregatetPoints", aggregatetPoints)
        writeTotxt(outListFolder, "forSNIP", forSNIP)
        writeTotxt(outListFolder, "streetVertices", streetVertices)
        writeTotxt(outListFolder, "edgeList", edgeList)
        writeToDoc(outListFolder, "streetGraph", streetGraph)
        writeTotxt(outListFolder, "buildings", buildings)
    else:
        forSNIP, streetGraph, startnode, edgeList, streetVertices, rasterSize, buildPoints, rasterPoints, aggregatetPoints = None, None, None, None, None, None, None, None, None
     
    if onlyTxtReadOut == 1:                         # If only .txt files are read out
        print("Finished reading out .txt files")
    else:                                           # Run SNIP
        ExpansionTime, MergeTime, sewers, pointsPrim, WWTPs, wtpstodraw, pumpList, edgeList, completePumpCosts, completeWWTPCosts, completePublicPipeCosts, totalSystemCosts, buildings, buildPoints, aggregatetPoints = SNIP(OnlyExecuteMerge, outListFolder, 1, forSNIP, 1, streetGraph, startnode, edgeList, streetVertices, rasterSize, buildPoints, buildings, rasterPoints, InputParameter, aggregatetPoints)
    
        totCostPrivateSewer = costsPrivateSewers(buildings, buildPoints, pipeDiameterPrivateSewer, avgTDprivateSewer, discountYearsSewers, interestRate, operationCosts, fc_SewerCost) # Calculate costs of Private Sewers
        print("Private sewer costs are calculated...")
        
        arcpy.AddMessage("totalSystemCosts: " + str(totalSystemCosts))
        
        # Draw optimal infrastrucutre layout in ArcGIS
        if OnlyExecuteMerge == 0:    
            inputStartNod = [[startnode, startX, startY]]           
            startNodeToDraw = createPolyPoint(inputStartNod, outPath_StartNode)     # Draw the wtps in ArcGIS
            writeStartnode(outPath_StartNode, startNodeToDraw)                      # Write out startnode
            arcpy.AddMessage("startnode is drawn")
            
        # Draw the graphs in ArcGIS, DrawHouse Connections
        list_GIS = primResultGISList(drawHouseConnections, sewers, pointsPrim, streetVertices, buildings, buildPoints, rasterPoints, edgeList)
        writeOutPipes(outListFolder, "info_pipes", list_GIS)
        
        createPolyLine(list_GIS, outPathPipes)                              # Draw Pipes in ArcGIS
        wwtoArDrawn = createPolyPointWWTP(wtpstodraw, outList_WWTPs)        # Draw the wtps in ArcGIS
            
        if wwtoArDrawn == 1:
            writeWWTPs(outList_WWTPs, wtpstodraw)
            arcpy.AddMessage("The wwtps are drawn...")
        else:
            arcpy.AddMessage("Error: No WWTPs to draw")
                    
        #Draw the nodes in ArcGIS
        createPolyPoint(pointsPrim, outList_nodes)
        writefieldsNodes(outList_nodes, pointsPrim)
        arcpy.AddMessage("The nodes are drawn...")
            
        #Draw Pumps
        draw = createPolyPointPump(pumpList, outList_pumpes)
        if draw == True:
            writeFieldNodesPUMPS(outList_pumpes, pumpList)
            arcpy.AddMessage("The pumps are drawn...")
        
        # Statistics
        totCostPrivateSewer = costsPrivateSewers(buildings, buildPoints, pipeDiameterPrivateSewer, avgTDprivateSewer, discountYearsSewers, interestRate, operationCosts, fc_SewerCost) # Calculate costs of Private Sewers
        print("Costs are calculated...")
        
        # Sum whole System Costs
        totSystemCostsNoPrivate = completePumpCosts  + completeWWTPCosts + completePublicPipeCosts
        totSystemCostsWithPrivate = completePumpCosts  + completeWWTPCosts + completePublicPipeCosts + totCostPrivateSewer
        
        # Calculate number of neighbours (density)
        densityRaster, startnode, startX, startY = densityBasedSelection(aggregatetPoints, tileSize)        # Select startnode with highest density
        for entry in densityRaster:
            if startX >= densityRaster[entry][0] and startX < (densityRaster[entry][0] + tileSize) and startY > (densityRaster[entry][1] - tileSize) and startY <= densityRaster[entry][1]:
                nrOfNeighboursDensity = densityRaster[entry][2]
                break

    # Write out statistics
    statistics = getStatistics(startnode, sewers, pointsPrim, aggregatetPoints, WWTPs, edgeList, nrOfNeighboursDensity, EW_Q, buildings, buildPoints)     
    statistics.append(completePumpCosts)                    # Append costs to statistics.
    statistics.append(completeWWTPCosts)                    # Append costs to statistics.
    statistics.append(completePublicPipeCosts)              # Append costs to statistics.
    statistics.append(totCostPrivateSewer)                  # Append costs to statistics.
    statistics.append(totSystemCostsNoPrivate)              # Append costs to statistics.
    statistics.append(totSystemCostsWithPrivate)            # Append costs to statistics.
    writeTotxt(outListFolder, "statistics", statistics)     # Append costs to statistics.
