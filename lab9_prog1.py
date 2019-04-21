import numpy as np
import matplotlib.pyplot as plt
import cmath
dp=float(input("enter dp"))	
ds=float(input("enter ds"))
wp=float(input("enter wp"))
ws=float(input("enter ws"))
e=(1.0/(ds**2))-1
f=(1.0/(dp**2))-1
w=np.arange(0,10000,10)
def bwfilter(dp,ds,wp,ws):
 if (wp<ws):
	m=np.log10(e/f)
	s=m/2
	r=np.log10(ws/wp)
	n=np.ceil(s/r)
	print n
	wc=wp/(e**(1.0/(2.0*n)))
	print wc
	l=1+((2*np.pi*w/wc)**(2*n))
	x=1/np.sqrt(l)
	return x
x=bwfilter(dp,ds,wp,ws)
plt.plot(np.log10(w),20*np.log10(x))
plt.show()

	
		

