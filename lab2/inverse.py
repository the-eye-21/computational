import numpy as np
import sys
a = np.loadtxt(sys.argv[1])
dim = np.shape(a)
if (dim[0]!=dim[1]):
    quit()
print(a)
upmat=a
lowmat = np.identity(dim[0])
for i in range(dim[0]):
    # i selects pivot element.
    # is also the code for Gauss elimination without pivoting
    if(upmat[i][i]!=0):
        for j in range(i+1, dim[0]):
            lowmat[j][i] = (upmat[j][i]/upmat[i][i])
            upmat[j] = upmat[j] - ((upmat[j][i]/upmat[i][i])*upmat[i])
    # in case there's no unique solution.
    if(upmat[i][i]==0):
        print("inverse not possible")
        quit()
print("Upper Triangular Matrix is: \n",upmat,"\nLower Triangular Matrix is: \n",lowmat)
#finding inverse. solving the equations with identity matrix in place of b.
inv = np.identity(dim[0])
for k in range(dim[0]):
    for i in range(dim[0]):
        for j in range(i):
            inv[i][k] = inv[i][k]-(inv[j][k]*lowmat[i][j])
#back substitution for all equations
for k in range(dim[0]):
    for i in range(dim[0]-1,-1,-1):
        for j in range(i+1,dim[0]):
            inv[i][k] = inv[i][k]-(inv[j][k]*upmat[i][j])
        inv[i][k]=inv[i][k]/upmat[i][i]
print("Inverse of the matrix is: \n" ,inv)

