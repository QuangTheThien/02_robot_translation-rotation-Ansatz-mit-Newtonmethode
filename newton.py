from typing import Callable
import numpy as np
import numpy.linalg as la

def newton(start:np.ndarray, f:Callable[[np.ndarray], np.ndarray], min=1e-4, maxIterations=1000):
    x = start.copy()
    for iteration in range(maxIterations):
        J = jacobi(x,f)
        delta_x = la.solve(J, -f(x))
        x = x + delta_x
        if np.linalg.norm(delta_x) < min:
            print(f"Converged in {iteration + 1} iterations.")
            return x
    print("Did not converge.")
    return x

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
        J[:,j] = (f(x2) - f(x1))/(2*eps)
    return J

    
# array1 = np.array([[1, 2],[3, 4]])
# array2 = np.array([5,6])
# jacobi(array1,array2)
# test = jacobi.J
# print(test)