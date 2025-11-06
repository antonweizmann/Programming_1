# -*- coding: utf-8 -*-
import random
import numpy as np

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
