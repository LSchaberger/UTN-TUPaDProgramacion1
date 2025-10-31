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

def validacion_solo_letras_input(mensaje_input, mensaje_error):
    while True:
        texto = input(mensaje_input).strip().title()

        #Elimina espacios duplicados entre palabras.
        texto = " ".join(texto.split())

        if not texto:
            print("\n****No ingresaste nada, volvé a intentarlo****")
            continue

        if not texto.replace(" ", "").isalpha():
            print(mensaje_error)
            continue

        return texto
    
#1) Crea una función recursiva que calcule el factorial de un número. Luego, utiliza esa
#función para calcular y mostrar en pantalla el factorial de todos los números enteros
#entre 1 y el número que indique el usuario.
print("______________________________________")

def factorial(n):
    if n == 0 or n == 1:  #Caso base.
        return 1
    else:                 #Caso recursivo.
        return n * factorial(n - 1)

numero = int(validacion_solo_numeros_enteros("\nIngrese un número entero positivo: ",
    "\n****Error: Solo se permiten números enteros positivos****"))

print(f"\nFactoriales desde 1 hasta {numero}:\n")

for i in range(1, numero + 1):
    print(f"{i}! = {factorial(i)}")
print("______________________________________")

#-----------------------------------------------

#2) Crea una función recursiva que calcule el valor de la serie de Fibonacci en la posición
#indicada. Posteriormente, muestra la serie completa hasta la posición que el usuario
#especifique.

# Función recursiva que calcula el número de fibonacci en la posición n
def fibonacci(n):
    if n == 0:     #Caso base 1.
        return 0
    elif n == 1:   #Caso base 2.
        return 1
    else:          #Caso recursivo.
        return fibonacci(n - 1) + fibonacci(n - 2)

numero = int(validacion_solo_numeros_enteros("\nIngrese la posición hasta donde quiere ver la serie de Fibonacci: ",
    "\n****Error: Solo se permiten números enteros positivos****"))

print(f"\nSerie de Fibonacci hasta la posición {numero}:\n")

for i in range(numero + 1):
    print(f"Pos {i} = {fibonacci(i)}")
print("______________________________________")

#-----------------------------------------------

#3) Crea una función recursiva que calcule la potencia de un número base elevado a un
#exponente, utilizando la fórmula 𝑛𝑚 = 𝑛 ∗ 𝑛(𝑚−1). Prueba esta función en un
#algoritmo general.

def potencia(base, exponente):
    if exponente == 0:      #Caso base.
        return 1
    else:                   #Caso recursivo.
        return base * potencia(base, exponente - 1)

base = int(validacion_solo_numeros_enteros("\nIngrese la base: ",
    "\n****Error: Solo se permiten números enteros positivos****"))

exponente = int(validacion_solo_numeros_enteros("Ingrese el exponente: ",
    "\n****Error: Solo se permiten números enteros positivos****"))

resultado = potencia(base, exponente)

print(f"\nResultado: {base} elevado a la {exponente} = {resultado}")
print("______________________________________")

#-----------------------------------------------

#4) Crear una función recursiva en Python que reciba un número entero positivo en base
#decimal y devuelva su representación en binario como una cadena de texto.

def decimal_a_binario(n):
    if n == 0:                    #Caso base 1.
        return "0"
    elif n == 1:                  #Caso base 2.
        return "1"
    else:
        #Caso recursivo: divide por 2 y concatena el resto.
        return decimal_a_binario(n // 2) + str(n % 2)

numero = int(validacion_solo_numeros_enteros("\nIngrese un número entero positivo en base decimal: ",
    "\n****Error: Solo se permiten números enteros positivos****"))

binario = decimal_a_binario(numero)

print(f"\nEl número {numero} en binario es: {binario}")
print("______________________________________")

#-----------------------------------------------

#5) Implementá una función recursiva llamada es_palindromo(palabra) que reciba una
#cadena de texto sin espacios ni tildes, y devuelva True si es un palíndromo o False si no
#lo es.

def es_palindromo(palabra):
    #Elimina espacios y pasa todo a minúsculas para comparar correctamente.
    palabra = palabra.replace(" ", "").lower()

    #Caso base: si la palabra tiene 0 o 1 letra, es palíndromo.
    if len(palabra) <= 1:
        return True

    #Si la primera y última letra son distintas no es palíndromo.
    if palabra[0] != palabra[-1]:
        return False

    #Caso recursivo: comprobar la subcadena sin el primer y último carácter.
    return es_palindromo(palabra[1:-1])

while True:

    palabra = validacion_solo_letras_input("\nIngrese una palabra (sin tildes ni números): ",
        "\n****Error: solo se permiten letras (sin números ni símbolos)****")
    
    tildes = "áâãäåāăąàæçćĉċčďđèéêëēĕėęěƒĝğġģĥħìíîïĩīĭįıĵķĺļľłñńņňŋòóôõöøōŏőœŕŗřśŝşšßťŧùúûüũūŭůűųŵýÿŷźżžÁÂÃÄÅĀĂĄÀÆÇĆĈĊČĎĐÈÉÊËĒĔĖĘĚƑĜĞĠĢĤĦÌÍÎÏĨĪĬĮİĴĶĹĻĽŁÑŃŅŇŊÒÓÔÕÖØŌŎŐŒŔŖŘŚŜŞŠŤŦÙÚÛÜŨŪŬŮŰŲŴÝŶŸŹŻŽ"

    #Verifica si hay alguna tilde en el texto
    if any(letra in tildes for letra in palabra):
        print("\n****Error: No se permiten palabras con tildes. Volvé a intentarlo****\n")
        continue

    if es_palindromo(palabra):
        print(f"\n'{palabra}' ES un palíndromo")
        pass
    else:
        print(f"\n'{palabra}' NO es un palíndromo")
        pass
    print("______________________________________")

#-----------------------------------------------

#6) Escribí una función recursiva en Python llamada suma_digitos(n) que reciba un
#número entero positivo y devuelva la suma de todos sus dígitos.

    def suma_digitos(n):
        #Caso base: si el número es menor a 10, su suma es el mismo número.
        if n < 10:
            return n
        else:
            #Toma el último dígito con % 10 y sigue con el resto del número usando //.
            return (n % 10) + suma_digitos(n // 10)

    numero = int(validacion_solo_numeros_enteros("\nIngrese un número entero positivo: ",
        "\n****Error: Solo se permiten números enteros positivos****"))

    resultado = suma_digitos(numero)

    print(f"\nLa suma de los dígitos de {numero} es: {resultado}")
    print("______________________________________")

#-----------------------------------------------

#7) Un niño está construyendo una pirámide con bloques. En el nivel más bajo coloca n
#bloques, en el siguiente nivel uno menos (n - 1), y así sucesivamente hasta llegar al
#último nivel con un solo bloque.
#Escribí una función recursiva contar_bloques(n) que reciba el número de bloques en el
#nivel más bajo y devuelva el total de bloques que necesita para construir toda la
#pirámide.

    def contar_bloques(n):
        #Caso base: si el nivel inferior tiene 1 bloque, solo se necesita 1.
        if n == 1:
            return 1
        else:
            #Caso recursivo: sumar los bloques del nivel actual más los del nivel superior.
            return n + contar_bloques(n - 1)

    nivel_inferior = int(validacion_solo_numeros_enteros("\nIngrese la cantidad de bloques del nivel más bajo: ",
    "\n****Error: Solo se permiten números enteros positivos.****"))

    total_bloques = contar_bloques(nivel_inferior)

    print(f"\nPara construir la pirámide con {nivel_inferior} bloques en la base,")
    print(f"se necesitan en total {total_bloques} bloques")
    print("______________________________________")

#-----------------------------------------------

#8) Escribí una función recursiva llamada contar_digito(numero, digito) que reciba un
#número entero positivo (numero) y un dígito (entre 0 y 9), y devuelva cuántas veces
#aparece ese dígito dentro del número.

    def contar_digito(numero, digito):
        #Caso base: si el número llega a 0, no hay más dígitos que contar
        if numero == 0:
            return 0
        else:
            #Verifica si el último dígito coincide con el buscado
            if numero % 10 == digito:
                return 1 + contar_digito(numero // 10, digito)
            else:
                return contar_digito(numero // 10, digito)

    numero = int(validacion_solo_numeros_enteros(
        "\nIngrese un número entero positivo: ",
        "\n****Error: Solo se permiten números enteros positivos****"))

    digito = int(validacion_solo_numeros_enteros("Ingrese el dígito que desea contar (0-9): ",
    "\n****Error: Solo se permiten números entre 0 y 9****"))

    # Validación adicional para asegurar que el dígito esté entre 0 y 9
    if digito < 0 or digito > 9:
        print("\nEl dígito debe estar entre 0 y 9.")
    else:
        cantidad = contar_digito(numero, digito)
        print(f"\nEl dígito {digito} aparece {cantidad} vez/veces en el número {numero}")

    print("______________________________________")
