'''from pylab import figure, show, rand
from matplotlib.patches import Ellipse

NUM = 250

#ells = [Ellipse(xy=rand(2)*10, width=rand(), height=rand(), angle=rand()*360)
#        for i in range(NUM)]

ells = [Ellipse(xy=rand(2)*10, width=1, height=1, angle=0)
        for i in 1]

print(ells)

fig = figure()
ax = fig.add_subplot(111, aspect='equal')

for e in ells:
    ax.add_artist(e)
    #e.set_clip_box(ax.bbox)
    #e.set_alpha(rand())
    #e.set_facecolor(rand(3))

ax.set_xlim(0, 10)
ax.set_ylim(0, 10)

show()
'''

from matplotlib.patches import Ellipse
import matplotlib.pyplot as plt


plt.figure()
#ax = plt.gca()
ax = plt.subplot(111)

ellipse = Ellipse(xy=(10, 10), width=1, height=20, edgecolor='r', fc='None', lw=2)
ax.add_patch(ellipse)
ax.set_xlim(0, 100)
ax.set_ylim(0, 100)
show()