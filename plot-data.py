import sys
import matplotlib.pyplot as plt
import numpy as np
import math
from datetime import datetime as dt

def recircle(n, off):
	"""
	Adds or subtracts to/from n, until
	it is between [0, n]
	"""
	if n < 0:
		while n < 0: 
			n += off
	elif n > off:
		while n > off:
			n -= off
	return n

fig = plt.figure()
fig.set_size_inches(24,12)		# World map will be drawn on a (20,10) inch grid, w/ (2,1) margin on each side
fig.set_dpi(300)				# Setting the DPI too low results in render artifacts between dots
fig.set_tight_layout(True)

canvas = fig.add_subplot(111)
canvas.set_xlim(left=-200, right=200)
canvas.set_ylim(bottom=-110,top=110)
canvas.set_aspect('equal')
canvas.set_facecolor((0.8, 0.8, 0.8))
canvas.set_axis_off()

# We need to calculate the sun's `Terminator`
# https://www.aa.quae.nl/en/antwoorden/zonpositie.html#v526
doy = dt.utcnow().timetuple().tm_yday

M = -3.6 + 0.9856 * doy
nu = M + 1.9 * math.sin(math.radians(M))
l = nu + 102.9
delta = 22.8 * math.sin(math.radians(l)) + 0.6 * math.sin(math.radians(l))**3		# Declination of the sun
delta = math.radians(delta)

utc = dt.utcnow()
mins_utc = utc.hour * 60. + utc.minute

lat = delta
lon = 180. - 15./60. * mins_utc
lon = recircle(lon, 360)
lon = math.radians(lon)
# This works correctly, but is commented out to test if it works with the above recircle line as well.
#lonold = 180. - 15./60. * mins_utc
#if lonold > 180:
#	lonold -= 360.
#if lonold < -180:
#	lonold += 360.
#lonold = math.radians(lonold)
#print("lon vs lonold", lon == lonold)


# Draw the terminator
xT, yT = [], []
for d in range(0, 360, 1):
	psi = math.radians(d)
	B = math.asin(math.cos(lat) * math.sin(psi))
	x = - math.cos(lon) * math.sin(lat) * math.sin(psi) - math.sin(lon) * math.cos(psi)
	y = - math.sin(lon) * math.sin(lat) * math.sin(psi) + math.cos(lon) * math.cos(psi)
	L = math.atan(y/x)
	if x < 0 : 
		L += math.pi
	L = recircle(L, 2*math.pi) - math.pi

	xT.append(math.degrees(L))
	yT.append(math.degrees(B))


# Sort the terminator points in pairs
xT, yT = (list(t) for t in zip(*sorted(zip(xT, yT))))
terminator = canvas.plot(xT, yT, c="red")


# Draw the parsed world map
# Marker size is related to their area
# We select a marker size, so that our plot can acommodate 360*180 points
# https://stackoverflow.com/questions/14827650/pyplot-scatter-plot-marker-size
x, y = [], []
for line in sys.stdin:
	tmp = line.strip().split(",")
	x.append(int(tmp[0]))
	y.append(int(tmp[1]))

canvas.scatter(x, y, s=2)
x1, y1 = [], []
# Interpolate the points of the terminator for each degree.
# This way we can draw the 'daylight' points in a different color
y_interp = np.interp(x,xT,yT)
for i in range(len(x)):
	if y[i] > y_interp[i]:
		x1.append(x[i])
		y1.append(y[i])
canvas.scatter(x1, y1, c = (0.8, 0.8, 0.8),  s=2)

fig.savefig('public/images/output_term.png', dpi='figure', format="png", transparent=True)
