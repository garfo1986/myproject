

def fun1(algo="cosa"):
    print("quiero una", algo)

fun1("roja")
fun1("de esas")
fun1("muy buena")
fun1()  
# cuando se deja la función abierta devuelve la variable definida en la linea 3 "def fun1(algo="cosa"):"
#___________________________


# lo que está dentro del parentesis se llama parametro, y le dice a Python que hay una variable en la función que
#se define al ser llamada en las lineas 19, 20 y 21
def a(name, age):
    print("hello " + name + ", you are " +  age)

a("Jason", "35")
a("Laura", "34")
a("Jhon", "22")


def sumar(number_one, number_two):
    return number_one + number_two
    
print(sumar(2, 3))
#___________________________

#la función lambda puede realizar la misma operación de forma más facíl

sumar = lambda número_1, número_2: número_1 + número_2
print(sumar(4,8))