# Variable global
texto = "Perro caliente"

def oracion ():
    print("Dentro de la funcion:")
    # Variable local
    texto2 = "Gato frio"
    print(texto)
    print(texto2 + "\n")

oracion()
print("Fuera de la funcion:\n" + texto)
#print(texto2) no se puede hacer porque es local 

