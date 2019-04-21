import numpy as np
from matplotlib import pyplot as plt
def timrev(a):
	y=[]
	m=len(a)
      	for i in range(m):
		y=np.append(y,a[x-i-1])
        return y
fs=500
k=np.arange(0,500)
a=np.sin(2*np.pi*(30.0/500.0)*k)
b=np.sin(2*np.pi*(60.0/500.0)*k)
d=a+b
x=len(a)
z=[]
l=timrev(a+b)
y=len(l)
for n in range(x+y-1):
        sum=0
        for k in range(x):
            if n-k<y and n-k>=0:
                sum=sum+d[k]*l[n-k]
        z=np.append(z,sum)
plt.plot(z)
plt.xlabel("time")
plt.ylabel("correlation")
plt.show()
