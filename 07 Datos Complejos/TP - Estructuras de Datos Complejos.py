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
        texto = input(mensaje_input).strip().lower()

        if not texto:
            print("\n****No ingresaste nada, volve a intentarlo****")
            continue

        if not texto.replace(" ", "").isalpha():
            print(mensaje_error)
            continue

        return texto

#Función que valida solo el ingreso de números. Mensaje input y mensaje error modificable.
def validacion_solo_numeros_input (mensaje_input, mensaje_error):
    while True:
        numeros = input(mensaje_input).strip()

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
    "\n****Caracteres inválidos, vuelva a intentarlo (solo letras)****")

    #Usuario ingresa el número de teléfono.
    ingreso_numero_telefono = validacion_solo_numeros_input ("\nIngrese el número de teléfono con su característica: ",
    "\n****Número inválido, vuelva a intentarlo, solo números (sin código país +)****")

    #Diccionario completo con cantidad de "maximo_contactos"
    contactos[ingreso_nombre_contacto] = int (ingreso_numero_telefono)

#Usuario ingresa nombre de contacto ya guardado para ver teléfono.
print ("\n--------------------- Busca un Contacto ---------------------")
busqueda_de_contacto = validacion_solo_letras_input ("\nIngrese un nombre de contacto guardado (exacto): ",
"\n****Caracteres inválidos, vuelva a intentarlo (solo letras)****")

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

import re

palabras_unicas = set()
recuento = {}

#Función con mensaje input y mensaje error modificables.
#Acepta letras (con tildes y ñ), espacios, comas, puntos, !, ?, ¡, ¿, :, '
def validacion_input_frase_normal_letras_y_algunos_caracteres (mensaje_input,mensaje_error):
    patron = r"^[a-zA-ZáéíóúüñÁÉÍÓÚÜÑ\s.,!?¡¿:']+$"
    while True:
        frase = input(mensaje_input).strip().lower()

        if not frase:
            print("****\nNo ingresaste nada, volve a intentarlo****")
            continue

        #Cuando el caracter ingresado no pertenece a la variable "patron".
        if not re.fullmatch(patron, frase):
            print(mensaje_error)
            continue

        return frase

frase_ingresada_usuario = validacion_input_frase_normal_letras_y_algunos_caracteres ("Ingrese una frase (separa con espacios): ",
"\n****Caracteres inválidos, vuelva a intentarlo (sin números)****")

#Borramos los caracteres que ingresó el usuario para evitar errores.
frase_limpia = re.sub (r"[.,!?¡¿:']", "", frase_ingresada_usuario)

#Separamos cada palabra leyendo uno o más espacios entre palabras.
separa_palabras = re.split (r"\s+", frase_limpia)

#Agrega las palabras al set().
for palabra in separa_palabras:
    palabras_unicas.add (palabra)

#Cuenta palabras repetidas y las agrega al diccionario "recuento{}"
for palabra_repetida in separa_palabras:
    if palabra_repetida in recuento:
        recuento[palabra_repetida] += 1
    else:
        recuento[palabra_repetida] = 1

print (f"\n{palabras_unicas}")
print (f"\n{recuento}")
print ("______________________________________")

#-----------------------------------------------

#6) Permití ingresar los nombres de 3 alumnos, y para cada uno una tupla de 3 notas.
#Luego, mostrá el promedio de cada alumno.

cantidad_alumnos = 3  #Valor de alumnos modificable.
cantidad_notas = 3  #Valor de notas modificable.
alumnos = {}  #Diccionario vacío para 'alumno': (tupla de "cantidad_notas" notas).
notas = []  #Lista temporal que será convertida a tupla.

#Ingresar como str "de_n", "hasta_m".
def validacion_input_solo_numeros_n_al_m_incluyendolos (mensaje_input, mensaje_error_no_es_numero,
de_n, hasta_m, mensaje_error_de_rango):
    while True:
        numeros = input(mensaje_input).strip()

        if not numeros:
            print("****\nNo ingresaste nada, volve a intentarlo****")
            continue

        numeros = numeros.replace (",", ".")

        try:
            numeros = float(numeros)
        except ValueError:
            print(mensaje_error_no_es_numero)
            continue

            #Los números del rango a ingresar tendrán que ser como int. (sino no funciona).
        if not de_n <= numeros <= hasta_m:
            print (mensaje_error_de_rango)
            continue

        return numeros
    
for ca in range (1, cantidad_alumnos + 1):
    ingreso_nombre_alumnos = validacion_solo_letras_input (f"\nIngrese nombre alumno {ca}: ",
    "\n****Caracteres inválidos, vuelva a intentarlo (solo letras)****")
    
    for cn in range (1, cantidad_notas + 1):
        ingreso_notas = validacion_input_solo_numeros_n_al_m_incluyendolos (f"\nIngrese nota {cn}°: ",
    "\n****Caracteres inválidos, vuelva a intentarlo (solo números)****", 0, 10, 
    "\n****Rango nota inválido, de 0 a 10, vuelva a intentarlo****")
        notas.append(ingreso_notas)
        
    alumnos[ingreso_nombre_alumnos] = tuple (notas)

print ("\n--------------------- Promedio Alumnos ---------------------")
for nombre, notas in alumnos.items():
    promedio = sum(notas) / len (notas)
    print (f"\n{nombre.title()}: {promedio:.2f}")
print ("______________________________________")

#-----------------------------------------------

#7) Dado dos sets de números, representando dos listas de estudiantes que aprobaron Parcial 1
#y Parcial 2:
#•Mostrá los que aprobaron ambos parciales.
#•Mostrá los que aprobaron solo uno de los dos.
#•Mostrá la lista total de estudiantes que aprobaron al menos un parcial (sin repetir).

#Los números dentro de cada set son las matrículas de cada alumno.
parcial_1_aprobado = {1000, 1095, 1010, 1200, 1500, 1350, 1005, 1201, 1325, 2525}
parcial_2_aprobado = {1095, 1200, 1350, 2525, 1005, 1325, 1010}

#Usé intersección.
aprobaron_ambos = parcial_1_aprobado & parcial_2_aprobado
print (f"Estudiantes que aprobaron ambos: {aprobaron_ambos}")

#Diferencia simétrica.
aprobaron_solo_uno = parcial_1_aprobado ^ parcial_2_aprobado
print (f"\nEstudiantes que aprobaron solo uno: {aprobaron_solo_uno}")

#Unión, sin repetir.
aprobaron_al_menos_uno = parcial_1_aprobado | parcial_2_aprobado
print (f"\nEstudiantes que aprobaron al menos uno: {aprobaron_al_menos_uno}")
print ("______________________________________")

#-----------------------------------------------

#8) Armá un diccionario donde las claves sean nombres de productos y los valores su stock.
#Permití al usuario:
#•Consultar el stock de un producto ingresado.
#•Agregar unidades al stock si el producto ya existe.
#•Agregar un nuevo producto si no existe.

diccionario_de_productos = {} #Claves = productos, Valores = stock.
menu = ["1. Consultar stock de un producto",
        "2. Agregar unidades al stock (si el producto ya existe)",
        "3. Agregar un nuevo producto (si no existe)",
        "4. Salir"]

while True:

    while True:
        print ("\n\n-----------------------MENU-----------------------")
        for m in menu:
            print (m)

        opcion = validacion_input_solo_numeros_n_al_m_incluyendolos ("\nIngrese una opción: ",
        "\n****Caracteres inválidos, vuelva a intentarlo (solo números)****", 1, 4, 
        "\n****Opción inválida, vuelva a intentarlo****")

        #La función reutilizable que usa "opcion" acepta float, y con esto se corrige.
        if isinstance(opcion, float) and not opcion.is_integer():
            print("\n\n****Opción inválida, vuelva a intentarlo****")
            continue

        match opcion:

            case 1:

                if not diccionario_de_productos:
                    print ("\n\n****Para consultar un stock primero tiene que ingresar prodúctos****")
                    continue

                nombre_producto = validacion_solo_letras_input ("\nIngrese nombre del producto a consultar: ",
                "\n****Caracteres inválidos, vuelva a intentarlo (solo letras)****")

                if nombre_producto in diccionario_de_productos:
                    print (f"\n\n<<< Stock de {nombre_producto.title()}: {diccionario_de_productos[nombre_producto]} unidades >>>")
                    continue
                else:
                    print ("\n\n****El producto no existe****")
                    continue
            case 2:

                if not diccionario_de_productos:
                    print ("\n\n****Aún no hay productos, para agregar stock primero debe ingresar productos con opción 3.****")
                    continue

                agrega_unidades = validacion_solo_letras_input ("\nIngrese nombre del producto (exacto) para agregar unidades: ",
                "\n****Caracteres inválidos, vuelva a intentarlo (solo letras)****")

                if agrega_unidades in diccionario_de_productos:
                    cantidad_stock = validacion_solo_numeros_input ("\nAgregue la cantidad de unidades: ",
                    "\n****Número inválido, vuelva a intentarlo****")

                    diccionario_de_productos[agrega_unidades] += int (cantidad_stock)
                    print (f"\n\n<<< Stock actualizado. {agrega_unidades.title()} tiene {diccionario_de_productos[agrega_unidades]} unidades >>>")
                    continue
                else:
                    print ("\n\n****Ese producto no existe****")
                    continue
            case 3:

                nuevo_producto = validacion_solo_letras_input ("\nIngrese nombre del nuevo producto: ",
                "\n****Caracteres inválidos, vuelva a intentarlo (solo letras)****")

                if nuevo_producto not in diccionario_de_productos:
                    stock_nuevo_producto = validacion_solo_numeros_input ("\nAgregue la cantidad de unidades: ",
                    "\n****Número inválido, vuelva a intentarlo****")

                    diccionario_de_productos[nuevo_producto] = int (stock_nuevo_producto)
                    print (f"\n\n<<< Producto: {nuevo_producto.title()} y Stock: {diccionario_de_productos[nuevo_producto]} agregado con éxito >>>")
                    continue
                else:
                    print ("\n\n****Ese producto ya existe, agregue unidades con opción 2.****")
                    continue
            case 4:

                print ("\n<<< Nos vemos pronto >>>")
                break
    break
print ("______________________________________")

#-----------------------------------------------

#9) Creá una agenda donde las claves sean tuplas de (día, hora) y los valores sean eventos.
#Permití consultar qué actividad hay en cierto día y hora.

agenda = {('lunes', '10:00'): 'Turno Carnet', ('martes', '06:00'): 'Trabajar',
('miércoles', '17:00'): 'Comprar comida', ('jueves', '09:00'): 'Parcial Programación'}

consulta_agenda = validacion_solo_letras_input ("\nIngrese un día de la semana: ",
                "\n****Caracteres inválidos, vuelva a intentarlo (solo letras)****")

for (dia, hora), actividad in agenda.items():
    if dia == consulta_agenda:
        print (f"\n<<< {dia.capitalize()}: {hora}hs = {actividad} >>>")
        break
else:
    print ("\nNo hay actividades ese día")
print ("______________________________________")

#-----------------------------------------------

#10) Dado un diccionario que mapea nombres de países con sus capitales, construí un nuevo
#diccionario donde:
#•Las capitales sean las claves.
#•Los países sean los valores.

original = {'argentina': 'buenos aires', 'brasil': 'brasilia',
            'chile': 'santiago', 'uruguay': 'montevideo'}
invertido = {}

for pais, capital in original.items():
    invertido[capital] = pais

print (invertido)
print ("______________________________________")
