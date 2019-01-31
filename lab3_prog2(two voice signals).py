import scipy.io.wavfile as wav
import numpy as np
from matplotlib import pyplot as mp
fs1,data1=wav.read('harshini123.wav')
fs2,data2=wav.read('moksha.wav')
print(fs1,len(data1),data1)
print(fs2,len(data2),data2)
t=np.arange(0,len(data1)/fs1,1.0/fs1)
s=np.arange(0,len(data2)/fs2,1.0/fs2)
mp.subplot(211)
mp.plot(t,data1)
mp.subplot(212)
mp.plot(s,data2)
mp.show()


