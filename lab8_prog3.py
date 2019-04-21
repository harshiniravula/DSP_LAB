import numpy as np
import matplotlib.pyplot as plt
m=int(input("enter the value of m"))
y[]
for n in range(0,m-1):
	x=0.54-0.46*np.cos(2*np.pi*n/(m-1))
	y=np.append(y,x)
n=np.arange(0,m-1,1)
plt.stem(n,y)
plt.title("hamming window")
plt.show()
