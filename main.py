 
def add(a, b):
    return a+b

def subtract(a, b):
    return a-b

def multiply(a, b):
    return a*b

def divide(a, b):
    if b == 0:
        raise ValueError("Division by zero is not allowed.") 
    return a/b
    
def factorial(n):
    if n==1:
        return 1
    return n*factorial(n-1)


def factorial2(n):
    res=1
    for i in range(1,n+1):
        res=res*i
    
    return res


def power(base, exponent):
    if exponent==1:
        return base
    return base*power(base,exponent-1)
    
def power2(base, exponent):
    res=1
    for i in range(exponent):
        res=res*base
    return res

def square_root(n):
    return 0


print(power(2,1))
print(power(2,2))
print(power(2,3))
print(power(2,4))
print(power(2,5))
print(power(2,6))





