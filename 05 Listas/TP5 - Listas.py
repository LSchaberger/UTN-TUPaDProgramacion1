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


#6) Dada una lista con 7 números, rotar todos los elementos una posición hacia la derecha (el
#último pasa a ser el primero).

print("")
print("Ingresá 7 números:")
print ("")
lista1 = []
for i in range(1, 8):
    lista1.append(float(input(f"Valor {i}: ")))
rotada = [lista1[-1]] + lista1[:-1]
print ("")
print("Lista original:", lista1)
print("Lista rotada:", rotada)
print ("______________________________________")


#7) Crear una matriz (lista anidada) de 7x2 con las temperaturas mínimas y máximas de una
#semana.
#• Calcular el promedio de las mínimas y el de las máximas.
#• Mostrar en qué día se registró la mayor amplitud térmica.

print ("")
dias = ["Lunes","Martes","Miércoles","Jueves","Viernes","Sábado","Domingo"]
matriz = []
#Cada fila [min, max]
for i in range(7):
    tmin = float(input(f"{dias[i]} - mínima: "))
    tmax = float(input(f"{dias[i]} - máxima: "))
    print ("")
    matriz.append([tmin, tmax])
suma_min = 0.0
suma_max = 0.0
for i in range(7):
    suma_min += matriz[i][0]
    suma_max += matriz[i][1]
prom_min = suma_min / 7
prom_max = suma_max / 7
print("Promedio mínimas:", prom_min)
print("Promedio máximas:", prom_max)
#Día con mayor amplitud
idx = 0
max_amp = matriz[0][1] - matriz[0][0]
for i in range(1, 7):
    amp = matriz[i][1] - matriz[i][0]
    if amp > max_amp:
        max_amp = amp
        idx = i
print("Mayor amplitud:", dias[idx], "(", max_amp, ")")
print ("______________________________________")


#8) Crear una matriz con las notas de 5 estudiantes en 3 materias.
#• Mostrar el promedio de cada estudiante.
#• Mostrar el promedio de cada materia.

print ("")
filas = 5
cols = 3
notas = []
print("Ingresá 3 notas (0 al 10) por estudiante de 3 materias diferentes:")
print ("")
print ("")
for f in range(filas):
    fila = []
    for c in range(cols):
        v = float(input(f"Estudiante {f+1}, Materia {c+1}: "))
        print ("")
        fila.append(v)
    notas.append(fila)
print ("")
print("Promedio por estudiante:")
print ("")
for f in range(filas):
    s = 0.0
    for c in range(cols):
        s += notas[f][c]
    print(f"Estudiante {f+1}: {s/cols}")
print ("")
print("Promedio por materia:")
print ("")
for c in range(cols):
    s = 0.0
    for f in range(filas):
        s += notas[f][c]
    print(f"Materia {c+1}: {s/filas}")
print ("______________________________________")


#9) Representar un tablero de Ta-Te-Ti como una lista de listas (3x3).
#• Inicializarlo con guiones "-" representando casillas vacías.
#• Permitir que dos jugadores ingresen posiciones (fila, columna) para colocar "X" o "O".
#• Mostrar el tablero después de cada jugada.

print ("")
tablero = [["-","-","-"],["-","-","-"],["-","-","-"]]
jugador = "X"
jugadas = 0
while True:
    print("Tablero:")
    for fila in tablero:
        print(" ".join(fila))
    fila = int(input(f"Turno de {jugador} - fila (1-3): "))
    col  = int(input(f"Turno de {jugador} - col  (1-3): "))
    tablero[fila-1][col-1] = jugador
    jugadas += 1
    gano = False
    for i in range(3):
        if tablero[i][0]==jugador and tablero[i][1]==jugador and tablero[i][2]==jugador:
            gano = True
        if tablero[0][i]==jugador and tablero[1][i]==jugador and tablero[2][i]==jugador:
            gano = True
    if (tablero[0][0]==jugador and tablero[1][1]==jugador and tablero[2][2]==jugador) or \
       (tablero[0][2]==jugador and tablero[1][1]==jugador and tablero[2][0]==jugador):
        gano = True
    if gano:
        print("Tablero final:")
        for fila_print in tablero:
            print(" ".join(fila_print))
        print ("")
        print(f"¡Ganó {jugador}!")
        break
    if jugadas == 9:
        print ("")
        print("¡Empate!")
        break
    jugador = "O" if jugador == "X" else "X"
print ("______________________________________")


#10) Una tienda registra las ventas de 4 productos durante 7 días, en una matriz de 4x7.
#• Mostrar el total vendido por cada producto.
#• Mostrar el día con mayores ventas totales.
#• Indicar cuál fue el producto más vendido en la semana.

print ("")
cantidad_productos = 4
cantidad_dias = 7
ventas_semana = []
print("Ingresá ventas de 4 productos x 7 días:")
for indice_producto in range(cantidad_productos):
    print ("")
    ventas_producto = []
    for indice_dia in range(cantidad_dias):
        print ("")
        monto_venta = float(input(f"Producto {indice_producto+1}, Día {indice_dia+1}: "))
        ventas_producto.append(monto_venta)
    ventas_semana.append(ventas_producto)
print ("")
print ("")
print("Total por producto:")
print ("")
totales_por_producto = []
for indice_producto in range(cantidad_productos):
    total_producto = 0.0
    for indice_dia in range(cantidad_dias):
        total_producto += ventas_semana[indice_producto][indice_dia]
    totales_por_producto.append(total_producto)
    print(f"Producto {indice_producto+1}: {total_producto}")
totales_por_dia = []
for indice_dia in range(cantidad_dias):
    total_dia = 0.0
    for indice_producto in range(cantidad_productos):
        total_dia += ventas_semana[indice_producto][indice_dia]
    totales_por_dia.append(total_dia)
indice_mejor_dia = 0
for indice_dia in range(1, cantidad_dias):
    if totales_por_dia[indice_dia] > totales_por_dia[indice_mejor_dia]:
        indice_mejor_dia = indice_dia
print ("")
print("Día con mayores ventas totales: Día", indice_mejor_dia+1, "(total", totales_por_dia[indice_mejor_dia], ")")
indice_producto_top = 0
for indice_producto in range(1, cantidad_productos):
    if totales_por_producto[indice_producto] > totales_por_producto[indice_producto_top]:
        indice_producto_top = indice_producto
print("Producto más vendido en la semana: Producto", indice_producto_top+1, "(total", totales_por_producto[indice_producto_top], ")")
print ("______________________________________")
