#Ejercicio1
#Func
def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n - 1)

#MainCode
n = int(input("Ingresa un número: "))
for i in range(1, n + 1):
    print(f"{i}! = {factorial(i)}")

#Ejercicio2
#Func
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

#MainCode
n = int(input("Mostrar serie de Fibonacci hasta la posición: "))
for i in range(n):
    print(fibonacci(i), end=" ")

#Ejercicio3
#Func
def potencia(base, exponente):
    if exponente == 0:
        return 1
    return base * potencia(base, exponente - 1)

#MainCode
b = int(input("Base: "))
e = int(input("Exponente: "))
print(f"{b}^{e} = {potencia(b, e)}")

#Ejercicio4
#Func
def decimal_a_binario(n):
    if n == 0:
        return ""
    return decimal_a_binario(n // 2) + str(n % 2)

#MainCode
num = int(input("Ingresa un número decimal: "))
binario = decimal_a_binario(num)
print(f"El número binario es: {binario or '0'}")

#Ejercicio5
#Func
def es_palindromo(palabra):
    if len(palabra) <= 1:
        return True
    if palabra[0] != palabra[-1]:
        return False
    return es_palindromo(palabra[1:-1])

#MainCode
texto = input("Ingresa una palabra: ")
print("Es palíndromo:", es_palindromo(texto))

#Ejercicio6
#Func
def suma_digitos(n):
    if n < 10:
        return n
    return n % 10 + suma_digitos(n // 10)

#MainCode
num = int(input("Número para sumar sus dígitos: "))
print("Suma de dígitos:", suma_digitos(num))

#Ejercicio7
#Func
def contar_bloques(n):
    if n == 1:
        return 1
    return n + contar_bloques(n - 1)

#MainCode
nivel = int(input("Bloques en el nivel más bajo: "))
print("Total de bloques:", contar_bloques(nivel))
