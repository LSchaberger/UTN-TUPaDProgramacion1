#Aclaración antes de comenzar:
#print ("______________________________________")
#print ("")
#Usaré esos dos print en todos los algorítmos para mejorar la estética visual al ejecutarlos en terminal.


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