import numpy as np
import math
import matplotlib.pyplot as plt
from math import sqrt
from math import pi
import matplotlib

#Global Constants
k = 6.6743 * (10**(-11))
M = 1.989 * (10**30)
step = 36000

#Taking position as an array and defining distance of a point from the origin
def dist(x):
	assert x.size == 2
	return sqrt((x[0]**2)+(x[1]**2))

#dv/dt = greq(r,v,t)
def greq(r,v,t):
	assert r.size == 2 and v.size == 2
	A = -k*M*r/(dist(r)**3)
	return A

#Defining RK4... Returns position and velocity at next time step
def RK4(r,v,t):
	assert r.size == 2 and v.size == 2
	r1 = v*step
	v1 = step*greq(r,v,t)
	r2 = step*(v+0.5*v1)
	v2 = step*greq(r+0.5*r1,v+0.5*v1,t+0.5*step)
	r3 = step*(v+0.5*v2)
	v3 = step*greq(r+0.5*r2,v+0.5*v2,t+0.5*step)
	r4 = step*(v+v3)
	v4 = step*greq(r+r3,v+v3,t+step)

	rf = r + (r1+2*r2 + 2*r3 + r4)/6
	vf = v + (v1 + 2*v2 + 2*v3 + v4)/6
	return rf, vf, t+step

#main

r= np.array([0,107.48*(10**9)])
v= np.array([39.5*(10**3),30000])
t=0
fig = plt.figure()
x=[]
y=[]
for i in range(0,1000000):
	r,v,t = RK4(r,v,t)
	x.append(r[0])
	y.append(r[1])
plt.plot(x,y)
plt.show()