#!/usr/bin/env python
# coding: utf-8

# In[11]:


# interp - Program to interpolate data using Lagrange 
# polynomial to fit quadratic to three data points

# Set up configuration options and special features
import numpy as np
import matplotlib.pyplot as plt


x1 = float(input("Enter the value of x1 = \t"))
y1 = float(input("Enter the value of y1 = \t"))
x2 = float(input("Enter the value of x2 = \t"))
y2 = float(input("Enter the vlaue of y2 = \t"))
x3 = float(input("Enter the value of x3 = \t"))
y3 = float(input("Enter the value of y3 = \t"))
x4 = float(input("Enter the value of x4 = \t"))
y4 = float(input("Enter the value of y4 = \t"))
xi = float(input("Enter the value of xi between x1 and x4 = \t"))

yi =  ((xi-x2)*(xi-x3)*(xi-x4)/((x1-x2)*(x1-x3)*(x1-x4)))*y1 +((xi-x1)*(xi-x3)*(xi-x4))/((x2-x1)*(x2-x3)*(x2-x4)))*y2 + ((xi-x1)*(xi-x2)*(xi-x4)/((x3-x1)*(x3-x2)*(x3-x4)))*y3 + ((xi-x1)*(xi-x2)*(xi-x3)/((x4-x1)*(x4-x2)*(x4-x3)))* y4

print(yi)
if (x1 < xi and xi < x4):
    print(yi)
else:
    print("Error")




