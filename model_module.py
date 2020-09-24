#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np


# # Runge-Kutta Method
# 

# $f(n)------>$fn
# 
# $f(n + 1)---->$ fn1

# In[2]:


def runge_kutta_theta(tn, tn1, theta_n, Vrn, Vln, R, L):
    h = (tn1 - tn)
    F1 = h*(R/L)*(Vrn- Vln)
    F2 = h*(R/L)*(Vrn- Vln)
    F3 = h*(R/L)*(Vrn- Vln)
    F4 = h*(R/L)*(Vrn- Vln)
    theta_n1 =  theta_n + (F1 + 2*F2 + 2*F3 + F4)/6
    return theta_n1


# In[3]:


def runge_kutta_x(tn, tn1, xn, theta_n, Vrn, Vln, R, L):
    h = (tn1 - tn)
    F1 = h*(R/2)*(Vrn + Vln)*np.cos(theta_n)
    F2 = h*(R/2)*(Vrn + Vln)*np.cos(theta_n)
    F3 = h*(R/2)*(Vrn + Vln)*np.cos(theta_n)
    F4 = h*(R/2)*(Vrn + Vln)*np.cos(theta_n)
    xn1 =  xn + (F1 + 2*F2 + 2*F3 + F4)/6
    return xn1


# In[4]:


def runge_kutta_y(tn, tn1, yn, theta_n, Vrn, Vln, R, L):
    h = (tn1 - tn)
    F1 = h*(R/2)*(Vrn + Vln)*np.sin(theta_n)
    F2 = h*(R/2)*(Vrn + Vln)*np.sin(theta_n)
    F3 = h*(R/2)*(Vrn + Vln)*np.sin(theta_n)
    F4 = h*(R/2)*(Vrn + Vln)*np.sin(theta_n)
    yn1 =  yn + (F1 + 2*F2 + 2*F3 + F4)/6
    return yn1


# # Initialize vectors 

# In[5]:


def initialize(t_size, theta_0, x0, y0):
    theta= np.zeros((t_size))
    x= np.zeros((t_size))
    y= np.zeros((t_size))    
    R = 1
    L = 2    
    theta[0] = theta_0
    x[0] = x0
    y[0] = y0
    return theta, x, y


# # Generate the outputs

# In[6]:


def generate(t, Vr, Vl, theta_0, x0, y0, R, L):  
    theta, x, y = initialize(t.shape[0], theta_0, x0, y0)
    for i in range(t.shape[0] - 1):    
        theta[i + 1] = runge_kutta_theta(t[i], t[i + 1], theta[i], Vr[i], Vl[i], R, L)    
        x[i + 1] = runge_kutta_x(t[i], t[i + 1], x[i], theta[i], Vr[i], Vl[i], R, L)
        y[i + 1] = runge_kutta_y(t[i], t[i + 1], y[i], theta[i], Vr[i], Vl[i], R, L)
    return theta, x, y

