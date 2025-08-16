# 1) 
# Crear un programa que imprima por pantalla el mensaje: “Hola Mundo!”.

# Salida de datos, se muestra por pantalla una línea para mejorar la estética visual.
print ("______________________________________")
# Salida de datos, print ("") espacio vacío entre líneas para mejorar la estética visual.
print ("")
# Salida de datos, muestra por pantalla el mensaje "Hola Mundo!".
print ("Hola Mundo!")
# Salida de datos, se muestra por pantalla una línea para mejorar la estética visual.
print ("______________________________________")
# Salida de datos, print ("") espacio vacío entre líneas para mejorar la estética visual.
print ("")

#____________________________________________________________________________

# 2) 
# Crear un programa que pida al usuario su nombre e imprima por pantalla un saludo usando
# el nombre ingresado. Por ejemplo: si el usuario ingresa “Marcos”, el programa debe imprimir
# por pantalla “Hola Marcos!”. Consejo: esto será más sencillo si utilizas print(f…) para
# realizar la impresión por pantalla.

# Salida y Entrada de datos, se inicializa la variable "nombre" pidiendole al usuario 
# por medio de un mensaje ingresar su nombre que se guardará en la variable nombre como string.
nombre = input ("Ingrese su nombre: ")
# Salida de datos, print ("") espacio vacío entre líneas para mejorar la estética visual.
print ("")

# Salida de datos, se muestra por pantalla el saludo "Hola" + el contenido de la variable "nombre" + "!".
# por medio de la función f-string.
print (f"Hola, {nombre}!")
# Salida de datos, se muestra por pantalla una línea para mejorar la estética visual.
print ("______________________________________")
# Salida de datos, print ("") espacio vacío entre líneas para mejorar la estética visual.
print ("")

#____________________________________________________________________________

# 3)
# Crear un programa que pida al usuario su nombre, apellido, edad y lugar de residencia e
# imprima por pantalla una oración con los datos ingresados. Por ejemplo: si el usuario ingresa
# “Marcos”, “Pérez”, “30” y “Argentina”, el programa debe imprimir “Soy Marcos Pérez, tengo 30
# años y vivo en Argentina”. Consejo: esto será más sencillo si utilizas print(f…) para realizar
# la impresión por pantalla.

# Salida y Entrada de datos, se inicializan las variables "nombre", "apellido", "edad" y "lugar"
# pidiendole al usuario por medio de un mensaje que ingrese datos que serán asignado a las variables.
# La variable nombre es un string.
nombre = input ("Ingrese su nombre: ")
# La variable apellido es un string.
apellido = input ("Ingrese su apellido: ")
# La variable edad transforma los números ingresados como string a enteros.
edad = int (input ("Ingrese su edad: "))
# La variable lugar es un string.
lugar = input ("Ingrese su país de residencia: ")
# Salida de datos, print ("") espacio vacío entre líneas para mejorar la estética visual.
print ("")

# Salida de datos, muestra por pantalla la concatenación de un mensaje y el contenido de las 4 variables,
# por medio de la función f-string.
print (f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {lugar}.")
# Salida de datos, se muestra por pantalla una línea para mejorar la estética visual.
print ("______________________________________")
# Salida de datos, print ("") espacio vacío entre líneas para mejorar la estética visual.
print ("")

#____________________________________________________________________________

# 4)
# Crear un programa que pida al usuario el radio de un círculo e imprima por pantalla su área y
# su perímetro.

# Se importa el módulo math para poder usar la constante math.pi (número PI).
import math

# Salida y Entrada de datos, se inicializa la variable radio pidiendole al usuario por medio de
# un mensaje que ingrese el valor que tendrá la variable "radio", éste pasará de ser un string
# a un entero por medio de la función "int" y se le asignará a la variable radio.
radio = float (input ("Ingrese el rádio del círculo: "))
# Salida de datos, print ("") espacio vacío entre líneas para mejorar la estética visual.
print ("")

# Se realiza la operación para calcular el área del círculo, "math.pi" (número PI)
# que se multiplicará con el resultado de la potenciación de la variable "radio" al cuadrado,
# y el resultado se almacenará en la variable "área".
área = math.pi * radio ** 2

# Se realiza la operatoria para calcular el perímetro del círculo multiplicando
# 2 por PI por el radio y el resultado se almacenará en la variable "perímetro".
perímetro = 2 * math.pi * radio

# Salida de datos, se muestra por pantalla dos mensajes concatenando uno de ellos con la
# variable "área" y otro con "perímetro".
print (f"El área es: {área}")
print (f"El perímetro es: {perímetro}")
# Salida de datos, se muestra por pantalla una línea para mejorar la estética visual.
print ("______________________________________")
# Salida de datos, print ("") espacio vacío entre líneas para mejorar la estética visual.
print ("")

#____________________________________________________________________________

# 5)
# Crear un programa que pida al usuario una cantidad de segundos e imprima por pantalla a
# cuántas horas equivale.

# # Salida y Entrada de datos, se inicializa la variable "segundos" pidiendole al usuario por medio de
# un mensaje que ingrese un número en segundos, como se antepone la función "int" automaticamente
# pasa de ser un string a un número entero y se almacena en la variable "segundos".
segundos = int (input ("Ingrese una cantidad en segundos: "))
# Salida de datos, print ("") espacio vacío entre líneas para mejorar la estética visual.
print ("")

# Se realiza la operatoria para transformar segundos a horas y el resultado se almacena en la 
# variable "horas".
horas = segundos / 3600

# Salida de datos, por medio de la función f-string se concatena el mensaje con las variables.
print (f"{segundos} segundos equivalen a: {horas} horas.")
# Salida de datos, se muestra por pantalla una línea para mejorar la estética visual.
print ("______________________________________")
# Salida de datos, print ("") espacio vacío entre líneas para mejorar la estética visual.
print ("")

#____________________________________________________________________________

# 6)
# Crear un programa que pida al usuario un número e imprima por pantalla la tabla de
# multiplicar de dicho número.

# Primero se inicializa la variable "num" para evitar posibles errores.
num = 0
i = 1

# Salida de datos, se muestra por pantalla el mensaje.
print ("Tabla multiplicadora")
# Salida de datos, print ("") espacio vacío entre líneas para mejorar la estética visual.
print ("")
# Salida y Entrada de datos, se le pide al usuario por medio de un mensaje en pantalla que ingrese
# un dato, el usuario ingresa un número en string y la función "int" lo convierte a número entero,
# este número se almacena en la variable "num".
num = int (input ("Ingrese un número entero: "))
# Salida de datos, print ("") espacio vacío entre líneas para mejorar la estética visual.
print ("")

# Estructura repetitiva "for", esto cuenta de forma ascendente del 1 al 10.
for i in range (1, 11):
    # Salida de datos, muestra por pantalla las variables "num" por cada iterador "i" del 1 al 10 y
    # se multiplican "num" * "i" para el resultado.
    print (f"{num} * {i} = {num * i}")
    # Salida de datos, se muestra por pantalla una línea para mejorar la estética visual.
print ("______________________________________")
# Salida de datos, print ("") espacio vacío entre líneas para mejorar la estética visual.
print ("")

#____________________________________________________________________________

# 7)
# Crear un programa que pida al usuario dos números enteros distintos del 0 y muestre por
# pantalla el resultado de sumarlos, dividirlos, multiplicarlos y restarlos.

# Se inicializan todas las variables para evitar posibles errores.
num1 = 0
num2 = 0

# Salida y Entrada de datos, se pide al usuario a traves de un mensaje que ingrese un dato numérico,
# el dato ingresado es un string pero automáticamente se convertirá en entero gracias a la función "int",
# y el dato se almacenará en la variable "num1".
num1 = int (input("Ingrese un número entero distinto a 0: "))
# Salida de datos, print ("") espacio vacío entre líneas para mejorar la estética visual.
print ("")

# Condicional while, si el usuario ingresó un 0 se vuelve verdadera y muestra el siguiente mensaje,
# pero si no ingresa un 0 es falsa, el mensaje nunca se muestra y sigue a la siguiente secuencia.
while num1 == 0:
    num1 = int (input ("El número no puede ser 0, vuelva a intentarlo: "))
    # Salida de datos, print ("") espacio vacío entre líneas para mejorar la estética visual.
    print ("")

# Salida y Entrada de datos, se pide al usuario a traves de un mensaje que ingrese un dato numérico,
# el dato ingresado es un string pero automáticamente se convertirá en entero gracias a la función "int",
# y el dato se almacenará en la variable "num2".
num2 = int (input("Ingrese el segundo número entero distinto a 0: "))
# Salida de datos, print ("") espacio vacío entre líneas para mejorar la estética visual.
print ("")

# Condicional while, si el usuario ingresó un 0 se vuelve verdadera y muestra el siguiente mensaje,
# pero si no ingresa un 0 es falsa, el mensaje nunca se muestra y sigue a la siguiente secuencia.
while num1 == 0:
    num1 = int (input ("El número no puede ser 0, vuelva a intentarlo: "))
    # Salida de datos, print ("") espacio vacío entre líneas para mejorar la estética visual.
    print ("")
    
print (f"Suma: {num1} + {num2} = {num1 + num2}")
print (f"Resta: {num1} - {num2} = {num1 - num2}")
print (f"Multiplicación: {num1} * {num2} = {num1 * num2}")
print (f"Divición: {num1} / {num2} = {num1 / num2}")
# Salida de datos, print ("") espacio vacío entre líneas para mejorar la estética visual.
print ("")

# Según se ubiquen los números los resultados pueden cambiar, me pareció necesario mostrarlos también.
print ("A la inversa:")

print (f"Resta: {num2} - {num1} = {num2 - num1}")
print (f"Divición: {num2} / {num1} = {num2 / num1}")
# Salida de datos, se muestra por pantalla una línea para mejorar la estética visual.
print ("______________________________________")
# Salida de datos, print ("") espacio vacío entre líneas para mejorar la estética visual.
print ("")

#____________________________________________________________________________

# 8)
# Crear un programa que pida al usuario su altura y su peso e imprima por pantalla su índice
# de masa corporal.

# Se inicializan todas las variables para evitar posibles errores.
altura = 0
peso = 0
indice = 0

# Salida de datos, muestra por pantalla el nombre del programa.
print ("Calculadora de Índice de Masa Corporal")
# Salida de datos, print ("") espacio vacío entre líneas para mejorar la estética visual.
print ("")
print ("Ingrese su altura en metros, ejemplo: 1.80")
# Salida de datos, print ("") espacio vacío entre líneas para mejorar la estética visual.
print ("")
# Salida y Entrada de datos, se muestra el mensaje Altura: y el usuario tiene que ingresar su altura,
# ésta se ingresa en formato string y automaticamente con la función "float" se transforma en un número
# flotante.
altura = float (input ("Altura: "))
# Salida de datos, print ("") espacio vacío entre líneas para mejorar la estética visual.
print ("")
print ("Ingrese su peso en kilogramos, ejemplo: 78.5")
# Salida de datos, print ("") espacio vacío entre líneas para mejorar la estética visual.
print ("")
peso = float (input ("Peso: "))
# Salida de datos, print ("") espacio vacío entre líneas para mejorar la estética visual.
print ("")

# Operación para calcular el índice de masa muscular, se almacenará en la variable "indice".
indice = peso / (altura ** 2)

# Salida de datos, se muestra por pantalla un mensaje concatenado con el contenido de la
# variable "indice", gracias a la función f-string.
print (f"Su índice de masa corporal es: {indice}")
# Salida de datos, se muestra por pantalla una línea para mejorar la estética visual.
print ("______________________________________")
# Salida de datos, print ("") espacio vacío entre líneas para mejorar la estética visual.
print ("")

#____________________________________________________________________________

# 9)
# Crear un programa que pida al usuario una temperatura en grados Celsius e imprima por
# pantalla su equivalente en grados Fahrenheit.

# Se inicializan todas las variables para evitar posibles errores.
celsius = 0
fahrenheit = 0

# Salida de datos, se muestra por pantalla el nombre del programa.
print ("Convertidor de Grados Celsius (°C) a Grados Fahrenheit (°F)")
# Salida de datos, print ("") espacio vacío entre líneas para mejorar la estética visual.
print ("")
#Salida de datos, se le pide al usuario a travez de un mensaje que ingrese un dato.
print ("Ingrese una temperatura en °C")
# Salida de datos, print ("") espacio vacío entre líneas para mejorar la estética visual.
print ("")

# Entrada de datos, el usuario ingresa una temperatura en grados celsius y se almacena en la variable
# "celsius" como flotante.
celsius = float (input ("°C: "))
# Salida de datos, print ("") espacio vacío entre líneas para mejorar la estética visual.
print ("")

# Operatoria para convertir celsius a fahrenheit. El resultado se almacenará en la variable "fahrenheit".
fahrenheit = (9 / 5) * celsius + 32

# Salida de datos, se muestra por pantalla un mensaje concatenando el valor de la variable "fahrenheit".
print (f"{celsius} °C equivalen a {fahrenheit} °F")
# Salida de datos, se muestra por pantalla una línea para mejorar la estética visual.
print ("______________________________________")
# Salida de datos, print ("") espacio vacío entre líneas para mejorar la estética visual.
print ("")

#____________________________________________________________________________

# 10)
# Crear un programa que pida al usuario 3 números e imprima por pantalla el promedio de dichos números.

# Se inicializan todas las variables para evitar posibles errores.
num1 = 0
num2 = 0
num3 = 0
promedio = 0

# Salida de datos, se muestra por pantalla el nombre del programa.
print ("Calculadora de Promedio")
# Salida de datos, print ("") espacio vacío entre líneas para mejorar la estética visual.
print ("")
# Salida y Entrada, se pide al usuario por medio de un mensaje que ingrese 3 números,
# cada número se almacena como flotante en sus respectivas variables "num1", "num2",
# "num3".
num1 = float (input ("Ingrese el primer número: "))
# Salida de datos, print ("") espacio vacío entre líneas para mejorar la estética visual.
print ("")
num2 = float (input ("Ingrese el segundo número: "))
# Salida de datos, print ("") espacio vacío entre líneas para mejorar la estética visual.
print ("")
num3 = float (input ("Ingrese el tercer número: "))
# Salida de datos, print ("") espacio vacío entre líneas para mejorar la estética visual.
print ("")

# Operatoria para calcular el promedio de esos 3 números, se almacenará en la variable "promedio".
promedio = (num1 + num2 + num3) / 3

# Salida de datos, se muestra por pantalla la concatenación de un mensaje y el valor de la variable
# "promedio".
print (f"El promedio es: {promedio}")
# Salida de datos, se muestra por pantalla una línea para mejorar la estética visual.
print ("______________________________________")
# Salida de datos, print ("") espacio vacío entre líneas para mejorar la estética visual.
print ("")