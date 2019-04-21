import numpy as np
import matplotlib.pyplot as plt
import cmath
j=cmath.sqrt(-1)
N=100
a=int(input("enter the no. of samples of x:"))
x=[]
for i in range(a):
	b=int(input())
	x=np.append(x,b)
def dtft(x): 
 n=len(x)
 y=[]
 q=np.linspace(0,N,1000)
 for i in range(-N,N):
	w=q[i]
	s=0
	for k in range(0,n,1):
		s=s+(x[k]*np.exp(-j*w*k))
	y=np.append(y,s)
 return y
y=dtft(x)
print(y)
ym=np.abs(y)
yp=np.angle(y)
plt.subplot(3,1,1)
plt.title("dtft")
plt.plot(y)
plt.subplot(3,1,2)
plt.title("mag spectrum")
plt.plot(ym)
plt.subplot(3,1,3)
plt.title("phase spectrum")
plt.plot(yp)
plt.show()


