import math

z=[12, 14]
print(z)
print(f"math.fsum({z}) gives: ",math.fsum(z))

n=int(input("enter a number: "))

print(f"math.factorial({n}) gives: ",math.factorial(n))

x = min(15, 100, 250)
y = max(500, 100, 250)
print("min(15, 100, 250) gives: ",x)
print("max(500, 100, 250) gives: ",y)

w = math.fabs(-7.56)
print("math.fabs(-7.56) gives: ",w)

x = math.ceil(0.12)
y = math.floor(-1.34)
print("math.ceil(0.12) gives: ",x) 
print("math.floor(-1.34) gives: ",y) 

x = math.pi
print("math.pi gives: ",x)

a=math.log2(n)
print(f"math.log2({n}) gives: ",a)

b=math.log10(n)
print(f"math.log10({n}) gives: ",b)

s=math.sqrt(n)
print(f"math.sqrt({n}) gives: ",a)

e=math.exp(n)
print(f"math.exp({n}) gives: ",e)
