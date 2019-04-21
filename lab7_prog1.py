from pylab import *
import numpy as np
import matplotlib.pyplot as plt
import cmath as cm
x=int(input("enter number of samples for x[n]:"))
y=[]
print("enter samples for x[n]")
for i in range(0,x):
	k=int(input())
	y=np.append(y,k)
print("x[n]=",y)
k=int(input("enter the k value"))
N=int(input("enter the dft points"))
j=cm.sqrt(-1)
X=[]
w=np.linspace(-np.pi,np.pi,N)
for i in range(0,k):
	sum=0
	for n in range(0,len(x)):
		k=np.exp(-j*2*np.pi*i*n/N)
		sum=sum+(y[n]*)
	X.append(sum)
plt.subplot(2,1,1)
plt.stem(np.abs(X))
plt.title("magnitude spectrum")
plt.subplot(2,1,2)
plt.stem(np.angle(X)/np.pi)
plt.title("phase spectrum")
plt.show()
