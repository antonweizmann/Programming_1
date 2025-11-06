import numpy as np
import matplotlib.pyplot as plt

def sum_even_rec(n : int) -> int: 
    """
        Implement the function sum_even_rec to take an integer n as a parameter and return the sum of all the even numbers from 0 to n. 
        Think of the following three question before starting the implementation : 
            - What is the base case?
            - What argument is passed to the recursive function call?
            - How does this argument become closer to the base case?
        Modify the base condition, the recursive condition and the returns of the program.
        Rewrite the docstring
    """
    base_condition = True
    recursive_condition = False
    # Base case(s)
    if base_condition : 
        return 
    # Recursive case(s)
    elif recursive_condition : 
        return 
    
def array_product_rec(numbers : np.ndarray[int]) -> int: 
    return None
    
def concat_rec(words : list[str]) -> str:
    return None
    
def half_christmas_tree_rec(height : int) -> str: 
    return None

def find_max(llist : list[int]) -> int:
    max_value = llist.pop()
    for value in llist:
        if value>max_value:
            max_value = value
    return max_value

def find_max_rec(llist : list[int]) -> int:
    return None

def main():
    x = np.arange(-5,5,0.05)
    f1 = -1*x**2+2*x +5
    f2 = 10*np.sin(2*np.pi*2*x) + 2*x
    f3 = f1*f2*0.01
    
    plt.subplot(2,1,1)    
    plt.plot(x,f1, 'r')
    plt.plot(x,f2, 'b')
    plt.xlabel('x')
    plt.ylabel('f(x)')

    plt.subplot(2,1,2)
    plt.plot(x,f3, 'k')
    plt.xlabel('x')
    plt.ylabel('f(x)')

    
    
if __name__=='__main__':
    main()    
    
    
    
    
