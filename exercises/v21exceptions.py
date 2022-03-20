#exceptions, we will create a calculator program, then, we will create an exception whe dividing by zero, explanation in line A

from ast import Return
from decimal import DivisionByZero


def sum (a,b):
    return (a+b)


def minus (a, b):
    return (a - b)

def multiply (a, b):
    return (a *b)

def divide (a,b):
    return (a/b)

#Line B: (Video 22) in this one, we have also included a while True which will create a loop unless we add a break at the end, that will return to ask a value for a and b in case user inputs an invalid digit (different from a #)

while True:

    try:
        a= int(input("insert first number: "))
        b = int(input("insert second number: "))

    except ValueError:
        print ("insert a value number")

        break

operation = input("insert operation: sum, minus, multiply, divide: ")



if operation == ("sum"):
    print (sum(a, b))

elif operation == ("minus"):
    print (minus (a,b))

elif operation == ("multiply"):
    print (multiply (a,b))

#Line A: if we know the name of the error we can include "try" and "except" and we add the name of the error and the message that will pop up. 

try:
    if operation == ("divide"):
        print (divide (a, b))
except ZeroDivisionError:
    print ("division by zero is not possible")

# then we can continue coding, next line can represent lines of coding

print ("process is finished") 
    


