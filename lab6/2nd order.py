import numpy as np
import matplotlib.pyplot as plt
import math 
import sys
from numpy import exp
from numpy import cos
# solves 2nd order Differential equation of the form A(x)D2x +B(x)Dx + C(x)=D(t)
# input file contains A,B,C&D separated by commas in the first line,
# initial values of x,x'and t in the second line
# range of t in third line
# actual solution in fourth line


file = open(sys.argv[1])
filein = file.readlines()
expre = np.asarray(filein[0].split(','))
A = lambda x: eval(expre[0])
B = lambda x: eval(expre[1])
C = lambda x: eval(expre[2])
D = lambda t: eval(expre[3])
xin, vin, tin = np.asarray(filein[1].split(','))
tlow, thigh = np.asarray(filein[2].split(','))
g = lambda t: eval(filein[3])

xin=float(xin)
vin=float(vin)
tlow=float(tlow)
thigh=float(thigh)
step = 0.5
numstep = (int)((thigh-tlow)//step)
initstep = 0
xdiff = np.zeros(numstep+1)
xact=np.zeros(numstep+1)
vdiff = np.zeros(numstep+1)
fig=plt.figure()


xdiff[0]=xin
xact[0]=xin
vdiff[0]=vin
t=float(tin)

#f is to calculate dv/dt at a certain x,v,t
def f(x,v,t):
	temp = (D(t)-C(x)-(B(x)*v))/A(x)
	return temp

if (sys.argv[2]=='euler'):
	for i in range(numstep):
		vdiff[i+1]=vdiff[i]+(step*f(xdiff[i],vdiff[i],t))
		xdiff[i+1]=xdiff[i]+(step*vdiff[i])
		t=t+step
		xact[i+1]=g(t)
		plt.scatter(t,xdiff[i+1],c='red')
		plt.scatter(t,xact[i+1],c='blue')
	
		
	plt.savefig('2euler.png')
	plt.show()
	quit()

if (sys.argv[2]=='mid'):
	for i in range(numstep):
		vdiff[i+1]=vdiff[i]+(0.25*step*f(xdiff[i],vdiff[i],t))
		xdiff[i+1]=xdiff[i]+(0.25*step*vdiff[i])
		tempv=(f(xdiff[i+1],vdiff[i+1],t+(0.25*step)))
		vdiff[i+1]=vdiff[i]+(0.5*tempv*step)
		xdiff[i+1]=xdiff[i]+(0.5*step*vdiff[i])
		tempv2=f(xdiff[i+1],vdiff[i+1],t+(0.5*step))
		xdiff[i+1]=xdiff[i]+(step*vdiff[i+1])
		vdiff[i+1]=vdiff[i]+(step*tempv2)
		t=t+step
		xact[i+1]=g(t)
		plt.scatter(t,xdiff[i+1],c='red')
		plt.scatter(t,xact[i+1],c='blue')
	plt.savefig('2mid.png')
	plt.show()
	quit()

if (sys.argv[2]=='heun'):
	for i in range(numstep):
		vdiff[i+1]=vdiff[i]+(step*f(xdiff[i],vdiff[i],t))
		xdiff[i+1]=xdiff[i]+(step*vdiff[i])
		temp=f(xdiff[i+1],vdiff[i+1],t+step)
		vdiff[i+1]=vdiff[i]+(0.5*step*(temp+f(xdiff[i],vdiff[i],t)))
		xdiff[i+1]=xdiff[i]+(0.5*step*(vdiff[i]+vdiff[i+1]))
		t=t+step
		xact[i+1]=g(t)
		plt.scatter(t,xdiff[i+1],c='red')
		plt.scatter(t,xact[i+1],c='blue')
	plt.savefig('2heun.png')
	plt.show()
	quit()