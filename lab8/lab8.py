import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

h = 0.01
slopes = np.zeros((4, 2))
t_final = 200
def F(t, x):
	A = h*(t-20)
	return A

def RK_4(t, z, x):
	a=t
	b=z
	slopes[0,0] = z
	slopes[0,1] = F(t, x)
	t = a + slopes[0,0]
	z = b + slopes[0,1]
	x = x + 1
	slopes[1,0] = z
	slopes[1,1] = F(t, x)
	t = a + slopes[1,0]
	z = b + slopes[1,1]
	slopes[2,0] = z
	slopes[2,1] = F(t, x)
	t = a + slopes[2,0]
	z = b + slopes[2,1]
	x = x + 1
	slopes[3,0] = z
	slopes[3,1] = F(t, x)
	t = a + ((slopes[0,0] + 2*(slopes[1,0] + slopes[2,0]) + slopes[3,0])/6)*2
	z = b + ((slopes[0,1] + 2*(slopes[1,1] + slopes[2,1]) + slopes[3,1])/6)*2

	return t, x

fig = plt.figure()

t1 = 40
x1 = 0
z1 = 10
t1_points = []
x1_points = []

for i in range(5):
	t1, x1 = RK_4(t1, z1, x1)
	t1_points.append(t1)
	x1_points.append(x1)
print(t1_points)
plt.plot(x1_points, t1_points, color = 'red', label = 'first shoot')
t2 = 40
x2 = 0
z2 = 20
t2_points = []
x2_points = []

for i in range(5):
	t2, x2 = RK_4(t2, z2, x2)
	t2_points.append(t2)
	x2_points.append(x2)
print(t2_points)
plt.plot(x2_points, t2_points, color = 'green', label = 'second shoot')
t_actual = 40
x_actual = 0
z_actual = (z2 - z1) + ((z2-z1)/(t2_points[4] - t1_points[4]))*(t_final-t1_points[4])
tactual_points = []
xactual_points = []

for i in range(5):
	t_actual, x_actual = RK_4(t_actual, z_actual, x_actual)
	tactual_points.append(t_actual)
	xactual_points.append(x_actual)
print(tactual_points)
plt.plot(xactual_points, tactual_points, color = 'blue', label = 'actual')
plt.legend()
plt.title('Plot of temperature v/s distance from shooting method')
plt.xlabel('Distance from left end(m)')
plt.ylabel('Temperature')
plt.show()