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

for i in range (1, maximo_contactos + 1):

    #Bucle infinito hasta que ingrese datos correctos.
    while True:
        nombre_contacto = input (f"\nIngrese el nombre del contacto {i}: ").lower()

        if not nombre_contacto.isalpha():
            print ("\n****Caracteres inválidos, vuelva a intentarlo (solo letras)****")
            continue
        else:
            break

    while True:
        numero_telefono = input ("\nIngrese el número de teléfono con su característica: ").strip()

        if not numero_telefono.isdigit():
            print ("\n****Número inválido, vuelva a intentarlo, solo números (sin código país +)****")
            continue
        else:
            break

    #Diccionario completo con cantidad "maximo_contactos"    
    contactos[nombre_contacto] = int (numero_telefono)

while True:
        print ("\n--------------------- Busca un Contacto ---------------------")
        busqueda_de_contacto = input ("\nIngrese un nombre de contacto guardado (exacto): ").lower()

        if not busqueda_de_contacto.isalpha():
            print ("\n****Caracteres inválidos, vuelva a intentarlo (solo letras)****")
            continue
        else:
            break

if busqueda_de_contacto in contactos:
    #Por estética usamos .capitalize() para mostrar el nombre.
    print (f"\n<<<Contacto {busqueda_de_contacto.capitalize()} encontrado, Teléfono: {contactos[busqueda_de_contacto]} >>>")

else:
    print ("\n****El contacto no existe****")
print ("______________________________________")
