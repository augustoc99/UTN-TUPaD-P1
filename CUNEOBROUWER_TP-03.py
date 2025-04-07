# Ejercicio 1
edad =int(input("Ingrese su edad"))
if edad >= 18: 
    print("Eres mayor de edad")

#Ejercicio 2
nota=float(input("Ingrese su calificación"))
if nota >= 6:
    print ("Aprobado")
else:
    print ("Desaprobado")

#Ejercicio3
num = int(input("Ingrese un número par"))
if num % 2 == 0:
    print("Ha ingresado un número par")
else:
    print ("Por favor ingrese un número par")

#Ejercicio4
edad = int(input("Ingrese su edad"))
if edad < 12:
    print("Usted es un niño")
elif edad>= 12 and edad<18:
    print("Usted es un adolecente")
elif edad>= 18 and edad<30:
    print ("Usted es un adulto joven")
else:
    print("Usted es un adulto")

#Ejercicio5
contrasena = input("Ingrese una contraseña que contenga entre 8 y 14 caractéres")
if len(contrasena)>= 8 and len(contrasena) <= 14:
    print("Ha ingresado una contraseña correcta")
else:
    print ("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")

#Ejercicio6
from statistics import mode, median, mean 
mi_lista = [1,2,5,5,3] 
mean(mi_lista)

import random 
numeros_aleatorios = [random.randint(1, 100) for i in range(50)]

media = mean(numeros_aleatorios)
mediana = median(numeros_aleatorios)
moda = mode(numeros_aleatorios)

print("Lista de números:", numeros_aleatorios)
print(f"Media: {media}")
print(f"Mediana: {mediana}")
print(f"Moda: {moda}")

if media > mediana and mediana > moda:
    print("Distribución con sesgo positivo (a la derecha).")
elif media < mediana and mediana < moda:
    print("Distribución con sesgo negativo (a la izquierda).")
elif media == mediana == moda:
    print("Distribución sin sesgo.")
else:
    print("La distribución no cumple estrictamente con ninguno de los patrones de sesgo definidos.")

#Ejercicio7
frase = input("Ingrese una frase")
if frase[-1] in 'aeiou':
     print(f"{frase}!")
else:
    print(frase)

#Ejercicio8
nombre = input("Ingrese su nombre")
numero = int(input("Ingrese el número 1 para imprimir en mayúsucla, el número 2 para imprimir en minúscula, o el número 3 para imprimirlo con la primer letra en mayúscula únicamente"))
if numero == 1:
     print(nombre.upper())
elif numero == 2:
     print(nombre.lower())
else:
     print(nombre)

#Ejercicio9
magnitud = float(input("Por favor, ingrese la magnitud del terremoto según la escala de Richter"))
if magnitud < 3:
     print("Muy leve")
elif magnitud >= 3 and magnitud < 4:
     print("Leve")
elif magnitud >= 4 and magnitud < 5:
     print("Moderado")
elif magnitud >= 5 and magnitud < 6:
     print("Fuerte")
elif magnitud >= 6 and magnitud < 7:
     print("Muy fuerte")
elif magnitud > 7:
     print("Extremo")

#Ejercicio10
hemisferio = input("¿En qué hemisferio te encuentras? (N/S): ").upper()
mes = int(input("¿Qué mes es? (1-12): "))
dia = int(input("¿Qué día es? (1-31): "))

fecha = (mes, dia)

if hemisferio == "N":
    if (mes == 12 and dia >= 21) or (mes in [1, 2]) or (mes == 3 and dia <= 20):
        estacion = "Invierno"
    elif (mes == 3 and dia >= 21) or (mes in [4, 5]) or (mes == 6 and dia <= 20):
        estacion = "Primavera"
    elif (mes == 6 and dia >= 21) or (mes in [7, 8]) or (mes == 9 and dia <= 20):
        estacion = "Verano"
    else:
        estacion = "Otoño"
elif hemisferio == "S":
    if (mes == 12 and dia >= 21) or (mes in [1, 2]) or (mes == 3 and dia <= 20):
        estacion = "Verano"
    elif (mes == 3 and dia >= 21) or (mes in [4, 5]) or (mes == 6 and dia <= 20):
        estacion = "Otoño"
    elif (mes == 6 and dia >= 21) or (mes in [7, 8]) or (mes == 9 and dia <= 20):
        estacion = "Invierno"
    else:
        estacion = "Primavera"
else:
    estacion = "Hemisferio no válido"

print("Estás en:", estacion)
