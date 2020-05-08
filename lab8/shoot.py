import math
import numpy as np
import matplotlib.pyplot as plt

T0 = 20
h = 0.01
dx = 1

def douder(x,T,z):
	return h*(T-T0)

def heun(x,T,Z,func,step):
	"""returns T and Z at next x"""
	temp1 = douder(x,T,Z)
	temp2 = douder(x+step,T+(Z*step),Z+(temp1*step))
	Zi=Z+(temp1+temp2)/2
	Ti=T+(Z+Zi)/2
	return Ti,Zi

#I have used Heun's method to get to the next stpe for each Ti, but any other method can be used.
def shoot(func,start,end,step,Tin,Zin):
	n=int((end-start)/step)
	T=[None]*(n+1)
	Z=[None]*(n+1)
	T[0]=Tin
	Z[0]=Zin
	x=start
	for i in range(1,n+1):
		T[i],Z[i]=heun(x,T[i-1],Z[i-1],func,step)
		x += step
	return T

#main
x=np.arange(0,10+dx,dx)
t10=shoot(douder,0,10,dx,40,10)
plt.plot(x,t10,label='first shoot',color='b',marker='x')
t20=shoot(douder,0,10,dx,40,20)
plt.plot(x,t20,label ='second shoot',color='r',marker = '<')
a=t10[-1]
b=t20[-1]
Z=10*(200-(a-(b-a)))/(b-a)
fin = shoot(douder,0,10,dx,40,Z)
print(Z)
plt.plot(x,fin,label = 'final shoot',color = 'g',marker = 'o')
plt.legend(loc="upper left")
plt.xlabel('x-coordinate')
plt.ylabel('Temperature')
plt.savefig('shoot.png')