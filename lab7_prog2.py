from pylab import *
import matplotlib.pyplot as plt
import numpy as np
import cmath as cm
x=int(input("enter number of samples of x[n]"))
y=[]
print("enter samples for x[n]:")
for i in range(0,x):
	k=int(input())
	y=np.append(y,k)
print("x[n]=",y)
N=1000
j=cm.sqrt(-1)
X=[]
w=np.linspace(-np.pi,np.pi,N)
for i in range(0,N):
	sum=0
	for n in range(0,len(y)):
		sum=sum+(x[n]*np.exp(-n*w[i]*j))
	X.append(sum)
print("X[n]=",np.abs(X))
plt.subplot(4,1,1)
plt.plot(w,np.abs(X))
plt.title("magnitude spectrum")
plt.grid()
plt.subplot(412)
plt.plot(w,angle(X)/np.pi)
plt.title("phase spectrum")
plt.grid()
plt.subplot(4,1,3)
plt.plot(w,real(X))
plt.title("real values of X")
plt.grid()
plt.subplot(4,1,4)
plt.plot(w,imag(X))
plt.title("imaginary values of X")
plt.grid()
plt.show()
