#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from wsgiref.util import request_uri

import numpy as np
import random as rnd

# maybe you need to install matplotlib
# pip install matplotlib
import matplotlib.pyplot as plt
from numpy.ma.core import shape


def check_order(a: int, b: int):
    if a > b:
        tmp = a
        a = b
        b = tmp
    return a, b

def random_array(a: int, b: int, n: int):
    """
    The function randint from module random to create an 1d-array of integers of size n.
    The values of the array should be randomly sampled between a and b (including both a and b).

    Parameters
    ----------
    a: int
        DESCRIPTION.
    b: int
        DESCRIPTION.
    n: int
        DESCRIPTION.

    Returns
    -------
    random_array: int
        DESCRIPTION.

    """
    a, b = check_order(a, b)
    arr = np.zeros(n, dtype=np.int32)
    for i in range(0,n):
        arr[i] = rnd.randint(a, b)
    return arr



def element_mult(x: np.ndarray, y: np.ndarray):
    if len(x) != len(y):
        return None
    z = np.zeros(len(x), dtype=x.dtype)
    for i in range(0, len(x)):
        z[i] = x[i] * y[i]
    return z


def find_max(x: np.ndarray):
    highest = 0
    for ele in x:
        if ele < 0:
            return None
        if ele >= highest:
            highest = ele
    idx = np.where(x == highest)[0][-1]
    return idx


    
def transpose(x: np.ndarray):
    shape = x.shape
    z = np.zeros([shape[1], shape[0]], dtype=x.dtype)
    for i in range(0, len(x)):
        for j in range(0, len(x[i])):
            z[j][i] = x[i][j]
    return z


def is_square(x: np.ndarray):
    x_shape = x.shape
    if x_shape[0] == 1 and len(x) == 1:
        return True
    elif len(x_shape) == 2 and x_shape[0] == x_shape[1]:
        return True
    return False

def check_col(magic_number, arr):
    for i in range(0, len(arr)):
        if magic_number != sum(arr[i]):
            return False
    return True

def check_row(magic_number, arr):
    for i in range(0, len(arr)):
        temp_sum = 0
        for j in range(0, len(arr)):
            temp_sum += arr[j][i]
        if magic_number != temp_sum:
            return False
    return True

def check_diagonal(magic_number, arr):
    temp_sum = 0
    for j in range(0, len(arr)):
        temp_sum += arr[0 + j][0 + j]
    if magic_number != temp_sum:
        return False
    temp_sum = 0
    for j in range(0, len(arr)):
        temp_sum += arr[0 + j][len(arr) -1 - j]
    if magic_number != temp_sum:
        return False
    return True

def is_magic(x: np.ndarray):
    x_shape = x.shape
    if len(x_shape) == 2 and x_shape[0] == x_shape[1]:
        magic_number = sum(x[0])
        if not check_col(magic_number, x) or not check_row(magic_number, x) or not check_diagonal(magic_number, x):
            return False
        return True
    return None
    
    
def main():
    """
    Main function
    """
    x = np.arange(10)
    
    try:
        # if your functions are working properly, you can implement changes in 
        # main() here
        
        y = random_array(0, 100, 10)
        imax = find_max(y)
        plt.plot(x, y, 'ko-')
        plt.plot(x[imax], y[imax], 'ro')
    except:
        
        # if your functions are not working properly, you can implement changes
        # in main() here:
            
        y = np.arange(100).reshape((4,25)).T.flatten()[0:10]
        imax = 7
        plt.plot(x, y, 'ko-')
        plt.plot(x[imax], y[imax], 'ro')
            
    
    # Example of magic matrix
    x = np.array([[2,7,6],[9,5,1],[4,3,8]])        
    print(x)
    
    return None
    

# The main body of your program should only call the main() function like this:
if __name__=="__main__":    
    main()
    
    
