# import and filename
filename = 'data.txt'
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

z, Ua = np.loadtxt(filename,delimiter=',', unpack=True)
tau = 0.045

def make_fourier(na, nb):
    def fourier(x, *a):
        ret = 0.0
        for deg in range(0, na):
            ret += a[deg] * np.cos((deg+1) * np.pi / tau * x)
        for deg in range(na, na+nb):
            ret += a[deg] * np.sin((deg+1) * np.pi / tau * x)
        return ret
    return fourier

popt, pcov = curve_fit(make_fourier(15,15), z, Ua, [0.0]*30)

# Plot data, 15 harmonics, and first 3 harmonics
fig = plt.figure()
ax1 = fig.add_subplot(111)
p1, = plt.plot(z,Ua)
p2, = plt.plot(z, (make_fourier(15,15))(z, *popt))
#p3, = plt.plot(z, (make_fourier(8,8))(z, popt[0], popt[1], popt[2]))
plt.show()