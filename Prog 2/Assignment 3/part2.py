# -*- coding: utf-8 -*-
import random
from time import perf_counter

import numpy as np
import matplotlib.pyplot as plt

def generate_rnd_array1(n, vmax=1000):
    x = np.zeros(n)
    for i in range(n):
        x[i] = random.randint(0, vmax)*0.01*i
    return x

def generate_rnd_array2(n, vmax=1000):
    x = np.zeros(n)
    for i in range(n):
        x[i] = i + 10*np.sin(2*np.pi*0.01)*random.randint(0, vmax)
    return x


def quicksort(arr2sort):
    # Base case:
    if arr2sort.shape[0]<=1:
        return arr2sort
    # Recursive case
    else:
        i = 0 # represents the size of the first partition  
        j = 0
        
        # Choosing a pivot:
        # in this implementation, the pivot is chosen 
        # as the last element
        pivot = arr2sort[-1] # the pivot
        
        # Looping over every element of the array
        # and creating a first partition of elements lower
        # than the pivot, and a second with elements greater 
        # than the pivot.
        for j in range(0,arr2sort.shape[0]):
            # check if the j element belongs to the first partition
            if arr2sort[j] <= pivot:
                # swap the element in j to the current partition
                # boundary (tracked by index i)
                temp = arr2sort[j]
                arr2sort[j] = arr2sort[i]
                arr2sort[i] = temp
                
                # increase the i, since the first partition 
                # has now one extra element
                i += 1
        
        # the element in arr2sort[i-1] is necessarily the pivot, 
        # and is guaranteed to be in the correct position
        # since it divides the two partitions!
        # we can then remove the pivot and repeat the process 
        # recursively!

        first = arr2sort[:i-1] # First partition (without pivot)
        second = arr2sort[i:] # Second partition (without pivot)
        
        # Repeat the process recursevely
        first_sorted = quicksort(first)
        second_sorted = quicksort(second)
        
        # Joining the resulting sorted partitions and pivot 
        return np.concatenate((first_sorted,np.array([arr2sort[i-1]]),second_sorted))

def mergesort(list2sort):
    # Base case
    if len(list2sort)<=1:
        return list2sort
    
    #Recursive case:
    else:
        # Dividing the list in two halves
        middle = len(list2sort)//2
        first = list2sort[:middle]
        second = list2sort[middle:]
        
        # Sort each half independently
        first_sorted = mergesort(first)
        second_sorted = mergesort(second)
        
        # Combining the two sorted lists into a new sorted list
        combined = []
        i = 0
        j = 0
        while i<len(first) and j<len(second):
            if first_sorted[i]<second_sorted[j]:
                combined.append(first_sorted[i])
                i+=1
            else:
                combined.append(second_sorted[j])
                j+=1
        
        # One of the partitions is empty.
        # Extending the last elements of the remaining list
        combined.extend(first_sorted[i:]) # maybe an empty list
        combined.extend(second_sorted[j:]) # maybe an empty list
        
        return combined        

def bubblesort(arr2sort):
    # Loop over the array
    for i in range(1,arr2sort.shape[0]):
        for j in range(arr2sort.shape[0]-i):
            # Sort neighboring elements
            if arr2sort[j]>arr2sort[j+1]:
                temp = arr2sort[j]
                arr2sort[j] = arr2sort[j+1]
                arr2sort[j+1] = temp
        # At the end of this loop, the maximum element is
        # at the end of the array. This means that the next 
        # time we do the same process we don't need to include 
        # that element. That's why j only goes until one less
        # element every time (shape-i)
    return arr2sort

def average_time(data: np.ndarray[float], n: float, f):
    total_time = 0
    for _ in range(n):
        data_copy = data.copy()
        start_time = perf_counter()
        f(data_copy)
        stop_time = perf_counter()
        total_time += (stop_time - start_time)
    avg_time = total_time / n
    return avg_time

def estimate_complexity(data: np.ndarray[float], n_samples: np.ndarray[int], f: object) -> None:
    estimated = np.zeros(n_samples.shape)
    for i in range(n_samples.shape[0]):
        estimated[i] = average_time(data[:n_samples[i]], 10, f)
    return estimated


def main():
    x = 1000
    unsorted_arr1 = generate_rnd_array1(x)
    unsorted_arr2 = generate_rnd_array2(x)
    number_of_samples = np.linspace(10, x, 200, dtype=int)

    plt.subplot(3,1,1)
    plt.plot(unsorted_arr1, label='Arr1')
    plt.plot(unsorted_arr2, label='Arr2')
    plt.legend()


    sorted_arr_merge = [mergesort(unsorted_arr1.copy()), mergesort(unsorted_arr2.copy())]
    sorted_arr_quick = [quicksort(unsorted_arr1.copy()), quicksort(unsorted_arr2.copy())]
    plt.subplot(3, 1, 2)
    plt.plot(sorted_arr_merge[0], 'r', label='Merge Arr1')
    plt.plot(sorted_arr_quick[1], 'b', label='Quick Arr2')
    plt.legend()
    plt.subplot(3, 1, 3)
    avg_times_merge = [estimate_complexity(unsorted_arr1, number_of_samples, mergesort), estimate_complexity(unsorted_arr2, number_of_samples, mergesort)]
    plt.plot(number_of_samples, avg_times_merge[0], 'g', label='Mergesort (Arr1)')
    plt.plot(number_of_samples, avg_times_merge[1], 'limegreen', label='Mergesort (Arr2)')
    avg_times_quick = [estimate_complexity(unsorted_arr1, number_of_samples, quicksort), estimate_complexity(unsorted_arr2, number_of_samples, quicksort)]
    plt.plot(number_of_samples, avg_times_quick[0], 'b', label='Quicksort (Arr1)')
    plt.plot(number_of_samples, avg_times_quick[1], 'cornflowerblue', label='Quicksort (Arr2)')
    plt.xlabel('Input Size (N)')
    plt.ylabel('Time (s)')
    plt.legend()
    plt.show()

if __name__=="__main__":
    main()