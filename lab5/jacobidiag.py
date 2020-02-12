import numpy as np
import sys
from math import sqrt
import numpy.linalg
#maximum of symmetric matrix exculding diagonal elements with index
def maxval(A):
	n = len(A)
	
	max_n = 0.0
	k, l = 0, 0
	
	for i in range(n - 1):
		for j in range(i + 1, n):
			if max_n <= abs(A[i][j]):
				max_n = abs(A[i][j])
				k = i
				l = j
	
	return max_n, k, l


#givens rotation, input parameters are matrix and indices of element to be made zero
def givrot(A,j,k):
    n=len(A)
    if abs(A[j][k])<1e-10:
        t=A[j][k]/abs(A[k][k]-A[j][j])
    else:
        the=(A[k][k]-A[j][j])/(2*A[j][k])
        t=np.sign(the)/(np.abs(the)+sqrt((the**2)+1))
    c=1/(sqrt((t**2)+1))
    s=c*t
    tau=s/(1+c)
    temp=A[j][k]
    A[j][k]=0
    A[k][j]=0
    A[j][j] -= t*temp
    A[k][k] += t*temp
    for i in range(j):
        temp = A[i][j]
        A[i][j] = temp - s*(A[i][k] + tau*temp)
        A[j][i]=A[i][j]
        A[i][k] = A[i][k] + s*(temp - tau*A[i][k])
        A[k][i]=A[i][k]
    for i in range(k+1,l):  # Case of k < i < l
        temp = A[j][i]
        A[j][i] = temp - s*(A[i][k] + tau*A[j][i])
        A[i][j]=A[j][i]
        A[i][k] = A[i][k] + s*(temp - tau*A[i][k])
        A[k][i]=A[i][k]
    for i in range(l+1,n):  # Case of i > l
        temp = A[j][i]
        A[j][i] = temp - s*(A[k][i] + tau*temp)
        A[i][j]=A[j][i]
        A[k][i] = A[k][i] + s*(temp - tau*A[k][i])
        A[i][k]=A[k][i]

    return A
np.set_printoptions(precision=4)
A=np.loadtxt(sys.argv[1])
n=len(A)
print(numpy.linalg.eig(A))
for i in range (100000):
    aMax,k,l=maxval(A)
    if aMax<1e-50:
        print(np.round(A,8),i,'done')
        quit()
    givrot(A,k,l)
print(b)