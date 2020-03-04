from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
import pandas as pd
import random



data = pd.read_csv('Meteorite_Landings.csv')  # importing csv file
df = pd.DataFrame(data, columns=['GeoLocation']) # selecting only the column with coordinates



# the output of the lambda's is made into a list, and set equal to a variable 
geoLocation = list(
    # Input is a list of float tuples
    filter(lambda latlon: latlon[0] != 0 or latlon[1] != 0,
           # Input is a list of lists containing 2 string elements that were separated with split
           map(lambda parsedCoordinates: (float(parsedCoordinates[0]), float(parsedCoordinates[1])),
               # Input is a list of strings
               map(lambda row: row.split(','), df['GeoLocation'].dropna()))))



m = Basemap(projection='mill') # creates a basic map
m.drawcoastlines()
m.drawcountries(color='red')
m.drawstates(color="yellow")
m.drawrivers(color='blue')
m.bluemarble() # gives the map a life-like effect



#list of colors for points plotted
colors = ['b.','g.','r.','c.','m.','y.']



# plotting points
for lon, lat in geoLocation:
    x, y = m.projtran(lon, lat) # coord transformation
    m.plot(x, y, random.choice(colors),markersize=2) # needs grid coords to plot



#displays map with plotted points
plt.show()
