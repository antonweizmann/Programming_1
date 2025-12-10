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
    """
    Ensure that a <= b by swapping the values if necessary.

    Parameters
    ----------
    a : int
        First integer.
    b : int
        Second integer.

    Returns
    -------
    a : int
        The smaller integer.
    b : int
        The larger integer.
    """
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
    a : int
        Lower bound of the random interval (inclusive).
    b : int
        Upper bound of the random interval (inclusive).
    n : int
        Size of the array to be generated.

    Returns
    -------
    random_array : np.ndarray
        A 1-dimensional NumPy array of length `n` containing random integers
        sampled uniformly between `a` and `b`.
    """
    a, b = check_order(a, b)
    arr = np.zeros(n, dtype=np.int32)
    for i in range(0, n):
        arr[i] = rnd.randint(a, b)
    return arr


def element_mult(x: np.ndarray, y: np.ndarray):
    """
    Element-wise multiplication of two 1-dimensional arrays.

    Parameters
    ----------
    x : np.ndarray
        First input array.
    y : np.ndarray
        Second input array. Must have the same length as `x`.

    Returns
    -------
    z : np.ndarray or None
        A new array containing the element-wise product of `x` and `y`.
        Returns None if the input arrays do not have the same length.
    """
    if len(x) != len(y):
        return None
    z = np.zeros(len(x), dtype=x.dtype)
    for i in range(0, len(x)):
        z[i] = x[i] * y[i]
    return z


def find_max(x: np.ndarray):
    """
    Find the index of the largest non-negative value in an array.
    If multiple entries share the maximum value, the last such index is returned.

    Parameters
    ----------
    x : np.ndarray
        Input array of non-negative integers.

    Returns
    -------
    idx : int or None
        Index of the largest value. Returns None if any value in `x` is negative.
    """
    highest = 0
    for ele in x:
        if ele < 0:
            return None
        if ele >= highest:
            highest = ele
    idx = np.where(x == highest)[0][-1]
    return idx


def transpose(x: np.ndarray):
    """
    Compute the transpose of a 2-dimensional array without using NumPy's built-in transpose.

    Parameters
    ----------
    x : np.ndarray
        2D input array.

    Returns
    -------
    z : np.ndarray
        A new array representing the transpose of `x`.
    """
    shape = x.shape
    z = np.zeros([shape[1], shape[0]], dtype=x.dtype)
    for i in range(0, shape[0]):
        for j in range(0, shape[1]):
            z[j][i] = x[i][j]
    return z


def is_square(x: np.ndarray):
    """
    Check whether an array represents a square matrix.

    Parameters
    ----------
    x : np.ndarray
        Input array.

    Returns
    -------
    flag : bool
        True if `x` is a square matrix, False otherwise.
    """
    if x.ndim == 1:
        return x.size == 1
    return len(set(x.shape)) == 1


def check_col(magic_number, arr):
    """
    Verify that all columns in a matrix sum to a given magic number.

    Parameters
    ----------
    magic_number : int
        Target column sum.
    arr : np.ndarray
        Square matrix to be checked.

    Returns
    -------
    flag : bool
        True if all columns sum to `magic_number`, False otherwise.
    """
    for i in range(0, len(arr)):
        if magic_number != my_sum(arr[i]):
            return False
    return True


def my_sum(arr):
    """
    Calculate the sum of all elements in a 1D array or list.

    Parameters
    ----------
    arr : np.ndarray or list
        Array or list to sum.

    Returns
    -------
    total : int or float
        Sum of all elements in the array.
    """
    total = 0
    for element in arr:
        total += element
    return total

def check_row(magic_number, arr):
    """
    Verify that all rows in a matrix sum to a given magic number.

    Parameters
    ----------
    magic_number : int
        Target row sum.
    arr : np.ndarray
        Square matrix to be checked.

    Returns
    -------
    flag : bool
        True if all rows sum to `magic_number`, False otherwise.
    """
    for i in range(0, len(arr)):
        temp_sum = 0
        for j in range(0, len(arr)):
            temp_sum += arr[j][i]
        if magic_number != temp_sum:
            return False
    return True


def check_diagonal(magic_number, arr):
    """
    Verify that both diagonals in a matrix sum to a given magic number.

    Parameters
    ----------
    magic_number : int
        Target diagonal sum.
    arr : np.ndarray
        Square matrix to be checked.

    Returns
    -------
    flag : bool
        True if both diagonals sum to `magic_number`, False otherwise.
    """
    temp_sum = 0
    for j in range(0, len(arr)):
        temp_sum += arr[0 + j][0 + j]
    if magic_number != temp_sum:
        return False

    temp_sum = 0
    for j in range(0, len(arr)):
        temp_sum += arr[0 + j][len(arr) - 1 - j]
    if magic_number != temp_sum:
        return False

    return True


def is_magic(x: np.ndarray):
    """
    Check whether a square matrix is a magic square.
    A magic square has equal row sums, column sums, and diagonal sums.

    Parameters
    ----------
    x : np.ndarray
        2D square matrix.

    Returns
    -------
    flag : bool or None
        True if `x` is a magic square, False otherwise.
        Returns None if `x` is not a square matrix.
    """
    x_shape = x.shape
    if len(x_shape) == 2 and x_shape[0] == x_shape[1]:
        magic_number = my_sum(x[0])
        if not check_col(magic_number, x) or not check_row(magic_number, x) or not check_diagonal(magic_number, x):
            return False
        return True
    return None


def main():
    """
    Main function.

    Generates a random array, finds and plots its maximum value,
    and prints an example magic square.
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

        y = np.arange(100).reshape((4, 25)).T.flatten()[0:10]
        imax = 7
        plt.plot(x, y, 'ko-')
        plt.plot(x[imax], y[imax], 'ro')

    # Example of magic matrix
    x = np.array([[2, 7, 6], [9, 5, 1], [4, 3, 8]])
    print(x)

    return None


# The main body of your program should only call the main() function like this:
if __name__ == "__main__":
    main()
