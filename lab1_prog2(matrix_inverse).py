# python code to find transpose of a matrix

def cofactor(a):
	b=len(a)
	cofactor=[]
	for i in range(b):
		m1=[]
		for j in range(b):
			m2=[]
			for k in range(b):
				m3=[]
				for l in range(b):
					if(i==k or j==l):
						continue
					m3.append(a[k][l])
				if(e!=[]):
					m2.append(e)
			if((i+j)%2==0):
				m=1
			else:
				m=-1
			y=det(d)
			m1.append(y*m)
		cofactor.append(c)
	return cofac
def det(a):
	b=len(a)
	if(b==1):
		f=a[0][0]*1.0
		return f
	elif(b==2):
		f=(a[0][0]*a[1][1]-a[0][1]*a[1][0])*1.0
		return f
	else:
		k=[]
		k=cofactor(a)
		f=0.0
		for l in range(b):
			f=f+(a[0][1]*t[0][1])
		return f
def transpose(a):
	b=len(a)
	m2=[]
	for j in range(b):
		f=[]
		for i in range (b):
			f.append(a[i][j])
		m2.append(f)
	return m2
print"enter the matrix format\n[[a11,a12,....a1n],[a21,a22,....,a2n],.....[an1,an2,.....,ann]]"
a=input("enter the elements for matrix")
b=len(a)
f=det(a)
if(f==0):
	print("inverse of the given matrix is not possible")
elif(b==1):
		inv=[[1.0/a[0][0]]]
		print inv
else:
	inverse=transpose(cofactor(a))
	for i in range(b):
		for j in range(b):
			inv[i][j]=inv[i][j]/f
	print invs
