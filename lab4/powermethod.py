import numpy as np
import sys
A= np.loadtxt(sys.argv[1])
dim = np.shape(A)
b=np.ones(dim[0])
bnext=b
for i in range(1000):
    b=bnext
    bnext=A@b
    normfac=np.absolute(bnext@bnext)
    bnext=bnext/normfac
    div=np.divide(bnext,b)
    div=div/div[0]
    if (np.allclose(div,1,atol = 1e-9,rtol = 0)):
        babs=np.abs(b)
        bmin=np.min(babs)
        b=b/bmin
        print('max',b,i)
        ev=((A@b)@b)/(b@b)
        print(ev)
        break
bnext=np.ones(dim[0])
ded = np.linalg.eig(A)
print('def',ded)
A=np.linalg.inv(A)

for i in range(1000):
    b=bnext
    bnext=A@b
    normfac=np.absolute(bnext@bnext)
    bnext=bnext/normfac
    div=np.divide(bnext,b)
    div=div/div[0]
    if (np.allclose(div,1,atol = 1e-9,rtol = 0)):
        babs=np.abs(b)
        bmin=np.min(babs)
        b=b/bmin
        print('min',b,i)
        ev1=(b@b)/((A@b)@b)
        print(ev1)
        break
    


