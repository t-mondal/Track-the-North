# import libraries
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from time import sleep
import pandas as pd

with open('dataframe.txt', 'r') as f:
	data = pd.read_csv(f)

print data
data = data.values
print data
t = data[:,1]
print t
x = data[:,4]

# fourier function for fourier series
tau = 1
def fourier(t, *a):
    ret = np.cos(np.pi / tau * t + a[0])
    for deg in range(1, len(a)):
        ret += a[deg] * np.cos((deg+1) * np.pi / tau * t + a[0])
    return ret

# fit to curve
# popt has optimal values for parameters
# pcov has estimated covariance
# h is number of harmonics
h = 5
# arguments and covariance for each fourier series for respectively x and y values over time
popt, pcov = curve_fit(fourier, t, x, [1.0] * (h+1))

# Plot x
fig = plt.figure()
ax1 = fig.add_subplot(111)
p1x = plt.plot(t, x, 'r-')
p2x = plt.plot(t,fourier(t, *argx))
# display graph
plt.show()

y = data[:,5]

popt, pcov = curve_fit(fourier, t, y, [1.0] * (h+1))
# Plot y
fig = plt.figure()
ay1 = fig.add_subplot(111)
p1y = plt.plot(t, y, 'r-')
p2y = plt.plot(t,fourier(t, *argy))
# display graph
plt.show()