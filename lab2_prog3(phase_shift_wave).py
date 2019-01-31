import numpy as NP
import matplotlib.pyplot as MP
fs=input("enter sampling frequency")
f1=input("enter first wave frequency")
t1=input("enter the phase to be shifted")
x=(0,100,2)
y=NP.sin(2*NP.pi*f1*x/fs)
z=NP.cos(2*NP.pi*f1*x/fs+t1)
MP.subplot(1,2,1)
MP.plot(x,y)
MP.xlabel('time')
MP.ylabel('amplitude')
MP.title("sinusoidal wave")
MP.subplot(1,2,2)
MP.plot(x,z)
MP.xlabel('time')
MP.ylabel('amplitude')
MP.title("wave after phase shift")
MP.show()




