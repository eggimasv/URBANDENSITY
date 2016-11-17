#!/usr/bin/env python
# a stacked bar plot with errorbars
import numpy
import numpy as np
import matplotlib.pyplot as plt
import pylab
from pylab import *
import glob
import os


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



def plotFigureCantons3Classes(statisticsPerCatchement):

    """
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
    
    """
    #pathToMainFolder = r'C:\_SCRAP_STAT\P4_CH_NEU\\'
    
    # http://chrisalbon.com/python/matplotlib_percentage_stacked_bar_plot.html
    kantonGeoBFS = [[1, 'Zurich', 'ZH'], [2, 'Bern', 'BE'], [3, 'Luzern', 'LU'], [4, 'Uri', 'UR'], [5, 'Schwyz', 'SZ'], [6, 'Obwalden', 'OW'], [7, 'Nidwalden', 'NW'], [8, 'Glarus', 'GL'], [9, 'Zug', 'ZG'], [10, 'Freiburg', 'FR'], [11, 'Solothurn', 'SO'], [12, 'Basel-Stadt', 'BS'], [13, 'Basel-Landschaft', 'BL'], [14, 'Schaffhausen', 'SH'], [15, 'Appenzell Ausserrhoden', 'AR'], [16, 'Appenzell Innerrhoden', 'AI'], [17, 'St. Gallen', 'SG'], [18, 'Graubuenden', 'GR'], [19, 'Aargau', 'AG'], [20, 'Thurgau', 'TG'], [21, 'Tessin', 'TI'], [22, 'Waadt', 'VD'], [23, 'Wallis', 'VS'], [24, 'Neuenburg', 'NE'], [25, 'Genf','GE'], [26, 'Jura', 'JU']]
    
    # Collect 
    #ListWithWWTPCatchments = collectDataAllRunsBefore(pathToMainFolder)
    
    ARANrAdded = []
    
    
    # Create Dictionaries to store results per canton
    ktDict = {} #_1, ktDict_05, ktDict_15 = {}
    
    for i in kantonGeoBFS:
        ktDict[i[2]] = [0,0,0,0,0,0,0,0,0,0,0,0] # 05--> small, middle large, 10 --> small, middle large, 15 --> small, middle, large, Sdv: small, middle, large

    # Sum population percentages for each canton for the three scenario
    for i in statisticsPerCatchement:
        ARANr = i[0]
        print("Entry Statistics per Catchement: " + str(i))
        if ARANr not in ARANrAdded: # if not already added catchement
            
            # Add populations
            # Sum 
            ktLabel = i[2]
            catchmentPop = i[7]
            
            #  Sum populations for different scenarios in KT dictionary
            ktDict[ktLabel][0] = ktDict[ktLabel][0] + catchmentPop* i[18]   # Summ 05 slope, small
            ktDict[ktLabel][1] = ktDict[ktLabel][1] + catchmentPop* i[19]   # Summ 05 slope, middle
            ktDict[ktLabel][2] = ktDict[ktLabel][2] + catchmentPop* i[20]   # Summ 05 slope, large
            ktDict[ktLabel][3] = ktDict[ktLabel][3] + catchmentPop* i[12]   # Summ 1 slope, small
            ktDict[ktLabel][4] = ktDict[ktLabel][4] + catchmentPop* i[13]   # Summ 1 slope, middle
            ktDict[ktLabel][5] = ktDict[ktLabel][5] + catchmentPop* i[14]   # Summ 1 slope, large
            ktDict[ktLabel][6] = ktDict[ktLabel][6] + catchmentPop* i[24]   # Summ 15 slope, small
            ktDict[ktLabel][7] = ktDict[ktLabel][7] + catchmentPop* i[25]   # Summ 15 slope, middle
            ktDict[ktLabel][8] = ktDict[ktLabel][8] + catchmentPop* i[26]   # Summ 15 slope, large
            
            ARANrAdded.append(ARANr)
        
    # Convert absolute numbers into percentages
    for ktLabel in ktDict:
        sum100Percent = ktDict[ktLabel][3] + ktDict[ktLabel][4] + ktDict[ktLabel][5]
        print("sum100Percent: " + str(sum100Percent))
        
        
        if sum100Percent is not 0:
            ktDict[ktLabel][0] = (100.00 / sum100Percent) * ktDict[ktLabel][0]   # Conert to percentages
            ktDict[ktLabel][1] = (100.00 / sum100Percent) * ktDict[ktLabel][1]   # Conert to percentages
            ktDict[ktLabel][2] = (100.00 / sum100Percent) * ktDict[ktLabel][2]   # Conert to percentages
            ktDict[ktLabel][3] = (100.00 / sum100Percent) * ktDict[ktLabel][3]   # Conert to percentages
            ktDict[ktLabel][4] = (100.00 / sum100Percent) * ktDict[ktLabel][4]   # Conert to percentages
            ktDict[ktLabel][5] = (100.00 / sum100Percent) * ktDict[ktLabel][5]   # Conert to percentages
            ktDict[ktLabel][6] = (100.00 / sum100Percent) * ktDict[ktLabel][6]   # Conert to percentages
            ktDict[ktLabel][7] = (100.00 / sum100Percent) * ktDict[ktLabel][7]   # Conert to percentages
            ktDict[ktLabel][8] = (100.00 / sum100Percent) * ktDict[ktLabel][8]   # Conert to percentages
       
    # Calculate Standard DEviation of Cantonal sums
    # Standard Deviations (Goes in each direction --> Total 2 Standardabweichung wenn nach unten und nach oben summiert wird --> 95% der Daten)
    for i in ktDict:
        ktDict[i][9] = numpy.std([ktDict[i][0], ktDict[i][3], ktDict[i][6]])  # Sbd Small
        ktDict[i][10] = numpy.std([ktDict[i][1], ktDict[i][4], ktDict[i][7]])  # Sbd Small
        ktDict[i][11] = numpy.std([ktDict[i][2], ktDict[i][5], ktDict[i][8]])  # Sbd Small
    
    
    print(".....................")
    print("Print Dictionary")
    print"----------------------"
    for i in ktDict:
        print(str(i) + str("   : ") + str(ktDict[i]))
    
    
    # Iterate Dictioanry 
    smallPercentage, middlePercentage, largePercentage = [], [], []
    smallPercentage_Std, middlePercentage_Std, largePercentage_Std = [], [], []
    
    XLabelsList = [] # ('G1', 'G2', 'G3', 'G4', 'G5', 'G1', 'G2', 'G3', 'G4', 'G5', 'G1', 'G2', 'G3', 'G4', 'G5', 'G1', 'G2', 'G3', 'G4', 'G5', 'G1', 'G2', 'G3', 'G4', 'G5', 'g3')
    
    for ktLabel in ktDict:
        smallPercentage.append(ktDict[ktLabel][3])      # standard scenario small
        middlePercentage.append(ktDict[ktLabel][4])     # standard scenario small
        largePercentage.append(ktDict[ktLabel][5])      # standard scenario small
        
        smallPercentage_Std.append(ktDict[ktLabel][9])      # standard deviation append small
        middlePercentage_Std.append(ktDict[ktLabel][10])      # standard deviation append small
        largePercentage_Std.append(ktDict[ktLabel][11])      # standard deviation append small
        
        XLabelsList.append(ktLabel)                      # Append label
    
    # Figure
    fig, ax = plt.subplots(facecolor="white")
    
    N = len(ktDict) #len(dataList)
    ind = np.arange(N)    # the x locations for the groups
    width = 0.8       # the width of the bars: can also be len(x) sequence
    
    #plt.bar(ind, [largePercentage, middlePercentage, smallPercentage])
    
    plt.bar(ind, largePercentage, width, color='#8da0cb', ecolor='gray', label="Large", yerr=largePercentage_Std) # 
    plt.bar(ind, middlePercentage, width, color='#66c2a5', ecolor='gray', bottom=largePercentage, label="Middle", yerr=middlePercentage_Std) #
    plt.bar(ind, smallPercentage, width, color='#fc8d62', ecolor='gray', bottom=[i+j for i,j in zip(largePercentage, middlePercentage)], label="Small", yerr=smallPercentage_Std)
    
    # Error Bars
    #plt.errorbar(ind+(width/2), largePercentage, yerr=largePercentage_Std, fmt='', color='cadetblue', linestyle='None')
    #plt.errorbar(ind+(width/2), middlePercentage, yerr=middlePercentage_Std, fmt='', color='black', linestyle='None')
    #plt.errorbar(ind+(width/2), smallPercentage, yerr=largePercentage_Std, fmt='', color='bisque', linestyle='None')

    plt.ylabel('Population [%]')
    plt.title('Cantons')
    
    #plt.xticks(ind + width/2, XLabelsList)
    ax.set_xticks(ind + width/2)
    ax.set_xticklabels(XLabelsList)
    
    # Legend
    
    # Place a legend above this subplot, expanding itself to fully use the given bounding box.
    plt.legend(bbox_to_anchor=(0, 1.02, 1., .102), loc=8, ncol=3, mode="expand", borderaxespad=0., frameon=None)
    
    
    # Axis 
    plt.ylim(0, 100)
    lengthXaxis =len(ind) #*width   # Total x axis length
    plt.xlim([0,lengthXaxis])
    
    plt.show()
    
    
    
    '''
    import numpy as np
    import matplotlib.pyplot as plt
    
    N = 5
    cantonData0 = (20, 35, 30, 35, 27)
    menStd = (2, 3, 4, 1, 2)
    
    ind = np.arange(N)  # the x locations for the groups
    width = 0.35       # the width of the bars
    
    
    # Figure
    fig, ax = plt.subplots(facecolor="white")
    
    
    rects1 = ax.bar(ind, cantonData0, width, color='b', yerr=menStd)
    
    womenMeans = (25, 32, 34, 20, 25)
    womenStd = (3, 5, 2, 3, 3)
    rects2 = ax.bar(ind + width, womenMeans, width, color='g', yerr=womenStd)
    
    # add some text for labels, title and axes ticks
    ax.set_ylabel('Scores')
    ax.set_title('Scores by group and gender')
    ax.set_xticks(ind + width)
    
    
    # X Axis labels
    ax.set_xticklabels(('G1', 'G2', 'G3', 'G4', 'G5'))
    
    
    # Legend
    ax.legend((rects1[0], rects2[0]), ('Men', 'Women'))
    
    
    def autolabel(rects):
        # attach some text labels
        for rect in rects:
            height = rect.get_height()
            ax.text(rect.get_x() + rect.get_width()/2., 1.05*height,
                    '%d' % int(height),
                    ha='center', va='bottom')
    
    autolabel(rects1)
    autolabel(rects2)
    
    plt.show()
    '''
    return