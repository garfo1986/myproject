
first =int(input("insert first digit: "))
op = input("insert operator: ")
second = int(input("insert second digit: "))

if op == "+":
    print (first + second)
elif op == "-":
    print (first - second)
elif op == "*":
    print (first * second)
elif op == "/":
    print (first / second)
else: print ("invalid operator")
