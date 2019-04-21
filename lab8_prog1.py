import numpy as np
import matplotlib.pyplot as plt
m=int(input("enter the value of m"))
h=[]
for n in range(0,m-1):
	x=1
	h=np.append(y,x)
n=np.arange(0,m-1,1)
plt.stem(n,y)
plt.title("rectangular window")
plt.show()


