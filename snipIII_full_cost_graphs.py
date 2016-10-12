from astropy.constants.si import alpha
def cleanMCR(MCR_Intersections, averageSCR):
    # Clean MCR"
    newMCR = []
    for run in MCR_Intersections:
        for i in run:
            if i != []:
                for entry in i:
                    if entry > averageSCR:
                        newMCR.append(entry)
    return newMCR

def rewritePath(inPath):
    ''' Replace Characters in string path to get correct path.'''
    replaceList = [["\a","REPLACEA"], ["\t", "REPLACET"], ["\r","REPLACER" ], ["\f", "REPLACEF"], ["\b", "REPLACEB"], ["\n", "REPLACEN"], ["\\", "//"], ["REPLACEA", "/a"], ["REPLACET","/t" ], ["REPLACER", "/r"], ["REPLACEF", "/f"], ["REPLACEB", "/b"], ["REPLACEN", "/n"]]
    for c in replaceList:
        inPath = inPath.replace(c[0], c[1])
    return inPath

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
        entry = lineArray[position] # Get line at position
        readLines.append(entry)     # Append line at position to empty List
        position += 1               # For the loop
    inputfile.close()                   # Close result .txt file 
    return readLines

def collectFolderNames(path):
    resultFolder = []  # List with all results from all the calculations
    
    # Get the folders
    mainfolderPaths = []
    folderList = os.listdir(path) 
    folderList.sort()
    for folder in folderList: #[0:2]: #[1:4]: #[2:27]:
        folderNoNumers = []
        noList = ["_", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
        folderNew = []
        for i in folder:
            if i not in noList:
                folderNew.append(i)
        folderNew = ''.join(folderNew)
        mainfolderPaths.append(folderNew)
    return mainfolderPaths
        
def collectData(path):
    '''
    Collect data of standardRun
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

        path = str(i) + "plot_Standard_RUN.txt"
        #path = str(i) + "plot_MATRIX_RUNS.txt"
        
        txtFileList = readLines(path)
        z = txtFileList[0]
        result = list(eval(z))
        resultFolder.append(result)
        
    return resultFolder


def collectDataAllRuns(path):
    '''
    Collect data of standardRun
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

def collectDataSustainabilityPoint(path):
    
    # List with all results from all the calculations
    resultFolder = []
    
    # Get the folders
    mainfolderPaths = []
    folderList = os.listdir(path) 
    folderList.sort()
    for folder in folderList:
        mainfolderPaths.append(path + "\\" + folder + "\\" + "ResultSNIP" + "\\")
    #print("mainfolderPaths:" + str(mainfolderPaths))
    # Reat our txt files
    for i in mainfolderPaths: #[0:2]: #[1:4]: #[2:27]: #[:20]:
        #print("i: " + str(i))
        path = str(i) + "plot_sustainabilityPoints.txt"
        
        txtFileList = readLines(path)
        z = txtFileList[0]
        result = list(eval(z))

        # Sustainiliby Point of Standard Scenario
        #standardSCR= result[0]
        #resultFolder.append([standardSCR])
        resultFolder.append(result)
        
    return resultFolder

def collectDataMCR(path):
    
    # List with all results from all the calculations
    resultFolder = []
    
    # Get the folders
    mainfolderPaths = []
    folderList = os.listdir(path) 
    folderList.sort()
    for folder in folderList: #[0:2]: #[1:4]: #[2:27]:
        mainfolderPaths.append(path + "\\" + folder + "\\" + "ResultSNIP" + "\\")
    #print("mainfolderPaths:" + str(mainfolderPaths))
    # Reat our txt files
    for i in mainfolderPaths: #[:20]:
        #print("i: " + str(i))
        path = str(i) + "plot_marketEquilibriumPoints.txt"
        
        txtFileList = readLines(path)
        z = txtFileList[0]
        result = list(eval(z))
        resultFolder.append([result])
        
    return resultFolder


def delFolder(path, folderName):
    
    # List with all results from all the calculations
    resultFolder = []
    
    # Get the folders
    mainfolderPaths = []
    folderList = os.listdir(path) 
    folderList.sort()
    for folder in folderList:
        mainfolderPaths.append(path + "\\" + folder + "\\" + folderName + "\\")
    
    # Remove Folder
    
    for i in mainfolderPaths:
        iNew = rewritePath(i) 
        try:
            print("Delete Folder:" + str(iNew))
            shutil.rmtree(iNew)    
        except:
            print("Folder does not exist: " + str(iNew))
    return resultFolder


import os
pathCollectData = "Q:\\Abteilungsprojekte\\eng\\SWWData\\Eggimann_Sven\\07-Fallbeispiele\\03-Glarus\\01-GIS_Data\\Glarus_communities"
#pathCollectData = "Q:\\Abteilungsprojekte\\eng\\SWWData\\Eggimann_Sven\\07-Fallbeispiele\\02_GIS_BERN\\604_Bleiken"

# Path to store PDF of standard run
plotPDF = True
#pathToStorePDF= "Q:\\Abteilungsprojekte\\eng\\SWWData\\Eggimann_Sven\\07-Fallbeispiele\\03-Glarus\\01-GIS_Data\\PDF_StandardRun\\"
pathToStorePDF= "Q:\\Abteilungsprojekte\\eng\\SWWData\\Eggimann_Sven\\07-Fallbeispiele\\03-Glarus\\01-GIS_Data\\PDF_ScenarioRuns\\"
    
# Collect data
sustainabilityCR_PNTS = collectDataSustainabilityPoint(pathCollectData)     # Collect Sustainability Points
MCR_PNTS_ReadIN = collectDataMCR(pathCollectData)                           # Collect
severalList = collectData(pathCollectData)                                  # Collect 
folderNames = collectFolderNames(pathCollectData)                           # Collect Folder Names

matrixRuns_ReadIN = collectDataAllRuns(pathCollectData)                           # 12.02.2016

print("len(sustainabilityCR_PNTS) " + str(len(sustainabilityCR_PNTS)))
print("len(MCR_PNTS_ReadIN) " + str(len(MCR_PNTS_ReadIN)))
print("len(severalList) " + str(len(severalList)))
print("len(folderNames) " + str(len(folderNames)))

#severalList = []
#severalList.append(costsStandardRun)

# Draw the curves# ------------
import numpy as np
import matplotlib.pyplot as plt
from pylab import *
import pylab
import matplotlib.ticker as ticker
from matplotlib.legend_handler import HandlerLine2D
from matplotlib.font_manager import FontProperties
from xlwt.Style import border_line_map
import shutil
import os

from matplotlib.patches import Ellipse # ellipse
from matplotlib.backends.backend_pdf import PdfPages

#from scipy import stats
import numpy
# --------------------------------------------
# If Folder Deletion is needed
# HANDLE WITH CAAAAAAAAAAAAAAAAAAAAAAAAAAAAARE
#delFolder(pathCollectData, "ResultSNIP")
#prnt("..")
# --------------------------------------------

#plt.figure(facecolor="white")       # Remove grey background
#ax = plt.subplot(111)

# yerr=errorBarUnsheduled

errorBarSCR, errorBarMCR = [], []

xMCR_diagramPlot, ySCR_diagramPlot = [],[] # PLot SCR vs MCR. Diagram PLot
   
#for costsStandardRun in severalList:
for costsStandardRun, SCR_pnts, MCR_pnts, folder, individualRuns in zip(severalList, sustainabilityCR_PNTS, MCR_PNTS_ReadIN, folderNames, matrixRuns_ReadIN): # STandard Scenario Only
    #print("costsStandardRun:" + str(len(costsStandardRun)))
    
    print("folder: " + str(folder))
            
    plt.figure(facecolor="white")       # Remove grey background
    ax = plt.subplot(111)
        
    # Plot Sustainability Points for line chart (standard scenario that pnts is on line)
    # ---------------------------
    xSCR, ySCR = SCR_pnts, []

    for i in costsStandardRun:
        for f in i[7]:
            #print f
            if f[0] >= xSCR[0]:
                #ySCR.append(f[2])
                ySCR.append(f[1]) 
                break
            
    print("LEN A: " + str(xSCR[0]))
    print("LEN A: " + str(ySCR))
    
    plt.plot(xSCR[0], ySCR, 'ro', color="#ED1C24") # Sustainabiliy Point
    
    # MCR, SCR Plot
    # -------------------
    #print("SCR_pnts " + str(SCR_pnts))
    #print("---")
    #print("MCR_pnts " + str(MCR_pnts))
    averageSCR = average(SCR_pnts) # Generate sensible Intersection Points
    MR_cleaned = cleanMCR(MCR_pnts, averageSCR)
    #print("MR_cleaned: " + str(MR_cleaned))
    MR_cleaned_average = average(MR_cleaned)
    #print("MR_cleaned: " + str(MR_cleaned))
    #print("averageSCR: " + str(averageSCR))
    #print("MR_cleaned_average: " + str(MR_cleaned_average))
    xMCR_diagramPlot.append(MR_cleaned_average)
    ySCR_diagramPlot.append(averageSCR)

    std_MCR = numpy.std(MR_cleaned)  # Standard deviation
    std_SCR = numpy.std(SCR_pnts)    # Standard deviation
    
    errorBarMCR.append(std_MCR)
    errorBarSCR.append(std_SCR)
    
    #print("ERROR std_MCR: " + str(std_MCR))
    #print("ERROR SCR_pnts: " + str(std_SCR))
    
    # --------------------Replace here if individual scenario runs
    
    
    print("Anzahl cost Matrix: " + str(len(costsStandardRun)))
    for i in costsStandardRun:
        x, y = [], []
        x1, y1 = [], []
        x2, y2 = [], []
        x3, y3 = [], []
        x4, y4 = [], []
        x5, y5 = [], []
        x6, y6 = [], []
        x7, y7 = [], [] # Marginal Sewer connection costs

        plot_WWTP = i[1]
        plot_sewers = i[2]
        plot_distrTreatment = i[3]
        plot_distrTransport = i[4]
        plot_SummedCentral = i[5] 
        plot_SummedDistributed = i[6]
        plot_summedTotal = i[7]
        
        #print("plot_SummedCentral: " + str(plot_SummedCentral))
        
        # If all cost curves of cost Matrix --> Then Summarize MATRIX RUNS
        # If only standard run is calculated, summarize Standard RUn
        # -------------------------------------------------------
        for i in plot_SummedCentral:
            x.append(i[0])                  # density
            y.append(i[2])                  # Z weighted
        
        for i in plot_SummedDistributed:
            x1.append(i[0])                  # density
            y1.append(i[2])                  # Z weighted
        
        for i in plot_summedTotal:
            x2.append(i[0])                  # density
            #y2.append(i[2])                  # Z weighted
            y2.append(i[1])                  # Z weighted
        
        cnt, old_popConnected = 0, 0
        for i in plot_sewers:
            
            # Average per capita costs
            x3.append(i[0])
            y3.append(i[2])      
            
            # Marginal costs            
            CRMarginal = i[0]
            totCatchmentPE = i[1]
            totAnnuitiyWholeCatchement = i[2]
            popNewConnected = (CRMarginal * totCatchmentPE) - old_popConnected
            totAnnuityCurrentSystem = (CRMarginal * totCatchmentPE) * totAnnuitiyWholeCatchement # Nr of connected people times annuity per person
            
            # Marginal Cost Calculations
            #if cnt == 1:
            #    marginalSewerCost = (totAnnuityCurrentSystem - old_totAnnuityCurrentSystem) / float(popNewConnected)
            #else:
            #    marginalSewerCost = totAnnuityCurrentSystem / float(popNewConnected)#First entry is marginal cost zero as no sewers are built
            #
            #if marginalSewerCost < 0:
            #    print("marginalSewerCost: " + str(marginalSewerCost))
            #    print("folder: " + str(folder))
            #    print("totAnnuityCurrentSystem: " + str(totAnnuityCurrentSystem))
            #    print("old_totAnnuityCurrentSystem: " + str(old_totAnnuityCurrentSystem))
            #    print("popNewConnected:   " + str(popNewConnected))
            #    print"---"
                
            ##print("---")    
            #x7.append(i[0])                               # density
            #y7.append(marginalSewerCost)                  # marginal sewer costs

            old_totAnnuitiyWholeCatchement = i[2]
            old_totAnnuityCurrentSystem = (CRMarginal * totCatchmentPE) * totAnnuitiyWholeCatchement # Nr of connected people times annuity per person
            old_popConnected = CRMarginal * totCatchmentPE
            cnt = 1
        
        #print("RES: " + str(x7))   
        #print("zz; " + str(y7))
        for i in plot_WWTP:
            x4.append(i[0])                  # density
            y4.append(i[2])                  # Z weighted
            
        for i in plot_distrTransport:
            x5.append(i[0])                  # density
            y5.append(i[2])                  # Z weighted
        
        for i in plot_distrTreatment:
            x6.append(i[0])                  # density
            y6.append(i[2])                  # Z weighted
            
        #area = [20]
        #plt.figure(facecolor="white")       # Remove grey background

        #print("plot_sewers:             " + str(plot_sewers))
        #print("-------------------------------")
        #print("plot_WWTP:               " + str(plot_WWTP))
        #print("-------------------------------")
        #print("plot_distrTransport:     " + str(plot_distrTransport))
        #print("-------------------------------")
        #print("plot_SummedCentral:      " + str(plot_SummedCentral))
        #print("-------------------------------")
        #print("plot_SummedDistributed:     " + str(plot_SummedDistributed))
        #print("-------------------------------")
        #print("plot_distrTreatment:     " + str(plot_distrTreatment))

        #print(x)
        #print(y)
        
        plt.plot(x, y, linestyle='-',  markersize=3, linewidth=2, color="#2E3192", label="Summed Centralized") # 46, 49, 146 --> CMYK to RGB Converted
        plt.plot(x1, y1, linestyle='-', markersize=3, linewidth=2, color="#006838", label="Summed Distributed") # 0, 104, 56
        plt.plot(x2, y2, linestyle=':', linewidth=2,  markersize=5, color="#ED1C24", label="Summed Total") # 
        #plt.plot(x3, y3, linestyle='-', linewidth=1, marker= "x", markersize=3, color="darkblue", label="Transport Central (sewer)")
        #plt.plot(x4, y4, linestyle='-', linewidth=1, marker= "x", markersize=3, color="grey", label="Treatment Central (WWTP)")
        #plt.plot(x5, y5, linestyle='-', linewidth=1, marker= "x", markersize=3, color="grey", label="Transport Decentral (space-dependent)")
        #plt.plot(x6, y6, linestyle='-', linewidth=1, marker= "x", markersize=1, color="pink", label="Treatment Decentral")
        #plt.plot(x7, y7, linestyle='-', linewidth=2, marker= "x", markersize=1, color="green", label="Marginal Sewer Costs")                  # Plot Marginal Costs
        
        # Data Series
        #ax = plt.subplot(111)
        
        # Make visible top and right border 
        #ax.spines['right'].set_visible(False)       # Remove frame line right
        #ax.spines['top'].set_visible(False)         # Remove frame line bottom
            
        ax.xaxis.set_tick_params(width = 1.5)       # Size of ticks
        ax.yaxis.set_tick_params(width = 1.5)       # Size of ticks
            
        ax.tick_params(axis='y', direction='out')   # Ticks outwards
        ax.tick_params(axis='x', direction='out')   # Ticks outwards
        
        ax.xaxis.set_ticks_position('bottom')       # Only tiks on bottom
        ax.yaxis.set_ticks_position('left')         # Only ticks on left
            
        # Get intervall ticks
        interval = 0.2
        nrOfInterval = 1
        cnt = 0
        labelPosition = [0.2, 0.4, 0.6, 0.8, 1.0]
        newLabels = [0.2, 0.4, 0.6, 0.8, 1.0]
            
        ax.set_xticks(labelPosition, minor=False)
        ax.set_xticklabels(newLabels, minor=False, visible=True, size=8, name='Arial')
        
        #newLabelsY = [0,100,200,300,400,500,600,700,800,900,1000]
        #ax.set_yticklabels(newLabelsY, size=10, name='Arial')
        
        #pylab.xlim([0,1])
        #pylab.ylim(0, 1000)
        #plt.show()
    
    '''
    # --------------------------------------------------------------------------------------------------------------------------------
    # ################################################################################################################################
    # Plot all scenario calculations
    # ################################################################################################################################
    # --------------------------------------------------------------------------------------------------------------------------------
    print("LENGTH INDIVIDUALRUNS: " + str(len(individualRuns)))
    
    for i in individualRuns: 
        x_allRuns, y_allRuns = [], []
        x1_allRuns, y1_allRuns = [], []
        x2_allRuns, y2_allRuns = [], []
        
        #print("INDIVIDUALRUN: " + str(i))
        
        plot_SummedCentral = i[5] 
        plot_SummedDistributed = i[6]
        plot_summedTotal = i[7]
        
        #print("plot_SummedCentral: " + str(plot_SummedCentral))
        
        # If all cost curves of cost Matrix --> Then Summarize MATRIX RUNS
        # If only standard run is calculated, summarize Standard RUn
        # -------------------------------------------------------
        for i in plot_SummedCentral:
            x_allRuns.append(i[0])                  # density
            y_allRuns.append(i[2])                  # Z weighted
        
        for i in plot_SummedDistributed:
            x1_allRuns.append(i[0])                  # density
            y1_allRuns.append(i[2])                  # Z weighted
        
        for i in plot_summedTotal:
            x2_allRuns.append(i[0])                  # density
            y2_allRuns.append(i[1])                  # Z weighted
        
        cnt, old_popConnected = 0, 0
                    
        #area = [20]
        #plt.figure(facecolor="white")       # Remove grey background

        plt.plot(x_allRuns, y_allRuns, linestyle='-',  markersize=3, linewidth=2, color="#2E3192", label="Summed Centralized") # 46, 49, 146 --> CMYK to RGB Converted
        plt.plot(x1_allRuns, y1_allRuns, linestyle='-', markersize=3, linewidth=2, color="#006838", label="Summed Distributed") # 0, 104, 56
        plt.plot(x2_allRuns, y2_allRuns, linestyle=':', linewidth=2,  markersize=5, color="#ED1C24", label="Summed Total") # 
            
        ax.xaxis.set_tick_params(width = 1.5)       # Size of ticks
        ax.yaxis.set_tick_params(width = 1.5)       # Size of ticks
            
        ax.tick_params(axis='y', direction='out')   # Ticks outwards
        ax.tick_params(axis='x', direction='out')   # Ticks outwards
        
        ax.xaxis.set_ticks_position('bottom')       # Only tiks on bottom
        ax.yaxis.set_ticks_position('left')         # Only ticks on left
            
        # Get intervall ticks
        interval = 0.2
        nrOfInterval = 1
        cnt = 0
        labelPosition = [0.2, 0.4, 0.6, 0.8, 1.0]
        newLabels = [0.2, 0.4, 0.6, 0.8, 1.0]
            
        ax.set_xticks(labelPosition, minor=False)
        ax.set_xticklabels(newLabels, minor=False, visible=True, size=8, name='Arial')
        
    '''
    
    if plotPDF == True:
        # PLot of standard run
        pylab.xlim([0,1])
        pylab.ylim(0, 1000)
        pathforGRAPHS = pathToStorePDF + folder + ".pdf"
        print("pathforGRAPHS: " + str(pathforGRAPHS))
        plt.savefig(pathforGRAPHS)
        #plt.show()
        # Save standard plot as PDF
        #pp = PdfPages(pathToStorePDF + folder + ".pdf")
        #pp.savefig(testPlot)
        #pp.close()


    
    #break #print("scrap")






# Plot Legend
#plt.legend(loc=2, frameon=False, fontsize=10)

pylab.xlim([0,1])
pylab.ylim(-100, 1000)
        
plt.xlabel('Connection rate', name='arial', weight='bold', fontsize=8)
plt.ylabel('Annuities [$/PE/Yearr]', name='arial', weight='bold', fontsize=8)

#plt.show()
    
    #plt.draw()


#plt.legend((cost_summed_central, cost_summed_distributed, cost_summed_total, cost_sewers, cost_WWTP), 
#           ('Summed Central', 'Summed Distributed', 'Summed Tot', 'Sewers', 'WWTP'), 
#           loc='top left', frameon=False)



# To save it
#plt.savefig(outPNGPath)
#plt.close()









#------------------------------------------------
# plot MCR,SCRPLot
# ------------------------------------------------------------
#print("xMCR_diagramPlot: " + str(xMCR_diagramPlot))
#print("xMCR_diagramPlot" + str(xMCR_diagramPlot))
#print("-------")
#print("ySCR_diagramPlot: " + str(ySCR_diagramPlot))
#print(len(ySCR_diagramPlot))

plt.figure(facecolor="white")       # Remove grey background

# Data Series
ax = plt.subplot(111)

print(errorBarSCR)
print(errorBarMCR)

# Plot Error Bar & Chart
plt.plot(xMCR_diagramPlot, ySCR_diagramPlot, 'ro', color='black', markersize=3)                                                                       # Points
plt.errorbar(xMCR_diagramPlot, ySCR_diagramPlot, yerr=errorBarSCR, xerr=errorBarMCR, color='grey', linestyle='')        # Error Bar

# plot Ellipse
'''colorlist = ['peru', 'peru', 'blue', 'peru', 'green', 
             'green', 'blue', 'green', 'peru', 'peru', 
             'peru', 'peru', 'peru', 'blue', 'blue', 
             'blue', 'green', 'blue', 'blue', 'blue',
             'green', 'peru', 'peru', 'peru', 'peru',
             'red', 'red', 'red'
             ]
'''

colorlist = ['peru', 'peru', 'peru', 'peru', 'peru', 
             'peru', 'peru', 'peru', 'peru', 'peru', 
             'peru', 'peru', 'peru', 'peru', 'peru', 
             'peru', 'peru', 'peru', 'peru', 'peru',
             'peru', 'peru', 'peru', 'peru', 'peru',
             'red', 'red', 'red'
             ]


# Ellipse
'''for xEllipse, yEllipse, std_MCR, std_SCR, color in zip(xMCR_diagramPlot, ySCR_diagramPlot, errorBarMCR, errorBarSCR, colorlist):
    
    ellipse = Ellipse(xy=(xEllipse, yEllipse), width=2*std_MCR, alpha=0.2, height=2*std_SCR, fc=color, edgecolor='none') # edgecolor=color,
    ax.add_patch(ellipse)
    #ax.set_xlim(0, 100)
    #ax.set_ylim(0, 100)
    #show()
'''


            
ax.spines['right'].set_visible(False)       # Remove frame line right
ax.spines['top'].set_visible(False)         # Remove frame line bottom
ax.xaxis.set_tick_params(width = 1.5)       # Size of ticks
ax.yaxis.set_tick_params(width = 1.5)       # Size of ticks
ax.tick_params(axis='y', direction='out')   # Ticks outwards
ax.tick_params(axis='x', direction='out')   # Ticks outwards
ax.xaxis.set_ticks_position('bottom')       # Only tiks on bottom
ax.yaxis.set_ticks_position('left')         # Only ticks on left
            
# Get intervall ticks
interval = 0.2
nrOfInterval = 1
cnt = 0
labelPosition = [0.2, 0.4, 0.6, 0.8, 1.0]
newLabels = [0.2, 0.4, 0.6, 0.8, 1.0]
            
ax.set_xticks(labelPosition, minor=False)
ax.set_xticklabels(newLabels, minor=False, visible=True, size=8, name='Arial')
        
#newLabelsY = [0,100,200,300,400,500,600,700,800,900,1000]
#ax.set_yticklabels(newLabelsY, size=10, name='Arial')

for i, txt in enumerate(folderNames):
    ax.annotate(str(txt), xy=(xMCR_diagramPlot[i],ySCR_diagramPlot[i]), xytext=(float(xMCR_diagramPlot[i]) + 0.01, float(ySCR_diagramPlot[i]) + 0.01))

pylab.xlim([0,1])
pylab.ylim(0, 1)
plt.xlabel('MCR', name='arial', weight='bold', fontsize=8)
plt.ylabel('LCR', name='arial', weight='bold', fontsize=8)


# Store file
pathforGRAPHS = pathToStorePDF + "MCR_LCR_all.pdf"
plt.savefig(pathforGRAPHS)

#plt.show()
