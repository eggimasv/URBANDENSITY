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
    buildingDensityList = []
    
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
        
        
        # Load Nr of Buildings ot calculate density_Buildings
        buildingsPerARADictionary = [[430900, 1874], [414100, 6233], [201, 3158], [401, 936], [701, 1643], [1001, 1346], [2501, 932], [2801, 1328], [3001, 1734], [3501, 1467], [3701, 1054], [3801, 421], [3901, 429], [4201, 1082], [5201, 2908], [5301, 3945], [5501, 754], [5801, 1003], [6602, 2498], [6801, 2777], [8301, 1109], [8901, 6032], [9401, 1234], [9601, 1652], [10001, 614], [11201, 707], [11301, 1167], [11501, 2705], [11701, 2150], [11801, 3220], [12001, 2539], [12101, 4648], [13201, 688], [13301, 2970], [13801, 2060], [14001, 696], [14101, 2802], [14201, 2958], [15301, 1595], [15401, 4421], [15501, 1681], [15601, 4146], [15801, 1174], [15802, 1043], [17101, 1574], [17102, 1044], [17201, 1525], [17401, 2667], [17701, 2382], [18001, 822], [19101, 4523], [19201, 2271], [19301, 3884], [19501, 1170], [19601, 616], [19801, 4635], [21101, 441], [21701, 944], [21801, 2380], [21901, 796], [22401, 2795], [22701, 1366], [23001, 16599], [24201, 4361], [24301, 7772], [26101, 28103], [26102, 3066], [30400, 586], [30600, 8470], [30800, 161], [32101, 12445], [32300, 525], [34500, 5139], [35100, 21933], [36000, 1935], [36200, 10842], [40100, 8230], [41100, 6282], [43500, 252], [44400, 2244], [44600, 1304], [44800, 2535], [49200, 931], [49602, 1377], [49700, 318], [56102, 2768], [56300, 4088], [56500, 1028], [56700, 637], [57102, 586], [57300, 3010], [57400, 498], [57500, 867], [57600, 4038], [58200, 581], [58400, 2852], [58800, 273], [58902, 478], [59300, 8569], [60400, 174], [60700, 3202], [60800, 808], [61100, 2279], [61600, 3885], [66700, 21996], [67100, 173], [69000, 2152], [69600, 2169], [70400, 2914], [71001, 109], [72200, 490], [72500, 348], [73300, 11194], [74000, 471], [74600, 3008], [75100, 3116], [78200, 369], [78400, 1571], [78500, 4031], [79100, 1649], [79400, 6003], [84300, 6377], [84301, 115], [86900, 5319], [88500, 449], [90200, 5620], [90600, 757], [92402, 436], [94400, 35023], [95200, 1168], [95600, 14613], [98123, 1275], [99200, 2844], [99400, 5503], [100100, 6704], [100401, 1805], [100900, 1632], [102300, 598], [102400, 19440], [103100, 2826], [103300, 1896], [103500, 2692], [106500, 3625], [106603, 825], [106700, 571], [106902, 1429], [108300, 894], [109800, 1803], [110200, 2123], [110400, 7983], [113400, 13149], [120101, 8841], [120200, 805], [120400, 43], [120401, 119], [120600, 3898], [120800, 294], [121100, 539], [121200, 240], [121500, 563], [121700, 236], [122000, 500], [130101, 4277], [130103, 2042], [131102, 805], [132200, 4881], [134400, 5294], [134600, 1918], [134800, 624], [136700, 2356], [137000, 695], [137100, 867], [137200, 6775], [140100, 11278], [140200, 1764], [140400, 521], [150200, 3751], [150700, 975], [150900, 5252], [160200, 16258], [160600, 2060], [170200, 21044], [170400, 150], [170500, 495], [200400, 1828], [201300, 1854], [201700, 2887], [202900, 770], [209600, 3577], [210100, 151], [212400, 4595], [212700, 2621], [216100, 6834], [217300, 3688], [218400, 291], [219600, 3084], [220000, 617], [220200, 129], [220600, 5910], [221900, 611], [222800, 2386], [224300, 3540], [226500, 2458], [227200, 257], [227400, 3694], [227900, 260], [231000, 3241], [240700, 6039], [242900, 474], [245400, 459], [245700, 2185], [247200, 318], [247801, 520], [247900, 837], [248000, 533], [249200, 243], [250100, 9763], [250200, 194], [253400, 22747], [254200, 1603], [254400, 204], [254501, 1757], [254600, 10435], [255400, 581], [255500, 388], [255600, 1004], [257500, 1347], [257800, 3506], [258300, 4960], [261801, 409], [261900, 543], [262100, 698], [262200, 541], [270101, 18234], [276600, 14721], [277500, 4984], [278800, 491], [279300, 7172], [282300, 3655], [282500, 6217], [283100, 4029], [284100, 197], [284400, 368], [284700, 132], [285100, 312], [285300, 301], [285500, 202], [286001, 104], [286100, 7569], [286500, 279], [286600, 269], [288100, 217], [288300, 330], [288700, 214], [289100, 1578], [289400, 195], [293700, 8259], [293800, 581], [295100, 259], [295200, 767], [296300, 2056], [296400, 2589], [297100, 3946], [300102, 3915], [300202, 768], [300501, 73], [300600, 1484], [300700, 639], [302100, 1856], [302301, 926], [302401, 2559], [302501, 1324], [303401, 618], [310100, 5764], [310200, 512], [320302, 6853], [320401, 4270], [321700, 6242], [323100, 10486], [323700, 12819], [325100, 3836], [325400, 3013], [325600, 1087], [327100, 6932], [327200, 1412], [327400, 2124], [327600, 1841], [329100, 3485], [329200, 3680], [329300, 577], [329404, 418], [329501, 2836], [329600, 4442], [329800, 1720], [331200, 1036], [333201, 2827], [333500, 3666], [333800, 5737], [335200, 2982], [335400, 2356], [335601, 3103], [335702, 429], [337200, 903], [337600, 735], [337700, 3245], [339100, 2850], [339200, 3196], [340200, 5576], [340301, 511], [340500, 1096], [340603, 2697], [340802, 3818], [342200, 5383], [342500, 3548], [342600, 1635], [350501, 789], [350601, 313], [350602, 1567], [351101, 956], [351501, 322], [352101, 543], [352301, 398], [353101, 249], [353201, 2164], [355101, 654], [356101, 2110], [357301, 176], [358201, 4348], [359201, 468], [359401, 514], [359501, 562], [359901, 471], [360301, 1026], [360501, 353], [360602, 473], [361201, 1510], [361401, 1784], [363201, 325], [366101, 5031], [369301, 313], [369401, 340], [371201, 1434], [372201, 1611], [373201, 1561], [373401, 254], [373402, 395], [374101, 278], [374201, 121], [374301, 122], [374401, 168], [374601, 495], [375101, 347], [375201, 433], [375301, 342], [376101, 288], [376201, 1418], [377501, 293], [377502, 338], [377601, 419], [378201, 2044], [378601, 833], [378801, 1161], [378902, 307], [379001, 478], [380501, 540], [382101, 2484], [382201, 228], [384301, 892], [385102, 3207], [385103, 294], [385104, 313], [387101, 2067], [387102, 453], [389101, 3916], [390101, 8882], [391101, 965], [392101, 866], [392401, 825], [392701, 1203], [394201, 4048], [397201, 4977], [398101, 1213], [398202, 1553], [398302, 855], [398601, 1256], [398701, 2579], [400100, 14318], [402700, 2002], [403000, 2186], [403300, 3306], [404100, 2609], [404200, 7185], [404300, 2674], [404400, 1591], [404700, 1030], [406300, 3373], [407500, 710], [407900, 2942], [408200, 5869], [411400, 294], [411800, 553], [412100, 2040], [412200, 496], [412300, 6086], [413500, 1340], [414400, 3058], [414500, 2480], [416700, 1305], [416900, 7535], [419800, 2417], [420300, 9047], [420600, 2675], [420800, 4288], [422900, 1434], [423400, 1673], [423500, 334], [423600, 1796], [423700, 676], [423900, 1791], [425400, 5412], [425800, 2403], [427100, 6193], [427200, 808], [427600, 3676], [428000, 7730], [430300, 705], [430700, 380], [431100, 450], [431300, 887], [432100, 1634], [432300, 2572], [441600, 5948], [442600, 1643], [443600, 3632], [447100, 2193], [449700, 323], [453400, 647], [454200, 1465], [455100, 3958], [456600, 7001], [459100, 5094], [463500, 1124], [469100, 2757], [469600, 1195], [474600, 5168], [480100, 1750], [483100, 2343], [483700, 1452], [486400, 1068], [494100, 943], [494600, 8142], [500500, 17356], [500900, 337], [504300, 1303], [506100, 1424], [507900, 1283], [509700, 2175], [511301, 12845], [511302, 17307], [511400, 640], [514700, 3073], [515100, 20130], [516300, 3574], [517800, 4437], [518100, 627], [520300, 337], [525500, 144], [526200, 8544], [526800, 5126], [528100, 4776], [540100, 1391], [540200, 2557], [540500, 1273], [540700, 999], [540900, 3294], [541001, 1323], [541002, 256], [541100, 1771], [541200, 148], [541300, 1693], [541500, 688], [542100, 299], [542200, 1159], [542300, 386], [542500, 415], [542800, 431], [543400, 327], [545100, 1008], [545200, 1207], [545600, 657], [547100, 128], [547300, 183], [547400, 198], [547900, 166], [548000, 212], [548200, 296], [548600, 318], [548700, 133], [549100, 238], [549200, 287], [549601, 1335], [549602, 374], [549800, 631], [549900, 225], [550000, 322], [551202, 410], [551300, 729], [551400, 280], [551500, 808], [551600, 383], [551800, 1261], [551900, 393], [552001, 204], [552701, 165], [552702, 140], [553000, 167], [553300, 175], [553900, 220], [555100, 166], [555300, 622], [555500, 459], [555600, 322], [556500, 166], [556600, 281], [558600, 15994], [559000, 2662], [560200, 1222], [560401, 131], [560402, 567], [560600, 1632], [561101, 995], [562200, 1236], [562400, 1417], [563000, 274], [563900, 328], [564200, 4404], [564400, 108], [564600, 1552], [565200, 112], [565400, 163], [566100, 283], [567500, 2723], [568200, 208], [568500, 184], [568900, 257], [570501, 388], [570800, 124], [571200, 1285], [571300, 585], [571700, 1061], [571900, 672], [581500, 469], [623300, 4328], [626601, 7260], [626603, 3713], [628300, 351], [628500, 1416], [628700, 897], [628900, 1718], [629200, 1599], [629300, 2295], [630000, 1825], [640200, 912], [640400, 263], [640600, 4350], [641300, 526], [641401, 1358], [641402, 106], [642100, 4406], [642300, 466], [643100, 430], [643200, 516], [643600, 1801], [643700, 541], [645500, 2276], [645700, 3292], [645800, 4555], [647600, 3118], [650200, 1903], [650800, 203], [651000, 1313], [660301, 97], [661100, 831], [661900, 1455], [662002, 656], [663801, 2329], [664000, 6901], [664301, 19268], [664302, 497], [670900, 10417], [671700, 220], [671800, 295], [671900, 267], [672200, 154], [674201, 554], [674300, 511], [675000, 359], [675100, 324], [675400, 645], [675700, 641], [677500, 639], [677800, 378], [678900, 259], [679300, 617], [679600, 140], [680000, 5330], [680400, 278]]
        for ARAEntry in buildingsPerARADictionary:
            if ARAEntry[0] == ARANr:
                nrOfBuildingsPerARACatchement = ARAEntry[1]
                break
            
        density_buildings = nrOfBuildingsPerARACatchement/float(totCatchmentArea/1000000) #km2

        
        # Add to list                
        standardScenarioSmallPercentageList.append(SmallPercent01 * 100) # In % --> 1 -> 1%
        standardScenarioMiddlePercentageList.append(MiddlePercent01 * 100) # In % --> 1 -> 1%
        standardScenarioSmallAndMiddle.append((SmallPercent01 + MiddlePercent01)*100)
        densityRetularList.append(densityRetular)
        densityNeighbourhoodList.append(NeighbourhoodDensity)
        buildingDensityList.append(density_buildings)
        
    '''print("WIESO HUHN")
    for a,b in zip(densityRetularList, standardScenarioSmallPercentageList):
        print a,b
    prnt("...")
    '''
    plt.figure(facecolor="white", figsize=(16,10))        # Remove grey background
    
    print("TEST: " )
    print(len(buildingDensityList))
    print(buildingDensityList[0])
    
    
    # Regular Density
    #scatterA = plt.scatter(densityRetularList, standardScenarioSmallPercentageList, color="peru", marker = "o", edgecolor='black', zorder=2)
    #scatterB = plt.scatter(densityRetularList, standardScenarioMiddlePercentageList, color="green", marker = "+", edgecolor='black', zorder=2)
    
    scatterC = plt.scatter(densityRetularList, standardScenarioSmallAndMiddle, color="blue", marker = "o", edgecolor='black', zorder=2)
    #scatterD = plt.scatter(densityNeighbourhoodList, standardScenarioSmallAndMiddle, color="green", marker = "+", edgecolor='black', zorder=2)
    #scatterE = plt.scatter(buildingDensityList, standardScenarioSmallAndMiddle, color="yellow", marker = "o", edgecolor='black', zorder=2)
    
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
    import scipy
    from scipy import stats
    
    #Convert densityRetularList into log-values for linear fit
    densityRetularListLog = []
    for dens in densityRetularList:
        densityRetularListLog.append(math.log10(dens)) #Convert to log 10
    
    #scrap
    #scatterC = plt.scatter(densityRetularListLog, standardScenarioSmallAndMiddle, color="green", marker = "o", edgecolor='black', zorder=2)    
    
    slope, intercept, r_value, p_value, std_err = scipy.stats.linregress(densityRetularListLog, standardScenarioSmallAndMiddle)
    x4_function = np.linspace(0.5, 4, 1000) # ?Start, Stop, Number of Points
    
    print("slope: " + str(slope))
    print("intercept: " + str(intercept))
    print("r_value: " + str(r_value))
    print("R_Saured: " + str(math.pow(r_value,2)))
    print("p_value: " + str(p_value))
    print("std_err: " + str(std_err))
    
    # Linear function
    y4_function = slope*x4_function + intercept
    
    # Plot for linear X-Scale
    #plt.plot(x4_function, y4_function, '-', color='pink')

    # plot for log X-Scale
    x4_function = 10**x4_function
    plt.plot(x4_function, y4_function, '-', color='red')
    
    

    
    
    # Power fit
    '''
    # Small and middle (regular density)
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
    
    # Small and middle (house density)
    m4,c4,d4, r_squared4 = createFit(buildingDensityList, standardScenarioSmallAndMiddle)
    x4_function = np.linspace(5, 4000, 1000) # ?, X-Axis, Number of points for creating the line
    y4_function_unscheduled = x4_function**m4 * c4 + d4
    plt.plot(x4_function, y4_function_unscheduled, '-', color='yellow')
    #plt.semilogx(x4_function, y4_function_unscheduled, '-', color='yellow')
    '''
    
    #Plot R2 value 
    #plt.text(1000, 5, 'r_squared: ' + str(r_squared))
    #plt.text(1000, 4, 'r_squared1: ' + str(r_squared1))
    #plt.text(1000, 80, 'blue r_squared2: ' + str(r_squared2))
    #plt.text(1000, 90, 'green r_squared3: ' + str(r_squared3))
    
    #plt.text(1000, 3, 'blue r_squared2: ' + str(r_squared2))
    #plt.text(1000, 2, 'green r_squared3: ' + str(r_squared3))
    
    #plt.xlim(0, 4000) #TODO: adjust
    #plt.xlim(0,) #TODO: adjust
    plt.ylim(-1, 102) #TODO: adjust
    
    # Set common labels
    ax.set_ylabel(' Percentage of Small WWTP [percent]', fontsize=10, fontname='Arial') # fontname="Arial"
    ax.set_xlabel('Population Density [PE/km2]', fontsize=10)
    
    ax.set_xscale('log')    # Convert Y-Axis to log-
    
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