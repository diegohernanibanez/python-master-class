nombre = "Papurri"
frase = "    asd"
texto = "La bella es bella"

# Imprimir por consola
print("Contenido de la variable: " + nombre) 
# type() muestra el tipo de la variable
print(f"Tipo de la variable: {type(nombre)}") 
# Chequea si se instanció una variable
print(f"Está instanciada: {isinstance(nombre, str)}") 
# strip() borra los espacios que hay al inicio y al final de un string
print(f"Frase con espacios adelante:\n{frase}\nFrase sin espacios adelante\n{frase.strip()}") 
# Eliminar variables con 'del'
del frase
# len() para saber la cantidad de elementos que tiene una variable
print(f"La cantidad de caracteres de nombre es {len(nombre)}")
# find() para encontrar la posicion de los elementos en una variable. Si no encuentra devuelve -1
print("Buscando la letra j " + str(nombre.find("j")))
print("Buscando la letra i " + str(nombre.find("i")))
print("Buscando la palabra bella " + str(texto.find("bella")))
# replace() para cambiar una palabra por otra en un string
texto_bien = texto.replace("bella", "vida", 1)
print(texto_bien)

