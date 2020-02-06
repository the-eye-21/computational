import numpy as np
import sys
A= np.loadtxt(sys.argv[1])
dim = np.shape(A)
ded = np.linalg.eig(A)
print('def',ded[0],'\n',ded[1])
b=np.ones(dim[0])
bnext=b

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
	print('[',ev,i,']',b)
	if (np.allclose(div,1,atol = 1e-6 	,rtol = 0)):
		print(b)
		break
bnext=np.ones(dim[0])
A=np.linalg.inv(A)

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
	print('[',ev1,i,']')
	if (np.allclose(div,1,atol = 1e-6 	,rtol = 0)):
		print(b)
		break

