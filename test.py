import numpy as np
a = np.loadtxt(r'mat1.txt')
b = np.loadtxt(r'mat2.txt')

prod = np.matmul(a,b)
print(prod)
