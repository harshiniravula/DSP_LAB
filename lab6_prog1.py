import numpy as np
import matplotlib.pyplot as plt
import cmath as cm
def dft(x):
    j=cm.sqrt(-1)
    y=[]
    n=len(x)
    N=10
    w=np.linspace(0,2*np.pi,10)
    for i in range(0,N):
	sum=0
        for k in range(0,n):
            sum=sum+(x[k]*np.exp((-k*2*np.pi*j*i)/N))
        y.append(sum)
    return y
a=int(input("enter the no. of samples of x:"))
x1=[]
for i in range(a):
	b=int(input())
	x1=np.append(x1,b)
t=dft(x1)
plt.plot(t)
plt.show()
