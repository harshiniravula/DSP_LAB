import numpy as NP
import matplotlib.pyplot as MP
fs=input("enter sampling frequency")
f1=input("enter first wave frequency")
f2=input("enter second wave frequency")
x=(0,100,2)
y=NP.sin(2*NP.pi*f1*x/fs)
z=NP.cos(2*NP.pi*f2*x/fs)
k=(y+z)
MP.subplot(1,3,1)
MP.plot(x,y)
MP.xlabel('time')
MP.ylabel('amplitude')
MP.title("first sinusoidal wave")
MP.subplot(1,3,2)
MP.plot(x,z)
MP.xlabel('time')
MP.ylabel('amplitude')
MP.title("second sinusoidal wave")
MP.subplot(1,3,3)
MP.plot(x,k)
MP.xlabel('time')
MP.ylabel('amplitude')
MP.title("resultant wave")
MP.show()




