import numpy as np
import sys
import math
import scipy as sp
import scipy.linalg as la
a = np.loadtxt(r'E:/code/gauss.txt')
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
print("L is" ,L)

#crossverification
lol = la.cholesky(A,lower=True)
print(lol)
lowmat=L
upmat = np.transpose(L)
b=np.transpose(b)
# transpose makes it easier to read *facepalm
dim1 = np.shape(b)
ux=b
#forward substitution for all equations
for k in range(dim1[0]):
    for i in range(dim[0]):
        for j in range(i):
            ux[k][i] = ux[k][i]-(ux[k][j]*lowmat[i][j])
print("\nux vectors are: \n",np.round_(ux,6),'\n')
#back substitution for all equations
x=ux
for k in range(dim1[0]):
    for i in range(dim[0]-1,-1,-1):
        for j in range(i+1,dim[0]):
            x[k][i] = x[k][i]-(x[k][j]*upmat[i][j])
        x[k][i]=x[k][i]/upmat[i][i]
print("x solution vectors are: \n" ,np.round_(x,6))
