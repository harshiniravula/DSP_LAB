import numpy as np
from scipy.signal import cheby1, freqz
import matplotlib.pyplot as plt
fs = 32
order = 5
Apass = 0.001
fcut = 0.25
wn = fcut / (0.5*fs)
b,a = cheby1(order, Apass, wn)
w,h = freqz(b, a, worN=8000)
plt.figure(1)
plt.plot(0.5*fs*w/np.pi, 20*np.log10(np.abs(h)))
plt.axvline(fcut, color='r', alpha=0.2)
plt.plot([0, fcut], [-Apass, -Apass], color='r', alpha=0.2)
plt.xlim(0, 0.3)
plt.xlabel('Frequency (Hz)')
plt.ylim(-5*Apass, Apass)
plt.ylabel('Gain (dB)')
plt.grid()
plt.title("Chebyshev Type I Lowpass Filter")
plt.show()