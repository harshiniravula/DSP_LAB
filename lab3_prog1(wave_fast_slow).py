import scipy.io.wavfile as wav
import numpy as np
from matplotlib import pyplot as mp
fs,data=wav.read('harshini123.wav')
print(fs,len(data),data)
mp.subplot(211)
mp.plot(data)
t=np.arange(0,len(data)/fs,1.0/fs)
mp.subplot(212)
mp.plot(t,data)
mp.show()
wav.write('harshini-fast',2*fs,data)
wav.write('harshini-slow',0.5*fs,data)


