import numpy as np
import sys
import matplotlib.pyplot as plt
A= np.loadtxt(sys.argv[1])
dim = np.shape(A)
fig=plt.figure()
plt.axis([0,1000,0,100])
ded = np.linalg.eig(A)
print('def',ded[0],'\n',ded[1],file=open("output.txt","w"))
b=np.ones(dim[0])
bnext=b
q=np.zeros((1000,2))
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
	ev=((A@b)@b)/(b@b)
	print('[',ev,i,']',b,file=open("output.txt", "a"))
	q[i]=(ev,i)
	plt.scatter(i,ev)
	if (np.allclose(div,1,atol = 1e-6 	,rtol = 0)):
		print(b,file=open("output.txt", "a"))
		break
bnext=np.ones(dim[0])
A=np.linalg.inv(A)
plt.show()
plt.savefig('max.png')
fig=plt.figure()
plt.axis([0,20,0,20])
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
plt.show()
