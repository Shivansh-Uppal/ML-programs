from sympy import false, true
from math import sqrt

n=int(input("enter a number: "))

def isPrime(n):
    if(n<=1):
        return false
    
    for i in range(2,int(sqrt(n))+1):
        if(n%i==0):
            return false
    
    return true

x=isPrime(n)

if(x):
    print(f"{n} is prime")
else:
    print(f"{n} is not prime")