# import and filename
filename = 'data.txt'
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

z, Ua = np.loadtxt(filename,delimiter=',', unpack=True)
tau = 0.045

def fourier(x, *a):
    ret = a[0] * np.cos(np.pi / tau * x)
    for deg in range(1, len(a)):
        ret += a[deg] * np.cos((deg+1) * np.pi / tau * x)
    return ret

# Fit with 15 harmonics
popt, pcov = curve_fit(fourier, z, Ua, [1.0] * 15)

# Plot data, 15 harmonics, and first 3 harmonics
fig = plt.figure()
ax1 = fig.add_subplot(111)
p1, = plt.plot(z,Ua)
p2, = plt.plot(z, fourier(z, *popt))
p3, = plt.plot(z, fourier(z, popt[0], popt[1], popt[2]))
plt.show()