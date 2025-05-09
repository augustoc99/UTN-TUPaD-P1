#Ejercicio1
listam4=list(range(4, 100, 4))
print(listam4)

#Ejercicio2
lista5 = ["mono", "perro", "gato", "oso", "tero"]
print(lista5)
posicionlista=lista5[3]
print(posicionlista)

#Ejercicio3
lista_vacia = []
lista_vacia.append("asado")
lista_vacia.append("ensalada")
lista_vacia.append("postre")
print(lista_vacia)

#Ejercicio4
animales=["perro","gato","conejo","pez"]
print(animales)
animales[1]="loro"
animales[3]="oso"
print(animales)

#Ejercicio5
numeros=[8,15,3,22,7]
print(numeros)
numeros.remove(max(numeros))
print(numeros)
print("Comprobada por terminal, las líneas de código en cuestión proceden a remover el elemento cuyo valor fuese el más alto encontrado a lo largo de la referida lista -NUMEROS-. En este caso se trta del número 22, quedando conformada la que originariamente fue una lista de 5 elementos en una lista de 4 elementos.")

#Ejercicio6
lista6=list(range(10, 31, 5))
print(lista6)
posicionlista=lista6[0]
posicionlista1=lista6[1]
print(posicionlista, posicionlista1)

#Ejercicio7
autos=["sedan","polo","suran","gol"]
print(autos)
autos[1]="hatchback"
autos[2]="coupe"
print(autos)

#Ejercicio8
dobles = []
dobles.append(5)
dobles.append(10)
dobles.append(15)
print(dobles)
dobles[0]=5*2
dobles[1]=10*2
dobles[2]=15*2
print(dobles)

#Ejercicio9
compras=[["pan", "leche"], ["arroz", "fideos", "salsa"], ["agua"]]
lista3=compras[2]
lista3.append("jugo")
print(lista3)
lista2=compras[1]
lista2[1]="tallarines"
print(lista2)
lista1=compras[0]
lista1.remove("pan")
print(lista1)
print("Finalmente, se procede a imprimir la conformación final de la lista con los cambios correspondientes:", compras)

#Ejercicio10
lista_anidada = [15, True, [25.5, 57.9, 30.6], False]
print(lista_anidada)
