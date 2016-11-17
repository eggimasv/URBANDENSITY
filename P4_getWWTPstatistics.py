
# This file reads out all WWTP file results

import os
import glob
import arcpy
import numpy
import sys
    
def get_immediate_subdirectories(a_dir):
    return [name for name in os.listdir(a_dir) if os.path.isdir(os.path.join(a_dir, name))]

def collectDataAllRuns(path):
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
    for i in txtFileList[:-1]:
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
        PE = i[1]/float(EW_Q)
        if PE <= sizeSmallWWTP:
            small += PE
        if PE > sizeSmallWWTP and PE <= sizeMiddleWWTP:
            middle += PE
        if PE > sizeMiddleWWTP:
            large += PE

    percentageSmallWWTP = (100.0/float(totalPE))*small
    percentageMiddle = (100.0/float(totalPE))*middle
    percentageLarge = (100.0/float(totalPE))*large
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

def readInARETypologieDictionary(pathInFile):
    """
    """
    
    txtFileList = readLines(pathInFile)
    catchements = []
    for i in txtFileList:
        # Add first element
        
        f = i.split(",", 4)
        catchements.append([int(f[0][1:]), str(f[1][1:-1]), int(f[2]), int(f[3][:-1])])
        
    return catchements



def getDensitiesCatchement(pathExtent_gem, pathBuildings_inhabited, pathSettArea):
    
    totSettlmentArea = 0
    totCatchmentArea = 0
    totPop = 0
    
    # Read in total Area & population
    settlementAreaRows = arcpy.da.SearchCursor(pathExtent_gem, ["Shape_Area"])    
    for i in settlementAreaRows:
        totCatchmentArea = i[0]
        
    buildlingPop = arcpy.da.SearchCursor(pathBuildings_inhabited, ["Pop_Build"])    
    for i in buildlingPop:
        totPop += i[0]
    
    # Read in Settlement Area
    settlementAreaRows = arcpy.da.SearchCursor(pathSettArea, ["AREA"])    
    for i in settlementAreaRows:
        totSettlmentArea += i[0]
    
    print("totCatchmentArea: " + str(totCatchmentArea))
    print("totPop: " + str(totPop))
    print("totSettlmentArea: " + str(totSettlmentArea))
    
    regularPopulationDensity = totPop / float(totCatchmentArea/1000000) # Person / km2
    NeighborhoodDensity = totPop / float(totSettlmentArea/1000000)
    return regularPopulationDensity, NeighborhoodDensity, totCatchmentArea, totPop, totSettlmentArea



def assignCatchementsToCanton(catchmentDictionaryNotSorted):
    
    # This function attributes the catchement to one canton depending on the number of communities
    
    catchmentPerCanton = []
    checkedCatchementNr = []
    
    def most_common(lst):
        return max(set(lst), key=lst.count)
    
    for i in catchmentDictionaryNotSorted:
        ARA_NR = i[3]
        listWithSameARANR, WWTPcommunities = [], []
        
        if ARA_NR not in checkedCatchementNr:
            
            for e in catchmentDictionaryNotSorted:
                if e[3] == ARA_NR:
                    listWithSameARANR.append(e[1]) # ADd Canton
                    WWTPcommunities.append(e)
            mostCommonKT = most_common(listWithSameARANR) # Get most often canton
        for f in WWTPcommunities:
            if f[1] == mostCommonKT:
                catchmentPerCanton.append(f)
                break
        checkedCatchementNr.append(ARA_NR)
    return catchmentPerCanton

# --------------------
# Input Paramters
# --------------------
kantonGeoBFS        = [[1, 'Zurich', 'ZH'], [2, 'Bern', 'BE'], [3, 'Luzern', 'LU'], [4, 'Uri', 'UR'], [5, 'Schwyz', 'SZ'], [6, 'Obwalden', 'OW'], [7, 'Nidwalden', 'NW'], [8, 'Glarus', 'GL'], [9, 'Zug', 'ZG'], [10, 'Freiburg', 'FR'], [11, 'Solothurn', 'SO'], [12, 'Basel-Stadt', 'BS'], [13, 'Basel-Landschaft', 'BL'], [14, 'Schaffhausen', 'SH'], [15, 'Appenzell Ausserrhoden', 'AR'], [16, 'Appenzell Innerrhoden', 'AI'], [17, 'St. Gallen', 'SG'], [18, 'Graubuenden', 'GR'], [19, 'Aargau', 'AG'], [20, 'Thurgau', 'TG'], [21, 'Tessin', 'TI'], [22, 'Waadt', 'VD'], [23, 'Wallis', 'VS'], [24, 'Neuenburg', 'NE'], [25, 'Genf','GE'], [26, 'Jura', 'JU']]
pathResultFolder    = r'C:\\CALCULATION_P4_CH_NEU\\' #r'C:\\_SCRAP_FOLDERSTRUCTURE\\'  # Is the same as in datPerparatorCHF the main folder  
pathToGeoDictionary = r'Q:\\Abteilungsprojekte\eng\SWWData\Eggimann_Sven\07-Fallbeispiele\04-finalCH\dictionaryGEO.txt'
pathToAreTypologieDictionary = r'Q:\\Abteilungsprojekte\eng\SWWData\Eggimann_Sven\07-Fallbeispiele\04-finalCH\LOOKUPAREGEMTYP_DICTIONARY.txt'
pathResults = "GIS_PYTHON\\"


kantonGeoBFS = [[1, 'Zurich', 'ZH'], [2, 'Bern', 'BE'], [3, 'Luzern', 'LU'], [4, 'Uri', 'UR'], [5, 'Schwyz', 'SZ'], [6, 'Obwalden', 'OW'], [7, 'Nidwalden', 'NW'], [8, 'Glarus', 'GL'], [9, 'Zug', 'ZG'], [10, 'Freiburg', 'FR'], [11, 'Solothurn', 'SO'], [12, 'Basel-Stadt', 'BS'], [13, 'Basel-Landschaft', 'BL'], [14, 'Schaffhausen', 'SH'], [15, 'Appenzell Ausserrhoden', 'AR'], [16, 'Appenzell Innerrhoden', 'AI'], [17, 'St. Gallen', 'SG'], [18, 'Graubuenden', 'GR'], [19, 'Aargau', 'AG'], [20, 'Thurgau', 'TG'], [21, 'Tessin', 'TI'], [22, 'Waadt', 'VD'], [23, 'Wallis', 'VS'], [24, 'Neuenburg', 'NE'], [25, 'Genf','GE'], [26, 'Jura', 'JU']]

EW_Q = 0.162    # NEEDS OT BE THE SAME asin all other files

# Classification criteriat for WWTP SIZE
sizeSmallWWTP = 20        # Size in PE of Small treatment package plant        # CREABETON 4 - 30
sizeMiddleWWTP = 200      # Size in PE of Middle treatment package plant

pythonScriptPath = "C://Users/eggimasv/URBANDENSITY/P4/"    # Path to Python SNIP Files
sys.path.append(pythonScriptPath)                           # Append paths

# Import Geo of all Catchements ([BFS_NUMMER, KANTONSNUM, NAME, ARA_Nr, ARA_Name])
catchmentDictionaryNotSorted = readInGeoDictionary(pathToGeoDictionary)

# Get one community for each catchement which is in the dominant canton
catchmentDictionary = assignCatchementsToCanton(catchmentDictionaryNotSorted)
print("Number of catchements: " + str(len(catchmentDictionary)))

# CAN BE USED FOR ARA
areTypologie = readInARETypologieDictionary(pathToAreTypologieDictionary) #TYP, NAME, KT_NO, BFS_N

# Read out all Folders
ListWithWWTPCatchments = collectDataAllRuns(pathResultFolder)

# STistics per Canton [ARA_NR, kantonNr, gemeindeNr, Z, Z_weighted, percentageSmallWWTP, percentageMiddle, percentageLarge]
statisticsPerCatchement = []        

print("ListWithWWTPCatchments:" + str(ListWithWWTPCatchments))

# Iterate Folder
for pathCatchement in ListWithWWTPCatchments[0:2]: 
    print("--------------------")
    print("Path Catchement : " + str(pathCatchement))
    
    getNR = pathCatchement.split("CALCULATION_P4_CH_NEU")
    ARA_NR = int(getNR[1][1:])
       
    # Iterate all SNIP Calculations
    folderListSNIPResults= get_immediate_subdirectories(pathCatchement)
    
    # Read in Densities
    # ----------------
    pathExtent_gem = pathCatchement + "\\" + "extent_gem.shp"
    pathBuildings_inhabited = pathCatchement + "\\" + "buildings_inhabited.shp"
    pathSettArea =pathCatchement + "\\" + "settlementArea.shp"
    regularpopDensity, NeighborhoodDensity, totCatchmentArea, totPopCatchement, totSettlmentAreaCatchement = getDensitiesCatchement(pathExtent_gem, pathBuildings_inhabited, pathSettArea)
    
    # ---------------------
    # Iterate SNIP Folders (mainly to get standard deviation)
    # ---------------------
    calc_SNIPs = [] # List for all calculations
    
    for SNIPcalculation in folderListSNIPResults:
        print("SNIP calculation: " + str(SNIPcalculation))
        SNIPFolder = SNIPcalculation[len(SNIPcalculation)-8:]
            
        # Path to WWTPs text file with results
        pathFolderWWWTPResults = pathCatchement + "\\" + SNIPFolder
        #print("pathFolderWWWTPResults: " + str(pathFolderWWWTPResults))
        
        slopeCriteria = float(SNIPFolder[5] + SNIPFolder[7])
        #print("slopeCriteria: "+ str(slopeCriteria))
    
        # All .txt Files
        allFilesInFolder = glob.glob(pathFolderWWWTPResults + "\\" +  "*.txt")
        
        pathstatisticsSNIP = allFilesInFolder[0] # Statistic File
        #print("pathstatisticsSNIP: " + str(pathstatisticsSNIP))
        
        statisticsSNIP_Slope = readStatistics(pathstatisticsSNIP)
        
        # Degress of Centralisation
        Z_SNIP = statisticsSNIP_Slope[3]
        Z_weighted_SNIP = statisticsSNIP_Slope[4]
        
        # Get WWTP statistics
        wwtpFile_SNIP = allFilesInFolder[11]
        WWTPS_SNIP = readInWWTPs(wwtpFile_SNIP)      
        
        # Calculate Populations
        totalPE_SNIP, percentageSmallWWTP_SNIP, percentageMiddle_SNIP, percentageLarge_SNIP = getPercentagesWWTP(WWTPS_SNIP, EW_Q, sizeSmallWWTP, sizeMiddleWWTP)
        
        # Append Results
        resultsIter = [slopeCriteria, Z_SNIP, Z_weighted_SNIP, percentageSmallWWTP_SNIP, percentageMiddle_SNIP, percentageLarge_SNIP]
        calc_SNIPs.append(resultsIter)
        
        # Restuls for the three scenario runs
        if SNIPcalculation == "SNIP_1_0":
            slopeCriteria_standardScenario = slopeCriteria
            Z_SNIP_standardScenario = Z_SNIP
            Z_weighted_SNIP_standardScenario = Z_weighted_SNIP
            percentageSmallWWTP_SNIP_standardScenario = percentageSmallWWTP_SNIP
            percentageMiddle_SNIP_standardScenario = percentageMiddle_SNIP
            percentageLarge_SNIP_standardScenario = percentageLarge_SNIP
        
        if SNIPcalculation == "SNIP_0_5":
            slopeCriteria_scenario05 = slopeCriteria
            Z_SNIP_scenario05 = Z_SNIP
            Z_weighted_SNIP_scenario05 = Z_weighted_SNIP
            percentageSmallWWTP_SNIP_scenario05 = percentageSmallWWTP_SNIP
            percentageMiddle_SNIP_scenario05 = percentageMiddle_SNIP
            percentageLarge_SNIP_scenario05 = percentageLarge_SNIP
        
        if SNIPcalculation == "SNIP_1_5":
            slopeCriteria_scenario15 = slopeCriteria
            Z_SNIP_scenario15 = Z_SNIP
            Z_weighted_SNIP_scenario15 = Z_weighted_SNIP
            percentageSmallWWTP_SNIP_scenario15 = percentageSmallWWTP_SNIP
            percentageMiddle_SNIP_scenario15 = percentageMiddle_SNIP
            percentageLarge_SNIP_scenario15 = percentageLarge_SNIP

    print("Iteratet Result Files")
    for i in calc_SNIPs:
        print i
    
    # Calculate Standard Deviation of three scenarios (for three scenario) for each catchement   
    stdv_Z_SNIP = numpy.std([calc_SNIPs[0][1], calc_SNIPs[1][1], calc_SNIPs[2][1]])
    stdv_Z_weighted_SNIP = numpy.std([calc_SNIPs[0][2], calc_SNIPs[1][2], calc_SNIPs[2][2]])
    stdv_percentageSmallWWTP_SNIP = numpy.std([calc_SNIPs[0][3], calc_SNIPs[1][3], calc_SNIPs[2][3]])
    stdv_percentageMiddle_SNIP = numpy.std([calc_SNIPs[0][4], calc_SNIPs[1][4], calc_SNIPs[2][4]])
    stdv_percentageLarge_SNIP = numpy.std([calc_SNIPs[0][5], calc_SNIPs[1][5], calc_SNIPs[2][5]])
    
    print("---------------------------------")
    print("Restuls for catchemetn Nr: " + str(ARA_NR))
    print("---------------------------------")
    print("stdv_Z_SNIP: " + str(stdv_Z_SNIP))
    print("stdv_Z_weighted_SNIP: " + str(stdv_Z_weighted_SNIP))
    print("stdv_percentageSmallWWTP_SNIP: " + str(stdv_percentageSmallWWTP_SNIP))
    print("stdv_percentageMiddle_SNIP: " + str(stdv_percentageMiddle_SNIP))
    print("stdv_percentageLarge_SNIP: " + str(stdv_percentageLarge_SNIP))
      
    # Find Geography in Dictionary
    for i in catchmentDictionary:
        if i[3] == ARA_NR:
            print("Alle INfos : " + str(i))
            # Adds for every community the statistics for the whole catchement
            gemeindeNr, kantonNr =  i[0], i[1]
                
            for kt in kantonGeoBFS:
                if kt[0] == kantonNr:
                    ktLabel = kt[2]
                    break
                    
            statCatchement = [
                    
                    # Infos
                    ARA_NR, 
                    kantonNr, 
                    ktLabel, 
                    gemeindeNr, 
                    regularpopDensity, 
                    NeighborhoodDensity, 
                    totCatchmentArea, 
                    totPopCatchement, 
                    totSettlmentAreaCatchement, 
                    
                    # Standard Scenario
                    slopeCriteria_standardScenario,          
                    Z_SNIP_standardScenario, 
                    Z_weighted_SNIP_standardScenario, 
                    percentageSmallWWTP_SNIP_standardScenario, 
                    percentageMiddle_SNIP_standardScenario, 
                    percentageLarge_SNIP_standardScenario, 
                    
                    # Slope 0.5 Scenario
                    slopeCriteria_scenario05,
                    Z_SNIP_scenario05,
                    Z_weighted_SNIP_scenario05,
                    percentageSmallWWTP_SNIP_scenario05,
                    percentageMiddle_SNIP_scenario05,
                    percentageLarge_SNIP_scenario05,
                    
                    # Slope 1.5 Scenario
                    slopeCriteria_scenario15,
                    Z_SNIP_scenario15,
                    Z_weighted_SNIP_scenario15,
                    percentageSmallWWTP_SNIP_scenario15,
                    percentageMiddle_SNIP_scenario15,
                    percentageLarge_SNIP_scenario15,
            
                    # Std Deviation for individual catchements
                    stdv_Z_SNIP, 
                    stdv_Z_weighted_SNIP, 
                    stdv_percentageSmallWWTP_SNIP, 
                    stdv_percentageMiddle_SNIP, 
                    stdv_percentageLarge_SNIP
                    ]
                    
            # Append Statistics to canton
            statisticsPerCatchement.append(statCatchement)

# ---------------------------------------------------------------------------
# Create Graphs
# ---------------------------------------------------------------------------
from P4_barcharts import *

# Plot Figure XY 
plotFigureCantons3Classes(statisticsPerCatchement)
