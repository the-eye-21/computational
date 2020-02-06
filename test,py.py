import numpy as np
A=[[1,2,3],[1,2,3]]
b=[[1,2],[1,2],[1,2]]
c=np.matmul(A,b)
print(c)
if(c.all()!=1):
    print('yayyy')