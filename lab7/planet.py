import numpy as np
import matplotlib.pyplot as plt
import math
import sys
from numpy import exp
from math import sqrt
from matplotlib.pyplot import plot
k = 6.643 * (10**(-11))
M = 5.972 * (10**24)

	#file = open(sys.argv[1])

	#ma = -kmM/(r^3) 
	#dr = dx + dy
	#take k,m,M,v0,H as input
	#take position as an array
	#RK4 - dx=dy=0.01
	#dr/dt = dx/dt, dy/dt 


def d2rdt(r):
	assert r.size==2
	a = np.zeros(2)
	d = sqrt((r[0]**2) + (r[1]**2))
	a = (-1) * k * M * r / (d**3)
	return a


def RK4sat(rin,vin,dt):
	"""Takes r(t0),v(t0),dt as inputs
	Gives r(t1),v(t1) as outputs"""
	assert rin.size==2 and vin.size==2
	r1 = rin + vin*dt/2
	v1 = vin + d2rdt(r1)*dt/2
	r2 = rin + v1*dt/2
	v2 = d2rdt(r2)*dt/2
	r3 = v2*dt
	v3 = d2rdt(r3)*dt
	rfi = rin + dt*(vin+ 2*v1 + 2*v2 +v3)/6
	vfi = vin + dt*(d2rdt(rin) + 2*d2rdt(r1) + 2*d2rdt(r2) + d2rdt(r3))/6
	return rfi, vfi

#main
r0 = np.array([0,107.48*(10**9)])
v0 = np.array([35.5*(10**3),0])
rnext = r0
vnext = v0
dt = 0.1
fig = plt.figure()
for i in range(100):
	r=rnext
	v=vnext
	rnext, vnext = RK4sat(r,v,dt)
	print(rnext,vnext)
	matplotlib.path(x=r[0],y=r[1])

plt.show()