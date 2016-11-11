
# This file reads out all WWTP file results

import os
import glob


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

def readLines(pathInFile):
    """
    This functions reads out lines of a .txt file
    
    Input Arguments: 
    pathInFile       --    Path to .txt file
    
    Output Arguments:
    readLines        --      Statistics
    """
    inputfile = open(pathInFile, 'r')   # Set Path to existing .txt-File with R results
    lineArray = inputfile.readlines()   # Read in single result lines from txtfile into List
    readLines = []                      # Create empty list to fill in whole txt File with results
    position = 0                        
    while position < len(lineArray):    # Iterate through list with line-results by position
        entry = lineArray[position]     # Get line at position
        readLines.append(entry)         # Append line at position to empty List
        position += 1                   # For the loop
    inputfile.close()                   # Close result .txt file 
    return readLines


def readInWWTPs(pathInFile):
    """
    This functions reads in a .txt file.
    
    Input Arguments: 
    pathInFile           --    Path to .txt file
    
    Output Arguments:
    liste                --   List with edges
    """
    txtFileList = readLines(pathInFile)
    liste = []
    # Read out only string
    for i in txtFileList:
        _ = i.split(",", 2)
        ID = int(_[0][1:])
        flow = float(_[1][1:-2])
        liste.append([ID, flow])               # append who line
    return liste


def calculateTotalWWTPSUM(WWTPS, EW_Q):
    
    # This functions sums total PE
    
    totalFlow = 0
    
    for i in WWTPS:
        totalFlow += i[1]
        
    totalPE = totalFlow/EW_Q
    
    return totalPE


def getPercentagesWWTP(WWTPS, EW_Q, sizeSmallWWTP, sizeMiddleWWTP):
    
    # Calculates percentages of each WWTP Distribution
    small, middle, large = 0, 0, 0
    
    totalPE = calculateTotalWWTPSUM(WWTPS, EW_Q)

    for i in WWTPS:
        PE = i[1]/EW_Q
        if PE <= sizeSmallWWTP:
            small += PE
        if PE > sizeSmallWWTP and PE <= sizeMiddleWWTP:
            middle += PE
        if PE > sizeMiddleWWTP:
            large += PE

    percentageSmallWWTP = (100.0/float(totalPE))*small
    percentageMiddle = (100.0/float(totalPE))*middle
    percentageLarge = (100.0/float(totalPE))*large
        
    #testSum = percentageSmallWWTP + percentageMiddle + percentageLarge

    return totalPE, percentageSmallWWTP, percentageMiddle, percentageLarge

def readStatistics(pathInFile):
    """
    This functions reads out statistical data from a .txt file
    
    Input Arguments: 
    pathInFile        --    Path to .txt file
    
    Output Arguments:
    statistics        --      Statistics
    """
    inputfile = open(pathInFile, 'r')   # Set Path to existing .txt-File with R results
    lineArray = inputfile.readlines()   # Read in single result lines from txtfile into List
    lines = []                          # Create empty list to fill in whole txt File with results
    position = 0                        
    while position < len(lineArray):    # Iterate through list with line-results by position
        entry = lineArray[position]     # Get line at position
        lines.append(entry)             # Append line at position to empty List
        position += 1                   # For the loop
    inputfile.close()                   # Close result .txt file 

    id_Startnode = float(lines[0])
    sources = float(lines[1][:-1])
    sinks = float(lines[2][:-1])
    degCen = float(lines[3][:-1])
    degCenWeighted = float(lines[4][:-1])  
    nrOfNeighboursDensity = float(lines[5][:-1])
    totalPipeLength = float(lines[6][:-1])   
    avreageTrenchDepth = float(lines[7][:-1])   
    averageHeight = float(lines[8][:-1])   
    averageWWTPSize = float(lines[9][:-1])   
    medianWWTOSize = float(lines[10][:-1])   
    completePumpCosts = float(lines[15][:-1])
    completeWWTPCosts = float(lines[16][:-1])
    completePublicPipeCosts = float(lines[17][:-1])
    totCostPrivateSewer = float(lines[18][:-1])
    totSystemCostsNoPrivate = float(lines[19][:-1])
    totSystemCostsWithPrivate = float(lines[20])

    statistics = [id_Startnode, sources, sinks, degCen, degCenWeighted, nrOfNeighboursDensity, totalPipeLength, avreageTrenchDepth, averageHeight, averageWWTPSize, medianWWTOSize, 
                  completePumpCosts, completeWWTPCosts, completePublicPipeCosts, totCostPrivateSewer, totSystemCostsNoPrivate, totSystemCostsWithPrivate]
    return statistics



def readInGeoDictionary(pathInFile):
    """
    This functions reads out statistical data from a .txt file
    
    Input Arguments: 
    pathInFile        --    Path to .txt file
    
    Output Arguments:
    statistics        --      Statistics
    """
    
    txtFileList = readLines(pathInFile)
    
    # Add first element
    catchements = []
    firstEntry= txtFileList[0]
    f = firstEntry.split(",", 4)
    catchements.append([int(f[0][2:]), int(f[1]), str(f[2][1:-1]), int(f[3]), str(f[4][1:-4])])

    #cnt= 1
    for f in txtFileList[1:]:
        g = f.split(",", 4)
        catchements.append([int(g[0][1:]), int(g[1]), str(g[2][1:-1]), int(g[3]), str(g[4][1:-4])])
        
        #print(catchements[cnt])
        #cnt+=1

    return catchements
    
    
    '''inputfile = open(pathInFile, 'r')   # Set Path to existing .txt-File with R results
    lineArray = inputfile.readlines()   # Read in single result lines from txtfile into List
    
    print"lineArray"
    print(lineArray[0])
    print(lineArray[1])
    
    lines = []
    
    for i in lineArray:
        lines.append(i)
        
    print("_-------")
    print(lines[0][0])
    print(lines[1])
    #print(lineArray)
    prnt("..")
    
    
    lines = []                          # Create empty list to fill in whole txt File with results
    position = 0                        
    while position < len(lineArray):    # Iterate through list with line-results by position
        entry = lineArray[position]     # Get line at position
        lines.append(entry)             # Append line at position to empty List
        position += 1                   # For the loop
    inputfile.close()                   # Close result .txt file 
    '''
    return lines



# --------------------
# Input Paramters
# --------------------
pathResultFolder = r'C:\\_SCRAP_FOLDERSTRUCTURE\\'
pathToGeoDictionary = r'Q:\\Abteilungsprojekte\eng\SWWData\Eggimann_Sven\07-Fallbeispiele\04-finalCH\dictionaryGEO.txt'

smallWWTP = 10 # Small PE
EW_Q = 0.162    # NEEDS OT BE THE SAME! 


# CREABETON 4 - 30

sizeSmallWWTP = 30        # Size in PE of Small treatment package plant    
sizeMiddleWWTP = 100      # Size in PE of Middle treatment package plant


#dictionaryWithAllCatchmentINFOs = # Import from ArcGIS
geoDictionary = readInGeoDictionary(pathToGeoDictionary)
print(geoDictionary)
prnt("geoDictionary")

# Read out all Folders
ListWithWWTPCatchments = collectDataAllRuns(pathResultFolder)


pathResults = "GIS_PYTHON\\"


# Iterate Folder
for pathCatchement in ListWithWWTPCatchments: # Remove the 1
    print("--------------------")
    print("Path Catchement : " + str(pathCatchement))
    
    getNR = pathCatchement.split("_SCRAP_FOLDERSTRUCTURE")
    print("getNR: " + str(getNR))
    
    ARA_NR = int(getNR[1][1:])
    print("ARA_NR: " + str(ARA_NR))
    
    # Path to WWTPs text file with results
    pathFolderWWWTPResults = pathCatchement + "\\" + pathResults

    # All .txt Files
    allFilesInFolder = glob.glob(pathFolderWWWTPResults +  "*.txt")
    print(allFilesInFolder)
    
    try:
        # Statistic File
        statistics = allFilesInFolder[0]
        print("Statistic File: " + str(statistics))
        
        # WWTP File
        wwtpFile = allFilesInFolder[11]
        print("wwtpFile File: " + str(wwtpFile))
        
        # ----------------------
        # CREATE WWPT STAITISCS
        # ----------------------
        WWTPS = readInWWTPs(wwtpFile)
        #print(WWTPS)
        
        # Get Percentage of small, middle and large WWTP
        totalPE, percentageSmallWWTP, percentageMiddle, percentageLarge = getPercentagesWWTP(WWTPS, EW_Q, sizeSmallWWTP, sizeMiddleWWTP)
     
        print(" ")
        print("-----------------")
        print("WWTP Distribution")
        print("-----------------")
        print("percentageSmallWWTP: " + str(percentageSmallWWTP))
        print("percentageMiddle:    " + str(percentageMiddle))
        print("percentageLarge:     " + str(percentageLarge))
        print("Test Total:          " + str(percentageSmallWWTP + percentageMiddle + percentageLarge))
        print("-----------------")
        
        
        # Read statistics from Statistics file
        statistics = readStatistics(statistics)
        
        Z = statistics[3]
        Z_weighted = statistics[4]
        

        # Find Geography in Dictionary
        
        #ARA_NR
        
        
        # Add to List
        
    except:
        print"The File was not found"