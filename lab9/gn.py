import math
import numpy as np
import matplotlib.pyplot as plt


def inverse(a):
	## this code is from the assignment for finding the inverse of a square matrix
	dim = np.shape(a)
	if (dim[0]!=dim[1]):
		quit()
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
	return inv

def gaussnewton(Z,D):
	Zt = np.transpose(Z)
	temp1=Zt@Z
	temp2=Zt@D
	A=inverse(temp1)@temp2
	return A

def func(A,x):
	f = A[0]*(1-np.exp(-A[1]*x))
	return f

def error(A,Z):
	n=np.shape(Z)[0]
	temp = 0
	for i in range (n):
		temp +=  (func(A,Z[i,0])-Z[i,1])**2
	return temp

def Zmat(A,X):
	n=np.shape(X)
	temp = np.zeros(n)
	for i in range(n[0]):
		temp[i,0]=1-np.exp(-A[1]*X[i,0])
		temp[i,1]=A[0]*np.exp(-A[1]*X[i,0])*X[i,0]
	return temp

def Dmat(A,Z):
	n=np.shape(Z)[0]
	temp = np.zeros(n)
	for i in range (n):
		temp[i] =  -(func(A,Z[i,0])-Z[i,1])
	return temp

#main
A=np.array([1.0,1.0])
X=np.matrix([[0.25,0.28],[0.75,0.57],[1.25,0.68],[1.75,0.74],[2.25,0.79]])
Z=Zmat(A,X)
D=Dmat(A,X)
er = error(A,X)
i=0
erprev = er
while True:
	erprev=er
	print(i,er,A)
	A += gaussnewton(Z,D)
	i += 1
	Z=Zmat(A,X)
	D=Dmat(A,X)
	er = error(A,X)
	if abs(erprev-er)<1e-20:
		print(i,er,A)
		break
	
Xfin=np.zeros(np.shape(X)[0])
Yfin=np.zeros(np.shape(X)[0])
for i in range(np.shape(X)[0]):
	Xfin[i]=X[i,0]
	Yfin[i]=func(A,Xfin[i])
	plt.scatter(X[i,0],X[i,1],marker = 'x')

plt.plot(Xfin,Yfin,color='green')
print(Xfin,Yfin,sep='\n')
plt.savefig('gaussnewton.png')
