import numpy as np
A=np.array([[5,-2],
            [-2,8]])
print('matrix is',A)
eign, vec=np.linalg.eigh(A)

while abs(A[0,1])>0.0001:
    Q,R=np.linalg.qr(A)
    A=R@Q

print('eigen values from QR decomposition are',A[0,0],A[1,1])
print('eigen values from numpy.linalg.eigh are',eign)
