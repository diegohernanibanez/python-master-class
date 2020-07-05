# Una funcion es un conjunto de instrucciones agrupadas en un bloque reutilizable

# Ejemplo 1 

print("--- Ejemplo 1 ----\n")

def muestro_cosas ():
    print("Hola somos cosas jajaja")

muestro_cosas()

# Ejemplo 2 Parametros

print("\n--- Ejemplo 2 ----\n")

def tabla (numero):
    print(f"Tabla de multiplicar del numero {numero}\n")

    for i in range(1, 11):
        resultado = numero * i
        print(f"{numero} x {i} = {resultado}")
    
# num = int(input("Ingrese un numero para saber su tabla: "))
for i in range(1, 4):
    tabla(i)

# Ejemplo 3 Parametros con valor inicial
print("\n--- Ejemplo 3 ----\n")

def getEmpleado (nombre, apellido, dni, edad = None):
    print("Empleado:")
    print(f"Nombre: {nombre}")
    print(f"Apellido: {apellido}")
    if edad != None:
        print(f"Edad: {edad}")
    print(f"DNI: {dni}\n")

getEmpleado("Diego","Ibañez","38079225")
getEmpleado("Empleado","Generico","11111111", 20)

# Ejemplo 4 Devolver datos con return

print("\n--- Ejemplo 4 ----\n")


def calculadora(num_1, num_2, basicas = False):
    suma = num_1 + num_2
    resta = num_1 - num_2
    producto = num_1 * num_2
    if num_2 != 0:
        cociente = num_1 / num_2
    else:
        cociente = "No se puede dividir por 0"

    cadena = ""

    cadena += f"{num_1} + {num_2} = {suma}"
    cadena += "\n"
    cadena += f"{num_1} - {num_2} = {resta}"
    cadena += "\n"
    if basicas == False:
        cadena += f"{num_1} * {num_2} = {producto}"
        cadena += "\n"
        cadena += f"{num_1} / {num_2} = {cociente}"
        cadena += "\n"
    
    return cadena

print(calculadora(5, 2))
print(calculadora(4, 0))

# Funciones dentro de funciones

print("\n--- Ejemplo 5 ----\n")

def getNombre(nombre):
    return f"El nombre es {nombre}"

def getApellido(apellido):
    return f"El apellido es {apellido}"

def getNombre_y_apellido(nombre, apellido):
    return f"{getNombre(nombre)} \n{getApellido(apellido)}"

print(getNombre_y_apellido("Diego", "Ibañez"))

# Funciones lambda son funciones de una linea

print("\n--- Ejemplo 5 ----\n")

verTexto = lambda texto1, texto2 = "": f"{texto1} {texto2}"

print(verTexto("soy la primer variable","y yo soy la segunda"))
