import numpy as np
import math
import sys
import matplotlib.pyplot as plt
from numpy import exp
#defining e
#reading input and making it a function.
file = open(sys.argv[1])
filein = file.readlines()
f = lambda x,y: eval(filein[0])
xin, yin = np.asarray(filein[1].split(','))
xlow, xhigh = np.asarray(filein[2].split(','))
g = lambda x: eval(filein[3])

xin=float(xin)
yin=float(yin)
xlow=float(xlow)
xhigh=float(xhigh)
step = 0.25
numstep = (int)((xhigh-xlow)//step)
initstep = 0
ydiff = np.zeros(numstep+1)
yact=np.zeros(numstep+1)

fig=plt.figure()


ydiff[0]=yin
yact[0]=yin
x=xin



if (sys.argv[2]=='mid'):
	for i in range(numstep):
		temp=ydiff[i]+(0.5*step*f(x,ydiff[i]))
		ydiff[i+1]=ydiff[i]+(step*f(x+(0.5*step),temp))
		x=x+step
		yact[i+1]=g(x)
		plt.scatter(x,ydiff[i+1],c='red')
		plt.scatter(x,yact[i+1],c='blue')
	plt.savefig('1mid.png')
	plt.show()

	quit()


elif(sys.argv[2]=='euler'):
	for i in range(numstep):
		ydiff[i+1]=ydiff[i]+(step*f(x,ydiff[i]))
		x=x+step
		yact[i+1]=g(x)
		plt.scatter(x,ydiff[i+1],c='red')
		plt.scatter(x,yact[i+1],c='blue')
	plt.savefig('1euler.png')
	plt.show()
	quit()


elif(sys.argv[2]=='heun'):
	for i in range(numstep):
		ydiff[i+1]=ydiff[i]+(step*f(x,ydiff[i]))
		temp1=f(x,ydiff[i])
		temp2=f(x,ydiff[i+1])
		ydiff[i+1]=ydiff[i]+(0.5*step*(temp1+temp2))
		x=x+step
		yact[i+1]=g(x)
		plt.scatter(x,ydiff[i+1],c='red')
		plt.scatter(x,yact[i+1],c='blue')
	plt.savefig('1heun.png')
	plt.show()
	quit()
