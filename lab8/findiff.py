import numpy as np
import matplotlib.pyplot as plt

dx =1
h = 0.01
T0 = 20

def diff(start,end,ini,fin,step):
    """returns both matrices to solve equation"""
    n=int((end-start)/step)-1
    A=np.zeros([n,n])
    B=np.zeros(n)    
    A[0][0]= 2+(step*step*h)
    A[0][1]=-1
    B[0]=ini+(h*step*step*T0)
    for i in range(1,n-1):
        A[i][i] = 2 +(step*step*h)
        A[i][i-1]=-1
        A[i][i+1]=-1
        B[i] = h*step*step*T0
    A[n-1][n-1] = 2+(step*step*h)
    A[n-1][n-2] = -1
    B[n-1]=fin+(step*step*h*T0)
    return A,B

def Thomas(A,B):
    """solves Ax=B and returns x for tridiagonal systems"""
    n=np.size(B)
    x=[None]*n
    for i in range(1,n):
        A[i][i-1]=A[i][i-1]/A[i-1][i-1]
        A[i][i] -= A[i][i-1]*A[i-1][i]
    for i in range(n):
        B[i] -= A[i][i-1]*B[i-1]
    x[n-1]=B[n-1]/A[n-1][n-1]
    for i in range(n-2,-1,-1):
        x[i]=(B[i]-(A[i][i+1]*x[i+1]))/A[i][i]
    return x

#main
A,B=diff(0,10,40,200,dx)
b=Thomas(A,B)
b.insert(0,40)
b.append(200)
plt.plot(np.arange(0,10+dx,dx),b,color='black',marker='^')
plt.xlabel('x-coordinate')
plt.ylabel('Temperature')
print(b)
plt.savefig('findiff.png') 