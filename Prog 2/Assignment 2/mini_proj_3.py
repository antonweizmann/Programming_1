#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np
import random as rnd

# maybe you need to install matplotlib
# pip install matplotlib
import matplotlib.pyplot as plt 


def random_array(a: int, b: int, n: int):
    """
    DESCRIPTION

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
    
    return None



def element_mult(x: np.ndarray, y: np.ndarray):

    
    return None


def find_max(x: np.ndarray):
    
    return None


    
def transpose(x: np.ndarray):
    
    return None


def is_square(x: np.ndarray):
    
    return None

    
def is_magic(x: np.ndarray):

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
    
    
