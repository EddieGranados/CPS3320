from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import random

data = pd.read_csv('Meteorite_Landings.csv')
df = pd.DataFrame(data, columns=['GeoLocation'])

geoLocation = list(
    # Input is a list of float tuples
    filter(lambda latlon: latlon[0] != 0 or latlon[1] != 0,
           # Input is a list of lists containing 2 string elements that were separated with split
           map(lambda parsedCoordinates: (float(parsedCoordinates[0]), float(parsedCoordinates[1])),
               # Input is a list of strings
               map(lambda row: row.split(','), df['GeoLocation'].dropna()))))


m = Basemap(projection='mill')

m.drawcoastlines()
m.drawcountries(color='red')
m.drawstates(color="yellow")
m.drawrivers(color='blue')
m.bluemarble()

colors = ['bo', 'go', 'ro', 'co', 'mo', 'yo', 'ko', 'wo']

# plotting points
for lon, lat in geoLocation:
    x, y = m.projtran(lon, lat)        # coord transformation
    m.plot(x, y, random.choice(colors))  # needs grid coords to plot

plt.show()
