#1. Crear una función llamada imprimir_hola_mundo que imprima por
#pantalla el mensaje: “Hola Mundo!”. Llamar a esta función desde el
#programa principal.
print ("______________________________________")

def imprimir_hola_mundo ():
    print ("Hola Mundo!")

#Programa principal.
imprimir_hola_mundo ()
print ("______________________________________")

#-----------------------------------------------

#2. Crear una función llamada saludar_usuario(nombre) que reciba
#como parámetro un nombre y devuelva un saludo personalizado.
#Por ejemplo, si se llama con saludar_usuario("Marcos"), deberá de-
#volver: “Hola Marcos!”. Llamar a esta función desde el programa
#principal solicitando el nombre al usuario.

def saludar_usuario (nombre):
    return (f"Hola {nombre}!")

#Programa principal.
primer_nombre = input ("Ingrese su nombre: ")
saludo = saludar_usuario (primer_nombre)
print ("\n" + saludo)
print ("______________________________________")

#-----------------------------------------------

#3. Crear una función llamada informacion_personal(nombre, apellido,
#edad, residencia) que reciba cuatro parámetros e imprima: “Soy
#[nombre] [apellido], tengo [edad] años y vivo en [residencia]”. Pe-
#dir los datos al usuario y llamar a esta función con los valores in-
#gresados.

def informacion_personal (nombre, apellido, edad, residencia):
    return (f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")

#Programa principal.
primer_nombre = input ("Ingrese su nombre: ")
apellido = input ("Ingrese su apellido: ")
edad = input ("Ingrese su edad: ").strip ()
residencia = input ("Ingrese su residencia: ")

#Se guardan los datos que ingresó el usuario para cuando haya que reutilizarlos sin llamar nuevamente a la función.
datos = informacion_personal (primer_nombre, apellido, edad, residencia)

print ("\n" + datos)
print ("______________________________________")

#-----------------------------------------------

#4. Crear dos funciones: calcular_area_circulo(radio) que reciba el ra-
#dio como parámetro y devuelva el área del círculo. calcular_peri-
#metro_circulo(radio) que reciba el radio como parámetro y devuel-
#va el perímetro del círculo. Solicitar el radio al usuario y llamar am-
#bas funciones para mostrar los resultados.

import math

def calcular_area_circulo (radio):
    return math.pi * radio ** 2

def calcular_perimetro_circulo (radio):
    return 2 * math.pi * radio

#Con .replace (",",".") reemplaza la "," (coma) por "." punto para evitar errores.
pidiendo_radio = float (input ("Ingrese el radio del círculo: ").replace (",",".").strip ())

area_circulo = calcular_area_circulo (pidiendo_radio)
perimetro_circulo = calcular_perimetro_circulo (pidiendo_radio)

print (f"\nEl área del círculo es: {area_circulo}")
print (f"El perímetro del círculo es: {perimetro_circulo}")
print ("______________________________________")

#-----------------------------------------------

#5. Crear una función llamada segundos_a_horas(segundos) que reciba
#una cantidad de segundos como parámetro y devuelva la cantidad
#de horas correspondientes. Solicitar al usuario los segundos y mos-
#trar el resultado usando esta función.

def segundos_a_horas (segundos):
    return segundos / 3600

segundos_ingresados = int (input ("Ingrese tiempo en segundos: ").strip ())
horas = segundos_a_horas (segundos_ingresados)

print (f"\n{segundos_ingresados} segundos son {horas:.2f} horas")
print ("______________________________________")

#-----------------------------------------------

#6. Crear una función llamada tabla_multiplicar(numero) que reciba un
#número como parámetro y imprima la tabla de multiplicar de ese
#número del 1 al 10. Pedir al usuario el número y llamar a la fun-
#ción.

def tabla_de_multiplicar (numero):
    tabla = ""
    for i in range (1,11):
        tabla += f"{numero} x {i} = {numero * i}\n"
    return tabla.rstrip () #.rstrip () elimina el último salto de línea innesesario de la tabla.

num = int (input ("Ingrese un número 1 al 10: ").strip ())
tabla_mult = tabla_de_multiplicar (num)

print (f"\n{tabla_mult}")
print ("______________________________________")

#-----------------------------------------------

#7. Crear una función llamada operaciones_basicas(a, b) que reciba
#dos números como parámetros y devuelva una tupla con el resulta-
#do de sumarlos, restarlos, multiplicarlos y dividirlos. Mostrar los re-
#sultados de forma clara.

def operaciones_basicas (a,b):
    suma = a + b
    resta = a - b
    multiplicación = a * b
    division = a / b if b != 0 else "No se puede dividir por 0"
    return (suma, resta, multiplicación, division)

num_a = float (input("Ingrese el primer número: ").replace (",",".").strip ())
num_b = float (input ("Ingrese el segundo número: ").replace (",",".").strip ())

resultados = operaciones_basicas (num_a,num_b)

print (f"\nSuma: {resultados[0]}")
print (f"Resta: {resultados[1]}")
print (f"Multiplicación: {resultados[2]}")
print (f"División: {resultados[3]}")
print ("______________________________________")

#-----------------------------------------------

#8. Crear una función llamada calcular_imc(peso, altura) que reciba el
#peso en kilogramos y la altura en metros, y devuelva el índice de
#masa corporal (IMC). Solicitar al usuario los datos y llamar a la fun-
#ción para mostrar el resultado con dos decimales.

def calcular_imc (peso,altura):
    imc = peso / (altura ** 2)
    return imc

pedir_peso = float (input("Ingrese su peso en kilogramos: ").replace (",",".").strip ())
pedir_altura = float (input("Ingrese su altura en metros: ").replace (",",".").strip ())

resultado_imc = calcular_imc (pedir_peso,pedir_altura)

print (f"\nSu indice de masa corporal es: {resultado_imc:.2f}")
print ("______________________________________")

#-----------------------------------------------

#9. Crear una función llamada celsius_a_fahrenheit(celsius) que reciba
#una temperatura en grados Celsius y devuelva su equivalente en
#Fahrenheit. Pedir al usuario la temperatura en Celsius y mostrar el
#resultado usando la función.

def celsius_a_fahrenheit (celsius):
    fahrenheit = (celsius * (9 / 5)) + 32
    return fahrenheit

pide_celsius = float (input ("Ingrese una temperatura en grados celsius °C: ").replace (",",".").strip ())
resultado_fahrenheit = celsius_a_fahrenheit (pide_celsius)

print (f"\n{pide_celsius} °C equivalen a {resultado_fahrenheit} °F")
print ("______________________________________")

#-----------------------------------------------

#10.Crear una función llamada calcular_promedio(a, b, c) que reciba
#tres números como parámetros y devuelva el promedio de ellos.
#Solicitar los números al usuario y mostrar el resultado usando esta
#función.

def calcular_promedio (a,b,c):
    return (a + b + c) / 3

prom_1 = float (input ("Ingrese nota 1: ").replace (",",".").strip ())
prom_2 = float (input ("Ingrese nota 2: ").replace (",",".").strip ())
prom_3 = float (input ("Ingrese nota 3: ").replace (",",".").strip ())

promedio_calculado = calcular_promedio (prom_1,prom_2,prom_3)

print (f"\nEl promedio de {prom_1}, {prom_2} y {prom_3} es: {promedio_calculado:.2f}")
print ("______________________________________")
