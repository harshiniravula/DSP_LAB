import numpy as NP
import matplotlib.pyplot as MP
fs=input("enter sampling frequency")
f1=input("enter first wave frequency")
f2=input("enter second wave frequency")
x=(0,100,1)
y=NP.sin(2*NP.pi*f1*x/fs)
z=NP.cos(2*NP.pi*f2*x/fs)
MP.subplot(1,2,1)
MP.plot(x,y)
MP.xlabel('time')
MP.ylabel('amplitude')
MP.title("first sinusoidal wave")
MP.subplot(1,2,2)
MP.plot(x,z)
MP.xlabel('time')
MP.ylabel('amplitude')
MP.title("second sinusoidal wave")
MP.show()




