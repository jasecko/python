 
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


# print(power(2,1))
# print(power(2,2))
# print(power(2,3))
# print(power(2,4))
# print(power(2,5))
# print(power(2,6))


# print('Tento program zisti ci je cislo parne pomocou funkcie s navratovou hodnotou')
# cislo=int(input('Zadaj cele cislo: '))

def guess_if_even(number):
    # 2 % 2 = 0
    # 3 % 2 = 1
    # 4 % 2 = 0
    # 5 % 2 = 1
    # 3 % 3 = 0
    # 4 % 3 = 1
    # 6 % 3 = 0
    remainder=number%2
    if remainder==0:
        return True
    else:
        return False

def main():
    print('Tento program zisti ci je cislo parne pomocou funkcie s navratovou hodnotou')
    number=int(input('Zadaj cele cislo: '))
    is_even = guess_if_even(number)
    if is_even == True:
        print('Zadal si parne cislo')
    else:
        print('Zadal si neparne cislo')



main()

