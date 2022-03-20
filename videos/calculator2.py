
number1 = int(input("type number 1: "))
number2 = int(input("type number 2: "))
operations = ["add", "rest","multiply","divide","add", "rest","multiply","divide"]


def sum (number1,number2):
        result = number1 + number2
        return (result)

def rest (number1,number2):
        result = number1 - number2
        return (result)

def multiply (number1,number2):
        result = number1 * number2
        return (result)

def divide (number1,number2):
        result = number1 / number2
        return (result)
    

def calculator (operation, number1, number2):
    if operation == "add":
       result=  sum(number1, number2)
    if operation == "rest":
       result=  rest(number1, number2)
    if operation == "multiply":
       result=  multiply(number1, number2)
    if operation == "divide":
       result=  divide(number1, number2)
    print (result)


        
for operation in operations:
    print (operation)
    calculator(operation, number1, number2)