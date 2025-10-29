print ("______________________________________")
#1. Crear archivo inicial con productos: Crear un archivo de texto llamado
#productos.txt con tres productos. Cada línea debe tener: nombre,precio,cantidad
import os

#Con esta función nos aseguramos que no reescriba siempre el archivo cada vez que ingresamos.
if not os.path.exists("productos.txt"):

#Encoding="utf-8" para que funcione de manera universal en linux, windows y mac.
#algunos caracteres del .txt con tilde "é" en windows no serían interpretados sin encoding.
    with open ("productos.txt", "w", encoding="utf-8") as archivo:

        archivo.write("NOMBRE,PRECIO,CANTIDAD\n")
        archivo.write("Agua Mineral,900,12\n")
        archivo.write("Yerba Mate,2500,5\n")
        archivo.write("Masitas Saladas,2200,3\n")

print ("<<< Archivo productos.txt creado exitosamente >>>")
print ("<<< 3 prodúctos almacenados >>>")
print ("______________________________________")

#-----------------------------------------------

#2. Leer y mostrar productos: Crear un programa que abra productos.txt, lea cada
#línea, la procese con .strip() y .split(","), y muestre los productos en el siguiente formato:
#Producto: Lapicera | Precio: $120.5 | Cantidad: 30

with open ("productos.txt", "r", encoding="utf-8") as archivo:

    #Saltamos el encabezado para que no aparezca en el ciclo for.
    next(archivo)

    for linea in archivo:

        linea = linea.strip()
        datos = linea.split(",")
        nombre, precio, cantidad = datos

        print (f"Producto: {nombre.title():<15} | Precio: ${precio:<8} | Cantidad: {cantidad}")
print ("______________________________________")

#-----------------------------------------------

#3. Agregar productos desde teclado: Modificar el programa para que luego de mostrar
#los productos, le pida al usuario que ingrese un nuevo producto (nombre, precio,
#cantidad) y lo agregue al archivo sin borrar el contenido existente.

#Función que valida el ingreso de letras solamente. Mensaje input y mensaje error modificable.
def validacion_solo_letras_input (mensaje_input,mensaje_error):
    while True:
        texto = input(mensaje_input).strip().title()

        #Elimina espacios duplicados entre palabras.
        texto = " ".join(texto.split())

        if not texto:
            print("\n****No ingresaste nada, volve a intentarlo****")
            continue

        if not texto.replace(" ", "").isalpha():
            print(mensaje_error)
            continue

        return texto
    
#Valida el ingreso de números enteros o decimales solamente. Mensaje input y mensaje error modificable.
def validacion_numeros_decimales_o_enteros (mensaje_input, mensaje_error):
    while True:
        numeros = input(mensaje_input).strip()

        numeros = numeros.replace (",", ".")

        try:
            numeros = float(numeros)
        except ValueError:
            print(mensaje_error)
            continue

        if not numeros:
            print("****\nNo ingresaste nada, volve a intentarlo****")
            continue

        if numeros.is_integer():
            return str(int(numeros))  #Borra el .0
        else:
            return str(numeros)  #Mantiene los decimales reales.

#Valida el ingreso solamente de numeros enteros.
def validacion_solo_numeros_enteros (mensaje_input, mensaje_error):
    while True:
        numeros = input(mensaje_input).strip()

        if not numeros:
            print("****\nNo ingresaste nada, volve a intentarlo****")
            continue

        if not numeros.isdigit():
            print(mensaje_error)
            continue

        return numeros

print ("\n--------------Ingrese un nuevo producto--------------")

nombre_nuevo_producto = validacion_solo_letras_input("\nNuevo producto: ",
"\n****Caracteres inválidos, vuelva a intentarlo (solo letras)****")

with open("productos.txt", "r", encoding="utf-8") as archivo_lectura:
    contenido = archivo_lectura.read().title()

    #Escribe en la lista el nuevo producto solo si no existe.
    if nombre_nuevo_producto in contenido:
        print ("\n****El producto ingresado ya existe, ingrese otro o actualice sus cantidades****")
    else:
        precio_nuevo_producto = validacion_numeros_decimales_o_enteros ("\nPrecio $: ",
        "\n****Caracteres inválidos (solo números enteros o decimales)****")

        cantidad_nuevo_producto = validacion_solo_numeros_enteros ("\nCantidad unidades: ",
        "\n****Caracteres inválidos (solo números enteros)****")

        with open ("productos.txt", "a", encoding="utf-8") as archivo:
            
            archivo.write(f"{nombre_nuevo_producto},{precio_nuevo_producto},{cantidad_nuevo_producto}\n")
            print ("\n<<< Producto ingresado con éxito >>>")
            print (f"\nProducto: {nombre_nuevo_producto:<15} | Precio: ${precio_nuevo_producto:<8} | Cantidad: {cantidad_nuevo_producto}\n")
print ("______________________________________")

#-----------------------------------------------

#4. Cargar productos en una lista de diccionarios: Al leer el archivo, cargar los datos en
#una lista llamada productos, donde cada elemento sea un diccionario con claves:
#nombre, precio, cantidad.

productos = []

with open ("productos.txt", "r", encoding="utf-8") as dic_productos:

    #Salta el encabezado.
    next(dic_productos)

    for linea_dic in dic_productos:
        linea_dic = linea_dic.strip()
        datos_dic = linea_dic.split(",")

        #Si esto se activa es porque desapareció una categoría o borraron un coma (,) separadora.
        while len(datos_dic) < 3:
            datos_dic.append("Falta categoría o separador (,) (Eliminado desde archivo base .txt)")

        #Si esto se activa borraron un dato entre coma y coma de una categoría desde el archivo base.
        datos_dic = [dato if dato.strip() else 
                    "Falta Dato (Eliminado desde archivo base .txt)" for dato in datos_dic]

        #Desempaqueta los 3 datos y los asigna a cada variable.
        nombre_dic, precio_dic, cantidad_dic = datos_dic

        producto = {"Nombre": nombre_dic.strip().title(),"Precio": precio_dic.strip(),
            "Cantidad": cantidad_dic.strip()}

        productos.append(producto)

for p in productos:
    print(f"Producto: {p["Nombre"]:<15} | Precio: ${p["Precio"]:<8} | Cantidad: {p["Cantidad"]}")
print ("______________________________________")

#-----------------------------------------------

#5. Buscar producto por nombre: Pedir al usuario que ingrese el nombre de un
#producto. Recorrer la lista de productos y, si lo encuentra, mostrar todos sus datos. Si
#no existe, mostrar un mensaje de error.
    
print ("\n-----------Buscador de Productos-----------\n")
producto_a_buscar = validacion_solo_letras_input ("\nIngrese el nombre de un producto: ",
                    "\n****Caracteres inválidos, vuelva a intentarlo (solo letras)****")

#Se usa como bandera.
encontrado = False

for bd in productos:
    if bd["Nombre"] == producto_a_buscar:
        print (f"\n<<< Producto encontrado: {bd["Nombre"]} | Precio: {bd["Precio"]} | Cantidad: {bd["Cantidad"]} >>>")

        encontrado = True
        break

if not encontrado:
    print ("\n****Producto no encontrado****")
print ("______________________________________")

#-----------------------------------------------

#6. Guardar los productos actualizados: Después de haber leído, buscado o agregado
#productos, sobrescribir el archivo productos.txt escribiendo nuevamente todos los
#productos actualizados desde la lista.

with open("productos.txt", "w", encoding="utf-8") as archivo_actualizado:

    #Se escribe nuevamente el encabezado.
    archivo_actualizado.write("NOMBRE,PRECIO,CANTIDAD\n")

    #Recorremos la lista de diccionarios y escribimos cada producto.
    for p in productos:
        archivo_actualizado.write(f"{p['Nombre']},{p['Precio']},{p['Cantidad']}\n")

print("\n<<< Archivo productos.txt actualizado correctamente >>>")
print("______________________________________")
