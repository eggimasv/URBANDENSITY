#!/usr/bin/python


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

#
# Example boxplot code
import sys
import os
import numpy as np
from matplotlib import *
import matplotlib.pyplot as plt
from pylab import *
import pylab
import matplotlib.ticker as ticker
from matplotlib.legend_handler import HandlerLine2D
from matplotlib.font_manager import FontProperties
from xlwt.Style import border_line_map
from matplotlib.lines import lineStyles
from operator import add  

## numpy is used for creating fake data
import matplotlib as mpl 
import matplotlib.pyplot as plt 


sustainabilityPoints = [0.45, 0.45, 0.45, 0.45, 0.45, 0.45, 0.45, 0.45, 0.45, 0.45, 0.45, 0.45, 0.45, 0.45, 0.45, 0.45, 0.45, 0.45, 0.45, 0.45, 0.45, 0.45, 0.45, 0.45, 0.45, 0.45, 0.45, 0.45, 0.45, 0.45, 0.45, 0.45, 0.45, 0.45, 0.45, 0.45, 0.45, 0.45, 0.45, 0.45, 0.45, 0.45, 0.45, 0.45, 0.45, 0.45, 0.45, 0.45, 0.45, 0.45, 0.45, 0.45, 0.45, 0.45, 0.45, 0.45, 0.45, 0.45, 0.45, 0.45, 0.45, 0.45, 0.45, 0.45, 0.45, 0.45, 0.45, 0.45, 0.45, 0.45, 0.45, 0.45, 0.45, 0.45, 0.45, 0.45, 0.45, 0.45, 0.45, 0.45, 0.45]
MCR_Intersections = [[0.49227502400526635], [0.4920117032149311], [0.4925384715787657], [0.6393964218925965, 0.675256926767157, 0.7427708147232346], [0.6389907403242866, 0.6767624980816932, 0.7425574762386318], [0.639802261945949, 0.6737531850026677, 0.7429842029700349], [0.0356700152469285, 0.4689292167995367], [0.036074562637989895, 0.4687755637548709], [0.03526563453094066, 0.4690829146130449], [0.5035360626869909], [0.5030913045276424], [0.5039811729733296], [0.7498235568824841], [0.749547060171719], [0.7504561586315185], [0.0356700152469285, 0.48505930875784076], [0.036074562637989895, 0.4848322058898859], [0.03526563453094066, 0.48528650739212], [0.49227502400526635], [0.4920117032149311], [0.4925384715787657], [0.6393964218925965, 0.675256926767157, 0.7427708147232346], [0.6389907403242866, 0.6767624980816932, 0.7425574762386318], [0.639802261945949, 0.6737531850026677, 0.7429842029700349], [0.0356700152469285, 0.4689292167995367], [0.036074562637989895, 0.4687755637548709], [0.03526563453094066, 0.4690829146130449], [0.409674699195999, 0.46422643403437763], [0.4106486439535175, 0.464062642731582], [0.40877238816892913, 0.4643902764375791], [0.24080662174841483, 0.5185565121977119, 0.5350657481553535, 0.5884125756625159, 0.591296018623486, 0.6028118122217749], [0.24172679023415347, 0.5179043003928995, 0.5361030440378418, 0.5861141616489832, 0.5931808960720524, 0.602199585435119], [0.23972750975018708, 0.5192094604486447, 0.5340302085592601, 0.6034244753596417], [], [], [], [0.3808477843232241, 0.4774990041770185], [0.38162445974038706, 0.47569570322734817], [0.3800721763185128, 0.47930843396567363], [0.22426245274115977, 0.6153642419374927, 0.6924568168170375, 0.7430649311880552], [0.22461255509390682, 0.6149074800413801, 0.6937453243939687, 0.7427791026648493], [0.2239124559437796, 0.6158212305621336, 0.6911696402675931, 0.7433508490288236], [], [], [], [0.409674699195999, 0.46422643403437763], [0.4106486439535175, 0.464062642731582], [0.40877238816892913, 0.4643902764375791], [0.24080662174841483, 0.5185565121977119, 0.5350657481553535, 0.5884125756625159, 0.591296018623486, 0.6028118122217749], [0.24172679023415347, 0.5179043003928995, 0.5361030440378418, 0.5861141616489832, 0.5931808960720524, 0.602199585435119], [0.23972750975018708, 0.5192094604486447, 0.5340302085592601, 0.6034244753596417], [], [], [], [], [], [], [0.39446877587375084, 0.48517428518168515], [0.39494236663021953, 0.48490772974313484], [0.39399557747959163, 0.4854409725455486], [], [], [], [], [], [], [0.37666245321573105, 0.4965878352781536, 0.5474671435641381, 0.5643673166983978], [0.37715221546401695, 0.49628265357915347, 0.548662375814362, 0.563836856413126], [0.37617311720950103, 0.49689318661874415, 0.5462741284594409, 0.5648981817647694], [], [], [], [], [], [], [0.39446877587375084, 0.48517428518168515], [0.39494236663021953, 0.48490772974313484], [0.39399557747959163, 0.4854409725455486], [], [], []]

# Generate Boxplot Data for MCR

averageSCR = average(sustainabilityPoints) # Generate sensible Intersection Points
MR_cleaned = cleanMCR(MCR_Intersections, averageSCR)

print("MR_cleaned: " + str(MR_cleaned))
print(averageSCR)
#prnt(":.")

## combine these different collections into a list    
data_to_plot = [sustainabilityPoints, MR_cleaned] #, scheduled, unscheduled]

plt.figure(facecolor="white")       # Remove grey background

# Create a figure instance
fig = plt.figure(1, figsize=(9, 6))

# Create an axes instance
ax = fig.add_subplot(111)

ax.spines['right'].set_visible(False)       # Remove frame line right
ax.spines['top'].set_visible(False)         # Remove frame line bottom

ax.xaxis.set_tick_params(width = 1.5)       # Size of ticks
ax.yaxis.set_tick_params(width = 1.5)       # Size of ticks

ax.tick_params(axis='y', direction='out')   # Ticks outwards
ax.tick_params(axis='x', direction='out')   # Ticks outwards

ax.xaxis.set_ticks_position('bottom')       # Only tiks on bottom
ax.yaxis.set_ticks_position('left')         # Only ticks on left

# Create the boxplot
bp = ax.boxplot(data_to_plot, sym='o', flierprops = dict(color='grey', markerfacecolor='grey', markersize = 0), boxprops = dict(linewidth=1, color='black'))

# color
## to get fill color
bp = ax.boxplot(data_to_plot, patch_artist=True) 


## Custom x-axis labels
ax.set_xticklabels(["SCR", "MCR"]) 

labelPositionY = [0, 0.2, 0.4, 0.6, 0.80, 1.0]
newLabelsY = [0, 0.2, 0.4, 0.6, 0.80, 1.0]

ax.set_yticks(labelPositionY, minor=False)
ax.set_yticklabels(newLabelsY, minor=False, visible=True, size='small')


#y = np.array([100, 200, 400, 600, 800, 1000, 1200])
#plt.yticks(np.arange(y.min(), y.max(), 200))
## change outline color, fill color and linewidth of the boxes

## change color and linewidth of the whiskers
for whisker in bp['whiskers']:  # Striche linie
    whisker.set(color='grey', linewidth=2)

for cap in bp['caps']:  # Oberer Querbalken
    cap.set(color='grey', linewidth=2)

## change color and linewidth of the caps
#for cap in bp['caps']:
#    cap.set(color='grey', linewidth=2)

## change color and linewidth of the medians
for median in bp['medians']:
    median.set(color='black', linewidth=3)

## change the style of fliers and their fill
for flier in bp['fliers']:
    flier.set(marker='o', color='black', alpha=0.5)
    
for box in bp['boxes']:
    box.set(color='green', linewidth=1, edgecolor = "none")     # change outline color
    box.set(facecolor = 'tan' )                                 # change fill color
    
#pylab.ylim([0,1300])  # real values
pylab.ylim([0,1])  # real values
plt.show()  
outPNGPath = 'Q:/Abteilungsprojekte/Eng/SWWData/Eggimann_Sven/06-Papers/03 - Third Paper - Full cost analysis/02-Figures/testFIg2.jpg'
plt.savefig(outPNGPath)
plt.close()