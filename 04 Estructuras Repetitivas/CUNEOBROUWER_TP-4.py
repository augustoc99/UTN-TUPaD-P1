#Ejercicio1
for i in range(0, 101):
    print(i)

#Ejercicio2
num=int(input("Ingrese un número entero a fin de determinar sus dígitos"))
contador = 0
num = abs(num)

while num > 0:
    num //= 10
    contador += 1

print("la cantidad de dígitos del número ingresado es", contador)

#Ejercicio3
numero1=int(input("Escribe el primer número"))
numero2=int(input("Escribe el segundo número"))
suma=0
for i in range(numero1 + 1, numero2):
    suma += i
print(f"La suma de los números comprendidos entre {numero1} y {numero2} es {suma}")

#Ejercicio4
suma = 0

num = int(input("Ingresa el número que se irá sumando: "))
while num != 0:
    suma += num
    num = int(input("Nuevamente, ingresa un número entero. Salvo desees terminar, para ello ingresa 0: "))

print(f"La suma de los números ingresados es: {suma}")

#Ejercicio5
import random
adivina=random.randint(0,9)
intentos=0
num = int(input("Ingresa un número para adivinar"))
while num != adivina:
    intentos=intentos + 1
    num = int(input("Nuevamente, ingresa un número."))

print(f"La cantidad de intentos llevados a cabo es: {intentos}. El número era el {adivina}")

#Ejercicio6
for i in range(100, -1, -1):
    print(i)

#Ejercicio7
num=int(input("Ingresa un número cuyos predecesores se sumarán"))
suma=0
for i in range(num):
    suma += i
print(f"La suma de los números es {suma}")

# Ejercicio8
contador = 0
positivos = 0
negativos = 0
pares = 0
impares = 0

while contador < 100:
    num = int(input("Ingresa un número: "))
    if num > 0:
        positivos += 1
    elif num < 0:
        negativos += 1
    if num % 2 == 0:
        pares += 1
    else:
        impares += 1
    
    contador += 1 

print(f"Números positivos: {positivos}")
print(f"Números negativos: {negativos}")
print(f"Números pares: {pares}")
print(f"Números impares: {impares}")

# Ejercicio9
contador = 0
suma=0
while contador < 100:
    num = int(input("Ingresa un número: "))
    suma += num
    contador += 1
promedio=float(suma/100)
print(f"Media de número ingresados {promedio}")

# Ejercicio10
num=input("Ingresa un número:")
numero_invertido=num[::-1]
print("El número invertido al usted ingresado es:", numero_invertido)
