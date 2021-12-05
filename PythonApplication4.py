import math
import random
import numpy as np
a = np.matrix([[1,2,3],[1,3,4],[2,-1,-1]])
b = np.matrix([[5],[6],[1]])

def gauss(a,b):
    n = len(b)
    
    for k in range(1,n):
        for i in range(k+1,n):
            if a[i,k] !=0.0:
                a[i,k:n]=a[i,k:n]-a[i,k]/a[k,k]*a[k,k:n]
                b[i]=b[i]-a[i,k]/a[k,k]*b[k]
    
    for k in range(n-1,-1,-1):
        b[k]=(b[k]- np.dot(a[k,k:n],b[k:n]))/a[k,k]
    
    print("Check", np.linalg.solve(a,b))
    print("Method of Jordan Gauss", np.linalg.inv(a)*b)
    return b
    
print(gauss(np.matrix([[1,2,3],[1,3,4],[2,-1,-1]]),np.matrix([[5],[6],[1]])))
