#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Still second Try with better Functions

# Functions 2.0
def calculate(a,b, operator):
    if operator == "+":
        return a+b
    elif operator == "-":
        return a-b
    elif operator == "*":
        return a*b
    elif operator == "/":
        return a/b if b != 0 else "Error: division by zero"
    else:
        return "Invalid operation"


# In[2]:


# First Try 

# Basic Interface
print("Basic Calculator on Python")
a = float(input("First Number: "))


while True:
    
    op = input("What operation do you want to do?(+, -, *, /): ")
    b = float(input("Second Number: "))

    result = calculate(a, b, op)
    print("Result:", result)

    choice = input("Do you want to continue with this result? (Y/N): ").upper()
    if choice == "Y":
        a = result
    if choice != "Y":
        again = input("Do you want to calculate again? (Y/N): ").upper()
        if again != "Y":
            print("Goodbye!")
            break

