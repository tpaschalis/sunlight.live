import geopandas as gpd
import matplotlib.pyplot as plt
from shapely.geometry import Point, Polygon
import os

gdf = gpd.read_file('ne_50m_land/ne_50m_land.shp')
#gdf = gpd.read_file('ne_110m_land/ne_110m_land.shp')
print("gdf :", type(gdf))

polygons = gdf["geometry"]
print(polygons.shape)

landX = []
landY = []
for i in range(-180, 180, 1):
	print(i)
	for j in range(-90, 90, 1):
		for poly in polygons:
			if Point(i, j).within(poly):
				landX.append(i)
				landY.append(j)


with open("land-points-shapefile", "w") as f:
	if len(landX) != len(landY):
		os.Exit(1)
	for i in range(len(landX)):
		f.write(str(landX[i])+","+str(landY[i])+"\n")


gdf.plot()

plt.show()

# Initially, I used something like this, below.
# Thing is, the API returned erroneous values, so I opted for the shapefile version
#x, y = [], []
# {"lon":85.0,"lat":174.0,"water":true}
#for line in sys.stdin:
#	coords = json.loads(line, object_hook=lambda d: namedtuple('X', d.keys())(*d.values()))
#	x.append(round(coords.lon))
#	y.append(round(coords.lat))
#print(len(x))
#print(len(y))
