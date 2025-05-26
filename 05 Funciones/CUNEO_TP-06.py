#Ejercicio1
mensaje =("Hola")
mensaje2=("Mundo!")
print(f"{mensaje} {mensaje2}")

#Ejercicio2
#Func
def saludar_usuario(nombre):
    return f"Hola {nombre}!"

#MainCode
nombre=input("Coloca tu nombre ")
saludo=saludar_usuario(nombre)
print(saludo)

#Ejercicio3
#Func
def informacion_personal(nombre, apellido, edad, residencia):
    return f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}"

#MainCode
nombre=input("Coloca tu nombre ")
apellido=input("Coloca tu apellido ")
edad=input("Coloca tu edad ")
residencia=input("Coloca tu lugar de residencia ")
saludocompleto=informacion_personal(nombre, apellido, edad, residencia)
print(saludocompleto)

#Ejercicio4
#Func
def calcular_area_circulo(radio):
    return 3.14*(radio*radio)

def calcular_perimetro_circulo(radio):
    return 2*3.14*radio

#MainCode
radio=float(input("Coloca, en centímetros, el radio del cículo "))
operac=calcular_area_circulo(radio)
operac2=calcular_perimetro_circulo(radio)
print(f" El area del cículo es de {operac} centímetros, mientras que su perímetro es de {operac2} centímetros.")

#Ejercicio5
#Func
def segundos_a_horas(segundos):
    return segundos/3600 

#MainCode
segundos=int(input("Coloca la cantidad de segundos cuyo total en horas quisieras conocer "))
operac=segundos_a_horas(segundos)
print(f"El total de {segundos} segundos equivale a {operac} horas")

#Ejercicio6
#Func
def tabla_multiplicar(numero):
    return numero*1,numero*2,numero*3,numero*4,numero*5,numero*6,numero*7,numero*8,numero*9,numero*10

#MainCode
numero=int(input("Ingresa un número cuyo resultado de multiplicación hasta 10 quisieras conocer: "))
operac=tabla_multiplicar(numero)
print("Se imprimirá una secuencia de 10 números, siendo desde el primero hasta el último los resultados de multiplicar el número ingresado hasta x10", operac)

#Ejercicio7
#Func
def operaciones_basicas(a, b):
    return  a+b, a-b,a*b, a/b

#MainCode
a=int(input("Ingresa un número: "))
b=int(input("Ingresa otro número:"))
operac=operaciones_basicas(a, b)
print("A continuación verás los resultados de sumar, restar, multiplicar y dividir los números ingresados", operac)

#Ejercicio8
#Func
def calcular_imc(peso,altura):
    return  peso/(altura)**2

#MainCode
peso=float(input("Ingrese su peso en kilogramos "))
altura=float(input("Ingrese su altura en metros "))
operac=calcular_imc(peso,altura)
print("Su IMC es de", operac, "kg/m2")

#Ejercicio9
#Func
def celsius_a_fahrenheit(celsius):
    return  celsius*(9/5)+32

#MainCode
celsius=float(input("Ingrese la temperatura en C° que quisiera conocer en Farenheit "))
operac=celsius_a_fahrenheit(celsius)
print(f"Los grados C° {celsius} en Ferenheit son {operac}")

#Ejercicio10
#Func
def calcular_promedio(a, b, c):
    return  (a+b+c)/3

#MainCode
a=float(input("Ingrese un número: "))
b=float(input("Ingrese el segundo número: "))
c=float(input("Ingrese el tercer número: "))
operac=calcular_promedio(a, b, c)
print(f"El promedio de los números {a}, {b}, {c} es {operac}")
