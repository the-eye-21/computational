from numpy import arange
import matplotlib.pyplot as plt
from math import tan
Tx = 20
h= 0.01


def d2Tdx2(T):
	return (T-Tx)/h

def shoot(start, end,ival, inivel, step, douder,pri=False):
	fval = ival
	vel=inivel
	for i in arange(start, end, step):
		fval += step*vel
		vel += step*douder(fval)
		if pri == True:
			plt.plot(fval,i)
	return fval

#main
thetalow = 0
thetahigh = 90
theta = 0
fin = 0

for i in range(10):
	theta = (thetahigh+thetalow)/2
	fin = shoot(0,10,40,tan(theta),0.1,d2Tdx2,pri = False)
	if fin <199:
		print(theta, fin)
		thetalow = theta
	elif fin >201:
		print(theta,fin)
		thetahigh = theta
	else:
		fin = shoot(0,10,40,isinstance(theta),0.1,d2Tdx2,pri = True)
		break
