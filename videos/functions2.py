#we will create a fuction to compare the greatest number

def greatest_number (numb1, numb2, numb3):
    if numb1 >= numb2 and numb1 >= numb3:
        return numb1
    elif numb2 >= numb1 and numb2 >= numb3:
        return numb2
    else:
        return numb3

numb1= input ("insert first number: ")
numb2= input ("insert second number: ")
numb3= input ("insert third number: ")

print (greatest_number(numb1, numb2, numb3))