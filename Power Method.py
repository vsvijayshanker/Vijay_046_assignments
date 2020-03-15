import numpy as np

A=np.array(((2,-1,0),(-1,2,-1),(0,-1,2)))   #matrix
print("Matrix is",'\n',A,'\n',)

g= np.array((1,0,0))         #guess vector
print('guess vector is','\n',g,'\n')


def EV(A, g):                 #definig the formula
    Av = np.dot(A,g)
    return g.dot(Av)

def power_iteration(A):
    k=0
    v=g
    ev = EV(A,v)
    while True:              #calculating the values 
        Av = np.dot(A,v)     #multiplication of matrix with vector
        v = Av / np.linalg.norm(Av)
        ev_n = EV(A,v)       #new eigen value
        k=k+1                #number of steps in calculation
        
        if np.abs((ev_n-ev)/ev) < 1e-5: #tollerence value
            break
        ev = ev_n           #if loop doent break then new eigen value is set to ev(old)

    print('total no. of steps',k,'\n')
    return ev_n, v,



E,V=power_iteration(A)
print('dominent eigen value is', E,'\n')
print('dominent eigen vector is','\n',V,'\n')
print('actual eigen values and eigen vecters are','\n',np.linalg.eigh(A))
