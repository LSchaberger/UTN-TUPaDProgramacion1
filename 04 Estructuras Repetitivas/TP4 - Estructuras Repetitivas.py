#Aclaración: print ("") y print ("______________________________________")
#son para mejorar visualmente la ejecución en terminal.

#1) Crea un programa que imprima en pantalla todos los números enteros desde 0 hasta 100
#(incluyendo ambos extremos), en orden creciente, mostrando un número por línea.

print ("")
# Esta constante podría no estar, pero usarla es una buena práctica y contribuye a un código más limpio.
cont = 0
for cont in range (cont,101):
    print (cont)
    #Otra buena práctica, con esto nos ahorramos de escribir duplicidad de variable: cont = cont + 1.
    cont += 1
print ("______________________________________")


#2) Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de
#dígitos que contiene.

print ("")
#Tener en cuenta que si ingresamos un 0 adelante de cualquier número al pasarse a string se pierde y no lo contará.
numero = int(input ("Ingrese un número entero: "))
digitos = len(str(abs(numero)))
print ("")
print (f"El número {numero} tiene {digitos} dígitos")
print ("______________________________________")


#3) Escribe un programa que sume todos los números enteros comprendidos entre dos valores
#dados por el usuario, excluyendo esos dos valores.

print ("")
num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))
suma = 0
#Ordena si es necesario, si ya viene ordenado pasa al for sin ejecutar el if.
if num1 > num2:
    num1, num2 = num2, num1
#"num2" no tiene -1 porque range llega siempre al anteúltimo.
for i in range (num1+1,num2):
        suma += i
print ("")
print (f"La suma de enteros entre {num1} y {num2} excluyendo ambos es: {suma}")
print ("______________________________________")


#4) Elabora un programa que permita al usuario ingresar números enteros y los sume en
#secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese
#un 0.

print ("")
suma = 0
num = 1
while num != 0:
    num = int(input("Ingrese un número entero, utilice 0 para cortar: "))
    suma = suma + num
print("")
print (f"La suma de enteros es: {suma}")
print ("______________________________________")


#5) Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el
#programa debe mostrar cuántos intentos fueron necesarios para acertar el número.

print ("")
import random
print ("Juego de Adivinanza! Adivine el número entre 0 y 9: ")
print ("")
objetivo = random.randint (0, 9)
intentos = 0
#Bucle "while" infinito.
while True:
    try:
        num = int(input("Ingrese su número: "))
    except ValueError:
        print("Debe ingresar un número entero")
        #Aunque haya error con el "continue" seguirá la secuencia sin detenerse.
        continue
    if not 0 <= num <= 9:
        print("El número debe estar entre 0 y 9")
        continue
    intentos += 1
    if num == objetivo:
        #Se corta el bucle infinito con "break".
        break
print("")
print (f"Correcto! El número es el {objetivo}, lo adivinaste en {intentos} intentos")
print ("______________________________________")


#6) Desarrolla un programa que imprima en pantalla todos los números pares comprendidos
#entre 0 y 100, en orden decreciente.

print ("")
#Se crea constantes para un código limpio y modificable en el futuro.
num1 = -1
num2 = 100
for i in range (num2, num1, -1):
    if i % 2 == 0:
        print (i)
print ("______________________________________")


#7) Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un
#número entero positivo indicado por el usuario.

print ("")
num1 = 0
suma = 0
num2 = 1
#Bucle infinito.
while 0 < num2:
    #Evitamos que se detenga por un ValueError.
    try:
        print ("")
        num2 = int((input("Ingrese un número entero positivo: ")))
        print ("")
        num2 == ValueError
        for i in range (num1, num2+1):
            suma = suma + i
        print (f"La suma entre {num1} y {num2} es: {suma}")
        #Cortamos el bucle infinito luego de la suma.
        break
    except:
        print ("")
        print ("Solo se permiten números enteros positivos, vuelva a intentarlo")
print ("______________________________________")
