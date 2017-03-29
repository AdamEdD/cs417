"""General
- Be able to construct an nxn matrix from a recursive formula
- Be able to fill a matrix row from a colon separated line of numbers
- Be able to manipulate a solution x i.e given an n-dimensional solution x return the sum of its components
- Be able to print out intermediate calculations if asked
"""

import math as mt
import numpy as np
import scipy as sp

def create_matrix(matrix):
    """create_matrix('1 2; 3 4')
    method to create a matrix from colon sep
    line of numbers
    """
    return np.matrix(matrix)

def matrix_sum(matrixA, matrixB):
    """matrix_sum(create_matrix('1 2; 3 4'),create_matrix('2 2; 3 4'))
    given an n-dimensional solution x return the sum of its components
    """
    return np.add(matrixA, matrixB)

def matrix_multi(matrixA, matrixB):
    """matrix multiplication
    """
    return matrixA*matrixB

