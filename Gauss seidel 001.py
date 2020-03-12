import numpy as np

#Matrix
A=np.array(((0.2,0.1,1,1,0),(0.1,4,-1,1,-1),(1,-1,60,0,-2),(1,1,0,8,4),(0,-1,-2,4,700)))

#Vector
V=np.array((1,2,3,4,5))


print('matrix A is ',A)
print('vector V is ',V)

#starting of Jacobi

X0=np.zeros(5) #initial guess value
X=np.zeros(5) #initial stored result value

T=0.01      #tollence value
k=0         #no of iterations

#starting the loop for Jacobi
while True:     
    for i in range(5):
        S=0
        for j in range(5):
            if i==j:
                continue
            S=S+A[i,j]*X0[j]    #in jacobi we are using X0[j] while in gauss-seidel we will use X[j] in calculation
        X[i]=(V[i]-S)/A[i,i]
    k=k+1
    if(np.sqrt(np.dot(X-X0,X-X0))<T):
        break
    X0=X.copy()

print('solution for jacobi')
print('Solution is',X)
print('No. of iterations ',k)

#End of Jacobi





#Starting of Gauss-Seidel

X0=np.zeros(5) #initial guess value
X=np.zeros(5) #initial stored result value

T=0.01      #tollence value
k=0         #no of iterations

#starting the loop for Gauss-Seidel
while True:     
    for i in range(5):
        S=0
        for j in range(5):
            if i==j:
                continue
            S=S+A[i,j]*X[j]     #in gauss-seidel we are using X[j] while in jacobi have used X0[j] in calculation
        X[i]=(V[i]-S)/A[i,i]
    k=k+1
    if(np.sqrt(np.dot(X-X0,X-X0))<T):
        break
    X0=X.copy()


print('solution for gauss-seidel')
print('Solution is',X)
print('No. of iterations ',k)

#End of Gauss-Seidel







