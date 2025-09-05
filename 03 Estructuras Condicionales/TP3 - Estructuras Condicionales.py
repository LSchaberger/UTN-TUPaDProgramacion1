#Aclaración antes de comenzar:
#print ("______________________________________")
#print ("")
#Usaré esos dos print en todos los algorítmos para mejorar la estética al ejecutarlos en terminal.


#Actividades:

#1) Escribir un programa que solicite la edad del usuario. Si el usuario es mayor de 18 años,
#deberá mostrar un mensaje en pantalla que diga “Es mayor de edad”.

print ("______________________________________")
print ("")
#Función "int" indica que el número a ingresar será un entero.
edad_usuario = int(input("Ingrese su edad: "))
print ("")
if edad_usuario >= 18:
    print ("Es mayor de edad")
else:
    # Función "pass" hace que el algoritmo acabe sin hacer nada.
    pass
print ("______________________________________")

#2) Escribir un programa que solicite su nota al usuario. Si la nota es mayor o igual a 6, deberá
#mostrar por pantalla un mensaje que diga “Aprobado”; en caso contrario deberá mostrar el
#mensaje “Desaprobado”.

print ("")
#Función "float" por si el usuario ingresa número con coma.
nota_usuario = float (input ("Ingrese su nota: "))
print ("")
if nota_usuario >= 6:
    print ("Aprobado")
else:
    print ("Desaprobado")
print ("______________________________________")

#3) Escribir un programa que permita ingresar solo números pares. Si el usuario ingresa un
#número par, imprimir por en pantalla el mensaje "Ha ingresado un número par"; en caso
#contrario, imprimir por pantalla "Por favor, ingrese un número par". Nota: investigar el uso del
#operador de módulo (%) en Python para evaluar si un número es par o impar.

print ("")
numero = int (input("Ingrese un número par: "))
print ("")
#Función módulo "%" divide numero/2 y el resto de la operación lo compara "==" con el resto 0.
if numero % 2 == 0:
    print ("Ha ingresado un número par")
else:
    print ("Por favor, ingrese un número par")
print ("______________________________________")

#4) Escribir un programa que solicite al usuario su edad e imprima por pantalla a cuál de las
#siguientes categorías pertenece:
#● Niño/a: menor de 12 años.
#● Adolescente: mayor o igual que 12 años y menor que 18 años.
#● Adulto/a joven: mayor o igual que 18 años y menor que 30 años.
#● Adulto/a: mayor o igual que 30 años.

print ("")
edad_para_categoria = int (input ("Ingrese su edad: "))
print ("")
#Estructura condicional anidada o múltiple (if - elif - else).
if 0 < edad_para_categoria <= 11:
    print ("Categoría: Niño/a")
#Usar operadores relacionales de esta manera evita usar un operador lógico "and" y duplicidad de variable.
elif 12 <= edad_para_categoria < 18:
    print ("Categoría: Adolescente")
elif 18 <= edad_para_categoria < 30:
    print ("Categoría: Adulto/a joven")
elif 30 <= edad_para_categoria < 120:
    print ("Categoría: Adulto/a")
else:
    print ("Por favor, ingrese una edad válida")
print ("______________________________________")

#5) Escribir un programa que permita introducir contraseñas de entre 8 y 14 caracteres
#(incluyendo 8 y 14). Si el usuario ingresa una contraseña de longitud adecuada, imprimir por en
#pantalla el mensaje "Ha ingresado una contraseña correcta"; en caso contrario, imprimir por
#pantalla "Por favor, ingrese una contraseña de entre 8 y 14 caracteres". Nota: investigue el uso
#de la función len() en Python para evaluar la cantidad de elementos que tiene un iterable tal
#como una lista o un string.

print ("")
contrasena = input ("Ingrese una contraseña de entre 8 y 14 caracteres: ")
print ("")
#Función "len ()" cuenta cantidad de caracteres que almacena la variable dentro de parentesis.
cantidad_caracteres = len (contrasena)
#Usar operadores relacionales de esta manera evita usar un operador lógico "and" y duplicidad de variable.
if 8 <= cantidad_caracteres <= 14:
    print ("Ha ingresado una contraseña correcta")
else:
    print ("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")
print ("______________________________________")

#6) Escribir un programa que tome la lista
#numeros_aleatorios, calcule su moda, su mediana y su media y las compare para determinar si
#hay sesgo positivo, negativo o no hay sesgo. Imprimir el resultado por pantalla.
#Definir la lista numeros_aleatorios de la siguiente forma:
#import random
#numeros_aleatorios = [random.randint(1, 100) for i in range(50)]
#Nota: el bloque de código anterior crea una lista con 50 números entre 1 y 100 elegidos de
#forma aleatoria.

print ("")
import random
#Agregué "StatisticsError" por si hay más de una moda para que el algoritmo no se rompa.
from statistics import mode, median, mean, StatisticsError
numeros_aleatorios = [random.randint(1, 100) for i in range(50)]
mediana = median (numeros_aleatorios)
media = mean (numeros_aleatorios)
#De esta forma agarramos el error, si lo hay, y hacemos que el algoritmo siga sin problemas.
try:
    moda = mode (numeros_aleatorios)
except StatisticsError:
    moda = None
print (f"Lista 50 Números: {numeros_aleatorios}")
print ("")
print (f"Mediana: {mediana}")
print (f"Media: {media}")
print (f"Moda: {moda}")
if moda == None:
    print ("")
    print ("No se pudo calcular la moda porque hay más de una moda, lamentablemente no se pueden calcular sus sesgos")
#Si moda es igual a None (Valor nulo) no se puede calcular su sesgo.
else:
    if media > mediana > moda:
        print ("")
        print ("Sesgo Positivo. Media > Mediana > Moda")
    elif media < mediana < moda:
        print ("")
        print ("Sesgo Negativo. Media < Mediana < Moda")
    elif media == mediana == moda:
        print ("")
        print ("Sin Sesgo. Media, Mediana y Moda son iguales")
    else:
        print ("")
        print ("No cumple con los criterios de sesgo")
print ("______________________________________")