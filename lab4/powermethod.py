import numpy as np
import sys
import matplotlib.pyplot as plt
#reading input
A= np.loadtxt(sys.argv[1])
dim = np.shape(A)
#initialise plot
fig=plt.figure()
plt.axis([0,1000,0,100])
#solution from python functions
ded = np.linalg.eig(A)
print('def',ded[0],'\n',ded[1],file=open("output.txt","w"))
b=np.ones(dim[0])
bnext=b
#iterations
for i in range(1000):
	b=bnext
	#multiplication
	bnext=A@b
	#normalisation factor
	normfac=np.absolute(bnext@bnext)
	bnext=bnext/normfac
	#to compare bnext and b
	div=np.divide(bnext,b)
	div=div/div[0]
	#to find minimum
	babs=np.abs(b)
	bmin=np.min(babs)
	b=b/bmin
	#finding eigen value
	ev=((A@b)@b)/(b@b)
	print('[',ev,i,']',b,file=open("output.txt", "a"))
	#plotting
	plt.scatter(i,ev)
	if (np.allclose(div,1,atol = 1e-6 	,rtol = 0)):
		print(bnext,file=open("output.txt", "a"))
		break
bnext=np.ones(dim[0])
A=np.linalg.inv(A)
plt.savefig('max.png')
plt.show()
for i in range(1000):
	b=bnext
	bnext=A@b
	normfac=np.absolute(bnext@bnext)
	bnext=bnext/normfac
	div=np.divide(bnext,b)
	div=div/div[0]
	babs=np.abs(b)
	bmin=np.min(babs)
	b=b/bmin
	ev1=((A@b)@b)/(b@b)
	print('[',1/ev1,i,']',b,file=open("output.txt", "a"))
	q[i]=(1/ev1,i)
	plt.scatter(i,1/ev1)
	if (np.allclose(div,1,atol = 1e-6 	,rtol = 0)):
		print(b,file=open("output.txt", "a"))
		break
plt.savefig('min.png')
