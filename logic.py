from pickle import TRUE
from sympy import false, true


str1=print("It is raining")
str2=print("I carry an umbrella")

a=int(input("Set the value for first string: "))
b=int(input("Set the value for first string: "))

if(a==1):
    A=true
else:
    A=false

if(b==1):
    B=true
else:
    B=false

if(A==true and B==true):
    print("Both statements are truth")

elif(A==true or B==true):
    print("One of the statements is truth")
    if(A==true):
        print("It is raining")
    else:
        print("I carry an umbrella")

else:
    print("Both are false statements")

if(not A or B):
    print("If it rains then I carry an umbrella")

if((not A or B) and (not B or A)):
    print("If and only if it rains then I carry an umbrella")