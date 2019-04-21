import numpy as np
import matplotlib.pyplot as plt
def movavg(x):
	l=int(input("enter the order:"))
	n=len(x)
	z=[]
	for i in range(n):
		s=0
		for k in range(l):
			if i-k<n and i-k>=0:
				s=s+x[i-k]
		k=float(s)/float(l)
		z=np.append(z,k)
	return(z)
l=[]
g=int(input("enter no of samples:"))
for j in range(g):
	s=int(input("enter samples:"))
	l=np.append(l,s)
print(l)
r=movavg(l)
print(r)
f=int(input("enter signal frequency:"))
fs=int(input("enter sampling frequency:"))
a=np.arange(0,100,0.1)
x=np.sin(2*np.pi*(float(f)/float(fs))*a)
plt.subplot(4,1,1)
plt.plot(x)
N=np.random.rand(x.shape[0])
plt.subplot(4,1,2)
plt.plot(N)
y=x+N
plt.subplot(4,1,3)
plt.plot(y)
d=movavg(y)
plt.subplot(4,1,4)
plt.plot(d)
plt.show()
