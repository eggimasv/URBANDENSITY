# ======================================================================
# Function for readin in .txt files
# ======================================================================
print "Importing: Textreadingfunctions"
import math
import arcpy



# Copitd from old
# ----------------------------

def writeARAs(shapefile_path, pointListNear):
    """
    This function create shapefiles for ArcGIS.
    
    Input Arguments: 
    shapefile_path             --    Path to Shapefile
    pointListNear    --    ???
    """
    from arcpy import env
    env.workspace = shapefile_path
    arcpy.AddField_management(shapefile_path, "ID_scratch", "FLOAT")
      
    arcpy.DeleteField_management(shapefile_path, "Id")  # Delete automatically created field
    arcpy.AddField_management(shapefile_path, "ID", "FLOAT")
    arcpy.AddField_management(shapefile_path, "FLOW", "FLOAT")
    arcpy.DeleteField_management(shapefile_path, "ID_scratch")  # Delete created field
    
    rows = arcpy.UpdateCursor(shapefile_path)
    counter = 0
      
    for row in rows:
        row.setValue("ID", pointListNear[counter][0])
        row.setValue("FLOW", pointListNear[counter][3])
        rows.updateRow(row)
        counter += 1
    return

def updateFieldAggregatedNodes(shapefile_path):
    """
    This function creates fields in a shapefile.
    
    Input Arguments: 
    shapefile_path             --   Path to point shapefile.
    """
    from arcpy import env
    env.workspace = shapefile_path
      
    arcpy.AddField_management(shapefile_path, "ID_scratch", "FLOAT")
    arcpy.DeleteField_management(shapefile_path, "Id")  # Delete automatically created field
    arcpy.AddField_management(shapefile_path, "ID_Aggre", "DOUBLE")
    arcpy.DeleteField_management(shapefile_path, "ID_scratch")
    return

def writefieldsAggregatedNodes(shapefile_path, pointListNear):
    """
    This function creates fields in a shapefile and adds a value from a list
    
    Input Arguments: 
    shapefile_path             --   Path to point shapefile.
    pointListNear    --    list with values
    """
    counter, rows = 0, arcpy.UpdateCursor(shapefile_path)
    for row in rows:
        row.setValue("ID_Aggre", pointListNear[counter][0])
        rows.updateRow(row)
        counter += 1
    return



# ----------------------------











def readFAST(pathInFile):
    """
    This functions reads out statistical data from a .txt file
    
    Input Arguments: 
    pathInFile    --    Path to .txt file
    
    Output Arguments:
    statistics        --      Statistics
      
    """
    inputfile = open(pathInFile, 'r')   # Set Path to existing .txt-File with R results
    lineArray = inputfile.readlines()   # Read in single result lines from txtfile into List
    lines = []                           # Create empty list to fill in whole txt File with results
    position = 0                        
    while position < len(lineArray):    # Iterate through list with line-results by position
            entry = lineArray[position] # Get line at position
            lines.append(entry)         # Append line at position to empty List
            position += 1               # For the loop
    inputfile.close()                   # Close result .txt file 
    
    #print(lines)
    
    id_Startnode = float(lines[0])
    sources = float(lines[1][:-1])
    sinks = float(lines[2][:-1])
    degCen = float(lines[3][:-1])
    #print("degCen" + str(degCen))
    degCenWeighted = float(lines[4][:-1])   # delete \n
    #print("degCenWeighted" + str(degCenWeighted))
    nrOfNeighboursDensity = float(lines[5][:-1])   # delete \n
    #print("nrOfNeighboursDensity" + str(nrOfNeighboursDensity))
    totalPipeLength = float(lines[6][:-1])   # delete \n
    #print("totalPipeLength" + str(totalPipeLength))
    avreageTrenchDepth = float(lines[7][:-1])   # delete \n
    #print("avreageTrenchDepth" + str(avreageTrenchDepth))
    averageHeight = float(lines[8][:-1])   # delete \n
    #print("averageHeight" + str(averageHeight))
    averageWWTPSize = float(lines[9][:-1])   # delete \n
    #print("averageWWTPSize" + str(averageWWTPSize))
    medianWWTOSize = float(lines[10][:-1])   # delete \n

    
    completePumpCosts = float(lines[15][:-1])
    #print("completePumpCosts" + str(completePumpCosts))
    completeWWTPCosts = float(lines[16][:-1])
    #print("completeWWTPCosts" + str(completeWWTPCosts))
    completePublicPipeCosts = float(lines[17][:-1])
    #print("completePublicPipeCosts" + str(completePublicPipeCosts))
    totCostPrivateSewer = float(lines[18][:-1])
    #print("totCostPrivateSewer" + str(totCostPrivateSewer))
    totSystemCostsNoPrivate = float(lines[19][:-1])
    #print("totSystemCostsNoPrivate" + str(totSystemCostsNoPrivate))
    totSystemCostsWithPrivate = float(lines[20])
    #print("totSystemCostsWithPrivate" + str(totSystemCostsWithPrivate))

    #statistics = [id_Startnode, degCen, totalPipeLength, avreageTrenchDepth, averageHeight, averageWWTPSize]
    #listWithFASTResult = [degCen]   # Non Weighted
    listWithFASTResult = [degCenWeighted]   # Weighted
    return listWithFASTResult


def readStatistics(pathInFile):
    """
    This functions reads out statistical data from a .txt file
    
    Input Arguments: 
    pathInFile    --    Path to .txt file
    
    Output Arguments:
    statistics        --      Statistics
      
    """
    inputfile = open(pathInFile, 'r')   # Set Path to existing .txt-File with R results
    lineArray = inputfile.readlines()   # Read in single result lines from txtfile into List
    lines = []                           # Create empty list to fill in whole txt File with results
    position = 0                        
    while position < len(lineArray):    # Iterate through list with line-results by position
            entry = lineArray[position] # Get line at position
            lines.append(entry)         # Append line at position to empty List
            position += 1               # For the loop
    inputfile.close()                   # Close result .txt file 
    
    #print(lines)
    
    id_Startnode = float(lines[0])
    #print("id_Startnode" + str(id_Startnode))
    sources = float(lines[1][:-1])
    #print("sources" + str(sources))
    sinks = float(lines[2][:-1])
    #print("sinks" + str(sinks))
    degCen = float(lines[3][:-1])
    #print("degCen" + str(degCen))
    degCenWeighted = float(lines[4][:-1])   # delete \n
    #print("degCenWeighted" + str(degCenWeighted))
    nrOfNeighboursDensity = float(lines[5][:-1])   # delete \n
    #print("nrOfNeighboursDensity" + str(nrOfNeighboursDensity))
    totalPipeLength = float(lines[6][:-1])   # delete \n
    #print("totalPipeLength" + str(totalPipeLength))
    avreageTrenchDepth = float(lines[7][:-1])   # delete \n
    #print("avreageTrenchDepth" + str(avreageTrenchDepth))
    averageHeight = float(lines[8][:-1])   # delete \n
    #print("averageHeight" + str(averageHeight))
    averageWWTPSize = float(lines[9][:-1])   # delete \n
    #print("averageWWTPSize" + str(averageWWTPSize))
    medianWWTOSize = float(lines[10][:-1])   # delete \n
    #print("medianWWTOSize" + str(medianWWTOSize))
    #p_to10EW = float(lines[11][:-1])   # delete \n
    #print("p_to10EW" + str(p_to10EW))
    #p_10to100EW = float(lines[12][:-1])   # delete \n$
    #print("p_10to100EW" + str(p_10to100EW))
    #p_100to1000EW = float(lines[13][:-1])   # delete \n
    #print("p_100to1000EW" + str(p_100to1000EW))
    #p_over1000EW = float(lines[14][:-1])
    #print("p_over1000EW" + str(p_over1000EW))
    
    completePumpCosts = float(lines[15][:-1])
    #print("completePumpCosts" + str(completePumpCosts))
    completeWWTPCosts = float(lines[16][:-1])
    #print("completeWWTPCosts" + str(completeWWTPCosts))
    completePublicPipeCosts = float(lines[17][:-1])
    #print("completePublicPipeCosts" + str(completePublicPipeCosts))
    totCostPrivateSewer = float(lines[18][:-1])
    #print("totCostPrivateSewer" + str(totCostPrivateSewer))
    totSystemCostsNoPrivate = float(lines[19][:-1])
    #print("totSystemCostsNoPrivate" + str(totSystemCostsNoPrivate))
    totSystemCostsWithPrivate = float(lines[20])
    #print("totSystemCostsWithPrivate" + str(totSystemCostsWithPrivate))
    
    
    #TOOD: NR: OF PUMPS, COSTS!
    #statistics = [startnode, sources, sinks, degCen, degCenWeighted, nrOfNeighboursDensity, totalPublicPipeLength, totalPrivatePipeLenth, avreageTrenchDepth, averageHeight, averageWWTPSize, medianWWTPSize, p_to10EW, p_10to100EW, p_100to1000EW, p_over1000EW]

    #statistics = [id_Startnode, degCen, totalPipeLength, avreageTrenchDepth, averageHeight, averageWWTPSize]
    statistics = [id_Startnode, sources, sinks, degCen, degCenWeighted, nrOfNeighboursDensity, totalPipeLength, avreageTrenchDepth, averageHeight, averageWWTPSize, medianWWTOSize, 
                  completePumpCosts, completeWWTPCosts, completePublicPipeCosts, totCostPrivateSewer, totSystemCostsNoPrivate, totSystemCostsWithPrivate]
    return statistics

def readLines(pathInFile):
    """
    This functions reads out lines of a .txt file
    
    Input Arguments: 
    pathInFile    --    Path to .txt file
    
    Output Arguments:
    readLines        --      Statistics
    """
    inputfile = open(pathInFile, 'r')   # Set Path to existing .txt-File with R results
    lineArray = inputfile.readlines()   # Read in single result lines from txtfile into List
    readLines = []                      # Create empty list to fill in whole txt File with results
    position = 0                        
    while position < len(lineArray):    # Iterate through list with line-results by position
            entry = lineArray[position] # Get line at position
            readLines.append(entry)     # Append line at position to empty List
            position += 1               # For the loop
    inputfile.close()                   # Close result .txt file 

    return readLines

def readInFastValues(pathInFile):
    """
    This functions reads out lines of a .txt file and creates a dictionary with unique ID
    
    # NOW FOR THREE VALUES

    Input Arguments:
    pathInFile    --    Path to .txt file

    Output Arguments:
    readLines        --      Statistics
    """
    inputfile = open(pathInFile, 'r')   # Set Path to existing .txt-File with R results
    lineArray = inputfile.readlines()   # Read in single result lines from txtfile into List
    readLines = {}                      # Create empty list to fill in whole txt File with results
    position = 0
    while position < len(lineArray):    # Iterate through list with line-results by position
        entry = lineArray[position] # Get line at position

        entry = entry.replace("\n", "")
        if len(entry) > 0:
            single = entry.split(",")
            
            anzEntries = len(single)
            
            newLine = []
            for i in range(anzEntries):
                newLine.append(float(single[i]))
                

            #newLine = [float(single[0]), float(single[1]), float(single[2])]
            readLines[position] = newLine     # Append line at position to empty List
            position += 1               # For the loop
        else:
            break
    
    inputfile.close()                   # Close result .txt file
    return readLines



def readResultsintermediateResults(pathInFile):
    """
    This functions ...
    
    Input Arguments: 
    pathInFile    --    Path to .txt file
    
    Output Arguments:
    outList        --      Statistics
    """
    txtFileList = open(pathInFile, 'r')   # Set Path to existing .txt-File with R results
    outList = []

    # Convert Dictionary
    for interResult in txtFileList:
        inter_P = interResult.split("[", 2)
        rest = inter_P[2]
        
        # First Entry
        #==============
        firstEntry = {}
        fe = inter_P[1][:-2]
        fe = fe.replace("()", "BRACKETREPLACEMENT")
        fe = fe.split("),", )
        
        # First and Last
        scrapFirst = fe[0][1:].split()
        scrapLast = fe[-1][1:].split()
        if scrapFirst[1][1:-1] == "BRACKETREPLACEMENT":
            firstEntry[int(scrapFirst[0][:-1])] = ((), float(scrapFirst[2])) #First in List
        else:
            firstEntry[int(scrapFirst[0][:-1])] = (int(scrapFirst[1][1:-1]), float(scrapFirst[2])) #First in List
        
        if scrapLast[1][1:-1] == "BRACKETREPLACEMENT":
            firstEntry[int(scrapLast[0][:-1])] = ((), float(scrapLast[2][:-2])) #First in List
        else:
            firstEntry[int(scrapLast[0][:-1])] = (int(scrapLast[1][1:-1]), float(scrapLast[2][:-2])) #First in List
        
        # Intermediate entries
        for i in fe[1:-1]:
            i = i.split()
            if i[1][1:-1] == "BRACKETREPLACEMENT":
                firstEntry[int(i[0][:-1])] = ((), float(i[2]))
            else:
                firstEntry[int(i[0][:-1])] = (int(i[1][1:-1]), float(i[2]))
        
        # Second Entry
        secondEntry = []
        fe = rest.split("]],", 1)
        
        rest = fe[1]
        fe = fe[0]
        fe = fe.split("],")
    
        for i in fe[1:-1]:
            _ = i.split()
            secondEntry.append([int(_[0][1:-1]), float(_[1][:-1]), float(_[2][:-1]), float(_[3][:-1]), float(_[4][:-1]), float(_[5][:-1]), float(_[6][:-1]), float(_[7][:-1])]) #, float(_[8][:-1]), float(_[9][:-1]), float(_[10][:-1])])

        # Third Entry
        thirdEntry = []
        fe = rest[2:].split("]]", 1)
        rest = fe[1][2:-2]
        scrap = fe[0].split("],", )
        for i in scrap:
            _ = i.split(",", )
            thirdEntry.append([int(_[0][2:]), float(_[1]), float(_[2]), float(_[3])]) 

        # Fourth Entry
        fourthEntry = []
        
        if rest != "[]":
            fe = rest.split("]]", 1)
            rest = fe[1][2:-2]
            
            scrap = fe[0].split("],", )
            for i in scrap:
                _ = i.split(",", )
                fourthEntry.append([int(_[0][2:]), float(_[1]), float(_[2]), float(_[3])]) 
        else:
            fourthEntry = []
        
        outList.append([firstEntry, secondEntry, thirdEntry, fourthEntry])    

    return outList

def readInbuildings(openPath, cluster):
    """
    This functions reads in a .txt file
    
    Input Arguments: 
    openPath    --    Path to .txt file
    
    Output Arguments:
    buildings        --      List with read in lines
    """
    txtFileList = readLines(openPath)
    buildings = []
    
    for i in txtFileList:
        liste = []
        _ = i.split(",", 2)
        #_ = _.replace("\r\n", "")   # New because problem with cluster
        if cluster == 1:
            lastElemente = _[2][2:-4].split()
        else:
            lastElemente = _[2][2:-3].split()

        if len(lastElemente) == 1:
            liste.append(float(lastElemente[-1]))
        else:
            for b in lastElemente[:-1]:
                liste.append(float(b[:-1]))
            
            liste.append(float(lastElemente[-1]))
            
        buildings.append([float(_[0][1:]), float(_[1]), liste])
    
    return buildings

def readInDictionary(pathInFile):
    """
    This functions reads a .txt file into a dictionary.
    
    Input Arguments: 
    pathInFile           --    Path to .txt file
    
    Output Arguments:
    outDictionary        --      Dictionary
    """
    txtFileList = readLines(pathInFile)
    outDictionary = {}  # empty Dictionary
    
    for i in txtFileList:
        spl = i.split(None, 1)  # get index
        index = int(spl[0])
        entries = spl[1].split(",",)
        subDict = {}

        # First Entry
        firstEntry = entries[0].split()
        subDict[int(firstEntry[0][1:-1])] = float(firstEntry[1][:-1])

        # entries in between
        if len(entries) >= 2:
            for entry in entries[1:-1]:
                splitEntry = entry.split(None,)
                subDict[int(splitEntry[0][:-1])] = float(splitEntry[1])
            
            # Last Entry
            lastEntry = entries[-1].split()
            subDict[int(lastEntry[0][:-1])] = float(lastEntry[1][:-1])
        else:  
            lastEntry = entries[-1].split()
            subDict[int(lastEntry[0][1:-1])] = float(lastEntry[1][:-1])
        outDictionary[index] = subDict
        
    return outDictionary


def readInRasterSize(pathInFile):
    """
    This functions reads in a .txt file.
    
    Input Arguments: 
    pathInFile           --    Path to .txt file
    
    Output Arguments:
    rasterSize        --      Raster Size
    """
    inputfile = open(pathInFile, 'r')   # Set Path to existing .txt-File with R results
    lineArray = inputfile.readlines()   # Read in single result lines from txtfile into List
    txtFileList, position = [], 0       # Create empty list to fill in whole txt File with results
    
    while position < len(lineArray):  # Iterate through list with line-results by position
            entry = lineArray[position]  # Get line at position
            txtFileList.append(entry)  # Append line at position to empty List
            position += 1  # For the loop
            
    inputfile.close()  # Close result .txt file 
    rasterSize = float(txtFileList[0][:-1])  # Read out only string
    return rasterSize

def readInStartnode(pathInFile):
    """
    This functions reads in a .txt file.
    
    Input Arguments: 
    pathInFile           --    Path to .txt file
    
    Output Arguments:
    rasterSize        --      Raster Size
    """
    inputfile = open(pathInFile, 'r')   # Set Path to existing .txt-File with R results
    lineArray = inputfile.readlines()   # Read in single result lines from txtfile into List
    txtFileList, position = [], 0       # Create empty list to fill in whole txt File with results
    
    while position < len(lineArray):  # Iterate through list with line-results by position
            entry = lineArray[position]  # Get line at position
            txtFileList.append(entry)  # Append line at position to empty List
            position += 1  # For the loop
    
    for i in txtFileList:
        s = i

    f = s.split(",",)

    idStartnode = int(f[0][2:-1])
    x, y = float(f[1][:-1]), float(f[2][:-1])
    startnode = [[idStartnode, x, y]]
    
    inputfile.close()  # Close result .txt file 
    
    return startnode

def readInedgesID(pathInFile):
    """
    This functions reads in a .txt file.
    
    Input Arguments: 
    pathInFile           --    Path to .txt file
    
    Output Arguments:
    liste        --      List with edges
    """
    txtFileList = readLines(pathInFile)
    liste = []
        
    # Read out only string
    for i in txtFileList:
        splittedLine = i.split("],",)

        # add first bracket
        z = []
        firstBracket = splittedLine[0].split()
        
        # Add first element of first bracket
        fstEle = firstBracket[0][2:-1] 

        z.append(int(fstEle))

        for entry in firstBracket[1:-1]:
            og = float(entry[:-1])
            z.append(og) 
            
        lastEle = firstBracket[-1]  # Add last element of first bracket
        z.append(float(lastEle))
        
        # add second bracket
        z1 = []
        firstBracket = splittedLine[1].split()
        fstEle = firstBracket[0][1:-1]  # Add first element of first bracket
        z1.append(int(fstEle))


        for entry in firstBracket[1:-1]:
            og = float(entry[:-1])
            z1.append(og) 
            
        lastEle = firstBracket[-1]  # Add last element of first bracket
        z1.append(float(lastEle))
        
        # add all in between
        for entry in splittedLine[2:-1]:
            z1.append(float(entry[:-1]))

        # add last two entries
        lastEntries = splittedLine[2].split()

        
        forList = [z, z1, float(lastEntries[0][:-1]), float(lastEntries[1][:-1]), float(lastEntries[2][:-1]), float(lastEntries[3][:-1])]        
        
        liste.append(forList)  # append who line
    return liste


def readInAggreatedPoints(pathInFile):
    """
    This functions reads in a .txt file.
    
    Input Arguments: 
    pathInFile           --    Path to .txt file
    
    Output Arguments:
    liste        --      List witz aggregated Points
    """
    txtFileList = readLines(pathInFile)
    liste = []  # Read out only string
    
    for i in txtFileList:
        z = []
        splittedLine = i.split(" ", 10)
        z.append(float(splittedLine[0][1:-1]))  # add first element
        
        # add all in between
        for entry in splittedLine[1:-1]:
            z.append(float(entry[:-1]))

        # last element
        lstEle = splittedLine[-1]
        lstEle = lstEle[1:-3]
        lstEle = lstEle.replace(",", "")
        lstEle = lstEle.split()
        
        subList = []
        for i in lstEle:
            subList.append(float(i))
        
        z.append(subList)  # add last elemen
        liste.append(z)
        
    return liste


def getNodesUntilCertainNumber(radius, copypnts, origin, number):
    """
    # Gets radius until a certain number of nodes is added
    
    Input Arguments: 
    pathInFile           --    Path to .txt file
    
    Output Arguments:
    radius        --      Radius
    """
    allPnts = []
    selectionPnts = []
    
    # calculate all distance to origin
    for i in copypnts:
        pnt = (i[1], i[2], i[8])
        dist = distanceCalc3d(origin, pnt)
        allPnts.append((dist, i[0], pnt))
    
    # Iterate until a certain number is achieved
    while len(selectionPnts) < number:
        allPnts, closestNode, radius = getClosest(allPnts)  # get closest and delete
        selectionPnts.append(closestNode)
    
    return radius


def distanceCalc3d(p0, p1):
    """
    This functions calculates the euclidian distance in 3d space.

    Input Arguments: 
    p0, p1    --    Two points
    
    Output Arguments:
    distance              --    Distance between the points
    slope                 --    Slope between the two points
    heightDiff            --    Height difference betwen the two points
    """
    xp0, xp1, yp0, yp1, zFrom, zTo = p0[0], p1[0], p0[1], p1[1], p0[2], p1[2]
    distancePlanar = math.hypot(xp0 - xp1, yp0 - yp1)  # XFrom - X_To, YFrom - Y_To

    if distancePlanar == 0:
        print "ERROR: DISTANCE TO ITSELF is calculated"
        return 0, 0, 0  # Distance zero is returned

    heightDiff = zTo - zFrom
    distanz = math.sqrt(pow(distancePlanar, 2) + pow(heightDiff, 2))
    slope = (float(heightDiff) / float(distancePlanar)) * 100  # Slope in percentage
    
    return distanz, slope, heightDiff

def getClosest(PN):
    """
    This functions gets the closest node and deletes the according PRIM-Distance in PN.

    Input Arguments: 
    p0, p1    --    Two points
    
    Output Arguments:
    distance              --    Distance between the points
    slope                 --    Slope between the two points
    heightDiff            --    Height difference betwen the two points
    """
    minDit = 999999999999 # scrapdistance
    zahler = -1
    for i in PN:
        zahler += 1
        if i[0] < minDit:
            minDit = i[0]  # shortest distance
            closestNode = i
            deletPosition = zahler
            radius = minDit
    del PN[deletPosition]
        
    return PN, deletPosition


def readInforPRIM(pathRasterPoints):
    """
    This functions reads in a .txt file.
    
    Input Arguments: 
    pathRasterPoints           --    Path to .txt file
    
    Output Arguments:
    lines        --      List with aggregated Points
    """
    txtFileList = readLines(pathRasterPoints)
    lines = []
    for i in txtFileList:
        lineElements = i.split(None, 10)
        allElements = i.split("],",)
        
        # First eight elements
        z = [int(lineElements[0][1:-1]), float(lineElements[1][:-1]), float(lineElements[2][:-1]), float(lineElements[3][:-1]), float(lineElements[4][:-1]), float(lineElements[5][:-1]), float(lineElements[6][:-1]), float(lineElements[7][:-1]), float(lineElements[8][:-1])]
 
        # Copy buildling list
        houses = lineElements[9].split("]",)
        lastList = str(houses[0][1:])

        if len(lastList) > 2:
            lastList = lastList.replace(",", "")
            lastList = lastList.split()
            ele = []
            for i in lastList:
                ele.append(float(i))
        else:
            ele = []
            
        z.append(ele)
        
        #Add last Elements
        nachList = allElements[1].split()  # Copy entries after list
        z.append(float(nachList[0][:-1]))
        lines.append(z)
    
    return lines

def readInRasterPointsTxtReadingFunctions(pathRasterPoints):
    """
    This functions reads in a .txt file.
    
    Input Arguments: 
    pathRasterPoints           --    Path to .txt file
    
    Output Arguments:
    demPnts        --      DEM Points
    """
    print("READ IN RASTER PINT txtFileReadingFunctions FUNCTIONS")
    txtFileList = readLines(pathRasterPoints)  
    demPnts = []
    for i in txtFileList:
        lineElements = i.split()
        demPnts.append([int(lineElements[0][1:-1]), float(lineElements[1][:-1]), float(lineElements[2][:-1]), float(lineElements[3][0:-1])])

    return demPnts



def readInbuildPoints(openPath):
    """
    This functions reads in a .txt file.
    
    Input Arguments: 
    openPath           --    Path to .txt file
    
    Output Arguments:
    buildPoints        --    Buildling points
    """
    txtFileList = readLines(openPath)
    buildPoints = []
    for i in txtFileList:
        lineElements = i.split()
        buildPoints.append([float(lineElements[0][1:-1]), float(lineElements[1][:-1]), float(lineElements[2][:-1]), float(lineElements[3][:-1]), float(lineElements[4][:-1])]) #, float(lineElements[5][:-1])])

    return buildPoints

def readInParameters(pathInputParameterDesign):
    """
    This functions reads in a .txt file.
    
    Input Arguments: 
    pathInputParameterDesign           --    Path to .txt file
    
    Output Arguments:
    parameters        --    Parameters
    """
    txtFileList = readLines(pathInputParameterDesign)
    parameters = []
    for i in txtFileList:
        parameters.append(float(i))

    return parameters

def readResultsresult_VerticGraph(pathInFile):
    """
    This functions reads in a .txt file.
    
    Input Arguments: 
    pathInFile           --    Path to .txt file
    
    Output Arguments:
    outList        --    Results SNIP
    """
    txtFileList = readLines(pathInFile)
    
    # Convert Dictionary
    outDict = {}
    for entry in txtFileList:
        i = entry.split()
        if str(i[1][1:-1]) == str(()):
            outDict[int(i[0])] = ((), float(i[2][:-1]))
        else:
            outDict[int(i[0])] = (int(i[1][1:-1]), float(i[2][:-1]))
        
    return outDict

def readInstreetVertices(pathstreetVertices):
    """
    This functions reads in a .txt file.
    
    Input Arguments: 
    pathstreetVertices           --    Path to .txt file
    
    Output Arguments:
    StreetVertices        --    Street Vertices
    """
    txtFileList = readLines(pathstreetVertices)
    StreetVertices = []
    for i in txtFileList:
        lineElements = i.split()
        StreetVertices.append([int(lineElements[0][1:-1]), float(lineElements[1][:-1]), float(lineElements[2][:-1]), float(lineElements[3][0:-1])])

    return StreetVertices


def readResultspointsPrim(pathInFile):
    """
    This functions reads in a .txt file.
    
    Input Arguments: 
    pathInFile           --    Path to .txt file
    
    Output Arguments:
    outList        --    Results SNIP
    """
    txtFileList = readLines(pathInFile)
    
    # Convert Dictionary
    outList = []
    for entry in txtFileList:
        i = entry.split()
        z = [int(i[0][1:-1]), float(i[1][:-1]), float(i[2][:-1]), float(i[3][:-1]), float(i[4][:-1]), float(i[5][:-1]), float(i[6][:-1]), float(i[7][:-1])] #, float(i[8][:-1]), float(i[9][:-1]), float(i[10][:-1])]
        outList.append(z)
        
    return outList


def readResultslistWTPs(pathInFile):
    """
    This functions reads in a .txt file.
    
    Input Arguments: 
    pathInFile           --    Path to .txt file
    
    Output Arguments:
    outList        --    Results SNIP
    """
    txtFileList = readLines(pathInFile)
    
    # Convert Dictionary
    outList = []
    for entry in txtFileList:
        i = entry.split()
        z = [int(i[0][1:-1]), float(i[1][:-1])]
        outList.append(z)
        
    return outList

def readResultswtpstodraw(pathInFile):
    """
    This functions reads in a .txt file.
    
    Input Arguments: 
    pathInFile           --    Path to .txt file
    
    Output Arguments:
    outList        --    Results SNIP
    """
    txtFileList = readLines(pathInFile)
    
    # Convert Dictionary
    outList = []
    for entry in txtFileList:
        i = entry.split()
        z = [int(i[0][1:-1]), float(i[1][:-1]), float(i[2][:-1]), float(i[3][:-1])]
        outList.append(z)
        
    return outList


def readInLine(pathInFile):
    """
    This functions reads in a .txt file.
    
    Input Arguments: 
    pathInFile           --    Path to .txt file
    
    Output Arguments:
    outDiction        --    Ditionary
    """
    txtFileList = readLines(pathInFile)
    outDiction = {}
    
    # Read out list with dictionary
    for i in txtFileList:  # read out linde
        splitted = i.split(None, 1)  # split line into two elements
        index = int(splitted[0][1:-1])  # get index of main dictionary
        splitTwo = splitted[1].split(",")  # split second entry
        subDict = {}  # create subDictionary
        for sub in splitTwo:
            subSplit = sub.split()  # split second index
            firstChar = subSplit[0][0]  # get first character
            lastChar = subSplit[-1][-1]  # get last character
            
            if firstChar == "{":            
                subIndex = int(subSplit[0][1:-1])
            else:
                subIndex = int(subSplit[0][:-1])
            
            if lastChar == "}":
                subcontent = float(subSplit[1][1:-2])
            else:
                subcontent = float(subSplit[1][:-1])
            
            subDict[subIndex] = subcontent
        outDiction[index] = subDict  # copy single line into graph

    return outDiction

