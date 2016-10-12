# ======================================================================================
# Copyright 2014  Swiss Federal Institute of Aquatic Science and Technology
#
# THIRD PAPER
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
# Date:      1.07.2015
# Autor:     Eggimann Sven
# ======================================================================================
#import os, sys
#sys.path.append("c:\\program files (x86)\\arcgis\\desktop10.2\\arcpy")
import arcpy

import os, sys               # General Imports
import gc; gc.disable()             # Don't allow garbage collection
from itertools import product

# Folder with all communities stored for III Paper # Path to Folder with Communities in it. 
mainFolder = "Q:\\Abteilungsprojekte\\eng\\SWWData\\Eggimann_Sven\\07-Fallbeispiele\\03-Glarus\\01-GIS_Data\\Glarus_communities"


#mainFolder ="Q:\\Abteilungsprojekte\\eng\\SWWData\\Eggimann_Sven\\07-Fallbeispiele\\02_GIS_BERN\\561_Adelboden"
#mainFolder ="Q:\\Abteilungsprojekte\\eng\\SWWData\\Eggimann_Sven\\07-Fallbeispiele\\02_GIS_BERN\\604_Bleiken"


# Change after the insallation of the ArcToolBox
pythonScriptPath = "Q://Abteilungsprojekte/Eng/SWWData/Eggimann_Sven/09-GIS-Python/0-PythonFiles/03-third_paper/"  # Path where SNIP Python files are stored
#pythonScriptPath = "..../Folder_With_SNIP_Python_Files/"  # Path where SNIP Python files are stored

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
in_street = sys.argv[1]                                 # Street shape file
buildings = sys.argv[3]                                 # Building shape file
inDHM = sys.argv[4]                                     # DEM point shape file (DEM needs to be converted to points)
outListFolder = sys.argv[2].replace("\\","/") + "/"     # Output Folder

#arcpy.AddMessage("INPUT ARCGIS")
#arcpy.AddMessage(in_street)
#arcpy.AddMessage(buildings)
#arcpy.AddMessage(inDHM)
#arcpy.AddMessage(outListFolder)

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
AggregateKritStreet = 1 # Must besmaller than tile size!                   # [m] How long the distances on the roads can be in maximum be before they get aggregated on the street network (must not be 0)
border = 3000                               # [m] How large the virtual dem borders are around topleft and bottom
tileSize = 50                               # [m] for selection of density based starting node
    
pipeDiameterPrivateSewer = 0.25             # Cost Assumptions private sewers: Pipe Diameter
avgTDprivateSewer = 0.25                    # Cost Assumptions private sewers: AVerage Trench Depth
    
# ArcGIS Representation related
drawHouseConnections = 1                    # 1: House connections are drawn in ArcGIS, 0: House Connections are not drawn in ArcGIS
interestRate = float(interestRate) / 100.0  # Reformulate real interest rate

# Add parameters into List for SNIP Algorithm
InputParameter = [minTD, maxTD, minSlope, f_merge, resonableCostsPerEW, neighborhood, f_street, pricekWh, pumpingYears, discountYearsSewers, interestRate, stricklerC, EW_Q,  wwtpLifespan, operationCosts, pumpInvestmentCosts,  f_topo, fc_SewerCost, fc_wwtpOpex, fc_wwtpCapex]


# ---------------------------
# THIRD PAPER
# ---------------------------
#numberOfSNIPruns = 1 # plus immer noch most dense and lowest

# Get all folder paths
allCommunitiesPaths = getAllFolders(mainFolder) 

arcpy.AddMessage( "--START THIRD PAPER--" + str(allCommunitiesPaths))

# Iterate folder
for i in allCommunitiesPaths[0:1]: #[24:]: #[1:2]: #[27:28]: #[15:16]: #[26:27]:
    
    onlyReadIn = False
    
    arcpy.AddMessage("Folder: " + str(i))

    startingNodes = [] # List with starting nodes

    in_street = i + str("streetNetwork.shp")           # Name of street network
    buildings = i + str("buildings_inhabited.shp")        # name of buildings
    inDHM  = i + str("dem_point.shp")                 # name of DEM
    
    '''# Input Parameter for SNIP_III
    in_street = i + str("street.shp")           # Name of street network
    buildings = i + str("buildings.shp")        # name of buildings
    inDHM  = i + str("DEM.shp")                 # name of DEM
    '''
    # Create folder to store result
    folderName = i
    outListFolderInitial = i + "_SNIP_FILES" + "\\"
    
    # Folder to store results
    nameSubFolder = "ResultSNIP" #_050"
    
    # Only Read In
    if onlyReadIn == True:

        outListFolderOneLevelUp = folderName + "ResultSNIP"      # Create result folder
        if not os.path.exists(outListFolderOneLevelUp):
            os.mkdir(outListFolderOneLevelUp)
                
        if not os.path.exists(outListFolderInitial):
            os.mkdir(outListFolderInitial)
            
        arcpy.AddMessage(" ")
        arcpy.AddMessage("Input Files for SNIP")
        arcpy.AddMessage("====================")
        arcpy.AddMessage("Current Folder: " + str(i))
        arcpy.AddMessage(in_street)
        arcpy.AddMessage(buildings)
        arcpy.AddMessage(inDHM)
        arcpy.AddMessage(outListFolderInitial)
        
        outListStep_point = outListFolderInitial + "aggregated_nodes.shp"
        aggregatetStreetFile = outListFolderInitial  + "streetGraph.shp"
        allNodesPath = outListFolderInitial + "allNodes.shp"
        
        # Create .txt files for SNIP Calculation and data preparation
        buildPoints = readBuildingPoints(buildings)                                                                 # Read out buildings. read ID from Field
        
        anzNumberOfConnections = len(buildPoints)                                                                   # used for setting new IDs
        arcpy.AddMessage("Start reading in raster points")
        rasterPoints, rasterSize = readRasterPoints(inDHM, anzNumberOfConnections)                                  # Read out DEM
        arcpy.AddMessage("finished reading in raster points")
        rasterSizeList = [rasterSize]                                                                               # Store raster size
        
        nearPoints = readClosestPointsAggregate(buildings)                                                          # Read the near_X, near_Y -points of the buildings into a list 
        aggregatetPoints, buildings = aggregate(nearPoints, AggregateKritStreet, outListStep_point, minTD)          # Aggregate houses on the street and create point file (sewer inlets).
        updateFieldStreetInlets(outListStep_point)                                                                  # Update field for the sewer inlets
        writefieldsStreetInlets(outListStep_point, aggregatetPoints)                                                # Write to shapefile
        splitStreetwithInlets(in_street, outListStep_point, aggregatetStreetFile)                                   # Split street network with the sewer inlets
        updatefieldsPoints(aggregatetStreetFile)                                                                    # Update fields in splitted street and add StreetID, the height to each points is assigned from closest DEM-Point
        streetVertices = readOutAllStreetVerticesAfterAggregation(aggregatetStreetFile, rasterPoints, rasterSize)
        aggregatetPoints =  correctCoordinatesAfterClip(aggregatetPoints, streetVertices)                           # Because after ArcGIS Clipping slightly different coordinate endings, change them in aggregatetPoints (different near-analysis)
        forSNIP, aggregatetPoints = assignStreetVertAggregationMode(aggregatetPoints, streetVertices, minTD)        # Build dictionary with vertexes and save which buildings are connected to which streetInlet   
        drawAllNodes(streetVertices, allNodesPath)                                                                  # Write out all relevant nodes
        updateFieldNode(allNodesPath)
        writefieldsAllNodes(allNodesPath, streetVertices)
        edges = createStreetGraph(aggregatetStreetFile)                                                             # Create list with edges from street network
        edgeList = addedgesID(edges, streetVertices)                                                                # Assign id and distance to edges
        streetGraph = appendStreetIDandCreateGraph(edgeList)                                                        # Create graph
        arcpy.AddMessage("RASTERSZE: " + str(rasterSize))
        aggregatetPoints = assignHighAggregatedNodes(aggregatetPoints, rasterPoints, rasterSize, minTD)             # Assign High to Aggregated Nodes
        forSNIP = addBuildingsFarFromRoadTo(aggregatetPoints, forSNIP)                                              # Add all buildings far from the road network 
    
        writeTotxt(outListFolderInitial, "inputParameters", InputParameter)                                         # Write to .txt files
        writeTotxt(outListFolderInitial, "rasterPoints", rasterPoints)                                                     # Write to .txt files
        writeTotxt(outListFolderInitial, "rastersize", rasterSizeList)                                                     # Write to .txt files
        writeTotxt(outListFolderInitial, "buildPoints", buildPoints)                                                       # Write to .txt files
        writeTotxt(outListFolderInitial, "forSNIP", forSNIP)                                                               # Write to .txt files
        writeTotxt(outListFolderInitial, "aggregatetPoints", aggregatetPoints)                                             # Write to .txt files
        writeTotxt(outListFolderInitial, "forSNIP", forSNIP)                                                               # Write to .txt files
        writeTotxt(outListFolderInitial, "streetVertices", streetVertices)                                                 # Write to .txt files
        writeTotxt(outListFolderInitial, "edgeList", edgeList)                                                             # Write to .txt files
        writeToDoc(outListFolderInitial, "streetGraph", streetGraph)                                                       # Write to .txt files
        writeTotxt(outListFolderInitial, "buildings", buildings)                                                           # Write to .txt files
        arcpy.AddMessage("...ready for SNIP Calculation")
        # Only to iterate folders and read in Files
    
    if onlyReadIn == False:
        
        # Create folders
        createFoldre = True
        
        if not os.path.exists(outListFolderInitial):    
            os.mkdir(outListFolderInitial)

        if createFoldre == True:
            outListFolderOneLevelUp = folderName + nameSubFolder      # Create result folder
            if not os.path.exists(outListFolderOneLevelUp):
                os.mkdir(outListFolderOneLevelUp)
        
        # Model Parameters
        
        # Standard run assumptions
        assumptionPEofOST = 10                          # Assumption of OST Size PE  
        PPP2014 = 0.73                                  # 1$ = 1.37 CHF --> 0.73 CHF # CONVERT SEWER COSTS IN DOLLAR 2014
        
        # For Boxplot- Sensitibity
        minSlopeList = [0.5, 1.5]                       # with startnode already run with standard parameter # First one must be 1 because this is standard slope for representation
        #minSlopeList = []                              # with startnode already run with standard parameter
        
        perecentageIdleCapacityList = [0, 0.5, 1.0]     # Percentage to generate WWTP capacity. First entry must be Zero (because of standard representatio)
        assumptionSizeofOST = [10, 5, 15]               # First Entry is standard for representation
        assumptionTransportOST =  [1.0, 0.8, 1.2]       # Percentage of cost variations
        
        # Startnode Selection
        pathForaggregatedPoints = outListFolderInitial + "aggregatetPoints.txt"
        aggregatetPoints = readInforSNIP(pathForaggregatedPoints)                       # Read in aggregated nodes
    
        # Densest Starting Node
        _, startnodeDensity, startXDensity, startYDensity = densityBasedSelection(aggregatetPoints, tileSize)     # Select start node with highest density  
        startingNodes.append([startnodeDensity, startXDensity, startYDensity])
        
        # Lowest Starting node
        #lowestNode, lowestX, lowestY, _ = selectLowestNode(aggregatetPoints)
        #startingNodes.append([lowestNode, lowestX, lowestY])
        #arcpy.AddMessage("LOWESTNODE: " + str(lowestNode))
        #arcpy.AddMessage("lowestX: " + str(lowestX))
        #arcpy.AddMessage("lowestY: " + str(lowestY))
        
        #startingNodes = selectRandomStartingNodes(startingNodes, aggregatetPoints, numberOfSNIPruns)
        arcpy.AddMessage("Number of starting Nodes: " + str(startingNodes))
        
        currentSNIPrun = 0
        listWithResults = []    # List to store SNIP results
        
        # Run SNIP with standard parameter with starting node
        for SNIPstartNode in startingNodes:
            currentSNIPrun += 1
            
            # Read in data
            arcpy.AddMessage(" ")
            arcpy.AddMessage("Read in already read out files..........." + str(outListFolderInitial))
            arcpy.AddMessage(" ")
            pathForSNIP = outListFolderInitial + "forSNIP" + ".txt"
            pathEdgeList = outListFolderInitial + "edgeList" + ".txt"
            pathStreetGraph = outListFolderInitial + "streetGraph" + ".txt"
            pathstreetVertices = outListFolderInitial + "streetVertices.txt"  
            pathbuildings = outListFolderInitial + "buildings.txt"
            pathbuildPoints = outListFolderInitial + "buildPoints.txt"
            pathForaggregatedPoints = outListFolderInitial + "aggregatetPoints.txt"
            pathRasterPnts = outListFolderInitial + "rasterPoints.txt"
            pathtotalAreaCaseStudy = folderName + "totalAreaCaseStudy.txt"
            
            forSNIP = readInforSNIP(pathForSNIP)                                            # Read in forPrim
            edgeList = readInedgesID(pathEdgeList)
            streetGraph = readInDictionary(pathStreetGraph)                                 # Read in edges List
            streetVertices = readInstreetVertices(pathstreetVertices)   
            buildings = readInbuildings(pathbuildings, 0)
            buildPoints = readInbuildPoints(pathbuildPoints)                                # Read in buildings points
            aggregatetPoints = readInforSNIP(pathForaggregatedPoints)                       # Read in aggregated nodes
            totalAreaCaseStudy = readInAreaTextFile(pathtotalAreaCaseStudy)                 # Read in AREA from .txt file
            rasterPoints, rasterSize = readInRasterPoints(pathRasterPnts)
            
            startnode, startX, startY= SNIPstartNode[0], SNIPstartNode[1], SNIPstartNode[2]
            arcpy.AddMessage("totalAreaCaseStudy: " + str(totalAreaCaseStudy))
    
            # Generate result folder
            outListFolder = folderName + nameSubFolder + "//" + "SNIP_" + str(currentSNIPrun) + "\\"       
            if not os.path.exists(outListFolder):
                os.mkdir(outListFolder)
    
            # Run SNIP
            ExpansionTime, MergeTime, sewers, pointsPrim, WWTPs, wtpstodraw, pumpList, edgeList, completePumpCosts, completeWWTPCosts, completePublicPipeCosts, totalSystemCosts, buildings, buildPoints, aggregatetPoints = SNIP(0, outListFolder, 1, forSNIP, 1, streetGraph, startnode, edgeList, streetVertices, rasterSize, buildPoints, buildings, rasterPoints, InputParameter, aggregatetPoints, totalAreaCaseStudy)
            
            # Calculate cost of private sewers
            totCostPrivateSewer = costsPrivateSewers(buildings, buildPoints, pipeDiameterPrivateSewer, avgTDprivateSewer, discountYearsSewers, interestRate, operationCosts, fc_SewerCost) # Calculate costs of Private Sewers
          
            inputStartNod = [[startnode, startX, startY]]           
            
            outListFolderStartnode = outListFolder + "startnode.shp"
            arcpy.AddMessage("write out inptustart" + str(outListFolderStartnode))
            arcpy.AddMessage("Startnode to write out: " + str(inputStartNod))
            
            startNodeToDraw = createPolyPoint(inputStartNod, outListFolderStartnode)     # Draw the wtps in ArcGIS
            writeStartnode(outListFolderStartnode, startNodeToDraw)                      # Write out startnode
                        
            # Draw the graphs in ArcGIS, DrawHouse Connections
            list_GIS = primResultGISList(drawHouseConnections, sewers, pointsPrim, streetVertices, buildings, buildPoints, rasterPoints, edgeList)
            writeOutPipes(outListFolder, "info_pipes", list_GIS)
                
            outListFolderWWTP = outListFolder + "WWTP.shp" 
            outPathPipes = outListFolder + "sewers.shp"
            outList_pumpesPath = outListFolder + "pumps.shp"
            outList_nodes = outListFolder + "nodes.shp"
            
            arcpy.AddMessage("outListFolderWWTP: " + str(outListFolderWWTP))
            
            createPolyLine(list_GIS, outPathPipes)                              # Draw Pipes in ArcGIS
            wwtoArDrawn = createPolyPointWWTP(wtpstodraw, outListFolderWWTP)        # Draw the wtps in ArcGIS
                        
            if wwtoArDrawn == 1:
                writeWWTPs(outListFolderWWTP, wtpstodraw)
            
            #Draw the nodes in ArcGIS
            createPolyPoint(pointsPrim, outList_nodes)
            writefieldsNodes(outList_nodes, pointsPrim)
                        
            #Draw Pumps
            draw = createPolyPointPump(pumpList, outList_pumpesPath)
            if draw == True:
                arcpy.AddMessage("DRAW PUMPS ")
                writeFieldNodesPUMPS(outList_pumpesPath, pumpList)
                
            # Statistics
            totCostPrivateSewer = costsPrivateSewers(buildings, buildPoints, pipeDiameterPrivateSewer, avgTDprivateSewer, discountYearsSewers, interestRate, operationCosts, fc_SewerCost) # Calculate costs of Private Sewers
                    
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
            
            arcpy.AddMessage(totSystemCostsNoPrivate)
    
            
            # Remove first Element
            totalSystemCosts = totalSystemCosts[1:]
            
            # Add first point
            totAnzLeute = totalSystemCosts[0][10]
            firstPnt = [0, 0, 0, 0, 0, 0, assumptionPEofOST, 0, 0, 0, totAnzLeute]
            totalSystemCosts.insert(0, firstPnt)

            SNIPresult= [startnode, startX, startY, totalSystemCosts] #, totSystemCostsNoPrivate, completePumpCosts, completeWWTPCosts, completePublicPipeCosts] #
            
            listWithResults.append(SNIPresult)        
            
        # Get cheapest calculation in List [(startnode, CR, Density, Nr of people....)...]
        cheapest, cheapestStartnode, cheapestStartX, cheapestStartY, chapestRun = getCheapestStartingNode(listWithResults) 
    
        # Add Cheaptest run with standard slope to Slope Calculation Results
        listWithResultsSlope = []
        listWithResultsSlope.append([minSlope, chapestRun]) # Slope, Result
        
        # Rerun SNIP with different starting parameters with the same startnode
        arcpy.AddMessage("------------------------------------------------------------------------------")
        arcpy.AddMessage("Calculate from same staring node with different slope factor..................")
        arcpy.AddMessage("------------------------------------------------------------------------------")

        for slopeSNIP in minSlopeList:
            arcpy.AddMessage("SINP WITH FOLLOWING SLOPE CRITERIA: " + str(slopeSNIP))
            
            minSlope = slopeSNIP        # Replace slope
            InputParameter = [minTD, maxTD, minSlope, f_merge, resonableCostsPerEW, neighborhood, f_street, pricekWh, pumpingYears, discountYearsSewers, interestRate, stricklerC, EW_Q,  wwtpLifespan, operationCosts, pumpInvestmentCosts,  f_topo, fc_SewerCost, fc_wwtpOpex, fc_wwtpCapex]
    
            # Read in data
            pathForSNIP = outListFolderInitial + "forSNIP" + ".txt"
            pathEdgeList = outListFolderInitial + "edgeList" + ".txt"
            pathStreetGraph = outListFolderInitial + "streetGraph" + ".txt"
            pathstreetVertices = outListFolderInitial + "streetVertices.txt"  
            pathbuildings = outListFolderInitial + "buildings.txt"
            pathbuildPoints = outListFolderInitial + "buildPoints.txt"
            pathForaggregatedPoints = outListFolderInitial + "aggregatetPoints.txt"
            
            forSNIP = readInforSNIP(pathForSNIP)                                            # Read in forPrim
            edgeList = readInedgesID(pathEdgeList)
            streetGraph = readInDictionary(pathStreetGraph)                                 # Read in edges List
            streetVertices = readInstreetVertices(pathstreetVertices)   
            buildings = readInbuildings(pathbuildings, 0)
            buildPoints = readInbuildPoints(pathbuildPoints)                                # Read in buildings points
            aggregatetPoints = readInforSNIP(pathForaggregatedPoints)                       # Read in aggregated nodes 
            startnode, startX, startY = cheapestStartnode, cheapestStartX, cheapestStartY   # Select cheapest staring node
        
            # Run SNIP with min and max Slope parameter
            
            # Generate result folder
            outListFolder = folderName + nameSubFolder + "\\"  + "SNIP_" + str(minSlope) + "\\"       
            if not os.path.exists(outListFolder):
                os.mkdir(outListFolder)
    
            # Run SNIP
            ExpansionTime, MergeTime, sewers, pointsPrim, WWTPs, wtpstodraw, pumpList, edgeList, completePumpCosts, completeWWTPCosts, completePublicPipeCosts, totalSystemCosts, buildings, buildPoints, aggregatetPoints = SNIP(0, outListFolder, 1, forSNIP, 1, streetGraph, startnode, edgeList, streetVertices, rasterSize, buildPoints, buildings, rasterPoints, InputParameter, aggregatetPoints, totalAreaCaseStudy)
            
            # Calculate cost of private sewers
            totCostPrivateSewer = costsPrivateSewers(buildings, buildPoints, pipeDiameterPrivateSewer, avgTDprivateSewer, discountYearsSewers, interestRate, operationCosts, fc_SewerCost) # Calculate costs of Private Sewers
          
            inputStartNod = [[startnode, startX, startY]]           
            
            outListFolderStartnode = outListFolder + "startnode.shp"
            arcpy.AddMessage("write out inptustart" + str(outListFolderStartnode))
            
            startNodeToDraw = createPolyPoint(inputStartNod, outListFolderStartnode)     # Draw the wtps in ArcGIS
            writeStartnode(outListFolderStartnode, startNodeToDraw)                      # Write out startnode
                        
            # Draw the graphs in ArcGIS, DrawHouse Connections
            list_GIS = primResultGISList(drawHouseConnections, sewers, pointsPrim, streetVertices, buildings, buildPoints, rasterPoints, edgeList)
            writeOutPipes(outListFolder, "info_pipes", list_GIS)
                
            outListFolderWWTP = outListFolder + "WWTP.shp" 
            outPathPipes = outListFolder + "sewers.shp"
            outList_pumpesPath = outListFolder + "pumps.shp"
            outList_nodes = outListFolder + "nodes.shp"
            
            arcpy.AddMessage("outListFolderWWTP: " + str(outListFolderWWTP))
            
            createPolyLine(list_GIS, outPathPipes)                              # Draw Pipes in ArcGIS
            wwtoArDrawn = createPolyPointWWTP(wtpstodraw, outListFolderWWTP)        # Draw the wtps in ArcGIS
                        
            if wwtoArDrawn == 1:
                writeWWTPs(outListFolderWWTP, wtpstodraw)
            
            #Draw the nodes in ArcGIS
            createPolyPoint(pointsPrim, outList_nodes)
            writefieldsNodes(outList_nodes, pointsPrim)
                        
            #Draw Pumps
            draw = createPolyPointPump(pumpList, outList_pumpesPath)
            if draw == True:
                writeFieldNodesPUMPS(outList_pumpesPath, pumpList)
                
            # Statistics
            totCostPrivateSewer = costsPrivateSewers(buildings, buildPoints, pipeDiameterPrivateSewer, avgTDprivateSewer, discountYearsSewers, interestRate, operationCosts, fc_SewerCost) # Calculate costs of Private Sewers
                    
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
            
            # Remove first Element
            totalSystemCosts = totalSystemCosts[1:]
            
            # Add First point
            totAnzLeute = totalSystemCosts[0][10]
            firstPnt = [0, 0, 0, 0, 0, 0, assumptionPEofOST, 0, 0, 0, totAnzLeute]
            totalSystemCosts.insert(0, firstPnt)

            # Store in List
            listWithResultsSlope.append([minSlope, [startnode, startX, startY, totalSystemCosts]]) # Slope, Result
        
        arcpy.AddMessage("----------------------------------------------------")
        arcpy.AddMessage("Number of slope calculations: " + str(len(listWithResultsSlope)))  
        arcpy.AddMessage("----")
        
        
        #----------------
        # Check if all slope calculations have same Connection rates/Results (e.g. not [0.04, 100] one and [0.05. 110] --> Otherweise
        #-----------------------
        xNormEntries = createNormXValues(1, 2) # Create Norm X Values for interpolation

        optCentralTreatment, optCentralTransport, optDitributedTreatment, optDistributedTransport = [], [], [], []  # Lists with stored results
        
        # -----------------
        # Central Treatment
        # Only calculate for standards scenario treatment costs. We assume that for different slope the treatment costs stay the same. 
        # -----------------
        for centralTrans in listWithResultsSlope[:1]: # Only take first element as we only calculate it for standard slope
            
            # Iterate percentage idle capacity
            for idlePercentage in perecentageIdleCapacityList:
                arcpy.AddMessage("IDLE PERCENTAGE: " + str(idlePercentage))
                capList = []                                                # List to store the three capacity costs
                for e in centralTrans[1][3]:
                    PEWWTP, CR, totCatchementPE = e[6], e[9], e[10]         # Nr of connected people, connection rate, total number of people in catchment
                    #arcpy.AddMessage("PEWWTP: " + str(PEWWTP))
                    #arcpy.AddMessage("CR: " + str(CR))
                    #arcpy.AddMessage("totCatchementPE: " + str(totCatchementPE))
                    
                    # If first node, add costs of dez plant
                    if CR == 0:
                        # For first entry, assume that size of plant is assumptionPEofOST
                        costTreatmentCapacityConsidered = getCostCentralTreatment(assumptionPEofOST, 0, totCatchementPE, assumptionSizeofOST[0]) # Initial costs at level of dez plant
                    
                    costTreatmentCapacityConsidered = getCostCentralTreatment(PEWWTP, idlePercentage, totCatchementPE, assumptionSizeofOST[0])    # WWTP Costs
                    #arcpy.AddMessage("costTreatmentCapacityConsidered: " + str(costTreatmentCapacityConsidered))
                    capList.append([CR, totCatchementPE, costTreatmentCapacityConsidered])

                capList = linearInterpolation(xNormEntries, capList) # linear interpolation OST density & Costs
                #arcpy.AddMessage("capList B: " + str(capList))
                optCentralTreatment.append(capList)
        
        #arcpy.AddMessage("LEngth optCentralTreatment: " + str(len(optCentralTreatment)))
        #arcpy.AddMessage("leng listWithResultsSlope: " + str(len(listWithResultsSlope)))
        
        #prnt("...")
        # -----------------
        # Central Transport
        # -----------------
        # ACHTUNG: SEWER & PUMPS???       
        for centralTrans in listWithResultsSlope:
            #arcpy.AddMessage("Other Slope----------------------------------")
            costTransportCentral = []
            
            # Iterate SNIP result
            for e in centralTrans[1][3]:
                costPipeAndPump = e[3] + e[5] # 3 = Pumps, 5 = Sewers
                #arcpy.AddMessage("costPipeAndPump: " + str(costPipeAndPump)) #arcpy.AddMessage("Pumps:           " + str(e[3])) #arcpy.AddMessage("Sewers:          " + str(e[5]))
                PEWWTP, _, CR, totCatchementPE = e[6], e[7], e[9], e[10]             # Nr of connected people, OST density , connection rate, total number of people in catchment
                costTranCentral = (costPipeAndPump/float(PEWWTP)) * PPP2014               # Pump & Sewer Costs Annuities per capita
                costTransportCentral.append([CR, totCatchementPE, costTranCentral]) 
            
            costTransportCentral = linearInterpolation(xNormEntries, costTransportCentral) # linear interpolation
            optCentralTransport.append(costTransportCentral)
        
        # -----------------
        # Decentral Treatment
        # -----------------       
        for distrTreat in listWithResultsSlope[:1]:     # Only for standard slope 
            for ostSIZEassump in assumptionSizeofOST:   # Iterate OST assumptions
                capList, costTreatmentDistributed= [], []
            
                # Iterate SNIP result
                for e in distrTreat[1][3]:
                    _, _, CR, totCatchementPE = e[6], e[7], e[9], e[10]                  # Nr of connected people, OST density , connection rate, total number of people in catchment
                    costDistrTreat = getCostDistributedTreatment(ostSIZEassump)               # Get annuities for decentral treatment
                    costTreatmentDistributed.append([CR, totCatchementPE, costDistrTreat])
                costTreatmentDistributed = linearInterpolation(xNormEntries, costTreatmentDistributed) # linear interpolation
                optDitributedTreatment.append(costTreatmentDistributed)
        
        # -----------------
        # Distributed Transport
        # -----------------
        # No Variations
        for centralTrans in listWithResultsSlope[:1]: # Only for standard slope 
            for transPortAssumptionCost in assumptionTransportOST:
                costTransportDistributed = []
                
                # Iterate SNIP result
                for e in centralTrans[1][3]:
                    _, dichte, CR, totCatchementPE = e[6], e[7], e[9], e[10]                    # Nr of connected people, OST density , connection rate, total number of people in catchment
                    dichte = fromLocalCRgetDensity(CR)                                          # Convert Connection rate to Density
                    costTranDist = getCostDensity(dichte) * transPortAssumptionCost             # Conert Density to Costs                                 
                    costTransportDistributed.append([CR, totCatchementPE, costTranDist])
                    
                costTransportDistributed = linearInterpolation(xNormEntries, costTransportDistributed) # linear interpolation  
                optDistributedTransport.append(costTransportDistributed)



        # ----------------------
        # Generate Cost Scenario Matrix
        # ----------------------
        costMatrix, Options, nrOfDatasets, selectionMatrix = [], [0,1,2], 4, [] # Parameters for Cost Matrix
        
        # Generate matrix with all possible combinations
        for i in product(Options, repeat=nrOfDatasets): 
            selectionMatrix.append(i) 
        
        arcpy.AddMessage("First Matrix Entry: " + str(selectionMatrix[0]))
        
        for i in selectionMatrix:
            posA, posB, posC, posD = i[0], i[1], i[2], i[3]
            # --> Depending on the slope, redo the calculations for the other parameters as the increments may not be the same!
            costMatrix.append([i, optCentralTreatment[posA], optCentralTransport[posB], optDitributedTreatment[posC], optDistributedTransport[posD]]) # InfoRunMattrix, Central Treatment, CentralTransport, DecentrlaTreamtne,t decentralTransport
            #break # trash NUR BEREITS EIN SZENARIO
            
        arcpy.AddMessage("NUMBER OF SCENARIO: "+ str(len(selectionMatrix)))
        
        # Calculated summed costs & total cost curve
        costMatrixWithSummedCostCurves = []
        
        # Calculate summed cost curves
        for i in costMatrix:
            #arcpy.AddMessage("Cost Matrix Options : " + str(i))
            summedCentral, summedDistributed, totalCostCurve = [], [], []
            
            centTreat, centTrans, distTreat, distTrans = i[1], i[2], i[3], i[4]  

            # Summed Central
            for f, b in zip(centTreat, centTrans):
                CR, CR2 = f[0], b[0]
                if CR != CR2:
                    arcpy.AddMessage(CR)
                    arcpy.AddMessage(CR2)
                    arcpy.AddMessage("ERROR THE SAME aa")
                    prnt("..")
    
                totCen = f[2] + b[2]                        # central treatment + central transport costs
                summedCentral.append([CR, f[1], totCen])
            
            # Summed Distributed  
            for f, b in zip(distTreat, distTrans):
                CR, CR2 = f[0], b[0]
                if CR != CR2:
                    arcpy.AddMessage(CR)
                    arcpy.AddMessage(CR2)
                    arcpy.AddMessage("ERROR THE SAME dd")
                    prnt("..")
    
                totDistr = f[2] + b[2] # central treatment + central transport
                summedDistributed.append([CR, f[1], totDistr])    
            
            # Summ the cost curves total
            for costCentral, costDistr in zip(summedCentral, summedDistributed):
                CRI = costCentral[0]
                totSummedCosts = (CRI * costCentral[2] + (1.0-CRI) * costDistr[2])  # total costs
                #totalCostCurve.append([CRI, costCentral[1], totSummedCosts])
                totalCostCurve.append([CRI, totSummedCosts])
                
            costMatrixWithSummedCostCurves.append([i[0], i[1], i[2], i[3], i[4], summedCentral, summedDistributed, totalCostCurve])
            
            #arcpy.AddMessage("costMatrixWithSummedCostCurves")
            arcpy.AddMessage(costMatrixWithSummedCostCurves)
            arcpy.AddMessage("-------")
            
            # Write data for plot into result folder
            #writeTotxtPlotData(outListFolder, "plot_plotresultData_NORMRUN", costMatrixWithSummedCostCurves)
            
            # Write data for plot with standard parameters (first entry in Matrix)
            # --------------------------------------------------------------------
            if i[0] == (0,0,0,0): # First entry of Matrix
                arcpy.AddMessage("Print out standard run... ")
                outListFolderStandard = folderName + nameSubFolder + "\\"
                writeTotxtPlotData(outListFolderStandard, "plot_Standard_RUN", costMatrixWithSummedCostCurves)
    
        # -----------------------
        # Get Intersection poitns
        # all the different CR
        # -----------------------
        lockInPoints, sustainabilityPoints, marketEquilibriumPoints = [], [], []
    
        # Market Equilibrium
        # ------------------------
        for i in costMatrixWithSummedCostCurves:
            CCCentral, CCDistributed = [], []
                
            for entry in i[5]: #Iterated summed central
                CCCentral.append([entry[0], entry[2]])
                
            for entry in i[6]: #Iterated summed distributred
                CCDistributed.append([entry[0], entry[2]])
                
            intserctions = getIntersection(CCCentral, CCDistributed)
            marketEquilibriumPoints.append(intserctions)
                
        arcpy.AddMessage("marketEquilibriumPoints: " + str(marketEquilibriumPoints))
        
        # Sustainability Point
        # ------------------------
        for i in costMatrixWithSummedCostCurves:
            lowestCR = getSustainabilityPoint(i[7])
            sustainabilityPoints.append(lowestCR)

            # Lock-In Point --> Wtihin Sustainabilty poitn as this info is needed
            CCCentral, CCDistributed = [], []
            sumCentral = i[5]
            sumDistributed = i[6]
            lockPnts = getLockInPoint(sumCentral, sumDistributed, lowestCR)
            
            for i in lockPnts:
                lockInPoints.append(i)
    
        #arcpy.AddMessage("sustainabilityPoints: " + str(sustainabilityPoints))
        #arcpy.AddMessage("lockInPoints: " + str(lockInPoints))
        
        outListFolder = folderName + "//" + nameSubFolder + "\\"  

        # Write out as well values!!!!
        writeTotxtPlotData(outListFolder, "plot_MATRIX_RUNS", costMatrixWithSummedCostCurves)
        writeTotxtPlotData(outListFolder, "plot_sustainabilityPoints", sustainabilityPoints)
        writeTotxtPlotData(outListFolder, "plot_marketEquilibriumPoints", marketEquilibriumPoints) # NEW STR
        
        #Create Cchart
        #plotBarSustainability(outListFolderInitial, sustainabilityPoints) # Plot Sustainability Bar Chart
        
        '''# Lock-In Point
        # ------------------------
        for i in costMatrixWithSummedCostCurves:
            CCCentral, CCDistributed = [], []
            sumCentral = i[5]
            sumDistributed = i[6]
            lockPnts = getLockInPoint(sumCentral, sumDistributed, )
            
            for i in lockPnts:
                lockInPoints.append(i)
        
        arcpy.AddMessage("lockInPoints: " + str(lockInPoints))
        '''
        # Write out 
        #prnt("..")
        #break

    # Create 


arcpy.prnt("..")