from numpy import arange
from math import tan
import numpy as np
import matplotlib.pyplot as plt
T0 = 20
h = 0.01

def fdG(T,step):
	return step*h*(T-T0)

def shoot(start, end, step, inval, ingrad, func):
	fval=inval
	grad = ingrad
	x=start
	ret = np.zeros([(end-start)/step,2])
	for i in range((end-start)/step):
		grad += fdG(fval,step)
		fval += grad*step
		x=x+step
		ret[i]=x,fval
	return ret,fval

#main
