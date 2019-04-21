import numpy as np
import matplotlib.pyplot as plt
import cmath
dp=float(input("enter dp"))	
ds=float(input("enter ds"))
wp=float(input("enter wp"))
ws=float(input("enter ws"))
t=0.001
e=(1/(ds**2))-1
f=(1/(dp**2))-1
m=np.log10(e/f)
s=m/2
r=np.log10(ws/wp)
n=np.ceil(s/r)
print n
wc=wp/(e**(1/(2*n)))
print wc
t=3*wc
w=np.arange(0,10000,10)
d=w/t
l=1+((w/wc)**(2*n))
x=1/np.sqrt(l)
if(n%2==0):
	e=1
	j=int(n/2)
	for k in range(1,j):
		v=(2*k-1)*np.pi/(2*n)
		b=2*np.sin(v)
		q=(d)**2+(b*wc*d)+wc**2
		e=e*q
                h=((wc)**n)/e
else:
	e=d+wc
	j=int(n/2)-1
	for k in range(1,j):
		v=(2*k-1)*np.pi/(2*n)
		b=2*np.sin(v)
		q=(d)**2+(b*wc*d)+wc**2
		e=e*q
                h=((wc)**n)/e
	
plt.subplot(1,2,1)
plt.plot(x)
plt.title("butterworth filter")
plt.subplot(1,2,2)
plt.stem(h)
plt.title("impulse invarient transform")
plt.show()

		

