'''# Box plots with custom fill colors

import matplotlib.pyplot as plt
import numpy as np

# Random test data
np.random.seed(123)
all_data = [np.random.normal(0, std, 100) for std in range(1, 4)]

fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(12, 5))

# rectangular box plot
bplot1 = axes[0].boxplot(all_data,
                         vert=True,   # vertical box aligmnent
                         patch_artist=True)   # fill with color



# adding horizontal grid lines
for ax in axes:
    ax.yaxis.grid(True)
    ax.set_xticks([y+1 for y in range(len(all_data))], )
    ax.set_xlabel('xlabel')
    ax.set_ylabel('ylabel')

# add x-tick labels
plt.setp(axes, xticks=[y+1 for y in range(len(all_data))],
         xticklabels=['x1', 'x2', 'x3', 'x4'])

plt.show()
'''





#!/usr/bin/python

#
# Example boxplot code
#
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

kantonGeoBFS = [[1, 'Zurich', 'ZH'], [2, 'Bern', 'BE'], [3, 'Luzern', 'LU'], [4, 'Uri', 'UR'], [5, 'Schwyz', 'SZ'], [6, 'Obwalden', 'OW'], [7, 'Nidwalden', 'NW'], [8, 'Glarus', 'GL'], [9, 'Zug', 'ZG'], [10, 'Freiburg', 'FR'], [11, 'Solothurn', 'SO'], [12, 'Basel-Stadt', 'BS'], [13, 'Basel-Landschaft', 'BL'], [14, 'Schaffhausen', 'SH'], [15, 'Appenzell Ausserrhoden', 'AR'], [16, 'Appenzell Innerrhoden', 'AI'], [17, 'St. Gallen', 'SG'], [18, 'Graubuenden', 'GR'], [19, 'Aargau', 'AG'], [20, 'Thurgau', 'TG'], [21, 'Tessin', 'TI'], [22, 'Waadt', 'VD'], [23, 'Wallis', 'VS'], [24, 'Neuenburg', 'NE'], [25, 'Genf','GE'], [26, 'Jura', 'JU']]


unscheduled_data = [4,5,6,4,6,5,3,5,67,4,43,5,3]
totalCosts_data = [4,5,6,4,6,5,3,5,67,4,43,5,3]


## combine these different collections into a list    
data_to_plot = [unscheduled_data, totalCosts_data]

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
bp = ax.boxplot(data_to_plot, sym='o') #flierprops = dict(color='grey', markerfacecolor='grey', markersize = 0), boxprops = dict(linewidth=1, color='black') 

# color
bp = ax.boxplot(data_to_plot, patch_artist=True) 

## Custom x-axis labels
ax.set_xticklabels(["Total Costs", "Scheduled", "Unscheduled"])

#labelPositionY = [50, 100, 200, 400, 600, 800, 1000, 1200]
#newLabelsY = [50, 100, 200, 400, 600, 800, 1000, 1200]

#ax.set_yticks(labelPositionY, minor=False)
#ax.set_yticklabels(newLabelsY, minor=False, visible=True, size='small')


## change color and linewidth of the whiskers
for whisker in bp['whiskers']:  # Striche linie
    whisker.set(color='grey', linewidth=1)

for cap in bp['caps']:  # Oberer Querbalken
    cap.set(color='grey', linewidth=1)

## change color and linewidth of the medians
for median in bp['medians']:
    median.set(color='black', linewidth=3)

## change the style of fliers and their fill
for flier in bp['fliers']:
    flier.set(marker='o', color='black', alpha=0.5)
    
for box in bp['boxes']:
    
    # change outline color
    box.set(color='black', linewidth=1, edgecolor = "none")
    
    # change fill color
    box.set(facecolor = 'tan' )

    
#pylab.ylim([0,1300])  # real values
#pylab.ylim([0,600])  # real values
plt.show()  
