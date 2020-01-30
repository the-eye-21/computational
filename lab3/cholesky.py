import numpy as np
import sys
import math
import scipy as sp
import scipy.linalg as la
a = np.loadtxt(r'mat1.txt')
dim = np.shape(a)
print(a)
#splitting the matrix.
[A,b]=np.split(a,[dim[0]],axis=1)
print(A,'\n',b)
#cholesky decomposition.
L = np.zeros((dim[0],dim[0]))
for i in range(dim[0]):
    L[i][i] = A[i][i]
    for j in range(i):
        if(A[j][i]!=A[i][j]):
          print('not symmetric')
          quit()
        L[i][j]=A[j][i]
        for k in range(j):
            L[i][j]=L[i][j]-(L[j][k]*L[i][k])
        L[i][j]=L[i][j]/L[j][j]
    for j in range(i):
        L[i][i]=L[i][i]-(L[i][j]**2)
        if (L[i][i]<0):
          print('not positive definite')
          quit()
    L[i][i]=np.sqrt(L[i][i])
print("L is \n" ,L)

#crossverification
lol = la.cholesky(A,lower=True)
print("cross verifying using scipy function, L is: \n",lol)

U=np.transpose(L)
print('Transpose of L is: \n',U)
mu = np.matmul(L,U)
print('product is: \n',mu)

