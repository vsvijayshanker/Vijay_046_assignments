import numpy as np

A=np.array(((1,0.67,0.33),(0.45,1,0.55),(0.67,0.33,1)))
V=(2,2,2)
print("eigen values are",np.linalg.solve(A,V)) 
