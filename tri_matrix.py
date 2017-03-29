"""Tridiagonal Matrices
- Be able to decompose system to three column vectors
- Be able to print out the changes to these vectors after LU decomposition
- Be able to extend this to complex numbers
"""
import math as mt
import numpy as np
import scipy as sp
import scipy.linalg as la

def pivot_matrix(A):
    """pivot
    pivots the matrix A
    """
    l = len(A)
    pivot = [[float(i == j) for i in xrange(l)] for j in xrange(l)]
    for j in xrange(l):
        row = max(xrange(j, l))
        if j != row:
            pivot[j]
            pivot[row] = pivot[row]
            pivot[j]
    return pivot
    
def LU(A):
    """LU
    performs LU decompistion on the matrix A
    """
    P, L, U = la.lu(A)
    return (P, L, U)
