# -*- coding: utf-8 -*-
"""
Created on Thu Jul 28 04:44:58 2016

@author: Wigas 2016
"""

from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
import numpy as np
import csv

eq_map = Basemap(projection='merc', lat_0=0, lon_0=125, \
           resolution='l', area_thresh=0.1, \
           llcrnrlon=90, llcrnrlat=-15, \
           urcrnrlon=155, urcrnrlat=15) 

# Open the earthquake data file
filename = 'csvlast60event.csv'

# Empty list
lats, lons = [], []
magnitudes = []

# parsing
with open(filename) as f:
    reader = csv.reader(f)
    
    next(reader)
    
    for row in reader:
        lats.append(float(row[3]))
        lons.append(float(row[4]))
        magnitudes.append(float(row[5]))

# Display the first 5 lats and lons
print('lats', lats[0:5])
print('lons', lons[0:5])

eq_map.drawcoastlines()
eq_map.drawcountries()
eq_map.drawmapboundary()
eq_map.fillcontinents(color = 'gray')
eq_map.drawmeridians(np.arange(0, 360, 30))
eq_map.drawparallels(np.arange(-90, 90, 30))

x,y=eq_map(lons,lats)

def get_marker_color(magnitude):
    # Returns green for small earthquakes, yellow for moderate
    #  earthquakes, and red for significant earthquakes.
    if magnitude < 5.0:
        return ('go')
    elif magnitude < 6.0:
        return ('yo')
    else:
        return ('ro')

min_marker_size = 2.25
for lon, lat, mag in zip(lons, lats, magnitudes):
    x,y = eq_map(lon, lat)
    msize = mag * min_marker_size
    marker_string = get_marker_color(mag)
    eq_map.plot(x, y, marker_string, markersize=msize)

title_string = "Earthquakes of Magnitude 5.0 or Greater\n"
title_string += "Between April to July 2016"
plt.title(title_string)

plt.show()

