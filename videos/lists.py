familia = ["Gelma", "Carlos", "Lau", "Jason", "Yeimy", "Jhon", "Perro"]

a= "el nombre de"
print (a, "la mamá es", familia[0], a, "del papá es", familia[1], a, "de los hermanos es", familia[3], familia[4], "y", familia[5] )

dog_name = input ("pongale nombre al perro: ")

familia[6] =dog_name

print (familia)

#si se tienen dos listas se pueden unir con .extend

amigos = ["Manuel", "Ricardo", "Jorge", "lambucio"]

familia.extend (amigos)
print ("esta es la lista de familia con amigos incluidos", familia)


# para agregar un item en la lista, se escoge la posición en la que se desea el item: 
familia.insert(0, "Dios")
print("esta es la familia completa", familia)

#para eliminar un elemento, se utiliza el comando .remove y en parentesis se pone el nombre del item que se desea
#quitar

familia.remove("lambucio")

print(familia)

# .clear limpia la lista y .pop quita el último item en la lista
# . index("nombre a buscar") genera la posiciòn de un item en la lista. .count("nombre a buscar") cuenta cuantos
# de esos se tienen en la lista. .sort() organiza la lista en orden númerico .reverse hace lo opuesto
# friends2 = friends.copy() crea una copia de esa variable

