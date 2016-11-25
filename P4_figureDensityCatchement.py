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

def createFit(xList, YList):

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
    result = minimize(func2, params, args=(xList, YList)) # Power Fit
 
    #R_squred = result.rsquared
    r_squared = 1 - result.residual.var() / np.var(YList)
    print("R-Squared: " + str(r_squared))
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
    return m, c, d, r_squared



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
    standardScenarioSmallAndMiddle = []
    
    # Sum population percentages for each canton for the three scenario
    for i in statisticsPerCatchement:
        ARANr = i[0]
        densityRetular = i[4]
        NeighbourhoodDensity = i[5]
        totCatchmentArea = i[6]
        totPopCatchement = i[7]
        SmallPercent01 = i[12]
        MiddlePercent01 = i[13]
    
        scrap = ((SmallPercent01 + MiddlePercent01)*100)
        if int(scrap) > 100.0:
            print("ERROR")
            prnt("...")
            
        # Alternative Mausre (settlement area/tot area)
        # SCRAP REMOVE
        #densityRetular = densityRetular * (i[8]/totCatchmentArea)
        
        # Convvert to expoenntial data --> Convert X-Axis value to Log in order to make sensible r_quared test
        #MiddlePercent01 = math.log(SmallPercent01)
        #densityRetular = math.log(densityRetular)
        
        # Add to list                
        standardScenarioSmallPercentageList.append(SmallPercent01 * 100) # In % --> 1 -> 1%
        standardScenarioMiddlePercentageList.append(MiddlePercent01 * 100) # In % --> 1 -> 1%
        standardScenarioSmallAndMiddle.append((SmallPercent01 + MiddlePercent01)*100)
        densityRetularList.append(densityRetular)
        densityNeighbourhoodList.append(NeighbourhoodDensity)
    
    '''print("WIESO HUHN")
    for a,b in zip(densityRetularList, standardScenarioSmallPercentageList):
        print a,b
    prnt("...")
    '''
    plt.figure(facecolor="white")        # Remove grey background
    
    # Regular Density
    #scatterA = plt.scatter(densityRetularList, standardScenarioSmallPercentageList, color="peru", marker = "o", edgecolor='black', zorder=2)
    #scatterB = plt.scatter(densityRetularList, standardScenarioMiddlePercentageList, color="green", marker = "+", edgecolor='black', zorder=2)
    scatterC = plt.scatter(densityRetularList, standardScenarioSmallAndMiddle, color="blue", marker = "o", edgecolor='black', zorder=2)
    scatterD = plt.scatter(densityNeighbourhoodList, standardScenarioSmallAndMiddle, color="green", marker = "+", edgecolor='black', zorder=2)
    
    # Catchement Density
    #plt.scatter(densityNeighbourhoodList, standardScenarioSmallPercentageList, color="green", marker = "o", edgecolor='black', zorder=2)
    #plt.scatter(densityNeighbourhoodList, standardScenarioMiddlePercentageList, color="green", marker = "o", edgecolor='black', zorder=2)
    
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
    #plt.legend((scatterA, scatterB, scatterC), ('Cat WWTP A', 'Cat WWTP B', 'Cat WWTP A + B'), scatterpoints=1, loc='upper right', ncol=1, fontsize=10)
    
    # Draw Power functions
    # -------------------
    '''#Small
    m,c,d, r_squared = createFit(densityRetularList, standardScenarioSmallPercentageList)
    x_function = np.linspace(5, 4000, 1000) # ?, X-Axis, Number of points for creating the line
    y_function_unscheduled = x_function**m * c + d
    #plt.plot(x_function, y_function_unscheduled, '-', color='peru')
    plt.semilogx(x_function, y_function_unscheduled, '-', color='peru')
    
    #Middle
    m1,c1,d1, r_squared1 = createFit(densityRetularList, standardScenarioMiddlePercentageList)
    x1_function = np.linspace(5, 4000, 1000) # ?, X-Axis, Number of points for creating the line
    y1_function_unscheduled = x1_function**m1 * c1 + d1
    #plt.plot(x1_function, y1_function_unscheduled, '-', color='green')
    plt.semilogx(x1_function, y1_function_unscheduled, '-', color='green')
    '''
    
    # Linear Fit
    """import scipy
    from scipy import stats
    slope, intercept, r_value, p_value, std_err = scipy.stats.linregress(densityRetularList, standardScenarioSmallAndMiddle)
    x4_function = np.linspace(5, 4000, 1000) # ?, X-Axis, Number of points for creating the line
    y4_function = slope*x4_function + intercept
    plt.plot(x4_function, y4_function, '-', color='pink')
    print("r_value: " + str(r_value))
    print("p_value: " + str(p_value))
    print("std_err: " + str(std_err))
    """
    
    # Small and middle (regular densit)
    m2,c2,d2, r_squared2 = createFit(densityRetularList, standardScenarioSmallAndMiddle)
    x2_function = np.linspace(5, 4000, 1000) # ?, X-Axis, Number of points for creating the line
    y2_function_unscheduled = x2_function**m2 * c2 + d2
    plt.plot(x2_function, y2_function_unscheduled, '-', color='blue')
    #plt.semilogx(x2_function, y2_function_unscheduled, '-', color='blue')
    
    # Small and middle (urban density)
    m3,c3,d3, r_squared3 = createFit(densityNeighbourhoodList, standardScenarioSmallAndMiddle)
    x3_function = np.linspace(5, 4000, 1000) # ?, X-Axis, Number of points for creating the line
    y3_function_unscheduled = x3_function**m3 * c3 + d3
    plt.plot(x3_function, y3_function_unscheduled, '-', color='green')
    #plt.semilogx(x3_function, y3_function_unscheduled, '-', color='green')
    
    #Plot R2 value 
    #plt.text(1000, 5, 'r_squared: ' + str(r_squared))
    #plt.text(1000, 4, 'r_squared1: ' + str(r_squared1))
    #plt.text(1000, 80, 'blue r_squared2: ' + str(r_squared2))
    #plt.text(1000, 90, 'green r_squared3: ' + str(r_squared3))
    
    #plt.text(1000, 3, 'blue r_squared2: ' + str(r_squared2))
    #plt.text(1000, 2, 'green r_squared3: ' + str(r_squared3))
    
    #plt.xlim(0, 4000) #TODO: adjust
    plt.xlim(0,) #TODO: adjust
    plt.ylim(-1, 102) #TODO: adjust
    
    # Set common labels
    ax.set_ylabel(' Percentage of Small WWTP [percent]', fontsize=10, fontname='Arial') # fontname="Arial"
    ax.set_xlabel('Population Density [PE/km2]', fontsize=10)
    
    #ax.set_xscale('log')    # Convert Y-Axis to log-
    
    plt.show()
    
    return















# scrapcnt

def funcLinear(params, x, data):
    a = params['a'].value
    c = params['c'].value
    model = x*a + c
    return model - data #that's what you want to minimize

def createLinearFit(xList, YList):

    from scipy.optimize import curve_fit
    import numpy as np 
    import matplotlib.pyplot as plt
    from lmfit import minimize, Parameters, Parameter, report_fit
    
    # create a set of Parameters
    params = Parameters()
    params.add('a', value= 0)
    params.add('c', value= 0) 
    
    # do fit, here with leastsq model
    result = minimize(funcLinear, params, args=(xList, YList)) # Linear Fit
    
    #R_squred = result.rsquared
    r_squared = 1 - result.residual.var() / np.var(YList)
    print("R-Squared: " + str(r_squared))
    b =  1 - result.redchi / np.var(YList, ddof=2)
    print("R-SQUARED: " + str(b))

    #----
    # http://stackoverflow.com/questions/22581887/python-lmfit-how-to-calculate-r-squared
    g = result.message
    print("G: " + str(g))

    #----
    f = result.params
    a = f['a'].value
    c = f['c'].value
    print("a value: " + str(a))
    print("c value: " + str(c))
    report_fit(params)        # All Infos
    return a, c, r_squared