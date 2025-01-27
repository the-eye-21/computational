import numpy as np
import sys
A = np.loadtxt('E:/code/lab2/mat1.txt')
dim = np.shape(A)
print(A)

#splitting the matrix.
[a,b]=np.split(A,[dim[0]],axis=1)
print(a,'\n',b)
upmat=a
lowmat = np.identity(dim[0])
for i in range(dim[0]):
    # i selects pivot element.
    # to check if pivot element is zero
    # remove this part from comments to add pivoting
    if (upmat[i][i] == 0):
        #to swap rows in case pivot element is zero.
        for k in range(i+1,dim[0]):
            if (upmat[k][i]!=0):               
                upmat[[i,k]]=upmat[[k,i]]
                lowmat[[i,k]]=lowmat[[k,i]]
                b[[i,k]]=b[[k,i]]
                break
    # after making sure that either pivot element is zero or there are no non-zero elements in that column
    # is also the code for Gauss elimination without pivoting
    if(upmat[i][i]!=0):
        for j in range(i+1, dim[0]):
            lowmat[j][i] = (upmat[j][i]/upmat[i][i])
            upmat[j] = upmat[j] - ((upmat[j][i]/upmat[i][i])*upmat[i])
    # in case there's no unique solution.
    if(upmat[i][i]==0):
        print("no unique solution")
        quit()
print("Upper Triangular Matrix is: \n",np.round_(upmat,6),"\nLower Triangular Matrix is: \n",np.round_(lowmat,6))
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



