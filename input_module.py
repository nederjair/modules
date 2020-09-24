#!/usr/bin/env python
# coding: utf-8

# # Libraries

# In[1]:


import numpy as np
from random import seed
from random import randint
import random


# # Generation function

# In[2]:


def generate(sample_number, Vmax):
    min_value = -Vmax
    max_value = Vmax
    seed(randint(0, 10000))
    index_a =randint(0, sample_number - 2) #initial value of the interval to fill the vector Vr or Vl
    index_b =randint(index_a, sample_number - 2) #final value of the interval to fill the vector Vr or Vl
    V = min_value + (random.random()*(max_value - min_value))
    V_input= np.zeros((sample_number))
    for i in range(index_b - index_a + 1):
        V_input[index_a + i] = V
    return V_input

