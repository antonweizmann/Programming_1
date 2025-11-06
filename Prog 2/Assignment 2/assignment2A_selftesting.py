#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# import the file with your solutions
import mini_proj_3 as asgmt


#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np
import random as rnd

def test_element_mult_type():
    try:
        x = np.zeros((100,), dtype=int)
        y = np.zeros((100,), dtype=int)
        
        z = asgmt.element_mult(x, y)
    
        x2 = np.zeros((100,), dtype=float)
        y2 = np.zeros((100,), dtype=int)
        
        z2 = asgmt.element_mult(x2, y2)
        correct_answer = type(z)
        correct_answer2 = type(z2)
        
        if correct_answer == type(x) and correct_answer2 == type(x2):
            print("Passed test_element_mult_type")
        else:
            print("Failed test_element_mult_type")
            print("  Expected:")
            print("    ", correct_answer)
            print("    ", correct_answer2)
            print("  Received:")
            print("    ", type(x))
            print("    ", type(x2))
    except Exception as e:
        print("Something went wrong running test_element_mult_type:")
        print(f"  {type(e).__name__}: {e}")
        
def test_element_mult():
    try:
        x = np.arange(10)
        y = np.arange(10,20)
        
        z = asgmt.element_mult(x, y)
        correct_answer = x*y
        if all(z == correct_answer):
            print("Passed test_element_mult")
        else:
            print("Failed test_element_mult")
            print("  Expected:")
            print("    ", correct_answer)
            print("  Received:")
            print("    ", z)
    except Exception as e:
        print("Something went wrong running test_element_mult:")
        print(f"  {type(e).__name__}: {e}")
    
def test_transpose():
    try:
        x = np.arange(10).reshape((5,2))
        correct_answer = x.T
        z = asgmt.transpose(x)
        if all(z.flatten() == x.T.flatten()):
            print("Passed test_transpose")
        else:
            print("Failed test_transpose")
            print("  Expected:")
            print("    ", correct_answer)
            print("  Received:")
            print("    ", z)
    except Exception as e:
        print("Something went wrong running test_transpose:")
        print(f"  {type(e).__name__}: {e}")
    
def test_is_square_1D():
    try:
        a = np.zeros((1,))
        b = np.zeros((10,))
        if asgmt.is_square(a) == True and asgmt.is_square(b)==False:
            print("Passed test_is_square_1D")
        else:
            print("Failed test_is_square_1D")
            print("  Expected:")
            print("    ", True)
            print("    ", False)
            print("  Received:")
            print("    ", asgmt.is_square(a))
            print("    ", asgmt.is_square(b))
    except Exception as e:
        print("Something went wrong running test_is_square_1D:")
        print(f"  {type(e).__name__}: {e}")
    
def test_is_square_2D():
    try:
        a = np.zeros((2,2))
        b = np.zeros((10,2))
        if asgmt.is_square(a) == True and asgmt.is_square(b)==False:
            print("Passed test_is_square_2D")
        else:
            print("Failed test_is_square_2D")
            print("  Expected:")
            print("    ", True)
            print("    ", False)
            print("  Received:")
            print("    ", asgmt.is_square(a))
            print("    ", asgmt.is_square(b))
    except Exception as e:
        print("Something went wrong running test_is_square_2D:")
        print(f"  {type(e).__name__}: {e}")
    
def test_is_magic():
    try:
        x = np.array([[2, 7, 6], [9, 5, 1], [4, 3, 8]])        
        y = np.array([[1, 2, 2], [1, 2, 2], [2, 1, 2]])
        if asgmt.is_magic(x) and not asgmt.is_magic(y):
            print("Passed test_is_magic")
        else:
            print("Failed test_is_magic")
            print("  Expected:")
            print("    ", True)
            print("    ", False)
            print("  Received:")
            print("    ", asgmt.is_magic(x))
            print("    ", asgmt.is_magic(y))
    except Exception as e:
        print("Something went wrong running test_is_magic:")
        print(f"  {type(e).__name__}: {e}")
    return


def test_is_magic_not_2D():
    try:
        x = np.zeros((2,2,2))
        y = np.zeros((2,))
        if asgmt.is_magic(x) is None and asgmt.is_magic(y) is None:
            print("Passed test_is_magic_not_2D")
        else:
            print("Failed test_is_magic_not_2D")
            print("  Expected:")
            print("    ", None)
            print("    ", None)
            print("  Received:")
            print("    ", asgmt.is_magic(x))
            print("    ", asgmt.is_magic(y))
    except Exception as e:
        print("Something went wrong running test_is_magic_not_2D:")
        print(f"  {type(e).__name__}: {e}")
    return

def test_is_magic_not_square():
    try:
        x = np.zeros((2,4))
        if asgmt.is_magic(x) is None:
            print("Passed test_is_magic_not_square")
        else:
            print("Failed test_is_magic_not_square")
            print("  Expected:")
            print("    ", None)
            print("  Received:")
            print("    ", asgmt.is_magic(x))
    except Exception as e:
        print("Something went wrong running test_is_magic_not_square:")
        print(f"  {type(e).__name__}: {e}")
    return
    
def test_random_array():
    try:
        passed = True
        for i in range(100):   
            x = asgmt.random_array(5, 10, 20)
            if np.min(x)<5 or np.max(x)>10 or np.max(x.shape)!=20:
                passed = False
                break
        if passed:
            print("Passed test_random_array")
        else:
            print("Failed test_random_array")
            print("  Expected: array with 20 values between 5 and 10")
            print("  Received:")
            print("    ", x)
    except Exception as e:
        print("Something went wrong running test_random_array:")
        print(f"  {type(e).__name__}: {e}")
        
def test_random_array_limits():
    try:
        passed = True
        x = asgmt.random_array(10, 10, 20)
        try:
            if np.min(x)!=10 or np.max(x)!=10:
                passed = False
        except:
            passed = False
        if passed:
            print("Passed test_random_array_limits")
        else:
            print("Failed test_random_array_limits")
            print("  Expected: array with 20 times the value 10")
            print("  Received:")
            print("    ", x)
    except Exception as e:
        print("Something went wrong running test_random_array_limits:")
        print(f"  {type(e).__name__}: {e}")
    return

def test_find_max():
    try:
        x = np.array([1,2,3,4,5,6,7,8,10,9])
        imax = asgmt.find_max(x)
        correct_answer = 8
        if correct_answer == imax:
            print("Passed test_find_max")
        else:
            print("Failed test_find_max")
            print('  Considering the array:')
            print("    ", x)
            print("  Expected:")
            print("    ", correct_answer)
            print("  Received:")
            print("    ", imax)
    except Exception as e:
        print("Something went wrong running test_find_max:")
        print(f"  {type(e).__name__}: {e}")
    return None
    
def test_find_max_tie():
    try:
        x = np.array([1,2,3,11,5,11,8,10,9])
        imax = asgmt.find_max(x)
        correct_answer = 5
        if correct_answer == imax:
            print("Passed test_find_max_tie")
        else:
            print("Failed test_find_max_tie")
            print('  Considering the array:')
            print("    ", x)
            print("  Expected:")
            print("    ", correct_answer)
            print("  Received:")
            print("    ", imax)
    except Exception as e:
        print("Something went wrong running test_find_max_tie:")
        print(f"  {type(e).__name__}: {e}")
    
    return None


# Define different testing functions
def main():
    """
    Main function
    """
    
    
    print("Testing find_max() function")
    test_find_max()
    test_find_max_tie()
    print(".................................")
    
    print("Testing random_array() function")
    test_random_array()
    test_random_array_limits()
    print(".................................")
    
    
    
    print("Testing element_mult() function")
    test_element_mult()
    test_element_mult_type()    
    print(".................................")
    
    print("Testing transpose() function")
    test_transpose()
    print(".................................")
    
    print("Testing is_square() function")
    test_is_square_1D()
    test_is_square_2D()
    print(".................................")
    
    
    print("Testing is_magic() function")
    test_is_magic()
    test_is_magic_not_2D()
    test_is_magic_not_square()
    print(".................................")
    
if __name__=="__main__":    
    main()
#%%
