#!/usr/bin/env python
# coding: utf-8

# In[46]:


# First Try

# Functions
def sum(a,b):
    return a+b

def deduct(a,b):
    return a-b

def mult(a,b):
    return a*b

def div(a,b):
    if b != 0:
        return a/b
    else:
        return "Error"

# Basic Interface
print("Basic Calculator on Python")
op = input("What operation do you want to do?(sum, deduct, mult, div): ")

a = float(input("First Number: "))
b = float(input("Second Number: "))

if op == "sum":
    print("Result: ", sum(a,b))
elif op == "deduct":
    print("Result: ", deduct(a,b))
elif op == "mult":
    print("Result: ", mult(a,b))
elif op == "div": 
    print("Result: ", div(a,b))
else:
    
    print("Invalid")


# In[ ]:




