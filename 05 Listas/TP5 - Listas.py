#1) Crear una lista con las notas de 10 estudiantes.
#• Mostrar la lista completa.
#• Calcular y mostrar el promedio.
#• Indicar la nota más alta y la más baja.

print ("")
notas = []
for i in range(1, 11):
    nota = float(input(f"Ingrese nota {i}: "))
    notas.append(nota)
print ("")
print("Notas cargadas:", notas)
print ("")
promedio = sum(notas) / len(notas)
print("Promedio:", promedio)
print("Máxima:", max(notas))
print("Mínima:", min(notas))
print ("______________________________________")


#2) Pedir al usuario que cargue 5 productos en una lista.
#• Mostrar la lista ordenada alfabéticamente. Investigue el uso del método sorted().
#• Preguntar al usuario qué producto desea eliminar y actualizar la lista.

print ("")
print("Ingresá 5 productos:")
productos = []
for i in range(1, 6):
    p = input(f"Ingrese producto {i}: ")
    productos.append(p)
#Con .sorted() se ordena alfabéticamente y con key=str.lower ignora mayúsculas y minúsculas.
productos = sorted(productos, key=str.lower)
print ("")
print("Lista ordenada:", productos)
print ("")
a_borrar = input("Producto a eliminar (exacto): ")
productos.remove(a_borrar)
print ("")
print("Lista final:", productos)
print ("______________________________________")


#3) Generar una lista con 15 números enteros al azar entre 1 y 100.
#• Crear una lista con los pares y otra con los impares.
#• Mostrar cuántos números tiene cada lista.

print ("")
import random
numeros = []
pares = []
impares = []
for i in range(15):
    numeros.append(random.randint(1, 100))
print("Lista:", numeros)
for n in numeros:
    if n % 2 == 0:
        pares.append(n)
    else:
        impares.append(n)
print ("")
print("Pares:", pares)
print("Impares:", impares)
print("Cantidad de pares:", len(pares))
print("Cantidad de impares:", len(impares))
print ("______________________________________")


#4) Dada una lista con valores repetidos:
#datos = [1, 3, 5, 3, 7, 1, 9, 5, 3]
#• Crear una nueva lista sin elementos repetidos.
#• Mostrar el resultado.

print ("")
datos = [1, 3, 5, 3, 7, 1, 9, 5, 3]
sin_repetidos = []
for x in datos:
    if x not in sin_repetidos:
        sin_repetidos.append(x)

print("Lista original:", datos)
print ("")
print("Lista sin repetidos:", sin_repetidos)
print ("______________________________________")


#5) Crear una lista con los nombres de 8 estudiantes presentes en clase.
#• Preguntar al usuario si quiere agregar un nuevo estudiante o eliminar uno existente.
#• Mostrar la lista final actualizada.

print ("")
print("Ingresá 8 nombres:")
print ("")
alumnos = []
for i in range(1, 9):
    nombre = input(f"Nombre {i}: ").strip().lower()
    alumnos.append(nombre)
    print ("")
print(f"Lista actual: {alumnos}")
print ("")
accion = input("Escribí 'agregar' o 'eliminar': ").strip().lower()
if accion == "agregar":
    nuevo = input("Nombre a agregar: ").strip().lower()
    alumnos.append(nuevo)
elif accion == "eliminar":
    print ("")
    borrar = input("Nombre a eliminar (exacto): ").strip().lower()
    alumnos.remove(borrar)
print ("")
print("Lista final:", alumnos)
print ("______________________________________")
