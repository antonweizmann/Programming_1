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
    # Base case(s)
    if n == 0:
        return n
    # Recursive case(s)
    elif n % 2 == 0:
        summed = sum_even_rec(n - 1) + n
        return summed
    else:
        return sum_even_rec(n - 1)
    
def array_product_rec(numbers : np.ndarray[int]) -> int: 
    if len(numbers) == 0:
        return 1
    else:
        product = array_product_rec(numbers[1:]) * numbers[0]
        return product
    
def concat_rec(words : list[str]) -> str:
    if len(words) == 1:
        return words[0]
    else:
        all_words = words[0] +  " " +concat_rec(words[1:])
        return  all_words

    
def half_christmas_tree_rec(height : int) -> str: 
    if height == 1:
        return "*"
    else:
        tree =  half_christmas_tree_rec(height - 1) + "\n" + height * "*"
        return tree

def find_max(llist : list[int]) -> int:
    max_value = llist.pop()
    for value in llist:
        if value>max_value:
            max_value = value
    return max_value

def find_max_rec(llist : list[int]) -> int:
    if len(llist) == 1:
        return llist[0]
    else:
        old_max = find_max_rec(llist[1:])
        if old_max > llist[0]:
            return old_max
        else:
            return llist[0]

def main():
    x = np.arange(-5,5,0.05)
    f1 = -1*x**2+2*x +5
    f2 = 10*np.sin(2*np.pi*2*x) + 2*x
    f3 = f1*f2*0.01
    
    plt.subplot(2,1,1)
    plt.plot(x,f1, 'r')
    plt.plot(x,f2, 'b')
    max_idx_f1 = np.where(f1 == np.max(f1))[0]
    plt.plot(x[max_idx_f1], f1[max_idx_f1], marker='X', color='red')
    max_idx_f2 = np.where(f2 == np.max(f2))[0]
    plt.plot(x[max_idx_f2], f2[max_idx_f2], marker='X', color='blue')
    plt.xlabel('x')
    plt.ylabel('f(x)')

    plt.subplot(2,1,2)
    plt.plot(x,f3, 'k')
    max_idx_f3 = np.where(f3 == np.max(f3))[0]
    mean_f3 = int(np.mean(f3))
    above_means = np.where(f3 > 2 * mean_f3)[0]
    plt.plot(x[above_means], f3[above_means], color='red')
    plt.plot(x[max_idx_f3], f3[max_idx_f3], marker='X', color='black')
    plt.xlabel('x')
    plt.ylabel('f(x)')

    
if __name__=='__main__':
    main()
    
    
    
