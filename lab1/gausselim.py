import numpy as np
a = np.loadtxt(r'E:\code\lab1\gauss.txt')
dim = np.shape(a)
print(a)
#scaling.
for i in range (dim[0]):
    a[i] = a[i] = a[i]/abs(np.min(a[i][np.nonzero(a[i])]))

print(a)
#gauss elimination with partial pivoting.
for i in range(dim[0]):
    # i selects pivot element.
    # to check if pivot element is zero
    if (a[i][i] == 0):
        # to swap rows in case pivot element is zero.
        for k in range(i+1,dim[0]):
            if (a[k][i]!=0):               
                a[[i,k]]=a[[k,i]]
                break
    # after making sure that either pivot element is zero or there are no non-zero elements in that column
    # is also the code for Gauss elimination without pivoting
    if(a[i][i]!=0):
        for j in range(i+1, dim[0]):
            a[j] = a[j] - ((a[j][i]/a[i][i])*a[i])
    # in case there's no unique solution.
    if(a[i][i]==0):
        print("no unique solution")
        quit(save="ask")

print("The matrix after Gauss Elimination is \n",a)
#backsubstitution.
x=np.zeros(dim[0])
for i in range(dim[0]):
    x[i] = a[i][dim[0]]
for i in range(dim[0]-1,-1,-1):
    for j in range(i+1,dim[0]):
        x[i] = x[i]-(x[j]*a[i][j])
    x[i]=x[i]/a[i][i]

print ("The solution vector is", x)