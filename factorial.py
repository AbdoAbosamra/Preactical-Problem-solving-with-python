# The perfect code of factorial by Recursion .

def factorial(n):
    if n < 0  or int(n) != n : # --> Unintentional cases
        return "Undefined"
    if n == 0 or n == 1 : # for Base Condition
        return 1
    else: 
        return n * factorial(n-1) # Recursive case

# Check cases 
print(factorial(-5))    # --> Undefined
print(factorial(2.8))   # --> Undefined
print(factorial(0))     # --> 1 
print(factorial(6))     # --> 720
