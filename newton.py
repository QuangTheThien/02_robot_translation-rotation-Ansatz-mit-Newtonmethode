from typing import Callable
import numpy as np
import numpy.linalg as la

def newton(start:np.ndarray, f:Callable[[np.ndarray], np.ndarray], min=1e-4, maxIterations=1000):
    JakobiMatrix = jacobi(start,f)
    Vektor = start
    i=1
    while i <= maxIterations:
        Vektor = Vektor -  np.multiply(f,JakobiMatrix)
        i+=1
    print(Vektor)
    return Vektor
    #     newtonmethode = 
    # return newtonmethode

def jacobi(x:np.ndarray, f:Callable[[np.ndarray], np.ndarray]) -> np.ndarray:
    rows = f(x).shape[0]
    cols = x.shape[0]
    eps = 1e-5
    J = np.zeros((rows, cols))
    for j in range(cols):
        x1 = x.copy()
        x2 = x.copy()
        x2[j] = x[j]+eps
        x1[j] = x[j]-eps
        J[:,[j]] = (f(x2) - f(x1))/(2*eps) #j selber in [] gesetzt
    return J

    
# array1 = np.array([[1, 2],[3, 4]])
# array2 = np.array([5,6])
# jacobi(array1,array2)
# test = jacobi.J
# print(test)