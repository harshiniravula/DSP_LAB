import numpy as np
import matplotlib.pyplot as plt
a=int(input("enter no. of samples:"))
x=[]
y=[]
for i in range(n):
	y=int(input("enter samples:"))
	x=np.append(x,y)
s=0
for i in range(n):
	s=s+x[i]
	y=np.append(y,s)
print("accumulator result:",y)
