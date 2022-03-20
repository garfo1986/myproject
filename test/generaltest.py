

euro = 4500
pesos_en_euros= ""
pesos = int(input("insert euros here:"))
if pesos >= 0:
    pesos_en_euros= pesos * euro
    print("esos " + str(pesos) + " euros, equivalen a " + str(pesos_en_euros) + " pesos")
else:
    print("insert a value higher than 0")
