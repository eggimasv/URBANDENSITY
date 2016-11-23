#!/usr/bin/env python
# a stacked bar plot with errorbars
import numpy
import numpy as np
import matplotlib.pyplot as plt
import pylab
from pylab import *
import glob
import os



# Import for curve fit
import math, random, numpy, copy                    # Import Numpy for standard deviation
from scipy.optimize import curve_fit # Packate scipy
print("Sucseeful loading functions_transport")




def func2(params, x, data):
    m = params['m'].value
    c = params['c'].value
    d = params['d'].value
    model = np.power(x,m)*c + d
    return model - data #that's what you want to minimize


def createPowerFit(xList, YList):

    from scipy.optimize import curve_fit
    import numpy as np 
    import matplotlib.pyplot as plt
    from lmfit import minimize, Parameters, Parameter, report_fit
    
    # create a set of Parameters
    params = Parameters()
    params.add('m', value= 0)              # value is the initial condition
    params.add('c', value= 0) #, min=0.00001)
    params.add('d', value= 0, min=0)    # min=0 prevents that d becomes negative
    
    # do fit, here with leastsq model
    result = minimize(func2, params, args=(xList, YList))
    
    #R_squred = result.rsquared
    a = 1 - result.residual.var() / np.var(YList)
    print("R-Squared: " + str(a))
    b =  1 - result.redchi / np.var(YList, ddof=2)
    print("R-SQUARED: " + str(b))

    #----
    # http://stackoverflow.com/questions/22581887/python-lmfit-how-to-calculate-r-squared
    g = result.message
    print("G: " + str(g))
    
    #res = result.residual # Resdiuals
    #print("res: " + str(res))
    
    chi_square = result.chisqr
    print("chi_square: " + str(chi_square))
    
    reduced_chi_square = result.redchi
    print("reduced_chi_square: " + str(reduced_chi_square))
    #----
    f = result.params
    m = f['m'].value
    c = f['c'].value
    d = f['d'].value
    print("m value: " + str(m))
    print("c value: " + str(c))
    print("d value: " + str(d))
    report_fit(params)        # All Infos
    return m, c, d

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

def figureRetularDensityCatchement(statisticsPerCatchement):

    """
    
    # This function plots the percetnages of a WWTP and the density
    # Die Anteile der bevlkerungsdichte pro WWTP Klasse werden also gezeigt je nach Bevlkerungsdichte
    
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
    print("Figure with Population percetnages versus density ")
    
    # http://chrisalbon.com/python/matplotlib_percentage_stacked_bar_plot.html
    kantonGeoBFS = [[1, 'Zurich', 'ZH'], [2, 'Bern', 'BE'], [3, 'Luzern', 'LU'], [4, 'Uri', 'UR'], [5, 'Schwyz', 'SZ'], [6, 'Obwalden', 'OW'], [7, 'Nidwalden', 'NW'], [8, 'Glarus', 'GL'], [9, 'Zug', 'ZG'], [10, 'Freiburg', 'FR'], [11, 'Solothurn', 'SO'], [12, 'Basel-Stadt', 'BS'], [13, 'Basel-Landschaft', 'BL'], [14, 'Schaffhausen', 'SH'], [15, 'Appenzell Ausserrhoden', 'AR'], [16, 'Appenzell Innerrhoden', 'AI'], [17, 'St. Gallen', 'SG'], [18, 'Graubuenden', 'GR'], [19, 'Aargau', 'AG'], [20, 'Thurgau', 'TG'], [21, 'Tessin', 'TI'], [22, 'Waadt', 'VD'], [23, 'Wallis', 'VS'], [24, 'Neuenburg', 'NE'], [25, 'Genf','GE'], [26, 'Jura', 'JU']]
    
    ARANrAdded = []
    
    # Create Dictionaries to store results per canton 
    standardScenarioSmallPercentageList = []
    standardScenarioMiddlePercentageList = []
    densityRetularList = []
    densityNeighbourhoodList = []
    
    # Sum population percentages for each canton for the three scenario
    for i in statisticsPerCatchement:
        ARANr = i[0]
        densityRetular = i[4]
        NeighbourhoodDensity = i[5]
        totCatchmentArea = i[6]
        totPopCatchement = i[7]
        SmallPercent01 = i[12]
        MiddlePercent01 = i[13]
        
        # ADd to list                
        standardScenarioSmallPercentageList.append(SmallPercent01 * 100) # In % --> 1 -> 1%
        standardScenarioMiddlePercentageList.append(MiddlePercent01 * 100) # In % --> 1 -> 1%
        densityRetularList.append(densityRetular)
        densityNeighbourhoodList.append(NeighbourhoodDensity)
    
    
    plt.figure(facecolor="white")        # Remove grey background
    
    # Regular Density
    scatterA = plt.scatter(densityRetularList, standardScenarioSmallPercentageList, color="peru", marker = "o", edgecolor='black', zorder=2)
    scatterB = plt.scatter(densityRetularList, standardScenarioMiddlePercentageList, color="green", marker = "+", edgecolor='black', zorder=2)
    
    # Catchement Density
    #plt.scatter(densityNeighbourhoodList, standardScenarioSmallPercentageList, color="green", marker = "o", edgecolor='black', zorder=2)
    #plt.scatter(densityNeighbourhoodList, standardScenarioMiddlePercentageList, color="green", marker = "o", edgecolor='black', zorder=2)
    
    
    # Draw Power functionscatterB
    # ------------------
    '''m_scatterA,c_scatterA,d_scatterA = createPowerFit(densityRetularList, standardScenarioSmallPercentageList)
    x_function_scatterA = np.linspace(1000000, 0.1, 1000) # Until which value, Abstand x-axis, Number of points for creating the line
    y_function_scatterA = x_function_scatterA**m_scatterA * c_scatterA + d_scatterA
    
    plt.plot(x_function_scatterA, y_function_scatterA, '-', color='peru')
    
    print("m_scatterA: " + str(m_scatterA))
    print("c_scatterA: " + str(c_scatterA))
    print("d_scatterA d: " + str(d_scatterA))
    
    # Draw Power function scatterB
    # ------------------
    m_scatterB,c_scatterB,d_scatterB = createPowerFit(densityRetularList, standardScenarioMiddlePercentageList)
    x_function_scatterB= np.linspace(10000, 0.2, 1000) # Until which value, Abastand x-axis, Number of points for creating the line
    y_function_scatterB = x_function_scatterB**m_scatterB * c_scatterB + d_scatterB
    
    plt.plot(x_function_scatterB, y_function_scatterB, '-', color='peru')
    
    
    print("m_scatterB: " + str(m_scatterB))
    print("c_scatterB: " + str(c_scatterB))
    print("d_scatterB d: " + str(d_scatterB))
    '''
    
    # Data Series
    ax = plt.subplot(111)
    
    ax.xaxis.set_tick_params(width = 1.5)       # Size of ticks
    ax.yaxis.set_tick_params(width = 1.5)       # Size of ticks
    
    ax.tick_params(axis='y', direction='out')   # Ticks outwards
    ax.tick_params(axis='x', direction='out')   # Ticks outwards
    
    ax.xaxis.set_ticks_position('bottom')       # Only tiks on bottom
    ax.yaxis.set_ticks_position('left')         # Only ticks on left
    
    # Size Beschrifutn achsen
    ax.tick_params(axis='x', labelsize=10)
    ax.tick_params(axis='y', labelsize=10)
    
    # no acsis on top and left
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
        
    # Legend
    plt.legend((scatterA, scatterB), ('Cat WWTP A', 'Cat WWTP B'), scatterpoints=1, loc='upper right', ncol=1, fontsize=10)
    
    
    # Draw Power function
    # -------------------
    m,c,d = createPowerFit(densityRetularList, standardScenarioSmallPercentageList)
    x_function = np.linspace(5, 4000, 1000) # ?, X-Axis, Number of points for creating the line
    y_function_unscheduled = x_function**m * c + d
    #plt.plot(x_function, y_function_unscheduled, '-', color='peru')
    plt.semilogx(x_function, y_function_unscheduled, '-', color='peru')
    
    m1,c1,d1 = createPowerFit(densityRetularList, standardScenarioMiddlePercentageList)
    x1_function = np.linspace(5, 4000, 1000) # ?, X-Axis, Number of points for creating the line
    y1_function_unscheduled = x1_function**m1 * c1 + d1
    #plt.plot(x1_function, y1_function_unscheduled, '-', color='green')
    plt.semilogx(x1_function, y1_function_unscheduled, '-', color='green')
    
    
    plt.xlim(0, 4000) #TODO: adjust
    plt.ylim(-2, 102) #TODO: adjust
    
    # Set common labels
    ax.set_ylabel(' Percentage of Small WWTP [percent]', fontsize=10, fontname='Arial') # fontname="Arial"
    ax.set_xlabel('Population Density [PE/km2]', fontsize=10)
    
    ax.set_xscale('log')    # Convert Y-Axis to log-
    
    plt.show()
    
    return