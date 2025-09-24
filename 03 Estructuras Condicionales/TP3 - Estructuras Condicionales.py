#Aclaración antes de comenzar:
#print ("______________________________________")
#print ("")
#Usaré esos dos print en todos los algorítmos para mejorar la estética al ejecutarlos en terminal.


#Actividades:

#1) Escribir un programa que solicite la edad del usuario. Si el usuario es mayor de 18 años,
#deberá mostrar un mensaje en pantalla que diga “Es mayor de edad”.

print ("______________________________________")
print ("")
edad_usuario = int (input("Ingrese su edad: "))
print ("")
if edad_usuario >= 18:
    print ("Es mayor de edad")
else:
    #"pass" para que el algoritmo acabe sin hacer nada.
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
else:
    print ("")
    if media > mediana > moda:
        print ("Sesgo Positivo. Media > Mediana > Moda")
    elif media < mediana < moda:
        print ("Sesgo Negativo. Media < Mediana < Moda")
    elif media == mediana == moda:
        print ("Sin Sesgo. Media, Mediana y Moda son iguales")
    else:
        print ("No cumple con los criterios de sesgo")
print ("______________________________________")


#7) Escribir un programa que solicite una frase o palabra al usuario. Si el string ingresado
#termina con vocal, añadir un signo de exclamación al final e imprimir el string resultante por
#pantalla; en caso contrario, dejar el string tal cual lo ingresó el usuario e imprimirlo por
#pantalla.

print ("")
frase = input ("Ingrese una frase: ")
vocales = "aeiouáéíóúAEIOUÁÉÍÓÚ"
#Conjunción "frase" and "frase[-1], primero evalúa si el usuario ingresó texto o está vacío y luego con frase[-1] evalúa la última letra"
if frase and frase[-1] in vocales:
    print ("")
    print (f"{frase}!")
else:
    print ("")
    print (frase)
print ("______________________________________")
    

#8) Escribir un programa que solicite al usuario que ingrese su nombre y el número 1, 2 o 3
#dependiendo de la opción que desee:
#1. Si quiere su nombre en mayúsculas. Por ejemplo: PEDRO.
#2. Si quiere su nombre en minúsculas. Por ejemplo: pedro.
#3. Si quiere su nombre con la primera letra mayúscula. Por ejemplo: Pedro.
#El programa debe transformar el nombre ingresado de acuerdo a la opción seleccionada por el
#usuario e imprimir el resultado por pantalla. Nota: investigue uso de las funciones upper(),
#lower() y title() de Python para convertir entre mayúsculas y minúsculas.

print ("")
nombre_usuario = input ("Ingrese su nombre: ")
print ("")
print ("""
1. Si quiere su nombre en mayúsculas. Por ejemplo: PEDRO.
2. Si quiere su nombre en minúsculas. Por ejemplo: pedro.
3. Si quiere su nombre con la primera letra mayúscula. Por ejemplo: Pedro.""")
print ("")
opcion = int (input("Ingrese una opción: "))
print ("")
if opcion == 1:
    print (nombre_usuario.upper())
elif opcion == 2:
    print (nombre_usuario.lower())
elif opcion == 3:
    print (nombre_usuario.title())
else:
    print ("Opción ingresada incorrecta, vuelva a intentarlo")
print ("______________________________________")


#9) Escribir un programa que pida al usuario la magnitud de un terremoto, clasifique la
#magnitud en una de las siguientes categorías según la escala de Richter e imprima el resultado
#por pantalla:
#● Menor que 3: "Muy leve" (imperceptible).
#● Mayor o igual que 3 y menor que 4: "Leve" (ligeramente perceptible).
#● Mayor o igual que 4 y menor que 5: "Moderado" (sentido por personas, pero
#generalmente no causa daños).
#● Mayor o igual que 5 y menor que 6: "Fuerte" (puede causar daños en estructuras
#débiles).
#● Mayor o igual que 6 y menor que 7: "Muy Fuerte" (puede causar daños significativos).
#● Mayor o igual que 7: "Extremo" (puede causar graves daños a gran escala).

print ("")
#"float" para que lea números decimales.
magnitud_terremoto = float (input("Ingrese la magnitud del terremoto: "))
print ("")
if magnitud_terremoto < 3:
    print ("Muy leve (imperceptible)")
elif 3 <= magnitud_terremoto < 4:
    print ("Leve (ligeramente perceptible)")
elif 4 <= magnitud_terremoto < 5:
    print ("Moderado (sentido por personas, pero generalmente no causa daños)")
elif 5 <= magnitud_terremoto < 6:
    print ("Fuerte (puede causar daños en estructuras débiles)")
elif 6 <= magnitud_terremoto < 7:
    print ("Muy Fuerte (puede causar daños significativos)")
elif magnitud_terremoto >= 7:
    print ("Extremo (puede causar graves daños a gran escala)")
else:
    print ("Magnitud incorrecta en escala Richter, vuelva a intentarlo")
print ("______________________________________")

#10) Escribir un programa que pregunte al usuario en cuál hemisferio se encuentra (N/S), qué mes
#del año es y qué día es. El programa deberá utilizar esa información para imprimir por pantalla
#si el usuario se encuentra en otoño, invierno, primavera o verano.

print ("")
#".strip()" eliminamos espacios vacios si los hay y ".lower() para normalizar a minúsculas"
hemisferio = input ("Ingrese la primera letra del hemisferio donde se encuentra N/S: ").strip().lower()
print ("")
#El mes se almacena como string, la idea es luego eliminar el 0 a la izquierda, si lo hay, para evitar errores.
mes = (input ("Ingrese el mes del año (1 - 12): "))
#El mes se convierte a entero y elimina automáticamente el 0 delante de cualquier número, ej: 01, queda 1.
mes = int (mes)
print ("")
dia = (input ("Ingrese el día del mes (1 - 31): "))
dia = int (dia)
print ("")
if hemisferio == "n":
    if (mes == 12 and dia >= 21) or mes == 1 or mes == 2 or (mes == 3 and dia <= 20):
        print ("Te encontras en invierno")
    elif (mes == 3 and dia >= 21) or mes == 4 or mes == 5 or (mes == 6 and dia <= 20):
        print ("Te encontras en primavera")
    elif (mes == 6 and dia >= 21) or mes == 7 or mes == 8 or (mes == 9 and dia <= 20):
        print ("Te encontras en verano")
    elif (mes == 9 and dia >= 21) or mes == 10 or mes == 11 or (mes == 12 and dia <= 20):
        print ("Te encontras en otoño")
    else:
        print ("Datos ingresados incorrectos, vuelva a intentarlo")
else:
    if hemisferio == "s":
        if (mes == 12 and dia >= 21) or mes == 1 or mes == 2 or (mes == 3 and dia <= 20):
            print ("Te encontras en verano")
        elif (mes == 3 and dia >= 21) or mes == 4 or mes == 5 or (mes == 6 and dia <= 20):
            print ("Te encontras en otoño")
        elif (mes == 6 and dia >= 21) or mes == 7 or mes == 8 or (mes == 9 and dia <= 20):
            print ("Te encontras en invierno")
        elif (mes == 9 and dia >= 21) or mes == 10 or mes == 11 or (mes == 12 and dia <= 20):
            print ("Te encontras en primavera")
        else:
            print ("Datos ingresados incorrectos, vuelva a intentarlo")
print ("______________________________________")
