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

#!/usr/bin/env python
# coding: utf-8

# In[2]:


# My best Try so far

# Functions 2.5
def get_number(prompt):
    """Ask number; accept 'Q/QUIT/EXIT' to esc."""
    while True:
        user_input = input(prompt).strip()
        if user_input.upper() in ("Q", "QUIT", "EXIT"):
            return None
        try:
            return float(user_input)
        except ValueError:
            print("Not a valid number. Try again (or 'Q', 'QUIT', 'EXIT' to quit)")

def bye():
    print("Goodbye!")

def get_op():
    """Ask for valid Operator"""
    valid = {"+", "-", "*", "/"}
    while True:
        op = input("What operation do you want to do? (+, -, *, /): ").strip()
        if op in valid:
            return op
        print("Invalid Operator. Use one of: + - * /")
print("Basic Calculator on Python (type 'Q', 'Quit' or 'EXIT' any time to quit)")


# In[3]:


# Interface for Calculator Ver. 2.5

a = get_number("First Number: ")
if a is None:
    bye()
else:
    while True:
        op = get_op()
        b = get_number("Second Number: ")
        if b is None:
            bye()
            break

        result = calculate(a, b, op)
        print("Result:", result)

        choice = input("Continue with this result [C], start new [N], or quit [Q]? ").strip().upper()
        if choice == "C":
            if isinstance(result, (int, float)):
                a = result
            else:
                print("Can not continue with a non-numeric result. Starting new. ")
                a = get_number("First Number: ")
                if a is None:
                    bye()
                    break
        elif choice == "N":
            a = get_number("First Number: ")
            if a is None:
                bye()
                break
        else:
            bye()
            break

