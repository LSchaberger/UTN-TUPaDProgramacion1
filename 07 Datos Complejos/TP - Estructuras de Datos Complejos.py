#1) Dado el diccionario precios_frutas
#precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450}
#Añadir las siguientes frutas con sus respectivos precios:
#● Naranja = 1200
#● Manzana = 1500
#● Pera = 2300

print ("______________________________________")

precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450}

precios_frutas |= {'Naranja': 1200, 'Manzana': 1500, 'Pera': 2300}

print (precios_frutas)
print ("______________________________________")

#-----------------------------------------------

#2) Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código
#desarrollado en el punto anterior, actualizar los precios de las siguientes frutas:
#● Banana = 1330
#● Manzana = 1700
#● Melón = 2800

precios_frutas |= {'Banana': 1330, 'Manzana': 1700, 'Melón': 2800}

print (precios_frutas)
print ("______________________________________")

#-----------------------------------------------

#3) Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código
#desarrollado en el punto anterior, crear una lista que contenga únicamente las frutas sin los
#precios.

for n, lista_fruta in enumerate (precios_frutas):
    print (f"{n + 1}. {lista_fruta}")
print ("______________________________________")

#-----------------------------------------------

#4) Escribí un programa que permita almacenar y consultar números telefónicos.
#• Permití al usuario cargar 5 contactos con su nombre como clave y número como valor.
#• Luego, pedí un nombre y mostrale el número asociado, si existe.

contactos = {}  #Diccionario se inicializa vacio.
#Con maximo_contactos controlamos la cantidad de contactos a ingresar (valor modificable).
maximo_contactos = 5

#Función que valida solo el ingreso de letras. Mensaje input y mensaje error modificable.
def validacion_solo_letras_input (mensaje_input,mensaje_error):
    while True:
        texto = input(mensaje_input)

        if not texto:
            print("****\nNo ingresaste nada, volve a intentarlo****")
            continue

        if not texto.isalpha():
            print(mensaje_error)
            continue

        return texto

#Función que valida solo el ingreso de números. Mensaje input y mensaje error modificable.
def validacion_solo_numeros_input (mensaje_input, mensaje_error):
    while True:
        numeros = input(mensaje_input)

        if not numeros:
            print("****\nNo ingresaste nada, volve a intentarlo****")
            continue

        if not numeros.isdigit():
            print(mensaje_error)
            continue

        return numeros

for i in range (1, maximo_contactos + 1):

    #Usuario ingresa el nombre de contacto.
    ingreso_nombre_contacto = validacion_solo_letras_input (f"\nIngrese el nombre del contacto {i}: ",
    "\n****Caracteres inválidos, vuelva a intentarlo (solo letras)****").lower()

    #Usuario ingresa el número de teléfono.
    ingreso_numero_telefono = validacion_solo_numeros_input ("\nIngrese el número de teléfono con su característica: ",
    "\n****Número inválido, vuelva a intentarlo, solo números (sin código país +)****").strip()

    #Diccionario completo con cantidad de "maximo_contactos"
    contactos[ingreso_nombre_contacto] = int (ingreso_numero_telefono)

#Usuario ingresa nombre de contacto ya guardado para ver teléfono.
print ("\n--------------------- Busca un Contacto ---------------------")
busqueda_de_contacto = validacion_solo_letras_input ("\nIngrese un nombre de contacto guardado (exacto): ",
"\n****Caracteres inválidos, vuelva a intentarlo (solo letras)****").lower()

if busqueda_de_contacto in contactos:
    #Por estética usamos .capitalize() para mostrar el nombre.
    print (f"\n<<<Contacto {busqueda_de_contacto.capitalize()} encontrado, Teléfono: {contactos[busqueda_de_contacto]} >>>")

else:
    print ("\n****El contacto no existe****")
print ("______________________________________")

#-----------------------------------------------

#5) Solicita al usuario una frase e imprime:
#• Las palabras únicas (usando un set).
#• Un diccionario con la cantidad de veces que aparece cada palabra.

